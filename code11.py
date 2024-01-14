def convert_bases(decimal_number):
    binary = bin(decimal_number)[2:]
    octal = oct(decimal_number)[2:]
    hexadecimal = hex(decimal_number)[2:]

    print("Decimal:", decimal_number)
    print("Binary:", binary)
    print("Octal:", octal)
    print("Hexadecimal:", hexadecimal)

decimal = int(input("Enter a decimal number: "))
convert_bases(decimal)
