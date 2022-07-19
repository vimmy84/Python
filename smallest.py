smallest = None
print("Before:",smallest)
for i in [6,67,345,35,2,83,7,2,99]:
    num=i
    if(smallest is None):
        smallest=num
        
    elif(num < smallest):
        smallest=num
    print(num, smallest)

print("After :", smallest)
(13)        
 