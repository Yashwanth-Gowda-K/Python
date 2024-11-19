def factorial(n):
    if n< 0:
        return "It can't be negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range (1 , n+ 1):
            result *=i
        return result
try :
    num = int(input("Enter a positive number: "))
    print(f"The factorial num of {num} is : {factorial(num)}")
except ValueError:
    print("Enter a valid integer.")

