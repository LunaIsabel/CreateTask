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

def story_male(name):
    print('''
You feel a gentle breeze touch your hair 
          ''')

def story_female(name):
    print('Story if person is female will go here')

if __name__ == '__main__':
    name = question_name()
    gender = question_gender();
    if gender == 'male':
        story_male(name)
    else:
        story_female(name)
