def say_hi(name) -> object:
    print("Hello " + name + "!")


print("Top")
say_hi("Mike")
# say_hi() --> gives error
print("Bottom")


def cube(num):
    return num * num * num


print(cube(3))


def make_decision(temp):
    if temp > 68 or temp < 97:
        print("Its hot outside!")
    elif 50 > temp > 0:
        print("Its cold outside!")
    else:
        print("Its normal today!")


make_decision(90)
