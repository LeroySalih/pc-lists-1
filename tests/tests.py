"""
level-3::for-3
"""

from testengine import *
from subprocess import run
import io
import sys


from main import *

import random

class MainTestEngine (TestEngine):

    def __init__(self, label):
        super().__init__(label);

    #Check a Def Exists
    
    def test_def_exists(self):
      self.assertDefExists("pupil_names")
    

    #Check the result of a def

    # def IsValid_UserChoice_Y(self):
    #     result = IsValid_Choice("Y")
    #     expected = True
    #     self.assertEqual( expected, result, f"\nExpected: {expected}.\nReceived:{result}")

    
    #Check the output

    # def test_output_is_correct(self): 
    #   user_input=b"A\ny\nn\Y"    
    #   result = run(["python", "main.py"], input=user_input, capture_output=True)
        
    #   expected = b"Enter a choice (Y/N)Incorrect choice, try again.\nEnter a choice (Y/N)Incorrect choice, try again.\nEnter a choice (Y/N)Incorrect choice, try again.\nEnter a choice (Y/N)"

    #   self.assertEqual(expected,  result.stdout, "\nExpected:\n{0}\nReceived:\n{1}".format(expected, result.stdout))

    def test_def_returns_correct_number(self):
      result = pupil_names()
      
      expected = str(3)
      actual = str(len(result))   

      self.assertEqual(bytes(expected, 'utf-8'), bytes(actual, 'utf-8'), "\nExpected:\n{0}\Actual:\n{1}".format(expected, actual))

    def test_def_returns_correct_names(self):
      result = pupil_names()

      expected = 'Ali'
      actual = result[0]    

      self.assertEqual(bytes(expected, 'utf-8'), bytes(actual, 'utf-8'), "\nExpected:\n{0}\Actual:\n{1}".format(expected, actual))

      expected = 'Bert'
      actual = result[1]    

      self.assertEqual(bytes(expected, 'utf-8'), bytes(actual, 'utf-8'), "\nExpected:\n{0}\Actual:\n{1}".format(expected, actual))

      expected = 'Charles'
      actual = result[2]    

      self.assertEqual(bytes(expected, 'utf-8'), bytes(actual, 'utf-8'), "\nExpected:\n{0}\Actual:\n{1}".format(expected, actual))

      




    # def test_def_output_is_correct(self):
    #  capturedOutput = io.StringIO()                  # Create StringIO object
    # sys.stdout = capturedOutput                     #  and redirect stdout.

      #execute the def
     # area_of_rect(24, 20)
      
     # sys.stdout = sys.__stdout__                     # Reset redirect.
      
     # expected = ""
     # actual = capturedOutput.getvalue()              # Now works as before.

     # self.assertEqual(bytes(expected, 'utf-8'), bytes(actual, 'utf-8'), "\nExpected:\n{0}\Actual:\n{1}".format(expected, actual))
      



    def getTests(self):
        return [
          self.test_def_exists,
          self.test_def_returns_correct_number,
          self.test_def_returns_correct_names
        ]