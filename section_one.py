# Section One

# 1
def explore_array():
    array = ["Alice", "Bob", "Jeremy", "Sam", "Henry", "Sarah", "Ashley"]

    # a, print each value in the array on a new line with the prefix “Hello my name is “
    for i in array:
        print("Hello my name is ", i)

    # b, print the 1st, 3rd, 5th and 7th name.
    print(array[0], array[2], array[4], array[6])

    # c, print the array backwards
    print(array[::-1])

    # d, print the last name in the array
    print(array[-1])


#2
def calculator(a, b, operator):
    '''
    Calculator function that takes 3 parameters; a, b and operator. 
    It can add, subtract, multiply and divide the two numbers
    '''

    add = lambda a, b: a + b
    subtract = lambda a, b: a - b
    multiply = lambda a, b: a * b
    divide = lambda a, b: a / b
    result = None

    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise ArithmeticError('Please input a number')

    if operator in ['+', 'add']:
        result = add(a, b)

    elif operator in ['-', 'subtract']:
        result = subtract(a, b)

    elif operator in ['*', 'multiply']:
        result = multiply(a, b)

    elif operator in ['/', 'divide']:
        result = divide(a, b)

    return result

# 3
class Users:
    ''' 
    Stores user's password and username in a text file,
    Also allows users to verify password
    '''
    
    def store_users(self, username, password):
        with open('users.txt', 'a') as f:
            f.write('{},{},'.format(username, password))

    def verify_password(self, password):
        with open('users.txt') as f:
            lines = f.readlines()
            for line in lines:
                if password in line:
                    print(f"Password: {password} Found..!")
                    return password
