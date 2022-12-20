# Recursive Functions

def iterTest(low, high):
    while low <= high:
        print(low)
        low=low+1

def recurTest(low,high):
    if low <= high:
            print(low)
            recurTest(low+1, high)


# list = [1,3,2,6,5,4]
# list.sort()
# print(list)

# iterTest(1,10)
recurTest(1,10)

