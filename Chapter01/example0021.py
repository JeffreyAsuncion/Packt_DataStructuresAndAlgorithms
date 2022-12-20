#testing

# # Version#01
# a = 10
# def my_function():
#     print(a)
# my_function()

######################3

# Version#02 - UnboundLocalError: local variable 'a' referenced before assignment
# a = 10
# def my_function():
#     print(a)
#     a += 1
# my_function()

######################3

# Version#03 - global fix
a = 10
def my_function():
    global a
    print(a)
    a += 1
my_function()