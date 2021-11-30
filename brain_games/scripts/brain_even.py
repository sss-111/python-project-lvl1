#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    a = 0
    while a < 3:
        number = random.randint(0, 50)
        if number % 2:
            answer = 'no'
        else:
            answer = 'yes'
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
