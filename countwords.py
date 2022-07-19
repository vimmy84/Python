counts=dict()

fhand=open(input('Input a file: '))
for lines in fhand:
    parts=lines.split()
    for words in parts:
        counts[words]=counts.get(words,0) + 1
print('counts',counts)
bigword = None
bigcount = None
print (counts.items())
for k,v in counts.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v
print(bigword,bigcount)

