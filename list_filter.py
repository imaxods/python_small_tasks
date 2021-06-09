#define a function with obligatory parametr array that reffer to given list and
#non-obligatory key that will reffer to function which will be called on itmes in list
#and return those items whose key didnt occqured
#print(tuple(first_with_given_key([[1], [2, 3, 4], [4], [5, 6, 7], [8, 9]], key=len)))   -->   ([1], [2, 3, 4], [8, 9])
def first_with_given_key(array, key=len):
    length = list(map(lambda i: key(i), array))#list of lengths of array items
    qniu_lengts = []
    indexes_that_repets = []
    count = 0
    for a in length:#cykle that appends uniq lengths and lengths whic repeats
        if a not in qniu_lengts:
            qniu_lengts.append(a)
        elif a in qniu_lengts:
            indexes_that_repets.append(count)

        count += 1
    new_array = []
    for i in indexes_that_repets:#exchange items with repeated keys by
        array[i] = ''

    for i in array:#forming new list without items with repeated keys
        if i == '':
            continue
        else:
            new_array.append(i)
    return new_array

print(tuple(first_with_given_key([[1], [2], [4], [5, 6, 7], [8, 9, 5]], key=len)))