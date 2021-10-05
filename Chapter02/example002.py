a=7; b=5
e = b**a# The operator (**) calculates power
print(e)
print(a%b)

f = 3 + 5j
print(f, "is of type", type(f))

print(f.real)

print(f*2)  #multiplication
print(f+3)  #addition
print(f-1)  #subtraction

print(bool(2))
print(bool(-2))
print(bool(0))
print("\n\n")
See_boolean = (4 * 3 > 10) and (6 + 5 >= 11)
print(See_boolean)

if (See_boolean):
    print("Boolean expression returned True")
else:
    print("Boolean expression returned False")
