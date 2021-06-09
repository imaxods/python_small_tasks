#diction is given. Task is to sort it by length of values if values are the same sort it by absolute value of key
diction={2:['A',3,4],0:['s'],-4:['r','u'],1:['v'],-2:[2,3],-5:['e',3,'y'],4:[5,'e'],3:['a',4,5]}

vals = list(diction.values())#all values of given dictionary in one list
len_vals = [len(i) for i in vals]#list of lengths of valus in dictionary
list_with_sorted_value = [[] for _ in range(max(len_vals))]#list with empty slots for in range of max length of value found
items_of_dictionary = list(diction.items())#dictionary items
items_of_dictionary.sort(key = lambda i: len(i[1]))#list of tuples with sourted values

for i in items_of_dictionary:#ading items with same value length in same slots so we can sort it by key
    list_with_sorted_value[len(i[1])-1].append(i)
list_sorted_value_and_keys=[]

for i in list_with_sorted_value:#creating new list with sorted values and keys
    if len(i) > 1:
       dict(i)
       i.sort(key=lambda i:abs(i[0]))
       list_sorted_value_and_keys.append(i)
    elif len(i) == 1:
        list_sorted_value_and_keys.append(i)
diction.clear()

for i in list_sorted_value_and_keys:#updating old dictionary with new sorted values
    diction.update(dict(i))

print(diction)