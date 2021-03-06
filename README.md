English | [简体中文](README.zh.md)
# Introduction
According the `C` column data (CID) of [data.xlsx](data.xlsx), download the `sdf` file of 3D structure from the website [Pubchem](https://pubchem.ncbi.nlm.nih.gov/), and name the file of the `A` column. If the `C` column data is empty (NAN), save the value of the `B` column as the `txt` file, and name it the `A` column name.
# API
[https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/SDF?record_type=3d](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/SDF?record_type=3d)
# Install
```bash
pip install pandas
pip install requests
pip install retrying
pip install alive_progress
```
# Usage
```bash
python main.py
```
# Build
```bash
git clone https://github.com/XavierJiezou/pubchem-sdf-3d.git
cd pubchem-sdf-3d
pip install pipenv
pipenv install
pipenv shell
pip install pandas
pip install openpyxl
pip install requests
pip install retrying
pip install alive_progress
pip install pyinstaller
pyinstaller -F -i favicon.ico main.py
```
# Reference
> [https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest](https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest)