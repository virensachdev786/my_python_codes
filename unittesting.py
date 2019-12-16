import unittest
from venv.sum1 import main

class ABC(unittest.TestCase):
    def setpu(self):
        pass
    def testadd(self):
        self.assertEqual(main(),3)

if __name__=="__main__":
    unittest.main()