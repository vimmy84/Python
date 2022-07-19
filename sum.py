count = 1
sum = 0
print("Before :", sum)
for i in (1,3,5,7,9):
    num = i
    sum = sum + num
    print(count,num,sum)
    count = count +1
print("After:",sum)