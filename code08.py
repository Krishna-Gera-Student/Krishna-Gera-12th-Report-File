import csv

def inputData():
    file = open(r'program-companions\user_credentials.csv', 'a+', newline='')
    writer = csv.writer(file)
    
    while True:
        user_id = input('Enter user-id (or type "exit" to finish): ')
        if user_id.lower() == 'exit':
            break
        password = input('Enter password: ')
        writer.writerow([user_id, password])

    file.close()  # Close the file after writing
    print('Your Data is stored successfully.')

def search_password(user_id):
    file = open(r'program-companions\user_credentials.csv', 'r')
    reader = csv.reader(file)

    for row in reader:
        if row and row[0] == user_id:
            file.close()
            return row[1]

    file.close()
    return None

def display_all_usernames():
    file = open(r'program-companions\user_credentials.csv', 'r')
    reader = csv.reader(file)

    usernames = [row[0] for row in reader]
    print('Usernames:-')
    for i in usernames:
        print ('\t',i)
    
    file.close()
    return usernames

def user():
    print("\nUSER MANAGEMENT \n\t1. Add Credentials \n\t2. Search Credentials \n\t3. Display all the Usernames")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        inputData()
    elif choice == '2':
        search_username = input("Enter the Username to search: ")
        password = search_password(search_username)

        if password:
            print('Password for Username %s is: %s' % (search_username, password))
        else:
            print("Username %s not found" % search_username)
    elif choice == '3':
        display_all_usernames()
    else:
        print("INVALID INPUT")
        user()

#__main__
while True:
    user()