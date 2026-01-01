# string work like arrays. each character has its own index
# indexing starts 

a = "Hello, World!"
print(a[1])  # prints 'e', the character at index 1
# at 0
print(a[0])  # prints 'H', the character at index 0
# negative indexing starts from the end of the string
print(a[-1])  # prints '!', the last character
print(a[-5])  # prints 'o', the fifth character from the end
# slicing strings
print(a[2:5])  # prints 'llo', characters from index 2 to 4 at 0
print(a[:5])   # prints 'Hello', characters from the start to
print(a[2:])   # prints 'llo, World!', characters from index 2 to the end

print(a[-5:-2])  # prints 'orl', characters from index -5 to -3


#slice with step

text = "programming"
print(text[0:10:2])  # prints 'pormn', characters from index 0 to 9 with a step of 2at 0
print(text[::3])    # prints 'pgai', every third character
print(text[::-1])   # prints 'gnimmargorp', the string in reverse orderfrom 0

# core string methods

word  = "pakistan"
print(word.upper())      # prints 'PAKISTAN', converts to uppercase
print(word.lower())      # prints 'pakistan', converts to lowercase 
# strip method
print(word.strip("p"))   # prints 'akistan', removes 'p' from the start
print(word.replace("k", "K"))  # prints 'paKistan', replaces 'k' with 'K'
print(word.split("i"))  # prints ['pak', 'stan'], splits the string at 'i'from 0
print("iran" in word)  # prints False, checks if 'india' is in 'pakistan'at 0 index 0 to 4
print("stan" in word)   # prints True, checks if 'stan' is in 'pakistan'at 0 index 0 to 4
print(word.startswith("pak"))  # prints True, checks if the string starts with 'pak'
print(word.endswith("tan"))    # prints True, checks if the string ends with 'tan
print(word.find("is"))        # prints 3, finds the index of substring 'is'
print(word.count("a"))       # prints 2, counts occurrences of 'a' in the string
print(word.capitalize())     # prints 'Pakistan', capitalizes the first character
print(word.title())          # prints 'Pakistan', capitalizes the first character of each word
print(word.index("k"))      # prints 2, finds the index of substring 'k'
print(word.isalpha())      # prints True, checks if all characters are alphabetic
print(word.isdigit())      # prints False, checks if all characters are digits
print(word.islower())      # prints True, checks if all characters are lowercase
print(word.isupper())      # prints False, checks if all characters are uppercase
print(word.isspace())     # prints False, checks if all characters are whitespace
print(word.zfill(12))    # prints '000pakistan', pads the string with zeros to a total length of 12
print(word.center(15, "-"))  # prints '---pakistan----', centers the string with '-' padding

#join method
words = ["Hello", "from", "Python"]
print(" ".join(words))  # prints 'Hello from Python', joins the list into a string with spaces

# f-string for formatting
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # prints 'My name is Alice and I am 30 years old.'at 0


# number formatting in f-strings
pi = 3.141592653589793
print(f"Pi rounded to 2 decimal places: {pi:.2f}")  # prints 'Pi rounded to 2 decimal places: 3.14'
number = 255    
print(f"Number in binary: {number:b}")  # prints 'Number in binary: 11111111'
print(f"Number in octal: {number:o}")   # prints 'Number in octal: 377'
print(f"Number in hexadecimal: {number:x}")  # prints 'Number in hexadecimal: ff'
print(f"Number in scientific notation: {pi:.2e}")  # prints 'Number in scientific notation: 3.14e+00'at 0   
print(f"Number with leading zeros: {number:05d}")  # prints 'Number with leading zeros: 00255'      
print(f"Number with commas: {1000000:,}")  # prints 'Number with commas: 1,000,000'
print(f"Percentage: {0.756:.2%}")  # prints 'Percentage: 75.60%'
print(f"Left aligned: {name:<10}")  # prints 'Left aligned: Alice     '
print(f"Right aligned: {name:>10}")  # prints 'Right aligned:      Alice'
print(f"Center aligned: {name:^10}")  # prints 'Center aligned:   Alice   ' 
print(f"Hexadecimal (uppercase): {number:X}")  # prints 'Hexadecimal (uppercase): FF'   
print(f"Octal with prefix: {number:#o}")  # prints 'Octal with prefix: 0o377'
print(f"Hexadecimal with prefix: {number:#x}")  # prints 'Hexadecimal
print(f"Hexadecimal with prefix: {number:#x}")  # prints 'Hexadecimal with prefix: 0xff' with prefix: 0xff'












