name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

yy = list()

for line in handle:
    if line.startswith('From:'):
        froms = line.split()
        yy.append(froms[1])
print(yy)
xx = dict()
for email in yy:
    xx[email] = xx.get(email,0) + 1
print(xx)

bigemail = None
bigcount = None
for email,count in xx.items():
    if bigcount is None or count > bigcount:
        bigemail = email
        bigcount = count
print(bigemail,bigcount)