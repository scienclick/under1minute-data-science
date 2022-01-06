# <editor-fold desc="prepping data for time series">

import numpy as np
import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)

def reformat_(df, lag_first=1, lag_last=3, l_=[]):
    ddf = df.copy()
    for c in l_:
        for i in range(lag_first, lag_last + 1):
            ddf["{}_lag_{}".format(c, i)] = ddf[c].shift(i)
    return ddf

df=pd.DataFrame({"col_A":np.arange(10,41),'col_B':np.arange(.1,.4,.01)})
tabular_=reformat_(df,lag_first=2,lag_last=5,l_=['col_A','col_B'])
tabular_.dropna(inplace=True)

_3d_data_=[]
for col in df.columns:
    l__=[tabular_[[c for c in tabular_.columns if col in c]]]
    _3d_data_+=l__
_3d_data = np.stack([df.values for df in _3d_data_], axis=2)

_3d_data_[1]
_3d_data.shape

len(_3d_data_)
# </editor-fold>