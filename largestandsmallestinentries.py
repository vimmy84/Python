
largest = None
smallest = None 

while True:
    num = input("Enter a number: ")
    if num == "done":
       break
    try:
        num = int(num)
        if largest is None:
            largest = num
        elif num > largest:
            largest = num

        if smallest is None:
            smallest = num
        elif num < smallest:
            small = num
    
        continue
    except:
        print("Invalid input")  
        continue  
print("The largest number is", largest)
print("The smallest number is",smallest)

    


        

        
