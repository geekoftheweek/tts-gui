# TTS Voiceover GUI

A simple GUI application for quickly generating A.I. voiceovers using the XTTSv2
model from Coqui.

## Running the app

**Note:** Immediately after starting up, the application will download nearly
4GB of required TTS model files.

### With `uv` (Recommended)

If you've already installed the excellent `uv` tool, the following command will
* create a virtual environment at `./.venv`
* activate the virtual environment
* install any missing application dependencies
* launch this app
* deactivate the virtual environment when execution is complete

```
uv run streamlit run main.py
```

### Without `uv`

If you aren't using uv, something like the following should get you up and
running:

```
python -m virtualenv .venv
source .venv/bin/activate
pip install .
streamlit run main.py
deactivate
```

## Recommended Voices

For my purposes the "Viktor Menelaos" and "Szofi Granger" voices have provided
the most consistently realistic intonation for English voiceovers, but your
mileage may vary, so try them all out.
