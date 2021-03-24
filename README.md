# Install

Installation process for Linux, Mac and Windows WSL users:

## 1. Create virtual environment:

```
python -m venv .venv
```

Do it only when you creating project. Dont create it each time.

Sometimes it could be `python3`, `py`, `py3`

## 2. Activating virtual environment:

```
source .venv/bin/activate
```

## 3. Install libraries:

```
pip install -r requirements.txt
```

# Usage

## How to Save results to file

To save result add `> filename.filetype` at the end of run string

Example:

```
python script_name.py > filename.csv
```

## General usage

Don't forget that you need to activate virtual environment <b>before</b> using scripts

Put your pairs `keyword|volume` in `data.csv` file and simply run:

```
python main.py
```
