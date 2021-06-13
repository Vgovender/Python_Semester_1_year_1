import unittest
from io import StringIO
import sys
from test_base import captured_io
from test_base import run_unittests
import mastermind
from unittest.mock import patch


def get_answer_input():
    return input('Enter your guess: ') 


class MyTestCase(unittest.TestCase):
    def test_create_code(self):
        for x in range(100):
            self.assertEqual(len(mastermind.create_code()),4)
            for i in range(4):
                self.assertGreater(mastermind.create_code()[i],0)
                self.assertLess(mastermind.create_code()[i],9)
    
    def test_check_correctness(self):
        self.assertTrue(mastermind.check_correctness(0,4))
        self.assertFalse(mastermind.check_correctness(0,3))
        self.assertFalse(mastermind.check_correctness(0,2))
        self.assertFalse(mastermind.check_correctness(0,1))
        self.assertFalse(mastermind.check_correctness(0,0))
    
    @patch("sys.stdin", StringIO("123\n12345\nasdf\n1234"))
    def test_get_answer_input(self):
        self.assertEqual(mastermind.get_answer_input(),"1234")
    
    @patch("sys.stdin", StringIO("4321\n1234\n1267\n1234"))
    def test_take_turn(self):
        self.assertEqual(mastermind.take_turn([1,2,3,4], "4321"), (0, 4))
        self.assertEqual(mastermind.take_turn([1,2,3,4], "1234"), (4, 0))
        self.assertEqual(mastermind.take_turn([1,2,3,4], "1267"), (2, 0))
        self.assertEqual(mastermind.take_turn([1,2,3,4], "1243"), (2, 2))


if __name__ == "__main__":
    unittest.main()