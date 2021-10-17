# Dictionaries for text analysis

def wordcount(fname):
    try:
        fhand=open(fname)
    except:
        print('File can not be opened')
        exit()

    count=dict()
    for line in fhand:
        words=line.split()
        for word in words:
            if word not in count:
                count[word]=1
            else:
                count[word]+=1
    return(count)

count=wordcount('alice.txt')
# count=wordcount('textcount.txt')

filtered={key:value for key, value in count.items() if value < 20 and value>16}

print(count)
print("="*20)
print(filtered)