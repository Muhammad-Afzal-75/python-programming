#store data in key-value pares

student = {
    "name" : "Afzal",
    "age" : 25,
    "city" : "Karachi",
    "Number" : 3070701703
}
print(student)

#dictionary methods
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
student["age"] = 26
print(student)
student["country"] = "Pakistan"
print(student)
del student["city"]
print(student)
student.pop("Number")
print(student)
student.popitem()
print(student)
student.clear()
print(student)
#nested dictionary
students = {
    "student1": {
        "name": "Afzal",
        "age": 25
    },
    "student2": {
        "name": "Aisha",
        "age": 22
    }
}
print(students)
for key, value in students.items():
    print(f"{key}: {value}")


#loop through dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")
for value in person.values():
    print(value)
for key in person.keys():
    print(key)
#dictionary comprehension
squares = {x: x**2 for x in range(6)}
print(squares)
#filtering with dictionary comprehension
even_squares = {x: x**2 for x in range(6) if x
    % 2 == 0}
print(even_squares) 
#merging dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}

print(merged_dict)
#using fromkeys()
keys = ['name', 'age', 'city']
default_value = None
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
#using setdefault()
person = {'name': 'Alice', 'age': 28}
city = person.setdefault('city', 'Unknown')
print(person)
print(f"City: {city}")
#using update()
person = {'name': 'Bob', 'age': 32}
person.update({'age': 33, 'city': 'Los Angeles'})
print(person)
#dictionary with different data types
mixed_dict = {
    'integer': 42,
    'float': 3.14,
    'string': 'Hello, World!',
    'list': [1, 2, 3],
    'tuple': (4, 5, 6),
    'set': {7, 8, 9},
    'boolean': True,
    'none': None
}
print(mixed_dict)
for key, value in mixed_dict.items():
    print(f"{key}: {value} (type: {type(value)})")
#dictionary with tuple keys
tuple_key_dict = {
    (1, 2): "Point A",
    (3, 4): "Point B",
    (5, 6): "Point C"
}
print(tuple_key_dict)
for key, value in tuple_key_dict.items():
    print(f"{key}: {value}")
#dictionary with frozenset keys
frozenset_key_dict = {
    frozenset([1, 2, 3]): "Set A",
    frozenset([4, 5, 6]): "Set B"
}
print(frozenset_key_dict)
for key, value in frozenset_key_dict.items():
    print(f"{key}: {value}")
#dictionary with complex number keys
complex_key_dict = {
    complex(1, 2): "Complex A",
    complex(3, 4): "Complex B"
}
print(complex_key_dict)
for key, value in complex_key_dict.items():
    print(f"{key}: {value}")
        