import unittest

class Math_Dojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in range ( len(nums) ):
            self.result += nums[i]
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in range ( len(nums) ):
            self.result -= nums[i]
        return self

class Tester( unittest.TestCase ):

    def setUp(self):
        self.md = Math_Dojo()

    def test_add1(self):
        self.assertEqual( self.md.add(2).result, 2 )
    def test_add2(self):
        self.assertEqual( self.md.add(2,8).result, 10 )
    def test_add3(self):
        self.assertEqual( self.md.add(3,7,9,5).result, 24 )

    def test_subtract1(self):
        self.assertEqual( self.md.subtract(2).result, -2 )
    def test_subtract2(self):
        self.assertEqual( self.md.subtract(2,3).result, -5 )
    def test_subtract3(self):
        self.assertEqual( self.md.subtract(2,4,6,8).result, -20 )


if __name__ == '__main__':
    unittest.main()