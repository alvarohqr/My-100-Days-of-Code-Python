############DEBUGGING#####################

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6) 
'''
a list index goes from 0 to n, so:
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
              0,   1,   2,   3,   4,   5
dice_num = randint(0, 5) 
'''
print(dice_imgs[dice_num])