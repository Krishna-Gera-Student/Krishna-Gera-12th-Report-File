fObj = open(r'program-companions\my-text.txt','r')
for lines in fObj:
    lines = lines.split()
    for words in lines:
        print (words, end="#")
    print()