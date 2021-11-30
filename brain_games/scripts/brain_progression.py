#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    a = 0
    while a < 3:
        count = random.randint(7, 25)
        number = random.randint(0, 50)
        step = random.randint(0, 50)
        pr = random.randint(1, count - 1)
        string = str(number)
        for i in range(1, count):
            if i == pr:
                string = string + ' ..'
                answer = number + step * i
            else:
                string = string + ' ' + str(number + step * i)
        print('Question: ' + string)
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
