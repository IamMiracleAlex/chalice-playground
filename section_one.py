# Section One

# 1
array = ["Alice", "Bob", "Jeremy", "Sam", "Henry", "Sarah", "Ashley"]

# a
for i in array:
    print("Hello my name is ", i)

# b
print(array[0], array[2], array[4], array[6])

#c
print(array[::-1])

# d
print(array[-1])


#2
def calculator(a, b, operator):
    add = lambda a, b: a + b
    subtract = lambda a, b: a - b
    multiply = lambda a, b: a * b
    divide = lambda a, b: a / b

    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise ArithmeticError('Please input a number')

    if operator in ['+', 'add']:
        return add(a, b)

    elif operator in ['-', 'subtract']:
        return subtract(a, b)

    elif operator in ['*', 'multiply']:
        return multiply(a, b)

    elif operator in ['/', 'divide']:
        return divide(a, b)


# 3
class Users:

    def __init__(username, password):
        self.username = username
        self.password = password

    def store_users(self, username, password):
        with open('users.txt', 'a') as f:
            f.write('{},{},'.format(username, password))

    def verify_password(self, password):
        with open('users.txt') as f:
            lines = f.readlines()
            for line in lines:
                if password in line:
                    print("Password Found..!")

