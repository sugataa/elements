"""
5.1

How would you go about computing hte parity of a very large number of 64-bit nonnegative integers?

"""

import unittest

def getParity(num):
    return 0

class Test(unittest.TestCase):

    def testClearLowestBit(self):

        A = ["111", "000", "001", "011", "0001"]

        for i in range(len(A)):
            y = getParity(A[i])
            if i == 0:
                self.assertEqual(y, 1)
            elif i == 1:
                self.assertEqual(y, 0)
            elif i == 2:
                self.assertEqual(y, 1)
            elif i == 3:
                self.assertEqual(y, 0)
            elif i == 4:
                self.assertEqual(y, 1)