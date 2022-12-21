def bitStr(n,s):
    if n==1: 
        print('base')
        return s
    return [str(n)+'.'+digit +'.'+ bits+'>' for digit in bitStr(1,s) for bits in bitStr(n-1,s)]

print(bitStr(3,'abc'))

# def bitStr(n,s):
#     if n==1: 
#         print('base')
#         return s
#     return [ bitStr(1,s) for bits in bitStr(n-1,s)]

# print(bitStr(3,'abc'))
