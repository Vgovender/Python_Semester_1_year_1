import unittest
from io import StringIO
import world.obstacles as obstacles

class MyTestCase(unittest.TestCase):


    def test_generate_random_obstacles(self):
        obstacles.random.randint = lambda a, b: 1
        obstacle_list = obstacles.generate_random_obstacles()
        self.assertEqual(obstacle_list, [(1,1)])

    def test_generate_random_obstacles2(self):
        obstacles.random.randint = lambda a, b: 0
        obstacle_list = obstacles.generate_random_obstacles()
        self.assertFalse(obstacle_list, [])


    def test_is_position_blocked(self):
        obstacles.list_of_obstacles = [(1,1)]
        self.assertEqual(obstacles.is_position_blocked(9,2), False)
        self.assertEqual(obstacles.is_position_blocked(1,1), True)

    def test_is_path_blocked(self):
        obstacles.list_of_obstacles = [(1,1)]
        self.assertEqual(obstacles.is_path_blocked(0,2, 8, 2), False)
        self.assertEqual(obstacles.is_path_blocked(0,1, 4, 1), True)

if __name__ == "__main__":
    unittest.main()