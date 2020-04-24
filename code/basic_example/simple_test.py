#!/usr/bin/python

import unittest

def potato_function(num1, num2):
    return num1 + num2

def sweet_potato_function(element, list):
    list.append(element)
    return list

class TestPotatoFunctions(unittest.TestCase):

    def test_potato(self):
        #Arrange
        #Act
        #Assert
        self.assertEqual(4, potato_function(2, 2))

    def test_sweet_potato(self):
        #Arrange
        expected = [1, 2, 3, 4]
        
        #Act
        result = sweet_potato_function(4, [1, 2, 3])
        
        #Assert
        self.assertIn(4, result)    

if __name__ == '__main__':
    unittest.main()

