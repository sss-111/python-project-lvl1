#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    a = 0
    while a < 3:
        number = random.randint(0, 100)
        d = 2
        while number % d != 0:
            d = d + 1
        if d == number:
            answer = 'yes'
        else:
            answer = 'no'
        print('Question: ' + str(number))
        answer_user = prompt.string('Your answer: ')
        if str(answer_user) == str(answer):
            print('Correct!')
        else:
            print("'" + answer_user
             + "' is wrong answer ;(. Correct answer was '"
             + answer + "'.")
            print("Let's try again, " + name + '!')
            break
        if a == 2:
            print('Congratulations, ' + name + '!')
        a = a + 1
