from lxml import objectify
import pandas as pd
xml = objectify.parse(open('xmldata.xml','r'))
root = xml.getroot()
print(root.tag)
df = pd.DataFrame(columns = ('number',"string","bool"))
for i in range(4):
    obj = root.getchildren()[i].getchildren()
    d = {"number":obj[0].text, "string":obj[1].text, "bool":obj[2].text}
    row = pd.Series(d)
    row.name = i
    df=df.append(row)
df

df1 = df.drop_duplicates()
df1