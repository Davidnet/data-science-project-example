"""
Submodule that contains function to separate the real state dataframe.
"""


def split_by_country_df(realstate_df):
    argentina_df = realstate_df.loc[realstate_df.pais == "Argentina", :]
    colombia_df = realstate_df.loc[realstate_df.pais == "Colombia", :]
    # Un return que devuelve mas de un objeto se devuelve como tupla
    return colombia_df, argentina_df
