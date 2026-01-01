# foor loop

for i in range(5):
    print("Iteration:", i)
# while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1      
# nested loop
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)
# loop with break
for i in range(10):
    if i == 5:
        break
    print("Breaking at:", i)
# loop with continue
for i in range(10):
    if i % 2 == 0:
        continue
    print("Odd number:", i)
# loop with else
for i in range(3):
    print("Looping:", i)
else:
    print("Loop completed")
# loop with pass
for i in range(5):
    if i == 2:
        pass
    print("Value:", i)
# loop with nested functions
for i in range(3):
    def inner_function(x):
        return x * 2
    print("Inner function result for", i, "is", inner_function(i))
# loop with list comprehension
squares = [x**2 for x in range(5)]
print("Squares:", squares)
# loop with generator expression
cubes = (x**3 for x in range(5))
for cube in cubes:
    print("Cube:", cube)
# loop with enumerate
for index, value in enumerate(['a', 'b', 'c']):
    print("Index:", index, "Value:", value)
# loop with zip
for a, b in zip([1, 2, 3], ['x', 'y', 'z']):
    print("A:", a, "B:", b)
# loop with dictionary
my_dict = {'one': 1, 'two': 2, 'three': 3}
for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
# loop with set
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print("Set item:", item)
# loop with string
my_string = "hello"
for char in my_string:
    print("Character:", char)
# loop with file
with open('sample.txt', 'w') as f:
    f.write("Line 1\nLine 2\nLine 3\n")
with open('sample.txt', 'r') as f:
    for line in f:
        print("File line:", line.strip())
# loop with range step
for i in range(0, 10, 2):
    print("Even number:", i)
# loop with reversed
for i in reversed(range(5)):
    print("Reversed:", i)
# loop with sorted
unsorted_list = [3, 1, 4, 2]
for item in sorted(unsorted_list):
    print("Sorted item:", item)
# loop with itertools
import itertools
for combo in itertools.combinations(['a', 'b', 'c'], 2):
    print("Combination:", combo)
# loop with time delay
import time
for i in range(3):
    print("Sleeping iteration:", i)
    time.sleep(1)
# loop with exception handling
for i in range(5):
    try:
        if i == 3:
            raise ValueError("An error occurred at i=3")
        print("Value:", i)
    except ValueError as e:
        print(e)
# loop with multiprocessing
from multiprocessing import Pool
def square(x):
    return x * x
with Pool(4) as p:
    results = p.map(square, range(5))
    print("Multiprocessing results:", results)
# loop with threading
from threading import Thread
def print_number(num):
    print("Thread number:", num)
threads = []
for i in range(5):
    t = Thread(target=print_number, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
# loop with async
import asyncio
async def async_loop():
    for i in range(3):
        print("Async iteration:", i)
        await asyncio.sleep(1)
asyncio.run(async_loop())
# loop with map
def double(x):
    return x * 2
doubled_values = list(map(double, range(5)))
print("Doubled values:", doubled_values)
# loop with filter
def is_even(x):
    return x % 2 == 0
even_values = list(filter(is_even, range(10)))
print("Even values:", even_values)
# loop with reduce
from functools import reduce
def add(x, y):
    return x + y
sum_value = reduce(add, range(5))
print("Sum value:", sum_value)
# loop with itertools.cycle
import itertools
counter = 0
for item in itertools.cycle(['A', 'B', 'C']):
    if counter >= 6:
        break
    print("Cycled item:", item)
    counter += 1
# loop with itertools.count
import itertools
for i in itertools.islice(itertools.count(10), 5):
    print("Counted item:", i)
# loop with itertools.chain
import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print("Chained item:", item)
# loop with itertools.groupby
import itertools
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4)]
for key, group in itertools.groupby(data, lambda x: x[0]):
    print("Key:", key, "Group:", list(group))
# loop with itertools.permutations
import itertools
for perm in itertools.permutations(['X', 'Y', 'Z']):
    print("Permutation:", perm)
# loop with itertools.product
import itertools
for prod in itertools.product([1, 2], ['a', 'b']):
    print("Product:", prod)
# loop with itertools.starmap
import itertools
def multiply(x, y):
    return x * y
data = [(2, 3), (4, 5)]
for result in itertools.starmap(multiply, data):
    print("Starmap result:", result)
# loop with itertools.tee
import itertools
data = itertools.tee(range(5), 2)
for item in data[0]:
    print("Tee item from first iterator:", item)
for item in data[1]:
    print("Tee item from second iterator:", item)
# loop with itertools.islice
import itertools
for item in itertools.islice(range(10), 2, 8, 2):
    print("Islice item:", item)
# loop with itertools.filterfalse
import itertools
def is_odd(x):
    return x % 2 != 0
for item in itertools.filterfalse(is_odd, range(10)):
    print("Filterfalse item (even numbers):", item)
# loop with itertools.accumulate
import itertools
for total in itertools.accumulate(range(5)):
    print("Accumulate total:", total)
# loop with itertools.zip_longest
import itertools
for a, b in itertools.zip_longest([1, 2, 3], ['x', 'y']):
    print("Zip longest A:", a, "B:", b)
# loop with itertools.repeat
import itertools
for item in itertools.repeat('Hello', 3):
    print("Repeated item:", item)
# loop with itertools.slice
import itertools
for item in itertools.islice(range(20), 5):
    print("Sliced item:", item)
# loop with itertools.compress
import itertools
data = range(10)
selectors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
for item in itertools.compress(data, selectors):
    print("Compressed item:", item)
# loop with itertools.dropwhile
import itertools
def less_than_five(x):
    return x < 5
for item in itertools.dropwhile(less_than_five, range(10)):
    print("Dropwhile item:", item)
# loop with itertools.takewhile
import itertools
def less_than_five(x):
    return x < 5
for item in itertools.takewhile(less_than_five, range(10)):
    print("Takewhile item:", item)
# loop with itertools.cumulate
import itertools
for total in itertools.accumulate(range(1, 6)):
    print("Cumulative total:", total)
# loop with itertools.pairwise
import itertools
for a, b in itertools.pairwise(['A', 'B', 'C', 'D']):
    print("Pairwise A:", a, "B:", b)

# loop with itertools.product
import itertools
for prod in itertools.product([1, 2], ['x', 'y']):
    print("Product:", prod)
# loop with itertools.permutations
import itertools
for perm in itertools.permutations(['X', 'Y', 'Z']):
    print("Permutation:", perm)
    

