# Import the time module to add delays

# Function to execute a task after a delay
# Print a message when the task is executed

# Ask the user for the delay duration in seconds

# Pause the program for the specified delay
# Execute the task


import time

def scheduled_task():
  print("I love you 💕💕💕\n .......Sodaaaaaaa")
  print("But i hate you😒😒")

delay = int(input("Enter the time to display the time: "))
print(f"task will be exectued after {delay} seconds.")
time.sleep(delay)
scheduled_task()