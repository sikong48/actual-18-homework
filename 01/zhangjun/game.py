# encoding: utf-8
"""
@file: game.py
@time: 2018/3/19/0019 12:44
"""
import random

random_num = random.randint(0, 100)
input_text = input('来猜个数吧，在控制台输入个0-100之间的整数：')
count = 1
while int(input_text) != random_num:
    if count == 5:
        print('太笨了，下次再来')
        break
    input_text = input('不对，你已经猜了' + str(count) + '次，再给你一次机会：')
    count += 1
    if int(input_text) == random_num:
        print('猜对了')
