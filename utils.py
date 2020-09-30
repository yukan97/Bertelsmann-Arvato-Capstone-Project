import numpy as nps
import pandas as pd

def format_mixed_types(df):
    '''This function is created for formating improper 
    values in columns CAMEO_DEUG_2015 and CAMEO_INTL_2015'''
    
    cols = ['CAMEO_DEUG_2015', 'CAMEO_INTL_2015']

    df[cols].replace({'X': np.nan, 'XX': np.nan})
    df[cols] = df[cols].astype(int)

    return df
