input_file = open(r'program-companions\my-text.txt','r')
output_file = open(r'program-companions\my-text-output.txt','w')

lines = input_file.readlines()
filtered_lines = [line for line in lines if 'a' not in line]
output_file.writelines(filtered_lines)

print("Lines containing 'a' removed and written to output file")