from lxml import objectify
import pandas as pd
from distutils import util
xml = objectify.parse(open('xmldata.xml'))
root = xml.getroot()
n=list(map(int,root.xpath('record/number')))
s=list(map(str,root.xpath('record/string')))
b=list(map(str,root.xpath('record/bool')))
print(n,s,b)
strto01=list(map(util.strtobool,b))
print(strto01)
o1toTF=list(map(bool,strto01))
print(o1toTF)
data = {'Number':n,'Boolean':o1toTF}
df = pd.DataFrame(data, columns=('Number', 'Boolean'),index=s)
print (df)
print (type(df.loc['one']['Number']))
print (type(df.loc['one']['Boolean']))