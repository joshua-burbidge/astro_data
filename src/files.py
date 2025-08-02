import pandas as pd

def read_gzoo_csv() -> pd.DataFrame:
    df = pd.read_csv('../data/GalaxyZoo1_DR_table2.csv')
    return df