#dictionary is given, task is to add values of upper-case letters to lower-case
#so keys of final dictionary will contain only lower-case letters with new values
#{'a':10, 'b': 34, 'A': 7, 'Z':3, 'B':23, 'c':12}  -->  {'a': 17, 'b': 57, 'z': 3, 'c': 12}
mcase = {'a':10, 'b': 34, 'A': 7, 'Z':3, 'B':23, 'c':12}
key=[]
value=[]
for ke,val in mcase.items():
    if ke.lower() in key:
      value[key.index(ke.lower())]+=val
      continue
    elif ke.upper() in key:
        pass
    key.append(ke.lower())
    value.append(val)
wanted=dict(zip(key,value))

print(wanted)
