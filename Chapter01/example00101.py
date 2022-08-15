list1=[[1,2,3],[4,5,6],[7,8,9]]

print([i*j*k for i in list1[0] for j in list1[1] for k in list1[2]])

words = 'here is a sentence'.split()

print([[word,len(word)] for word in words])