import pickle

def insertData():
    fObj = open(r'program-companions/student_names.dat','ab')
    n = int(input("Enter number of students:"))
    for i in range(0,n):
        data = {}
        data["name"] = input("Enter name: ")
        data["rno"] = int(input("Enter roll number: "))
        pickle.dump(data,fObj)
        print("\n Data inserted successfully")
    fObj.close()
    
def displayData():
    fObj = open(r'program-companions/student_names.dat','rb')
    try: 
        while True:
            data = pickle.load(fObj)
            print(data['rno'],' : ',data['name'],)
    except EOFError:
        pass
    fObj.close()
    
def searchData():
    fObj = open(r'program-companions/student_names.dat','rb')
    found = 0
    rollNo = int(input("Enter roll number to search in file: "))
    try: 
        while True:
            data = pickle.load(fObj)
            if data["rno"] == rollNo:
                print(data['rno'],' : ',data['name'],)
                found = 1
                break
    except EOFError:
        pass
    
    if found == 1: 
        print("Record found")
    else:
        print("Record not Found")
    fObj.close()
    
while True:
    choice = int(input("1 Insert new record \n2 Display all records \n3 Search a particular student by Roll No.\n4 Exit \n Enter your Choice :"))
    if choice==1:
        insertData()
    elif choice==2:
        displayData()
    elif choice==3:
        searchData()
    elif choice==4:
        exit()