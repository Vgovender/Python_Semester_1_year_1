import random
import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import robot
class MyTestCase(unittest.TestCase):

    def test_off_lowercase(self):
        with captured_io(StringIO('hal\noff')) as (out,err):
            random.randint = lambda a, b: 0
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
        self.maxDiff == None
        with captured_io(StringIO('hal\nhelp\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula

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
        with captured_io(StringIO('hal\nright\nforward 109\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned right.
 > hal now at position (0,0).
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
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 5 steps.
 > hal moved forward by 4 steps.
 > hal moved forward by 3 steps.
 > hal moved forward by 2 steps.
 > hal moved forward by 1 steps.
 > hal now at position (0,15).
hal: What must I do next? hal: Shutting down..
'''
        self.maxDiff == None
        self.assertEqual(output,value)


    def test_replay(self):
        
        with captured_io(StringIO('hal\nforward 10\nforward 5\nback 2\nleft\nright\nsprint 5\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved forward by 5 steps.
 > hal now at position (0,15).
hal: What must I do next?  > hal moved back by 2 steps.
 > hal now at position (0,13).
hal: What must I do next?  > hal turned left.
 > hal now at position (0,13).
hal: What must I do next?  > hal turned right.
 > hal now at position (0,13).
hal: What must I do next?  > hal moved forward by 5 steps.
 > hal moved forward by 4 steps.
 > hal moved forward by 3 steps.
 > hal moved forward by 2 steps.
 > hal moved forward by 1 steps.
 > hal now at position (0,28).
hal: What must I do next? hal: Shutting down..
'''
        self.maxDiff == None
        self.assertEqual(output,value)


    def test_replay_silent(self):
        with captured_io(StringIO('HAL\nforward 10\nforward 5\nreplay silent\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL replayed 2 commands silently.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_replay_reversed(self):
        with captured_io(StringIO('hal\nforward 10\nforward 5\nreplay reversed\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved forward by 5 steps.
 > hal now at position (0,15).
hal: What must I do next?  > hal moved forward by 5 steps.
 > hal now at position (0,20).
 > hal moved forward by 10 steps.
 > hal now at position (0,30).
 > hal replayed 2 commands in reverse.
 > hal now at position (0,30).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)


    def test_replay_reversed_silent(self):
        with captured_io(StringIO('hal\nforward 10\nforward 5\nreplay reversed silent\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved forward by 5 steps.
 > hal now at position (0,15).
hal: What must I do next?  > hal replayed 2 commands in reverse silently.
 > hal now at position (0,30).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)


    def test_replay_n(self):
        with captured_io(StringIO('hal\nforward 10\nforward 5\nreplay 2\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved forward by 5 steps.
 > hal now at position (0,15).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,25).
 > hal moved forward by 5 steps.
 > hal now at position (0,30).
 > hal replayed 2 commands.
 > hal now at position (0,30).
hal: What must I do next? hal: Shutting down..
'''
        self.assertEqual(output,value)


    def test_replay_n_m(self):
        with captured_io(StringIO('hal\nforward 10\nright\nforward 10\nright\nforward 5\nreplay 3-1\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal turned right.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (10,10).
hal: What must I do next?  > hal turned right.
 > hal now at position (10,10).
hal: What must I do next?  > hal moved forward by 5 steps.
 > hal now at position (10,5).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (10,-5).
 > hal turned right.
 > hal now at position (10,-5).
 > hal replayed 2 commands.
 > hal now at position (10,-5).
hal: What must I do next? hal: Shutting down..
'''
        self.maxDiff == None
        self.assertEqual(output,value)


    def test_replay_silent_n(self):
        with captured_io(StringIO('hal\nforward 10\nright\nforward 10\nright\nforward 5\nreplay silent 2\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal turned right.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (10,10).
hal: What must I do next?  > hal turned right.
 > hal now at position (10,10).
hal: What must I do next?  > hal moved forward by 5 steps.
 > hal now at position (10,5).
hal: What must I do next?  > hal replayed 2 commands silently.
 > hal now at position (5,5).
hal: What must I do next? hal: Shutting down..
'''
        self.maxDiff == None
        self.assertEqual(output,value)

    
    def test_replay_silent_n_m(self):
        with captured_io(StringIO('hal\nforward 10\nright\nforward 10\nright\nforward 5\nreplay silent 2-1\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal turned right.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (10,10).
hal: What must I do next?  > hal turned right.
 > hal now at position (10,10).
hal: What must I do next?  > hal moved forward by 5 steps.
 > hal now at position (10,5).
hal: What must I do next?  > hal replayed 1 commands silently.
 > hal now at position (10,5).
hal: What must I do next? hal: Shutting down..
'''
        self.maxDiff == None
        self.assertEqual(output,value)


    def test_replay_reversed_n(self):
        with captured_io(StringIO('hal\nforward 10\nright\nreplay reversed 2\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal turned right.
 > hal now at position (0,10).
hal: What must I do next?  > hal turned right.
 > hal now at position (0,10).
 > hal moved forward by 10 steps.
 > hal now at position (0,0).
 > hal replayed 2 commands in reverse.
 > hal now at position (0,0).
hal: What must I do next? hal: Shutting down..
'''
        self.maxDiff == None
        self.assertEqual(output,value)


    def test_replay_reversed_n_m(self):
        with captured_io(StringIO('hal\nforward 10\nright\nreplay reversed 2-1\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal turned right.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (10,10).
 > hal replayed 1 commands in reverse.
 > hal now at position (10,10).
hal: What must I do next? hal: Shutting down..
'''
        self.maxDiff == None
        self.assertEqual(output,value)


    def test_replay_reversed_silent_n(self):
        with captured_io(StringIO('hal\nforward 10\nright\nreplay reversed silent 2\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal turned right.
 > hal now at position (0,10).
hal: What must I do next?  > hal replayed 2 commands in reverse silently.
 > hal now at position (0,0).
hal: What must I do next? hal: Shutting down..
'''
        self.maxDiff == None
        self.assertEqual(output,value)


    def test_replay_reversed_silent_n_m(self):
        with captured_io(StringIO('hal\nforward 10\nright\nreplay reversed silent 2-1\noff')) as (out,err):
            robot.robot_start()
        output = out.getvalue()
        # print(output)
        value ='''What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal turned right.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (10,10).
 > hal replayed 1 commands in reverse silently.
 > hal now at position (10,10).
hal: What must I do next? hal: Shutting down..
'''
        self.maxDiff == None
        self.assertEqual(output,value)