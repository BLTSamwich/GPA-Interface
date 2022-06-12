#Samuel Leyzerov
#5/4/22
#Python Final Project: Transcript App

#Dictionary with each term and its corresponding courses and GPA. Each course has a credit and grade value.
terms ={"Fall 2020" : {"GPA" : "" ,"CMP200" : {"Credits" : "", "Grade" : ""},
         "CMP131" : {"Credits" : "", "Grade" : ""},
         "CMP120" : {"Credits" : "", "Grade" : ""}},
 "Spring 2021" : {"GPA" : "" ,"CMP130" : {"Credits" : "", "Grade" : ""},
         "CMP124" : {"Credits" : "", "Grade" : ""},
         "TEL107" : {"Credits" : "", "Grade" : ""}},
 "Summer 2021" : {"GPA" : "" ,"CMP239" : {"Credits" : "", "Grade" : ""}},
 "Fall 2021" : {"GPA" : "" ,"CMP128" : {"Credits" : "", "Grade" : ""},
         "TEL110" : {"Credits" : "", "Grade" : ""},
         "CMP125" : {"Credits" : "", "Grade" : ""}},
 "Spring 2022" : {"GPA" : "" ,"CMP255" : {"Credits" : "", "Grade" : ""},
         "CMP243" : {"Credits" : "", "Grade" : ""},
         "CMP280" : {"Credits" : "", "Grade" : ""}}}
#Function used to collect input from user on which function to run
def getChoice():
    choice = input("Please Make your Selection: ")
    choice = choice.upper()
    while choice != 'U' and choice != 'C' and choice != 'D' and choice != 'E':
        choice = input("Please Make your Selection either 'U', 'C', 'D', or 'E': ")
        choice = choice.upper()
    return choice
#Function to end the program
def exitApplication():
    print("Thank You, have a good day")
    input("Press enter to close: ")
#Function to display list of options
def displayMenu():
    print("-------Menu-------")
    print('U\u0332','pdate Grade',sep='')
    print('C\u0332','alculate Term GPA',sep='')
    print('D\u0332','isplay Transcript',sep='')
    print('E\u0332','xit Application',sep='')	
    print("------------------")
#Function to change the credit and grade values of courses
def updateGrade():
    print()
    print("Terms: ")
    for key, value in terms.items():
        print(key)
    #Find the term that the class is in
    term = input("Which term is the class from?: ")
    term = term.lower()
    term = term.capitalize()
    while term not in terms.keys():
        #validation
        term = input("Which term is the class from?: ")
        term = term.lower()
        term = term.capitalize()
    print()
    print("Classes: ")
    for x in terms[term]:
        if x != "GPA":
            print(x)
    #Select the course
    subject = input("Which class do you want to update?: ")
    subject = subject.upper()
    while subject not in terms[term] or subject == 'GPA':
        #validation
        subject = input("Which class do you want to update?: ")
        subject = subject.upper()
    print("How many credits is",subject,"worth?(3,4): ")
    terms[term][subject]["Credits"] = input()
    #Input the credit for the selected course
    while terms[term][subject]["Credits"] != str(3) and terms[term][subject]["Credits"] != str(4):
        #validation
        print("How many credits is",subject,"worth?(3,4): ")
        terms[term][subject]["Credits"] = input()
    print("What letter grade did you get for",subject,"(A,B,C,D,F)?: ")
    #Input the grade for the selected course
    terms[term][subject]["Grade"] = input()
    terms[term][subject]["Grade"] = terms[term][subject]["Grade"].upper()
    while terms[term][subject]["Grade"]!= 'A' and terms[term][subject]["Grade"] != 'B' and terms[term][subject]["Grade"] != 'C' and terms[term][subject]["Grade"] != 'D' and terms[term][subject]["Grade"] != 'F':
        #validation
        print("What letter grade did you get for",subject,"(A,B,C,D,F)?:")
        terms[term][subject]["Grade"] = input()
        terms[term][subject]["Grade"] = terms[term][subject]["Grade"].upper()
#Function to print term, each term's gpa, each term's classes, each class' grade, and each class's credit
def displayTranscript():
    for x in terms:
        print(x)
        for i in terms[x]:
            print(i)
            print(terms[x][i])
        print()
#Function to calculate the GPA from previously provided credits and grades
def calculateTermGPA():
    print()
    print("Terms: ")
    for key, value in terms.items():
        print(key)
    term = input("Which term do you want to calculate GPA for?: ")
    term = term.lower()
    term = term.capitalize()
    while term not in terms.keys():
        #validation
        term = input("Which term do you want to calculate GPA for?: ")
        term = term.lower()
        term = term.capitalize()
    #define values used in loop
    keyGPA = 0
    add = 0
    credit = 0
    creditAdd = 0
    grade = 0
    realGrade = 0
    for key, value in terms[term].items():
        if key != "GPA":
            if terms[term][key]['Credits'] == '':
            #If credits are not already submited, the user will be notified
                print("Please submit Grades and Credits for your classes before calculating GPA")
            else:
                if terms[term][key]["Grade"] == '':
                #If grades are not already submited, the user will be notified
                    print("Please submit Grades for your classes before calculating GPA")
                else:
                    #convert letter grade to number
                    credit = terms[term][key]["Credits"]
                    grade = terms[term][key]["Grade"]
                    if grade == 'A':
                        realGrade = 4
                    elif grade == 'B':
                        realGrade = 3
                    elif grade == 'C':
                        realGrade = 2
                    elif grade == 'D':
                        realGrade = 1
                    elif grade == 'F':
                        realGrade = 0
                    #calculate amount of credits
                    creditAdd = creditAdd + int(credit)
                    add = int(credit)*realGrade
                    keyGPA = keyGPA + int(float(add))
    if creditAdd == 0:
        #if not credits are found in term, the GPA will not be able to be calculated
        print()
        print("Not enough information to calculate GPA")
        print("Please Update your grades and credits")
    else:
        #calculate final GPA
        finalGPA = keyGPA / creditAdd
        print("Your current gpa for this term is",finalGPA)
        terms[term]['GPA'] = finalGPA
#Code used to run the program and the defined functions
displayMenu()
choice = getChoice()
while choice != "E":
   if choice == "U":
       updateGrade()
   elif choice == "C":
       calculateTermGPA()
   elif choice == "D":
       displayTranscript()
   displayMenu()
   choice = getChoice()
#Once the user chooses to end the application, the exitApplication() function will run
exitApplication()
