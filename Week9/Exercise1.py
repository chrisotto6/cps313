# Chris Otto
# Week 9 - Program Exercise 1
# CPS313

# Course Information

def main():
    room =  {'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1244, 'CM241':1411}
    instructor = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
    time = {'CS101':'8:00 AM', 'CS102':'9:00 AM', 'CS103':'10:00 AM', 'NT110':'11:00 AM', 'CM241':'1:00 PM'}

    course = input('Please enter a course code: ')
    course = course.upper()
    if course in room:
        print('\nCourse information:', course)
        print('Room number:', room[course])
        print('Instructor:', instructor[course])
        print('Time:', time[course])
    else:
        print('\nInvalid course ID.')

main()