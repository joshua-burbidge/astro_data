# galaxy-zoo

#### Dependencies

Install all dependencies: `pip install -r requirements.txt`

To install new dependencies, add them to requirements.in, then run `pip-compile -v requirements.in` and then `pip install -r requirements.txt`

#### Data

```bash
wget https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table2.csv.gz
gunzip GalaxyZoo1_DR_table2.csv.gz
mkdir data
mv GalaxyZoo1_DR_table2.csv data/GalaxyZoo1_DR_table2.csv
```

#### pyenv

Create new venv: 
```bash
python3 -m venv venv
```

Activate:
```bash
source venv/bin/activate
```
