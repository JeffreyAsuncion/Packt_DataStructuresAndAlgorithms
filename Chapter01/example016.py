# static methods and class methods

class exponentialA(object):
    base = 3
    @classmethod
    def exp(cls, x):
        return(cls.base**x)

    @staticmethod
    def addition(x, y):
        return (x+y)

class exponentialB(exponentialA):
    base = 4

a = exponentialA()
b = a.exp(3)
print("the value : 3 to the power 3 is", b)
print("the sum is: ", a.addition(15,10))
print(exponentialB.exp(3))

