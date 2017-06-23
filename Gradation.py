#Login

users = {'Moey':'nano2831996','nano':'moey1611997'}
userCode = ['BOSTES']

#Function

def main():
    login()

def verifyUsername():
    username = input('Enter Gradation Username: ')
    return username

def verifyPassword():
    password = input('Enter password: ')
    print('\n')
    return password

def login():
    print('Welcome to Gradation.\n')
    username = verifyUsername()
    password = verifyPassword()
    if username in users and users[username] == password:
        mainMenu()
    else:
        i = 3
        while i > 0:
            i -= 1
            print("Invalid Password. You have",i," more tries left.\n")
            print('Not a user? Press 1 to add user: ')
            username = verifyUsername()
            if username == '1':
                addUser()
            password = verifyPassword()
            if username in users and users[username] == password:
                mainMenu()
            print('\nERROR: No more valid tries available left. EXIT_FAILURE')

def addUser():
    userCoder = input('Enter user code for BOSTES authentication: ')
    if userCoder in userCode:
        newUser = input('Enter new username: ')
        newPass = input('Enter new password: ')
        users[newUser] = newPass
        print('\n')
        main()

def mainMenu():
    print('What would you like to do today?\n')
    print('1) Enter student grades.')
    print('2) Remove a student from the system.')
    print("3) Calculate the average of a student's mark.")
    print('4) Print current Student database.')
    print('5) Exit Gradation.')
    choices()
    
def backToMainMenu():
    print('What would you like to do now?\n')
    print('1) Enter student grades.')
    print('2) Remove a student from the system.')
    print("3) Calculate the average of a student's mark.")
    print('4) Print current Student database.')
    print('5) Exit Gradation.')
    choices()

def failMenu():
    print('\nInvalid choice; please try again')
    choices()
    
def choices():
    choice = input('\nPlease select the corresponding number'
               ' and press enter: ')
    if choice == '1':
        print('You have selected enter grades.')
        enterMarks(studDict)
        backToMainMenu()
    elif choice == '2':
        print('You have selected to remove a student from the system.\n')
        deleteStud(studDict)
        backToMainMenu()
    elif choice == '3':
        print("You have selected to calculate the average of a student's"
              ' grade.\n')
        average(studDict)
    elif choice == '4':
        print('Current student database:\n\n',studDict,'\n')
        backToMainMenu()
    elif choice == '5':
        print('\nThank you for using Gradation.\n')
        exit()
    else:
        failMenu()
        
    
def enterMarks(studDict):
    newStud = input('Enter Student name: ')
    studMark = int(input('Enter the mark: '))
    if newStud in studDict:
        studDict[newStud].append(studMark)
    else:
        studDict[newStud] = [studMark]
    print('\n\nStudent Database:\n')
    print(studDict)
    print('\n')

def deleteStud(studDict):
    if studDict == {}:
        print('No students detected in database, please add students.')
        backToMainMenu()
    print("Enter the student's name from the database:\n",studDict)
    DelStud = input()
    if DelStud in studDict:
        del studDict[DelStud]
        print(studDict)
    else:
        invalidStudDel()

def average(studDict):
    if studDict == {}:
        print('No students detected in database, please add students.')
        backToMainMenu()
    print('Select a student from the follow list:')
    from statistics import median
    print('\n',studDict)
    student = input()
    print('\n')
    if student in studDict:
        AvgGrade = median(studDict[student])
        print('Average grade of ',student,' is: ', AvgGrade,'\n')
        backToMainMenu()
    else:
        invalidStudAvg()

def invalidStudAvg():
    print('Student does not exist in database; please try again.\n')
    average(studDict)

def invalidStudDel():
    print('\n\nStudent does not exist in database; please try again.')
    deleteStud(studDict)

#Beginning of program
    
studDict = {}
main()
