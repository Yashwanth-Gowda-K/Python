# Step 1: Take a list of numbers as input from the user
# Use map() to convert the input strings into integers, split() to separate numbers by spaces
# Example input: "23 1 45 12 78 3 19"

# Step 2: Sort the list in ascending order (modifies the original list)
# Use the sort() method, which by default sorts in ascending order

# Step 3: Sort the list in descending order (modifies the original list again)
# Use the sort() method with reverse=True to sort in descending order

# Step 4: Use the sorted() function to sort without modifying the original list
# For ascending order, use sorted() without additional arguments
# For descending order, use sorted() with reverse=True


num = list(map(int, input("Enter the numbers: ").split()))

num.sort()
print("Ascending order:", num)

num.sort(reverse=True)
print("Descending order:", num)

orginal_num = list(map(int,input("Enter number again for sorted function: ")))
asscending_sorted = sorted(orginal_num)
print("Ascending order (using sorted): ",asscending_sorted)

descending_sorted = sorted(orginal_num, reverse=True)  # Descending order without changing 'original_numbers'
print("Descending Order (using sorted):", descending_sorted)