## pypkgs 

![](https://github.com/TomasBeuzen/pypkgs/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/TomasBeuzen/pypkgs/branch/master/graph/badge.svg)](https://codecov.io/gh/TomasBeuzen/pypkgs) ![build](https://github.com/TomasBeuzen/pypkgs/workflows/build/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pypkgs/badge/?version=latest)](https://pypkgs.readthedocs.io/en/latest/?badge=latest)

Python package that eases the pain of concatenating Pandas categoricals!

### Installation

```
pip install -i https://test.pypi.org/simple/ pypkgs
```

### Dependencies

See [poetry.lock](poetry.lock) for a list of dependencies.

### Usage

```python
>>> from pypkgs import pypkgs
>>> import pandas as pd
>>> a = pd.Categorical(["character", "hits", "your", "eyeballs"])
>>> b = pd.Categorical(["but", "integer", "where it", "counts"])
>>> pypkgs.catbind(a, b)
[character, hits, your, eyeballs, but, integer, where it, counts]
Categories (8, object): [but, character, counts,
eyeballs, hits, integer, where it, your]
```

### Documentation
The official documentation is hosted on Read the Docs: https://pypkgs.readthedocs.io/en/latest/

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
