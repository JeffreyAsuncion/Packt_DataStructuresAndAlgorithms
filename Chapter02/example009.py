# Beginning with dictionaries

a = {
    'Monday'    :   1,
    'Tuesday'   :   2,
    'Wednesday' :   3
}   # creates a dictionary

b = dict({
            'Monday'    :   1,
            'Tuesday'   :   2,
            'Wednesday' :   3
})   # creates a dictionary

print(b)

c = dict(zip(['Monday', 'Tuesday', 'Wednesday'],
             [1, 2, 3]))
            
print('c : ',c)

d = dict([
            ('Monday', 1),
            ('Tuesday',  2),
            ('Wednesday', 3)
])

print('d : ', d)