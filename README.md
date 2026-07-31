# 📚 EDIS 8100 Teaching Subsets

Course-sized extracts of openly licensed learning analytics datasets, prepared for **EDIS 8100: Teaching and Learning Analytics** (University of Virginia, Fall 2026, Dr. Hakeoung Hannah Lee).

Nothing here is original data. Every dataset here was collected, anonymized, and released by other researchers, and both are redistributed under the licenses their authors chose. This repository exists for one practical reason: the full releases run to hundreds of megabytes each, which is more than a seminar wants to download during class. What follows is a documented, reproducible extract of each, small enough to load in seconds and complete enough to do real work with.

**If you are using these for research rather than for this course, go to the original sources and cite the original papers.** Links and citations are below.

---

## What is here

### `oulad-bbb/`: Open University Learning Analytics Dataset, module BBB

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

### `persuade-4prompts/`: PERSUADE 2.0 corpus, four prompts

| File | Rows | What it is |
|---|---|---|
| `essays.csv.gz` | 5,531 | One row per essay: full text, holistic score, writer demographics |
| `discourse_elements.csv.gz` | 63,211 | One row per annotated span: type, effectiveness, character offsets |

**The extract:** four prompts spanning both writing tasks. `Distance learning` and `Cell phones at school` are independent writing; `Driverless cars` and `Does the electoral college work?` are source-based. The full corpus has fifteen prompts, and holding prompt roughly constant makes comparisons across writers interpretable.

The original data ships as one wide table that repeats each essay's full text on every annotation row, which is why it is 617 MB. Here it is normalized into an essay table and a discourse table joined on `essay_id`. No rows were dropped other than by the prompt filter, and no values were altered.

Discourse types are `Lead`, `Position`, `Claim`, `Counterclaim`, `Rebuttal`, `Evidence`, `Concluding Statement`, and `Unannotated`. Each annotated span carries a human effectiveness rating of `Effective`, `Adequate`, or `Ineffective`. Writer fields include `grade_level`, `gender`, `ell_status`, `race_ethnicity`, `economically_disadvantaged`, and `student_disability_status`.

### `uci-student-performance/`: secondary school students in Portugal

`student-mat.csv`, 395 rows by 33 columns, the mathematics cohort. One flat file, one row per student, an outcome (`G3`, final grade out of 20) and a dozen background columns beside it, with values written as words rather than codes. Semicolon delimited, so `pd.read_csv(path, sep=";")`.

Used in Week 1 because it is the friendliest real table we could find and because it carries its own lesson: 38 students have a final grade of exactly 0, all 38 have zero recorded absences, and not one of the 280 students with any recorded absence scores 0. Those zeros are records that were never entered, not students who failed.

### `justhink/`: children collaborating with a robot

Per-child speech and interface actions from the JUSThink study at EPFL, joined to the PE-HRI team-level channels.

| File | Rows | What it is |
|---|---|---|
| `per_participant.csv` | 78 | One row per child: speech seconds, turns, words, adds, removes, presses, pre-test, post-test, gain |
| `participant_with_team_channels.csv` | 68 | The same children joined to their team's gaze, voice activity, and outcome measures |
| `pehri_team_outcomes.csv` | 34 | Team learning gain and final task error |
| `pehri_temporal.csv.gz` | 4,676 | The team channels again, in one-minute windows |

Used in Week 6. Two channels exist per child, speech and interface actions, and gaze exists only at the team level. Gesture and chat do not exist here, and neither does any demographic field: no age, no gender, no language background. That absence is part of what the week teaches.

### `ednet-kt3-500/`: an AI tutor in Korea

`actions.csv.gz`, 1,893,105 action rows by 7 columns, a 500-user extract of the public KT3 mirror. Columns are `timestamp`, `action_type`, `item_id`, `source`, `user_answer`, `platform`, `user_id`. Action types include entering and quitting an item, submitting a response, and requesting or reading an explanation, so the order of help seeking and answering is recoverable.

Used in Week 7. **Non-commercial use only.**

### `collab-chat/`: a computer networks course working online

`chat_logs.csv`, 1,374 messages by 4 columns, 8 groups of 4 or 5 students over four days in February 2021. Semicolon delimited. Columns are `timestamp`, `authorid`, `Group`, `message`.

Used in Week 9 alongside the JUSThink transcripts. Group sizes are nearly constant, so differences in how evenly the talk is distributed are not simply a function of how many people were in the room.

### `fieldday-aqualab/` and `fieldday-waves/`: two educational games

Open Game Data from the Field Day Lab at the University of Wisconsin-Madison, released into the public domain.

| File | Rows | What it is |
|---|---|---|
| `fieldday-aqualab/players.csv.gz` | 19,031 | One row per player, 145 derived features |
| `fieldday-aqualab/player_jobs.csv.gz` | 96,322 | One row per player per attempted job: tries, argument failures, help requests, time |
| `fieldday-waves/sessions.csv.gz` | 1,581 | One row per session that reached the difficulty spike, 870 features |

Used in Week 10. The two games disagree about whether persistence pays, which is the point of having both.

### `canvas-network/`: 325,199 course registrations

`person_course.csv.gz`, 325,199 rows by 26 columns. One row per person per course across the Canvas Network open courses, January 2014 to September 2015. Carries the usual activity and completion measures, and unusually also carries what the learner said they wanted before starting: `primary_reason`, `learner_type`, and `expected_hours_week` from an intake survey.

Used in Week 11, because a co-design session needs a dataset where the choice of measure visibly changes who looks successful. Take the top 500 learners by final grade and the top 500 by total events and the two lists share no one at all.

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
