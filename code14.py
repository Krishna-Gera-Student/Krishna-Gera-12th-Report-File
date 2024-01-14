def vowelCount(file_path):
    file_name = file_path.split('/')[-1]  
    vowels = "aeiouAEIOU"
    vowel_count = 0

    try:
        with open(file_path, 'r') as file:
            poem_text = file.read()

            for char in poem_text:
                if char in vowels:
                    vowel_count += 1

        print("Number of vowels in *",file_name, "* :", vowel_count)

    except FileNotFoundError:
        print("File not found:", file_name)

file = "program-companions/Poem.txt"  
vowelCount(file)
