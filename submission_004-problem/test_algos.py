import unittest
import super_algos
from unittest.mock import patch
from io import StringIO


class TestFunctions(unittest.TestCase):

    def test_find_min(self):
        self.assertEqual(super_algos.find_min([1,2,3,4]),1)
        self.assertEqual(super_algos.find_min([5,6,7,8]),5)
        self.assertEqual(super_algos.find_min([18,52,34,42]),18)
        self.assertEqual(super_algos.find_min([300,200,100,400]),100)
        self.assertEqual(super_algos.find_min(['a',2,3,4]),-1)
    
    def test_sum_all(self):
        self.assertEqual(super_algos.sum_all([1,2,3,4]),10)
        self.assertEqual(super_algos.sum_all([5,6,7,8]),26)
        self.assertEqual(super_algos.sum_all([18,52,34,42]),146)
        self.assertEqual(super_algos.sum_all([90,200,300,400]),990)
        self.assertEqual(super_algos.sum_all(['a',2,3,4]),-1)

    def test_find_possible_strings(self):
        self.assertEqual(super_algos.find_possible_strings(['a','b'],2),['aa','ab','ba','bb']) 
        self.assertEqual(super_algos.find_possible_strings(['x','y'],3),['xxx','xxy','xyx','xyy','yxx','yxy','yyx','yyy'])
        self.assertEqual(super_algos.find_possible_strings(['a',2,3,4],1),[])
        self.assertEqual(super_algos.find_possible_strings([1,'2',3,4],1),[])

if __name__ == "__main__":
    unittest.main()