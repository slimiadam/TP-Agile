import morpion
import unittest
from unittest import mock 
from io import StringIO
import io 
import sys

class TestMorpion(unittest.TestCase):
            
    def test_choose_number1(self):
            user_input = "1"
            expected_result = 0
            with mock.patch('builtins.input', side_effect=user_input):
                result = morpion.choose_number()
            self.assertEqual(result, expected_result)

    def test_check_board(self):
        board = ["X", "X", "X", 4, 5, 6, 7, 8, 9]
        expected_result = True
        self.assertEqual(morpion.check_board(board), expected_result)
    
    def test_check_board2(self):
        board = ["X", "X", "O", 4, 5, "O", 7, 8, "O"]
        expected_result = True
        self.assertEqual(morpion.check_board(board), expected_result)

    def test_check_board3(self):
            board = ["X", "O", "X", "X", "O", "X", "O", "X", "O"]
            expected_result = True
            self.assertEqual(morpion.check_board(board), expected_result)

    def test_p1(self):
        user_input = "1"
        expected_result = True
        with mock.patch('builtins.input', side_effect=user_input):
            result = morpion.p1()
            self.assertEqual(result, expected_result)

    def test_p2(self):
        user_input = "2"
        expected_result = True
        with mock.patch('builtins.input', side_effect=user_input):
            result = morpion.p2()
            self.assertEqual(result, expected_result)


        


if __name__ == '__main__':
  unittest.main()