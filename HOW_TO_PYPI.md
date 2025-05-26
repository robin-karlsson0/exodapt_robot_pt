# How to update and upload package to pypi

Install dependencies
```
pip install build twine
```

Update version in
- `pyproject.toml`
- `src/exodapt_robot_pt/__init__.py`

Build and check package
```
python -m build
twine check dist/*
```

Package is built in `dist/`

Optional: Test upload to `testpy`
```
twine upload -r testpy dist/*
```

Upload built package to `pypi`
```
twine upload dist/*
```