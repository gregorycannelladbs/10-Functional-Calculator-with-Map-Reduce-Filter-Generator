# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:54:57 2020

@author: Greg
"""
import unittest
from calculator_class import Calculator

class TestCalculator(unittest.TestCase):
    
    # Set up the test environement
    def setUp(self):
        self.lst1 = [1, 2, 3, 4]
        self.lst2 = [5, 6, 7, 8]
        self.lst3 = [-5, 6, 7]
        
    def test_add(self):
        self.assertEqual([6, 8, 10, 12], Calculator.add(self.lst1, self.lst2))
    
    def test_add_lst_comp(self):
        self.assertEqual([6, 8, 10, 12], Calculator.add_lst_comp(self.lst1, self.lst2))
        self.assertEqual([-4, 8, 10], Calculator.add_lst_comp(self.lst1, self.lst3))
        self.assertEqual([-4, 8, 10], Calculator.add_lst_comp(self.lst3, self.lst1))
    
    def test_even(self):
        self.assertEqual([2, 4], Calculator.even(self.lst1))
        self.assertEqual([6, 8], Calculator.even(self.lst2))

    def test_even_lst_comp(self):
        self.assertEqual([2, 4], Calculator.even_lst_comp(self.lst1))
        self.assertEqual([6, 8], Calculator.even_lst_comp(self.lst2))
        
    def test_odd(self):
        self.assertEqual([1, 3], Calculator.odd(self.lst1))
        self.assertEqual([5, 7], Calculator.odd(self.lst2))

    def test_odd_lst_comp(self):
        self.assertEqual([1, 3], Calculator.odd_lst_comp(self.lst1))
        self.assertEqual([5, 7], Calculator.odd_lst_comp(self.lst2))
    
    def test_max_value(self):
        self.assertEqual(4, Calculator.max_value(self.lst1))
        self.assertEqual(8, Calculator.max_value(self.lst2))
        
    def test_min_value(self):
        self.assertEqual(1, Calculator.min_value(self.lst1))
        self.assertEqual(5, Calculator.min_value(self.lst2))
        
    def test_fib_recursion(self):
        self.assertEqual([1, 1, 2, 3], Calculator.fib_recursion(self.lst1))
        self.assertEqual([5, 8, 13, 21], Calculator.fib_recursion(self.lst2))
        self.assertRaises(RecursionError, Calculator.fib_recursion(self.lst3))
    
    def test_fib_recursion_memo(self):
        self.assertEqual([1, 1, 2, 3], Calculator.fib_recursion_memo(self.lst1))
        self.assertEqual([5, 8, 13, 21], Calculator.fib_recursion_memo(self.lst2))
        self.assertRaises(RecursionError, Calculator.fib_recursion_memo(self.lst3))
    
    def test_fib_gen(self):
        results = [0, 1, 1, 2, 3, 5]
        lst = [5, 6]
        fibo = Calculator.fib_gen(lst)
        for i in range(lst[0]):
            self.assertEqual(results[i], next(fibo))
            
        for i in range(lst[1]):
            self.assertEqual(results[i], next(fibo))
    
    def test_square_gen_comp(self):
        lst = [-2, 3, 4, 5]
        results = [4, 9, 16, 25]
        square = Calculator.square_gen_comp(lst)
        for i in lst:
            self.assertEqual(results[lst.index(i)], next(square))
    
if __name__ == '__main__':
    unittest.main()