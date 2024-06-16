# -*- coding: utf-8 -*-

'''
日期:20240616
修改人员:流明Lumen
内容:20240616学术英语二级英语口语随机题目小程序
'''


import random

if __name__ == '__main__':
    
    key = 'o'
    
    while key != 'q':
        
        num = random.randint(0,5)
        
        if num == 0:
            
            print("Which one do you prefer, a new energy vehicle or a traditional IC engine vehicle? Explain your reasons.")
    
            key = input()
    
        if num == 1:
            
            print("What do you know about Mars? Explain the importance of space exploration.")

            key = input()
            
        if num == 2:
            
            print("What do you think is the best type of green energy to promote? Explain your reasons.")
            
            key = input()
            
        if num == 3:
            
            print("Why do you think Darwin/Lincoln is so great? Who do you think is greater? Explain your reasons.")
            
            key = input()
        
        if num == 4:
            
            print("What is the value of positive emotion? How to cultivate a positive attitude towards life?")
            
            key = input()
            
        if num == 5:
            
            print("What do you think are the causes of climate change? What are possible solutions to global climate change?")
            
            key = input()
            





