from unittest import TestCase
from TestedObject import Tested


class TestTested(TestCase):

    def test_correct(self):
        t = Tested

        self.assertTrue(t.comparing([1,2,3],[1,2,3]))

    def test_negative(self):
        t = Tested

        self.assertRaises(Exception, t.comparing([1,2,3],[5,6,7]))

    def test_notCorrect(self):
        t = Tested

        self.assertFalse(t.comparing([1,2,3],[2]))

    def test_sameType(self):
        t = Tested

        self.assertRaises(Exception, t.comparing(["a","b","c"],[1,2,3]))

    def test_empty(self):
        t = Tested

        self.assertRaises(Exception, t.comparing([],[]))

    def test_empty2(self):
        t = Tested

        self.assertRaises(Exception, t.comparing([4,8,3],[]))

    def test_empty1(self):
        t = Tested

        self.assertRaises(Exception, t.comparing([],[4,8,3]))