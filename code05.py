import pickle

def insertData():
    fObj = open(r'program-companions\student_names2.dat','ab+')
    n = int(input("Enter number of students:"))
    for i in range(0,n):
        data = {}
        data["name"] = input("Enter name: ")
        data["rno"] = int(input("Enter roll number: "))
        data["marks"] = int(input("Enter marks: "))
        pickle.dump(data,fObj)
        print("\n Data inserted successfully")
    fObj.close()
    
def displayData():
    fObj = open(r'program-companions\student_names2.dat','rb')
    try: 
        while True:
            data = pickle.load(fObj)
            print(data['rno'],' : ',data['name'],' : ',data['marks'])
    except EOFError:
        pass
    fObj.close()
    
def updateMarks():
    fObj = open(r'program-companions\student_names2.dat','rb+')
    found = False
    rollNo = int(input("Enter roll number to update marks: "))
    try: 
        while True:
            pos = fObj.tell()
            data = pickle.load(fObj)
            if data["rno"] == rollNo:
                data["marks"] = int(input("Enter marks to be updated: "))
                fObj.seek(pos)
                pickle.dump(data,fObj)
                print('Updated Data is:-')
                print(data['rno'],' : ',data['name'],' : ',data['marks'])
                found = True
                break
    except EOFError:
        pass
    
    if found: 
        print("Record found and Updated.")
    else:
        print("Record not Found")
    fObj.close()
    
while True:
    choice = int(input("1 Insert new record \n2 Display all records \n3 Update marks of a particular student by Roll No.\n4 Exit \n Enter your Choice :"))
    if choice==1:
        insertData()
    elif choice==2:
        displayData()
    elif choice==3:
        updateMarks()
    elif choice==4:
        print('Bye Bye!!')
        exit()
        