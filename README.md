# Compiler

## Poetry

[Poetry](https://python-poetry.org/docs/#installation) is a tool for dependency management and packaging in Python.

[Linux installation](https://python-poetry.org/docs/#installation)

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

[powershell installation](https://python-poetry.org/docs/#installation)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## How to run

install dependencies

```shell
poetry install
```

## tests

```shell
python -m pytest .\tests\
```

## run

```shell
poetry run python .\compiler\
```
