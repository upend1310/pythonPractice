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


def loops():
    i = 1
    while i <= 10:
        print(i)
        i += 1


loops()


def raise_to_power(num, power):
    return num ** power


print(raise_to_power(3, 5))


def raise_to_power_using_for(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power_using_for(3, 2))
