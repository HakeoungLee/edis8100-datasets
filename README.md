# 📚 EDIS 8100 Teaching Subsets

Course-sized extracts of two openly licensed learning analytics datasets, prepared for **EDIS 8100: Teaching and Learning Analytics** (University of Virginia, Fall 2026, Dr. Hakeoung Hannah Lee).

Nothing here is original data. Both datasets were collected, anonymized, and released by other researchers, and both are redistributed under the licenses their authors chose. This repository exists for one practical reason: the full releases are 464 MB and 617 MB, which is more than a seminar wants to download during class. What follows is a documented, reproducible extract of each, small enough to load in seconds and complete enough to do real work with.

**If you are using these for research rather than for this course, go to the original sources and cite the original papers.** Links and citations are below.

---

## What is here

### `oulad-bbb/` — Open University Learning Analytics Dataset, module BBB

| File | Rows | What it is |
|---|---|---|
| `studentInfo.csv` | 4,529 | One row per enrollment: demographics and final result |
| `studentRegistration.csv` | 4,529 | Registration and unregistration dates |
| `studentVle.csv.gz` | 891,062 | Daily click counts per student per VLE resource |
| `studentAssessment.csv` | 21,783 | Submission date and score for each assessment |
| `assessments.csv` | 18 | Assessment type, deadline, weight |
| `vle.csv` | 528 | What each VLE resource is |
| `courses.csv` | 2 | Module presentation lengths |

**The extract:** module `BBB`, presentations `2013J` and `2014J`. Two presentations of the same course, roughly 2,200 students each, so it is possible to ask whether a finding from one term replicates in the next. That question is hard to ask in a single-term extract and it is one of the more useful habits a doctoral student can build.

**Why BBB:** it is one of the larger modules, it has all ten deciles of the deprivation index populated, and its outcome distribution is not degenerate (roughly 48 percent pass, 29 percent withdraw).

Demographic fields include `gender`, `region`, `highest_education`, `imd_band` (Index of Multiple Deprivation decile, a UK area-level measure of socioeconomic deprivation), `age_band`, and `disability`.

### `persuade-4prompts/` — PERSUADE 2.0 corpus, four prompts

| File | Rows | What it is |
|---|---|---|
| `essays.csv.gz` | 5,531 | One row per essay: full text, holistic score, writer demographics |
| `discourse_elements.csv.gz` | 63,211 | One row per annotated span: type, effectiveness, character offsets |

**The extract:** four prompts spanning both writing tasks. `Distance learning` and `Cell phones at school` are independent writing; `Driverless cars` and `Does the electoral college work?` are source-based. The full corpus has fifteen prompts, and holding prompt roughly constant makes comparisons across writers interpretable.

The original data ships as one wide table that repeats each essay's full text on every annotation row, which is why it is 617 MB. Here it is normalized into an essay table and a discourse table joined on `essay_id`. No rows were dropped other than by the prompt filter, and no values were altered.

Discourse types are `Lead`, `Position`, `Claim`, `Counterclaim`, `Rebuttal`, `Evidence`, `Concluding Statement`, and `Unannotated`. Each annotated span carries a human effectiveness rating of `Effective`, `Adequate`, or `Ineffective`. Writer fields include `grade_level`, `gender`, `ell_status`, `race_ethnicity`, `economically_disadvantaged`, and `student_disability_status`.

---

## Licenses and citation

**These are not the same license. Check which dataset you are using before you reuse anything.**

### OULAD: CC BY 4.0

Free to share and adapt, including commercially, with attribution.

> Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, 4, 170171. https://doi.org/10.1038/sdata.2017.171

Original: https://analyse.kmi.open.ac.uk/open_dataset (now served from https://research.stem.open.ac.uk/ouanalyse/dataset/)

### PERSUADE 2.0: CC BY-NC-SA 4.0

Attribution, **non-commercial use only**, and derivatives must carry the same license. A university course is non-commercial use. Building a commercial product on it is not.

> Crossley, S. A., Baffour, P., Tian, Y., Franklin, A., Benner, M., & Boser, U. (2024). A large-scale corpus for assessing written argumentation: PERSUADE 2.0. *Assessing Writing*, 61. https://doi.org/10.1016/j.asw.2024.100865

Original: https://github.com/scrosseye/persuade_corpus_2.0

The `student_disability_status` field means the student has an IEP or a 504 plan. No further information is available, and the corpus authors say so explicitly. Do not infer more than that from it.

---

## Using these in a notebook

Both files load straight from a raw URL with no authentication and no account.

```python
import pandas as pd

BASE = "https://raw.githubusercontent.com/HakeoungLee/edis8100-datasets/main"

students = pd.read_csv(f"{BASE}/oulad-bbb/studentInfo.csv")
clicks   = pd.read_csv(f"{BASE}/oulad-bbb/studentVle.csv.gz")   # pandas handles .gz

essays    = pd.read_csv(f"{BASE}/persuade-4prompts/essays.csv.gz")
discourse = pd.read_csv(f"{BASE}/persuade-4prompts/discourse_elements.csv.gz")
```

If you want the full releases rather than these extracts, `build_subsets.py` in this repository documents exactly where they come from and what was done to them.

---

## Reproducing the extracts

`build_subsets.py` downloads both originals and regenerates everything here. It is the honest version of "we used a subset": anyone can check what was kept and what was left out.

```bash
python build_subsets.py --work-dir /tmp/oulad-persuade --out .
```

The OULAD download is about 47 MB and takes seconds. The PERSUADE download is about 617 MB from Google Drive and takes a few minutes.

---

## A note for students

You are looking at a small piece of the work that sits between "there is a dataset somewhere" and "I can analyze it." Someone had to find the data, read the license, decide what a defensible subset was, write down what they removed, and record the citation so the original researchers get credit. That work is not glamorous and it is not optional, and it is the reason the analysis you are about to run is trustworthy.

When you go looking for data for your own project, start with the repositories rather than with a search engine. The [PEERS Data Hub](https://www.icpsr.umich.edu/web/pages/peersdatahub/) at ICPSR is built for exactly this, and the course guide *Finding and Evaluating Learning Analytics Data* walks through the others.

---

Prepared for EDIS 8100 at the University of Virginia School of Education and Human Development. The extraction code in this repository is released under the MIT License. The data retain the licenses of their original publishers, as described above.
