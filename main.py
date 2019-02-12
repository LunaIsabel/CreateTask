__author__ = "Luna"
__copyright__ = "Copyright (c) 2019 Isabel Luna"
__credits__ = ["Luna, Isabel"]
__license__ = "MIT lisence"

import random

def endings():
    ending1 = 'You died'
    ending2 = 'You become hero'
    ending3 = 'Live ordinary life'
    ending_list = [ending1, ending2, ending3]
    chosen_ending = random.choice(ending_list)
    print(chosen_ending)
