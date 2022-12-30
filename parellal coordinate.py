from pandas.plotting import parallel_coordinates
from sklearn.datasets import load_iris
import pandas as pd
iris=load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
df['label']=pd.Series( [iris.target_names[k] for k in iris.target],dtype='category')
df['group']=iris.target
pl=parallel_coordinates(df,'label')