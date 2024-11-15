import time

def countdown(seconds):
    while seconds > 0:
        mins , secs = divmod(seconds , 60)
        print(f"{mins:02} : {secs:02}", end="\r")
        time.sleep(1)
        seconds -=1
    print("00.00 - Time is up! ")

time_in_seconds = int(input("Enter time in seconds: "))
countdown(time_in_seconds)
