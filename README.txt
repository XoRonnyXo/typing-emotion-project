Emotion Detection from Keyboard Typing Patterns
==================================================

Quick start
-----------
1) Open train_model.ipynb and run all cells (uses synthetic_session_level.csv).
2) (Optional) Collect your own keystroke events with collect_typing_data.py 
   then aggregate to session-level features before training.

Files
-----
- data_template.csv  : schema for per-keystroke logging
- synthetic_session_level.csv : demo session-level dataset
- train_model.ipynb  : end-to-end pipeline (features → models → eval)
- collect_typing_data.py : local data collector (no raw text content)
- Report_Emotion_from_Typing.(docx|md) : polished report
- Emotion_From_Typing_Presentation.(pptx|txt) : slides
