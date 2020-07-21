import pandas as pd


def catbind(a, b):
    concatenated = pd.concat([pd.Series(a.astype("str")), pd.Series(b.astype("str"))])
    return pd.Categorical(concatenated)
