"""Rebuild the EDIS 8100 teaching subsets from their original sources.

Run this to verify that the CSVs in this repository are exactly what they claim
to be: filtered extracts of two published datasets, with no values altered.

    python build_subsets.py --work-dir /tmp/edis8100-data --out .

OULAD is CC BY 4.0 (Kuzilek, Hlosta, & Zdrahal, 2017).
PERSUADE 2.0 is CC BY-NC-SA 4.0 (Crossley et al., 2024).
See README.md for full citations and the terms of each license.
"""

import argparse
import gzip
import io
import os
import shutil
import zipfile

import pandas as pd
import requests

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

OULAD_ZIP = "https://schools.stem.open.ac.uk/cdn/files/anonymisedData.zip"
PERSUADE_DRIVE_ID = "13phHyDzIsb0MHyJr6q-B-qIa9P2tM135"

# What the extracts keep. Change these and you get a different subset, which is
# the point of writing them down rather than burying them in a notebook.
OULAD_KEEP = [("BBB", "2013J"), ("BBB", "2014J")]
PERSUADE_KEEP = [
    "Distance learning",
    "Driverless cars",
    "Does the electoral college work?",
    "Cell phones at school",
]

ESSAY_COLS = [
    "essay_id", "prompt_name", "task", "assignment", "holistic_essay_score",
    "essay_word_count", "grade_level", "gender", "ell_status", "race_ethnicity",
    "economically_disadvantaged", "student_disability_status", "full_text",
]
DISCOURSE_COLS = [
    "essay_id", "discourse_id", "discourse_start", "discourse_end",
    "discourse_type", "discourse_type_num", "discourse_effectiveness",
    "discourse_text",
]


def download(url, dest, params=None, session=None):
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print(f"  cached: {dest}")
        return dest
    get = (session or requests).get
    print(f"  downloading {url}")
    with get(url, params=params, headers={"User-Agent": UA}, stream=True, timeout=600) as r:
        r.raise_for_status()
        with open(dest, "wb") as fh:
            for chunk in r.iter_content(1 << 20):
                fh.write(chunk)
    print(f"  wrote {dest} ({os.path.getsize(dest) / 1e6:.1f} MB)")
    return dest


def fetch_oulad(work):
    zip_path = download(OULAD_ZIP, os.path.join(work, "oulad.zip"))
    out = os.path.join(work, "oulad")
    if not os.path.isdir(out):
        with zipfile.ZipFile(zip_path) as z:
            z.extractall(out)
    return out


def fetch_persuade(work):
    """Google Drive interposes a confirmation page on large files."""
    dest = os.path.join(work, "persuade.csv")
    if os.path.exists(dest) and os.path.getsize(dest) > 1e8:
        print(f"  cached: {dest}")
        return dest
    s = requests.Session()
    base = "https://drive.usercontent.google.com/download"
    first = s.get(base, params={"id": PERSUADE_DRIVE_ID, "export": "download"},
                  headers={"User-Agent": UA}, timeout=120)
    confirm, uuid = "t", None
    for key, target in (("confirm", "confirm"), ("uuid", "uuid")):
        marker = f'name="{key}" value="'
        if marker in first.text:
            value = first.text.split(marker, 1)[1].split('"', 1)[0]
            if target == "confirm":
                confirm = value
            else:
                uuid = value
    params = {"id": PERSUADE_DRIVE_ID, "export": "download", "confirm": confirm}
    if uuid:
        params["uuid"] = uuid
    return download(base, dest, params=params, session=s)


def write_csv(df, path, compress):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if compress:
        with gzip.open(path, "wt", encoding="utf-8", newline="", compresslevel=9) as fh:
            df.to_csv(fh, index=False)
    else:
        df.to_csv(path, index=False)
    print(f"    {os.path.basename(path):32} {len(df):>9,} rows  "
          f"{os.path.getsize(path) / 1e6:6.1f} MB")


def build_oulad(src, out):
    print("\nOULAD subset:", ", ".join(f"{m} {p}" for m, p in OULAD_KEEP))
    keep = set(OULAD_KEEP)
    sel = lambda d: d[[(m, p) in keep for m, p in zip(d.code_module, d.code_presentation)]]
    dest = os.path.join(out, "oulad-bbb")

    assessments = sel(pd.read_csv(os.path.join(src, "assessments.csv")))
    for name in ("studentInfo", "studentRegistration", "courses", "vle"):
        write_csv(sel(pd.read_csv(os.path.join(src, name + ".csv"))),
                  os.path.join(dest, name + ".csv"), compress=False)
    write_csv(assessments, os.path.join(dest, "assessments.csv"), compress=False)

    sa = pd.read_csv(os.path.join(src, "studentAssessment.csv"))
    write_csv(sa[sa.id_assessment.isin(set(assessments.id_assessment))],
              os.path.join(dest, "studentAssessment.csv"), compress=False)

    # 454 MB, so stream it rather than loading it whole.
    chunks = [sel(c) for c in pd.read_csv(os.path.join(src, "studentVle.csv"),
                                          chunksize=2_000_000)]
    write_csv(pd.concat(chunks), os.path.join(dest, "studentVle.csv.gz"), compress=True)


def build_persuade(src, out):
    print("\nPERSUADE subset:", ", ".join(PERSUADE_KEEP))
    d = pd.read_csv(src, low_memory=False)
    dest = os.path.join(out, "persuade-4prompts")

    essays = d.drop_duplicates("essay_id")[ESSAY_COLS]
    essays = essays[essays.prompt_name.isin(PERSUADE_KEEP)].reset_index(drop=True)
    discourse = d[DISCOURSE_COLS]
    discourse = discourse[discourse.essay_id.isin(set(essays.essay_id))].reset_index(drop=True)

    write_csv(essays, os.path.join(dest, "essays.csv.gz"), compress=True)
    write_csv(discourse, os.path.join(dest, "discourse_elements.csv.gz"), compress=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--work-dir", default="./_work", help="where originals are downloaded")
    ap.add_argument("--out", default=".", help="where the subsets are written")
    ap.add_argument("--skip", choices=["oulad", "persuade"], action="append", default=[])
    args = ap.parse_args()

    os.makedirs(args.work_dir, exist_ok=True)
    if "oulad" not in args.skip:
        build_oulad(fetch_oulad(args.work_dir), args.out)
    if "persuade" not in args.skip:
        build_persuade(fetch_persuade(args.work_dir), args.out)
    print("\nDone. Originals are in", args.work_dir,
          "and can be deleted once you have checked the output.")


if __name__ == "__main__":
    main()
