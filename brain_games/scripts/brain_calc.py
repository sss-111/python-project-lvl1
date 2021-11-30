#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    a = 0
    array = ['+', '-', '*']
    while a < 3:
        number1 = random.randint(0, 50)
        number2 = random.randint(0, 50)
        index = random.randint(0, 2)
        if index == 0:
            answer = number1 + number2
        elif index == 1:
            answer = number1 - number2
        else:
            answer = number1 * number2
        print('Question: ' + str(number1)
              + ' ' + array[index] + ' ' + str(number2))
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
