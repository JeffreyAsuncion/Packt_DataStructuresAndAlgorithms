# Variable Scope

# A
a = 15; b=25
print("before function")
print(a)
print(b)
def my_function():
    global a
    a = 11; b = 21
    print("in function")
    print(a)
    print(b)    

my_function()
print("out of function")
print(a)
print(b)