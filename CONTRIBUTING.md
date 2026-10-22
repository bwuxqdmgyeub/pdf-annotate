# Contributing to pdf-annotate

Thanks for wanting to help improve the PDF Editor. This project is a
plugin-host based desktop application, so most contributions land as
either **core host** changes or **extension modules**.

## Ground rules

- Python 3.11+ only. We test against 3.11, 3.12 and 3.13.
- Every new editor capability should be a plugin under `src/pdf_annotate/extensions/`.
- The host must never import an extension directly — go through the registry.
- Keep `pymupdf` mutations inside `core/document.py`. Extensions talk to the
  document through the shared contract, not raw fitz objects.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate      # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -e .
python -m pdf_annotate
```

## Plugin authoring

1. Create a package under `src/pdf_annotate/extensions/<your_plugin>/`.
2. Expose a module-level `PLUGIN` object implementing `EditorPlugin`.
3. Register it in `extensions/loader.py` discovery list (or drop a
   `pyproject.toml` entry point named `pdf_annotate.plugins`).
4. Add a smoke test under `tests/`.

## Pull requests

- One feature per PR.
- Run `pytest -q` before pushing.
- If you touch the shared contract in `contracts/`, bump the
  `PLUGIN_API_VERSION` constant and note the change in the PR body.