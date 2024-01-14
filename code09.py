def rotate_list_elements(lst):
    if len(lst) <= 1:
        return lst

    last_element = lst[-1]

    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = last_element
    return lst

my_list = eval(input("Enter the list you wanna rotate: "))
print("Original List:", my_list)

rotated_list = rotate_list_elements(my_list)
print("Rotated List:", rotated_list)