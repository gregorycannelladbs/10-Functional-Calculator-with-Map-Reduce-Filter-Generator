# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:51:35 2020

@author: Greg
"""
from functools import reduce
class Calculator:
    
    @staticmethod
    def add(lst1, lst2):
        '''Takes two lists of numeric values, if lists have unequal length,
            resise to match the shortest list lenghth and returns a list of
            added values based on index position'''
        return list(map(lambda x,y:x+y, lst1,lst2))
        
    @staticmethod
    def add_lst_comp(lst1, lst2):
        '''Takes two lists of numeric values, if lists have unequal length,
            resise to match the shortest list lenghth and returns a list of
            added values based on index position'''
        if len(lst1) > len(lst2):
            lst1 = lst1[:len(lst2)]
        
        elif len(lst1) < len(lst2):
            lst2 = lst2[:len(lst1)]

        else:
            pass

        return [x + lst2[lst1.index(x)] for x in lst1]
    
    @staticmethod
    def even(lst):
        '''Takes a list of numeric values and returns a list of even numbers'''
        return list(filter(lambda x: x%2==0, lst))
    
    @staticmethod
    def even_lst_comp(lst):
        '''Takes a list of numeric values and returns a list of even numbers'''
        return [x for x in lst if x%2==0]
    
    @staticmethod
    def odd(lst):
        '''Takes a list of numeric values and returns a list of odd numbers'''
        return list(filter(lambda x: x%2, lst))

    @staticmethod
    def odd_lst_comp(lst):
        '''Takes a list of numeric values and returns a list of odd numbers'''
        return [x for x in lst if x%2]
    
    @staticmethod
    def max_value(lst):
        '''Takes a list of numeric values and returns the maximum value'''
        return reduce(lambda x,y: x if x>y else y, lst)
    
    @staticmethod
    def min_value(lst):
        '''Takes a list of numeric values and returns the minimum value'''
        return reduce(lambda x,y: x if x<y else y, lst)

    @staticmethod
    def fib_recursion(lst):
        ''' Takes a list of integers >= 0 denominated x and
            returns a list of fibonacci of x using recursion'''    
        def fibonacci(x):
            if x == 0:
                return 0
            
            elif x == 1:
                return 1
            
            else:
                return fibonacci(x-1) + fibonacci(x-2)
        try:
            return [fibonacci(x) for x in lst]
        
        except RecursionError:
            print('\nWarning: only enter integers >= 0')

    @staticmethod
    def fib_recursion_memo(lst):
        ''' Takes a list of integers >= 0 denominated x and
            returns a list of fibonacci of x using recursion
            and memorisation for better speed performance''' 
        d = {0:0, 1:1}
        def fibonacci(x, d):
            if x in d:
                return d[x] 
            else:
                answer = fibonacci(x-1, d) + fibonacci(x-2, d)
                d[x] = answer
                return answer
        
        try:
            return [fibonacci(x, d) for x in lst]
        
        except RecursionError:
            print('\nWarning: only enter integers >= 0')

    
    @staticmethod
    def fib_gen(lst):
        ''' Takes a list of integers >= 0 and returns full fibonnaci sequence 
            from 0 up to x elements as a generator'''         
        for i in lst:
            a = 0
            b = 1
            counter = 0
            while counter < i:
                yield a
                c = a
                a = b
                b = c + b
                counter += 1
    
    @staticmethod
    def square_gen_comp(lst):
        '''Takes a list of numeric values and returns a list of the square 
            of each value'''
        return (x**2 for x in lst)