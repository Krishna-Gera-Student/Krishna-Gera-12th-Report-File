def INDEX_LIST(L):
    indexList = []
    for i in range(len(L)):
        if L[i] != 0:
            indexList.append(i)
    return indexList

L = eval(input("Enter your list: "))
result = INDEX_LIST(L)
print('Index List is: ',result)
