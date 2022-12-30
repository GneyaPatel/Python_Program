import pandas as pd
s = pd.Series([1,2,3, np.NAN, 5,6,None])
print(s.fillna(s.mean()))
print()