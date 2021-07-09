import pandas as pd
import numpy as np
import datetime
import mbf_pandas_msgpack

df = pd.DataFrame(
    {
        "A_int": [0, 1, 2],
        "C_float": [123.3, 1.8, np.nan],
        "D_str": ["a", "b", "c"],
        "E_date": [
            datetime.datetime.fromtimestamp(0),
            datetime.datetime.fromtimestamp(16e8),
            datetime.datetime.fromtimestamp(16e9),
       ],
        "F_tuple": [("shu", 23), ("sha, 24"), ("shum", 25)],
    }
)
mbf_pandas_msgpack.to_msgpack(open(f"samples/sample_pandas_{pd.__version__}.msgpack", "wb"), df)
