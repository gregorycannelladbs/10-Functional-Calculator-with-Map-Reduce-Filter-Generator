# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:15:09 2020

@author: Greg
"""

from calculator_class import Calculator

# Process operation function
def process_operation():
    loop_back = 'y'
    while loop_back == 'y':
        
        # user input to select operation type
        print("\nSelect operation")
        print("1. Add two lists")
        print("2. Add two lists the Guido van Rossum's way")
        print("3. Even numbers in a list")
        print("4. Even numbers in a list the Guido van Rossum's way")
        print("5. Odd numbers in a list")
        print("6. Odd numbers in a list the Guido van Rossum's way")
        print("7. Max value in a list")
        print("8. Min value in a list")
        print("9. Fibonacci of numbers in a list using recursion")
        print("10. Fibonacci of numbers in a list using recursion and memorisation")
        print("11. Fibonacci sequence generator up to n elements")
        print("12. Square generator of a list of numbers the Guido van Rossum's way")
        
        try:
            choice = int(input("\nEnter choice: "))

            if choice in range(1,3):
                try:
                    lst1 = [eval(num) for num in input("Enter the numbers of the first list separated by space: ").strip().split()]
                    lst2 = [eval(num) for num in input("Enter the numbers of the second list separated by space: ").strip().split()]
                
                    if choice == 1:
                        print("\nThe added values are: ", Calculator.add(lst1, lst2))
                    
                    elif choice == 2:
                        print("\nThe added values are: ", Calculator.add_lst_comp(lst1, lst2))
                
                except (NameError, SyntaxError, TypeError):
                    print("\nWarning: only enter numbers")
                        
            elif choice in range(2,13):
                try:
                    lst = [eval(num) for num in input("Enter the list numbers separated by space: ").strip().split()]
                
                    if choice == 3:
                        print("\nThe even numbers are: ", Calculator.even(lst))
                    
                    elif choice == 4:
                        print("\nThe even numbers are: ", Calculator.even_lst_comp(lst))
                    
                    elif choice == 5:
                        print("\nThe odd numbers are: ", Calculator.odd(lst))
                        
                    elif choice == 6:
                        print("\nThe odd numbers are: ", Calculator.odd_lst_comp(lst))
                    
                    elif choice == 7:
                        print("\nThe maximum value is: ", Calculator.max_value(lst))
                    
                    elif choice == 8:
                        print("\nThe minimum value is: ", Calculator.min_value(lst))
                    
                    elif choice == 9:
                        print("\nThe fibonacci numbers are: ", Calculator.fib_recursion(lst))
                    
                    elif choice == 10:
                        print("\nThe fibonacci numbers are: ", Calculator.fib_recursion_memo(lst))
                        
                    elif choice == 11:
                        fibonacci = Calculator.fib_gen(lst)
                        answer = 'y'
                        while answer == 'y':
                            try:
                                print("\nThe next fibonacci is", next(fibonacci))
                                answer = input("Do you want to see the next fibonacci'y/n'? ")
                            
                            except StopIteration:
                                print("\nYou have now seen all fibonacci numbers")
                                answer = input("Enter 'n' to exit fibonacci numbers: ")
                    
                    elif choice == 12:
                        square = Calculator.square_gen_comp(lst) 
                        answer = 'y'
                        while answer == 'y':
                            try:
                                print("\nThe next square is", next(square))
                                answer = input("Do you want to see the next square number'y/n'? ")
                            
                            except StopIteration:
                                print("\nYou have now seen all square numbers")
                                answer = input("Enter 'n' to exit square numbers: ")
                
                except (NameError, SyntaxError, TypeError):
                    print("\nWarning: only enter numbers")
                    
        # Any other choice that is not in the expected list
        except ValueError:
            print("\nWarning: choice must be an integer between 1 and 12")
            
        # user input for loop_back          
        loop_back = input("\nDo you want to compute another operation 'y/n'? ")

# Process operation
process_operation()