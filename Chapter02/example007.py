# Tuples part 2

tup1 = 1, 2, 3, 4, 5    # braces are optional
print("tuple value at index 1 is : ", tup1[1])

print("tuple[1:3] is : ", tup1[1:3])

tup12 = (11, 12, 13)
tup13 = tup1 + tup12
print(tup13)

print("repetition for tuples : ", tup13)

print("membership test : ", 5 in tup13)

print("negative indexing : ", tup1[-1])

print("length function of tuple : ", len(tup1))

print("max function of tuple : ", max(tup1))
print("min function of tuple : ", min(tup1))

# this will throw a type error
# tup1[1] = 5     # modification of a tuple is not allowed

print(tup1 == tup12)
print(tup1 > tup12)

