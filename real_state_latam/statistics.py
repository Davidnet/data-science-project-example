"""
Submodule that implements important functions of statistics to the real state latam dataset.
Author: Davidnet <david@cerberusdata.ai>
Property of WTM.
"""
from pathlib import Path
import pandas as pd
from .split import split_by_country_df


def dict_country_counts(train_path):
    """
    Function that returns a dict of value counts of columns of the latam dataset.
    Arguments:
        * train_path (str): location of train.csv.
    Returns:
        * dict object with keys of country and statistic
    """
    train_location = Path(train_path)
    train_df = pd.read_csv(train_location)
    colombia_df, argentina_df = split_by_country_df(train_df)
    statistics_dict = {
        "colombia": colombia_df.price.mean(),
        "argentina": argentina_df.price.mean(),
    }
    return statistics_dict
