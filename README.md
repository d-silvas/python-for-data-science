
# Installation

```
py -m venv ./venv
.\venv\Scripts\activate # windows
source venv/bin/activate # linux
pip install -r requirements.txt
```

## vscode:

- Need to run the commands (with ctrl-P) `Python: Enable linting`, `Python: Select Linter` (and use pylint) and `Python: Select Interpreter` ( and choose the one under the `/.venv` folder). (TODO: check if we can write these in settings.json).
- The included `settings.json` includes a python path only for Windows.