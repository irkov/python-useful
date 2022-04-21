'''Generate any passoword'''

import random

def random_pass(length):
    lower = ['abcdefghijklmnopqrstuvwxyz']
    upper = ['ABCDEFGHIKLMNOPQRSTUVWXYZ']
    numbers = ['1234567890']
    symbols = ['!@#$%^&*().']

    string = "".join(lower + upper + numbers + symbols)

    password = "".join(random.sample(string, length))
    return password



if __name__ == '__main__':

    for i in range(16):
        print('Your password is:', random_pass(i))
