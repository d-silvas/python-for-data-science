
# Installation

```
py -m venv ./venv
.\venv\Scripts\activate # windows
source venv/bin/activate # linux
pip install -r requirements.txt
```

## vscode:

- May need to run the commands (with ctrl-P) `Python: Enable linting`, `Python: Select Linter` (and use pylint) and `Python: Select Interpreter` ( and choose the one under the `/.venv` folder), if vscode does not load properly.
- The included `settings.json` includes a python path only for Windows.