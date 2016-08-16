"""

Write a function that takes an array A and an index i into a, and rearranges the elements such that all elements less than A[i] appear first, followed by elements equal to A[i], followed by elements greater than A[i]. Your algorithm should have O(1) space complexity and O(|A|) time complexity.

"""

import unittest

def dutch_flag(A, pivot):

    smaller = 0
    equal = 0
    larger = len(A) - 1

    while equal <= larger:
        if (A[equal] == A[pivot]):
            equal += 1
        elif (A[equal] < A[pivot]):
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif (A[equal] > A[pivot]):
            A[equal], A[larger] = A[larger], A[equal]
            larger -= 1

    return A

class Test(unittest.TestCase):

    def test_dutch_flag(self):

        A = [0, 0, 1, 3, 1, 1, 0]

        result = [0, 0, 0, 1, 1, 1, 3]

        self.assertEqual(dutch_flag(A, 4), result)

if __name__ == '__main__':
    unittest.main()