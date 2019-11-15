# -*- coding: utf-8 -*-
'''
# Created on Nov-15-19 11:34
# test003.py
# @author: liuji
'''
import os 
def main():
    print ("Hello World!")
    print ("这是Alice\'的问候")
    foo(5,20)
    print ("=" * 10)
    print ("这将直接执行"+os.getcwd())
    counter = 0
    counter += 1
    food = ['苹果','杏子','李子','鸭梨']
    for i in food:
        print ("这个水果是"+i)
    print("数到十")
    for i in range(10):
        print(i)
def foo(parmal, secondParam): 
    res = parmal+secondParam
    print("hello %s + %s = %s"%(parmal,secondParam,res))
    if res < 50:
        print ("this")
    elif (res> 50) and ((parmal==42) or (secondParam==24)):
        print("'that")
    else:
        print ("go")
    return res
if __name__ == "__main__":
    main()

#OK
                                                                                                                                                                                                                                                                    




