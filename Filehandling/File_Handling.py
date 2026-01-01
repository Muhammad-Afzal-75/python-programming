# File Handling = python provides several functions for creating, reading, updating, and deleting files.
# this  is  extremely  vital for saving data , logs, records etc.

# File Modes:

# "r" = Read = file.read() , file.readline() , file.readlines()
# "w" = write (Overwrite file) = file.write() , file.writelines()
# "a" = append (Add data to the end of the file) = file.write() , file.writelines()
# "x" = create new file (error if file exists) = open("data.txt", "x")
# "b" = binary mode (for non-text files like images) = open("image.png", "rb")
# "t" = text mode (default mode for text files) = open("file.txt", "rt")
# "+" = read and write mode = open("file.txt", "r+")


#File opening and Reading



# file = open("Filehandling/data.txt", "r")
# print(file.read())
# file.close()


# reading line by line

# file = open("Filehandling/data.txt", "r")

# for line in file:
#     print(line.strip())

# file.close()

# readline()

# file = open("Filehandling/data.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close()

#File Writing


# file = open("Filehandling/text.txt", "w")
# file.write("This is a new line.\n and another line.\n")
# file.write("Writing to a file in Python is easy.\n")

# file.close()

# using with statement

# with open("Filehandling/data.txt", "r") as file:
#     print(file.read())

    #file deletion

# import os

# if os.path.exists("Filehandling/text.txt"):
#     os.remove("Filehandling/text.txt")
#     print("File deleted successfully.")

# json file handling

import json

student = {
    "name": "shayan", 
    "age": 6,
    "courses": ["Math", "Science"]
}
with open("Filehandling/student.json", "w") as json_file:
    json.dump(student, json_file, indent=4)

    # reading json file
with open("Filehandling/student.json", "r") as json_file:
    data = json.load(json_file)
    print(data)

