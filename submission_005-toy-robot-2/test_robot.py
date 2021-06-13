import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import robot

class TestFunction(unittest.TestCase):
    def test_off_lowercase(self):
        with captured_io(StringIO('hal\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)
    
    def test_off_mixed_case(self):
        with captured_io(StringIO('hal\nOFF')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)

    def test_off(self):
        with captured_io(StringIO('hal\nOfF')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)
    
    def test_help_off(self):
        with captured_io(StringIO('hal\nhelp\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - moves the robot forward from current position
BACK - moves the robot back from current position
RIGHT - turns the robot right
LEFT - turns the robot left
SPRINT - robot sprints

hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)

    def test_forward_10(self):
        with captured_io(StringIO('hal\nforward 10\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)
    
    def test_back_10(self):
        with captured_io(StringIO('hal\nback 10\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved back by 10 steps.
 > hal now at position (0,-10).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)

    def test_right_forward_10_off(self):
        with captured_io(StringIO('hal\nright\nforward 10\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned right.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (10,0).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)

    def test_right_right_forward_10_off(self):
        with captured_io(StringIO('hal\nright\nright\nforward 10\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned right.
 > hal now at position (0,0).
hal: What must I do next?  > hal turned right.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,-10).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)

    def test_right_right_right_forward_10_off(self):
        with captured_io(StringIO('hal\nright\nright\nright\nforward 10\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned right.
 > hal now at position (0,0).
hal: What must I do next?  > hal turned right.
 > hal now at position (0,0).
hal: What must I do next?  > hal turned right.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (-10,0).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)

    def test_left_forward_10_off(self):
        with captured_io(StringIO('hal\nleft\nforward 10\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned left.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (-10,0).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)

    def test_left_left_forward_10_off(self):
        with captured_io(StringIO('hal\nleft\nleft\nforward 10\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned left.
 > hal now at position (0,0).
hal: What must I do next?  > hal turned left.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,-10).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)
    
    def test_left_left_left_forward_10_off(self):
        with captured_io(StringIO('hal\nleft\nleft\nleft\nforward 10\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned left.
 > hal now at position (0,0).
hal: What must I do next?  > hal turned left.
 > hal now at position (0,0).
hal: What must I do next?  > hal turned left.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (10,0).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)

    def test_forward_109(self):
        with captured_io(StringIO('hal\nforward 109\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next? hal: Sorry, I cannot go outside my safe zone.
 > hal now at position (0,0).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)

def test_sprint_5(self):
        with captured_io(StringIO('hal\nsprint 5\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? L
hal: Hello kiddo!
hal: What must I do next? sprint 5 
 > L moved forward by 5 steps.
 > L moved forward by 4 steps.
 > L moved forward by 3 steps.
 > L moved forward by 2 steps.
 > L moved forward by 1 steps.
 > L now at position (0,15).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)