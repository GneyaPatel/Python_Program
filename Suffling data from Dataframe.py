
import pandas as pd
import numpy as np
df = pd.DataFrame({'A':[2,1,2,3,3,5,4],'B':[1,2,3,5,4,2,5], 'C': [5,3,4,1,1,2,3]})
df= df.sort_values(by = ['A','B'], ascending = [True, True])
df= df.reset_index(drop = True)
print(df)
index = df.index.tolist()
print('index = ',index)
print("\n")
np.random.shuffle(index)
print('index after shuffle',index)
df = df.loc[index]
print(df)
print("\n")
df = df.reset_index(drop=True)
print(df)