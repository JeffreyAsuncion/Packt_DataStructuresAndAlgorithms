# Sequences

print("this is an empty list: ", list())   

list1 = [1,2,3,4]
print("before : ",list1)
list1.append(1)
print("after  : ",list1)

print('*'*10)

list2 = list1 * 2
print(list2)

print("min : ", min(list1))

print("max : ", max(list1))

list1.insert(0,2)   # insert an value 2 at index 0
print("insert an value 2 at index 0 : ", list1)

list1.reverse()
print("reverse list : ", list1)

list2 = [11, 12]
list1.extend(list2)
print("exteded list : ", list1)


print("This is sum(list) : ", sum(list1))
print("This is len(list) : ", len(list1))
list1.sort()
print("This is list1.sort : ", list1)

list1.remove(12)
print("This is list1.remove(12) : ", list1)



