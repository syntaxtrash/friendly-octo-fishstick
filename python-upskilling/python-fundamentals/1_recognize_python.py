num1 = 42  # variable declaration, Data Types - Primitive - Numbers
num2 = 2.3  # variable declaration, Data Types - Primitive - Numbers
boolean = True  # variable declaration, Data Types - Primitive - Boolean
string = 'Hello World'  # variable declaration, Data Types - Primitive - Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # variable declaration, Data Types - Composite - List - initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # variable declaration, Data Types - Composite - Dictionary - initialize
fruit = ('blueberry', 'strawberry', 'banana')  # variable declaration, Data Types - Composite - Tuples - initialize

print(type(fruit))  # log statement, type check
print(pizza_toppings[1])  # log statement, Data Types - Composite - List - access value
pizza_toppings.append('Mushrooms')  # Data Types - Composite - List - add value
print(person['name'])  # log statement, Data Types - Composite - Dictionary - access value
person['name'] = 'George'  # Data Types - Composite - Dictionary - change value
person['eye_color'] = 'blue'  # Data Types - Composite - Dictionary - add value
print(fruit[2])  # log statement, Data Types - Composite - Tuples - access value

if num1 > 45:  # conditional - if
    print("It's greater")  # log statement
else:  # conditional - else
    print("It's lower")  # log statement

if len(string) < 5:  # length check, conditional - if
    print("It's a short word!")  # log statement
elif len(string) > 15:  # length check, conditional - else if
    print("It's a long word!")  # log statement
else:  # conditional - else
    print("Just right!")  # log statement

for x in range(5):  # for loop - start, stop, increment, sequence
    print(x)  # log statement
for x in range(2, 5):  # for loop - start, stop, increment, sequence
    print(x)  # log statement
for x in range(2, 10, 3):  # for loop - start, stop, increment, sequence
    print(x)  # log statement
x = 0  # variable declaration
while(x < 5):  # while loop - start, stop, increment
    print(x)  # log statement
    x += 1  # while loop - increment

pizza_toppings.pop()  # Data Types - Composite - List - delete value
pizza_toppings.pop(1)  # Data Types - Composite - List - delete value

print(person)  # log statement
person.pop('eye_color')  # Data Types - Composite - Dictionary - delete value
print(person)  # log statement

for topping in pizza_toppings:  # for loop - sequence
    if topping == 'Pepperoni':  # conditional - if
        continue  # for loop - continue
    print('After 1st if statement')  # log statement
    if topping == 'Olives':  # conditional - if
        break  # for loop - break

def print_hello_ten_times():  # function - parameter
    for num in range(10):  # for loop - start, stop, increment, sequence
        print('Hello')  # log statement

print_hello_ten_times()  # function - argument

def print_hello_x_times(x):  # function - parameter
    for num in range(x):  # for loop - start, stop, increment, sequence
        print('Hello')  # log statement

print_hello_x_times(4)  # function - argument

def print_hello_x_or_ten_times(x = 10):  # function - parameter, Data Types - Primitive - Numbers
    for num in range(x):  # for loop - start, stop, increment, sequence
        print('Hello')  # log statement

print_hello_x_or_ten_times()  # function - argument
print_hello_x_or_ten_times(4)  # function - argument

"""
Bonus section
"""

# print(num3)  # log statement, NameError: name <variable name> is not defined
# num3 = 72  # variable declaration
# fruit[0] = 'cranberry'  # Data Types - Composite - Tuples - change value, TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])  # log statement, KeyError: 'favorite_team'
# print(pizza_toppings[7])  # log statement, IndexError: list index out of range
#   print(boolean)  # log statement, IndentationError: unexpected indent
# fruit.append('raspberry')  # Data Types - Composite - Tuples - add value, AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  # Data Types - Composite - Tuples - delete value, AttributeError: 'tuple' object has no attribute 'pop'
