# galaxy-zoo

#### Dependencies

Install all dependencies: 
```bash
pip install -r requirements.txt
```

To install new dependencies, add them to requirements.in, then run 

```bash
pip-compile -v requirements.in && pip install -r requirements.txt
``` 

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

## Galaxy Zoo Data Reference

### Columns

- ObjID: SDSS Object ID
- RA, Dec: Coordinates of the galaxy. Can be used to find image of it.
  - RA: Right Ascension
  - Dec: Declination
- NVote: Number of votes on this galaxy.
- Vote Fractions:
  - P_EL: Elliptical
  - P_CW: Clockwise Spiral
  - P_ACW: AntiClockwise Spiral
  - P_EDGE: Edge-on Spiral
  - P_DK: Don't Know
  - P_MG: Merge
  - P_CS: Combined Spiral (Edge + CW + ACW)
- Debiased Votes:
  - P_EL_DEBIASED: Debiased elliptical vote fraction
  - P_CS_DEBIASED: Debiased spiral (CS) vote fraction
- Type Flags: require 80% consensus after debiasing
  - SPIRAL: considered a spiral galaxy
  - ELLIPTICAL: considered an elliptical galaxy
  - UNCERTAIN: no 80% consensus

#### Bias

The "bias" here is due to the fact that small, faint, or distant galaxies may appear as elliptical even though they are spiral, because the spiral arms are not visible. The bias is corrected for by assuming that the fraction of galaxy types is constant throughout the depth of the SDSS survey (in oversimplified terms).
