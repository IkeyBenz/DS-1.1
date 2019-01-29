import numpy as np
import pandas as pd

# Creating a Series by passing a list of values, letting pandas create a default integer index:
series = pd.Series([1, 2, 3, np.nan, 6, 8])

# Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 5), index=dates, columns=list('ABCDE'))


# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({
    'A': 1.0,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='int32'),
    'D': np.array([3]*4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'foo'
})
print(df.describe())