import pandas as pd

from os import environ

def read_csv(object_name, header = 'infer', names = None, sep = ',', index_col = None):
    object_name = f"{environ['S3_BUCKET']}/{object_name}"
    return pd.read_csv(object_name, header = header, names = names, sep = sep, index_col = index_col)