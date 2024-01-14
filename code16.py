def push(data):
    filteredList = []
    for key in data:
        if data[key] > 75:
            filteredList.append(key)
    return filteredList

def pop_display(filteredList):
    if filteredList == []:
        print("No data found.")
    else:
        while len(filteredList)>0 :
            print(filteredList.pop(), end=" ")

R = {"OM":76,"JAI":45,"BOB":89,"ALI":65,"ANU":90,"TOM":80}
filteredList = push(R)
pop_display(filteredList)
            