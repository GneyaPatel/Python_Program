a={}
print(type(a))
a['name']="Bond"
a['en_no.']="007"
a['contact_no.']="9870307802"
print(a)
print("value of name is ",a.get('name'))
print("value of age is ",a.get('age',19))
c=sorted(a)
print("sorted dictionary is :",c)