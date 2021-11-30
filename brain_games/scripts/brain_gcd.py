#!/usr/bin/env python3
import prompt
import random
import math


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    a = 0
    while a < 3:
        number1 = random.randint(0, 50)
        number2 = random.randint(0, 50)
        answer = math.gcd(number1, number2)
        print('Question: ' + str(number1) + ' ' + str(number2))
        answer_user = prompt.string('Your answer: ')
        if str(answer_user) == str(answer):
            print('Correct!')
        else:
            print("'" + str(answer_user)
                  + "' is wrong answer ;(. Correct answer was '"
                  + str(answer) + "'.")
            print("Let's try again, " + name + '!')
            break
        if a == 2:
            print('Congratulations, ' + name + '!')
        a = a + 1
