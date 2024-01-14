def lenWords(STRING):
    STRING_List = STRING.split()
    word_Count = []
    for words in STRING_List:
        word_Count.append(len(words))
    return(tuple(word_Count))
        
String = input("Enter a string: ")
result=lenWords(String)
print("Output tuple is: ",result)