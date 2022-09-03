import datetime

wallet = 41

print(wallet)

wallet = 32

print(wallet)

# make a variable called day and set it equal to the date of the month

day = datetime.datetime.now().day

print(day)


# Global and Local Python Variables

# Local variables - Local variables are the ones that are defined and declared inside a function.
# We can not call this variable outside the function.
def f():
    # Local scope
    s = "Welcome geeks"
    print(s)


f()


def fn():
    print(t)


# Global scope
t = "I love Geeksforgeeks"
fn()

# Global keyword in Python - Global keyword is a keyword that allows a user
# to modify a variable outside the current scope.

# Rules of global keyword:
"""If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local unless 
explicitly declared as global. Variables that are only referenced inside a function are implicitly global. We Use 
global keyword to use a global variable inside a function. There is no need to use global keyword outside a function. 
"""
x = 15


def change():
    # using a global keyword
    global x

    # increment value of a by 5
    x = x + 5
    print("Value of x inside a function :", x)


change()
print("Value of x outside a function :", x)
