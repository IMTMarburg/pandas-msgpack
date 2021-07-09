import pandas as pd
import mbf_pandas_msgpack
import datetime
import numpy as np
from pandas.testing import assert_frame_equal

supposed = pd.DataFrame(
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


class TestReadingOldVersions:


    def test_1_0(self):
        df = mbf_pandas_msgpack.read_msgpack("samples/sample_pandas_1.0.0.msgpack")
        assert_frame_equal(df, supposed)

    def test_1_1(self):
        df = mbf_pandas_msgpack.read_msgpack("samples/sample_pandas_1.1.0.msgpack")
        assert_frame_equal(df, supposed)

    def test_1_2(self):
        df = mbf_pandas_msgpack.read_msgpack("samples/sample_pandas_1.2.0.msgpack")
        assert_frame_equal(df, supposed)

    def test_1_3(self):
        df = mbf_pandas_msgpack.read_msgpack("samples/sample_pandas_1.3.0.msgpack")
        assert_frame_equal(df, supposed)
