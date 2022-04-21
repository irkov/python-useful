'''Generate any passoword'''

import random

def random_pass1(length):
    lower = ['abcdefghijklmnopqrstuvwxyz']
    upper = ['ABCDEFGHIKLMNOPQRSTUVWXYZ']
    numbers = ['1234567890']
    symbols = ['!@#$%^&*().']

    string = "".join(lower + upper + numbers + symbols)

    password = "".join(random.sample(string, length))
    return password

def macos_pass():
    lower = ['abcdefghijklmnopqrstuvwxyz']
    upper = ['ABCDEFGHIKLMNOPQRSTUVWXYZ']
    numbers = ['1234567890']
    #symbols = ['!@#$%^&*().']

    string = "".join(lower + upper + numbers)

    password = "".join(random.sample(string,10))
    for i in range(2):
        password = password + '-' + "".join(random.sample(string,6))
    return password

if __name__ == '__main__':

    for i in range(20):
        print('Your password is:', macos_pass())
