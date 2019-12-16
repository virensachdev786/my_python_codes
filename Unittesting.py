import unittest

class ABC(unittest.TestCase):
    def setpu(self):
        pass
    def testThis(self):
        self.assertEqual('a' * 4, 'aaaa')

if __name__=="__main__":
    unittest.main()