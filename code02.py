filename = open(r'program-companions\my-text.txt','r') 
vowels = 0
consonants = 0
uppercase = 0
lowercase = 0

all_vowels = "aeiouAEIOU"
text = filename.read()

for char in text:
    if char.isalpha():
        if char.lower() in all_vowels:
            vowels += 1
        else:
            consonants += 1

        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of uppercase characters:", uppercase)
print("Number of lowercase characters:", lowercase)