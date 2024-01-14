users_list = []

def addUser(name, user_id, city):
    user = {'name': name, 'id': user_id, 'city': city}
    users_list.append(user)
    print("User added successfully.")

def removeUser(user_id):
    for user in users_list:
        if user['id'] == user_id:
            users_list.remove(user)
            print("User with ID", user_id, "removed successfully.")
            return
    print("User with ID", user_id, "not found.")

def displayUser(user_id=' '):
    if user_id is ' ':
        for user in users_list:
            print("ID:", user['id'])
            print("Name:", user['name'])
            print("City:", user['city'])
            print("-----------------------")
    else:
        for user in users_list:
            if user['id'] == user_id:
                print("ID:", user['id'])
                print("Name:", user['name'])
                print("City:", user['city'])
                return
        print("User with ID", user_id, "not found.")

while True:
    print("\nUSER MANAGEMENT")
    print("1. Add User")
    print("2. Remove User")
    print("3. Display User")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter name: ")
        user_id = input("Enter ID: ")
        city = input("Enter city: ")
        addUser(name, user_id, city)
    elif choice == '2':
        user_id = input("Enter ID of user to remove: ")
        removeUser(user_id)
    elif choice == '3':
        user_id = input("Enter ID of user to display (or leave blank to display all): ")
        displayUser(user_id)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-4).")
