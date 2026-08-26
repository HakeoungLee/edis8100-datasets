# 📚 EDIS 8100 Teaching Subsets

Course-sized extracts of openly licensed learning analytics datasets, prepared for **EDIS 8100: Teaching and Learning Analytics** (University of Virginia, Fall 2026, Dr. Hakeoung Hannah Lee).

Nothing here is original data. Every dataset here was collected, anonymized, and released by other researchers, and each is redistributed under the license its own authors chose. They are not the same license; see the table below. This repository exists for one practical reason: the full releases run to hundreds of megabytes each, which is more than a seminar wants to download during class. What follows is a documented, reproducible extract of each, small enough to load in seconds and complete enough to do real work with.

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
| `pehri_temporal.csv.gz` | 4,676 | The team channels again, in 10-second windows |

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

### `edx-mooc-forum/`: a real MOOC discussion forum with reply threading

One course run of a UC3Mx programming MOOC on edX, chosen because it is the size a seminar can reason about: 311 people posted, 181 of them appear in the reply graph, and 167 sit in one connected component.

| File | Rows | What it is |
|---|---|---|
| `posts.csv` | 1,478 | One row per post: type (thread, response, comment), author, timestamp, the post it answers, category, forum role, country, body |
| `reply_edges.csv` | 520 | One row per ordered pair: who replied to whom, and how often |
| `people.csv` | 311 | One row per person: post counts by type, role, country, first and last post |

Used in Week 8, where an edge means "A replied to B". The reply structure is native rather than inferred from timestamps: a response records the thread it answers and a comment records the response it answers.

Two things to say out loud before analysing it. The source is edX's **tracking log**, filtered to forum events, so it records forum *acts* rather than the state of the forum database: later edits and deletions do not appear, and posts a moderator removed are still in the file. And 2 percent of posts carry an anonymous-to-peers flag while still carrying the author hash, which is a gap between what a learner believed was anonymous and what the log kept.

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

### UCI Student Performance: CC BY 4.0

Attribution. Free to use, share, and adapt.

> Cortez, P., & Silva, A. (2008). Using data mining to predict secondary school student performance. In A. Brito & J. Teixeira (Eds.), *Proceedings of the 5th FUture BUsiness TEchnology Conference (FUBUTEC 2008)* (pp. 5-12). EUROSIS.
>
> Cortez, P. (2008). *Student performance* [Data set]. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T

Original: https://archive.ics.uci.edu/dataset/320/student+performance (donated November 2014; the repository lists Paulo Cortez as the creator and gives the Cortez and Silva conference paper as the introductory reference)

### JUSThink and PE-HRI: CC BY 4.0

Two deposits from the CHILI lab at EPFL, both attribution only.

> Norman, U., Dinkar, T., Nasir, J., Bruno, B., Clavel, C., & Dillenbourg, P. (2021). *JUSThink Dialogue and Actions Corpus* (v1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4627104
>
> Nasir, J., Norman, U., Bruno, B., Chetouani, M., & Dillenbourg, P. (2021). *PE-HRI: A multimodal dataset for the study of productive engagement in a robot mediated collaborative educational setting* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4633092
>
> Nasir, J., Bruno, B., & Dillenbourg, P. (2024). *PE-HRI-temporal: A multimodal temporal dataset in a robot mediated collaborative educational setting* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.13834073

Three deposits, not two. `pehri_temporal.csv.gz` comes from the 2024 PE-HRI-temporal release, which has its own DOI and a shorter author list than the 2021 PE-HRI deposit. Cite all three if you use the temporal file; CC BY 4.0 asks for attribution to the deposit you actually used.

### EdNet KT3: CC BY-NC 4.0

Attribution, **non-commercial use only**. A university course is non-commercial use. A product is not.

> Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., Baek, J., Bae, C., Kim, B., & Heo, J. (2020). EdNet: A large-scale hierarchical dataset in education. In *Artificial intelligence in education. AIED 2020* (Lecture Notes in Computer Science 12164, pp. 69-73). Springer. https://doi.org/10.1007/978-3-030-52240-7_13

Original: https://github.com/riiid/ednet, which states the terms directly: "The dataset is publicly released under Creative Commons Attribution-NonCommercial 4.0 International license for research purposes."

### edX MOOC forum (UC3Mx): CC BY 4.0

Attribution is required wherever a result from this file is shown, including on a slide.

> Alario-Hoyos, C. (2021). *Dataset MOOC Forum edX* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.5115573

### Online collaborative learning chat logs: CC BY 4.0

> Villa-Torrano, C. (2021). *Dataset on an online collaborative learning situation in a computer networks course* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.5150537

The deposit holds six files. Only `chat_logs.csv` is extracted here; the document edit logs, Moodle logs, submissions, learning design and final questionnaire stay at the source.

### Open Game Data, AQUALAB and WAVES: CC0 1.0

Public domain. It asks nothing of you, not even attribution, which you should give anyway. The dedication is stated in Field Day's own dataset documentation, per game: "These anonymous data are provided in service of future educational data mining research. They are made available under the Creative Commons CC0 1.0 Universal license."

The same documentation gives a suggested citation, which is the form to use even though nothing compels it:

> Field Day. (2019). *Open educational game play logs: AQUALAB and WAVES* [Data set]. Field Day Lab, University of Wisconsin-Madison. Retrieved from https://opengamedata.fielddaylab.wisc.edu

### Canvas Network Person-Course: CC BY 4.0

> Canvas Network. (2016). *Canvas Network person-course (1/2014 - 9/2015) de-identified open dataset* [Data set]. Harvard Dataverse. https://doi.org/10.7910/DVN/1XORAL

**A note on the citations above.** Every one of them has been checked against the source record itself rather than against another document in this course: the Zenodo API records for 4627104, 4633092, 13834073, 5150537 and 5115573; the Harvard Dataverse record for doi:10.7910/DVN/1XORAL; the UCI Machine Learning Repository page for dataset 320; Crossref for the OULAD, PERSUADE and EdNet papers; and Field Day's per-game dataset readme in `opengamedata/ogd-core`, which is where the CC0 dedication and the suggested citation are actually stated. Titles, author lists, years and licences match what the depositors recorded.

One entry is still open, and it is the only one. The published PERSUADE 2.0 article deposits its author list at Crossref in the order **Crossley, Tian, Baffour, Franklin, Benner, Boser**, while the corpus author's own repository README and the 2023 preprint both give **Crossley, Baffour, Tian, ...**. This repository uses the second order. Open the article itself and settle it before citing it in work that leaves this course. Everything else in that entry (title, journal, volume 61, article 100865, DOI) is confirmed.

Do the same check yourself before you reuse any of these. It is the habit this repository exists to teach, and it caught three errors here.

---

## Using these in a notebook

Every file here loads straight from a raw URL with no authentication and no account.

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

`build_subsets.py` currently covers **OULAD and PERSUADE only**: it downloads those two originals and regenerates their folders here. It is the defensible version of "we used a subset" for those two, and anyone can check what was kept and what was left out. The other seven folders are documented above but are not yet regenerable from this script; each section above names the original release so the extract can be checked by hand in the meantime.

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
