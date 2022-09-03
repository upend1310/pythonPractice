# Integer
day = 21
temp = -15
print(type(day))

# Float
weight = 50.67

print(3+6)
print(day+3)
print(weight*2)
print(type(weight))

# Complex Numbers
num = 4 + 3j
print(num)
print(type(num))

# String
color = 'Blue'
store = 'Upendra\'s shirt is blue. It is the "best" color'

print(store)
print(f"This color is {color}. Today its {day}.")
print("\nFirst character of String is: ")
print(store[0])
print("\nLast character of String is: ")
print(store[-1])

# Boolean
light_is_on = True
fan_is_on = False

print(light_is_on)

if light_is_on:
    print("The light is on!")
    print("Hello")
else:
    print("Light is off!")

if weight >= 50:
    print("You are overweight!")

# List
List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List[0])
print(List[2])

List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)

# Tuples - Diff between List and Tuple is that tuples are immutable
# i.e. tuples cannot be modified after it is created
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)

list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

# Set - Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)

set1 = set(["Geeks", "For", "Geeks"])
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")
print("Geeks" in set1)

# Dictionary - Dictionary in Python is an unordered collection of data values,
# used to store data values like a map in key:value pair
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("Accessing a element using key:")
print(Dict['name'])
print("Accessing a element using get:")
print(Dict.get(3))

# Operations on data types
# Can we use + for different types also?
# No use for different types would produce an error.
a = 10
b = "Geeks"
print(a+b)




