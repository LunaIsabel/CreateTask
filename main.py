__author__ = "Luna"
__copyright__ = "Copyright (c) 2019 Isabel Luna"
__credits__ = ["Luna, Isabel"]
__license__ = "MIT lisence"

# import for random story
import random

def endings():
    ending1 = 'You died'
    ending2 = 'You become hero'
    ending3 = 'Live ordinary life'
    ending_list = [ending1, ending2, ending3]
    chosen_ending = random.choice(ending_list)
    print(chosen_ending)

def question_name():
    print('What\'s your name?')
    name = input(' ')
    return name

def question_gender():
    print('Are you female or male?')
    gender = input('')
    return gender

def start_story(name, gender):
    pass
name = question_name()
gender = question_gender();
start_story(name, gender)
