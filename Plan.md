- Get the contents (short links beginning with `https://top.zhan.com/toefl/[subject]/alltop[xx].html`). `../get_contents/contents.py`
  - 4 files for each subject's short links
- Get the indexes (long links beginning with `https://top.zhan.com/toefl/[subject]/review-[index].html?article_id=[index]`). `../get_indexes/indexes.py`
  - 4 files for each subejct's long links
- According to each (subject) index file, execute scraping. `../scripts/subject/task number`
  - Reading
    - No task number differences
      - 2(or 3) passages in linear arrangement
      - corresponding questions (dictionay of lists: `{question number: [choice A, choice B, choice C, choice D], ...}`)
  - Listening
    - Task number differences
      - order: `C1->L1->C2->L2->L3`
      - listening, transcripts, 
      - corresponding questions (dictionay of lists: `{question number: [choice A, choice B, choice C, choice D], ...}`)
  - Speaking
    - Task number differences
      - task1: reading (question)
      - task2: reading, listening (conversation), transcripts
      - task3: reading, listening (lecture), transcripts
      - task4: listening (lecture), transcripts
  - Writing
    - Integrated only
      - reading, listening(lecture), transcripts

- Formatter `../formatter/type.py`
  - Text
    - Remove unexpected line breaks
    - Insert appropriate line breaks
    - Blank spaces
  - Audio
    - Metadata, if required by other packages

- UI `../UI/subject.ui` & `../UI/subject_generated.py` & `../UI/subject_uiScript.py` & `../UI/res/*.svg` 
  - Reading
    - article display **(make rich text, larger)**
    - question display (Inherited stacked widget)
  - Listening
    - audio player
    - transcript player **(make rich text, larger)**
    - question display (Inherited stacked widget)
  - Speaking
    - article display **(make rich text, larger)**
    - audio player
    - transcript player **(make rich text, larger)**
  - Writing
    - article display **(make rich text, larger)**
    - audio player
    - transcript player **(make rich text, larger)**

- Pyinstaller to make distributable packages