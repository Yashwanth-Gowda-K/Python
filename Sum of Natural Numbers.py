def sum_of_natural_numbers(n):
    return n*(n+1)//2

num =int(input("Enter a number: "))

if num <1:
    print("Enter a postive number...")
else:
    result = sum_of_natural_numbers(num)
    print(f"The sum of the first {num} natural numbers is {result}")