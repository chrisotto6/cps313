# Chris Otto
# Week 2 - Program Exercise 15
# CPS313

# Based on user function return seconds in terms of different time intervals
def main():
    # Prompt the user for input and then begin the logic checks
    seconds = int(input('Enter the seconds: '))

    if(seconds >= 60 and seconds < 3600):
        minutes = seconds / 60
        print("Minutes: ", minutes)
    elif(seconds >= 3600 and seconds < 86400):
        hours = seconds / 3600
        print("Hours: ", hours)
    elif(seconds >= 86400):
        days = seconds / 86400
        print("Days: ", days)
    else:
        print("Seconds: ", seconds)
main()