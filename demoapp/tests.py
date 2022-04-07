from django.test import TestCase
from arithmetic import Rational
import unittest

class TestArithmetic(unittest.TestCase):

    def setUp(self):
        self.rational = Rational()

    def testAdd(self):
        self.assertEqual(4, self.rational.add(2, 2))      # first test
        self.assertEqual(10, self.rational.add(3, 7))     # second test
        self.assertEqual(90, self.rational.add(-10, 100)) # third test

    def testDivide(self):
        self.assertEqual(4, self.rational.divide(8, 2))      # first test
        self.assertEqual(10, self.rational.divide(100, 10))     # second test
        self.assertEqual(2, self.rational.divide(4, 2)) # third test

    def testMultiply(self):
        self.assertEqual(4, self.rational.multiply(2, 2))      # first test
        self.assertEqual(21, self.rational.multiply(3, 7))     # second test
        self.assertEqual(1000, self.rational.multiply(10, 100)) # third test


unittest.main()