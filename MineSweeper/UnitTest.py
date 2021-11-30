import unittest

from MineSweeper import MineSweeper

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.m=MineSweeper(3,1)
        self.m.mineSweeperMap=[[-1,1,0],[1,1,0],[0,0,0]]
        self.m2=MineSweeper(3,1)
        self.m2.mineSweeperMap=[[-1,1,0],[1,1,0],[0,0,0]]
        self.m3=MineSweeper(3,1)
        self.m3.mineSweeperMap=[[-1,1,0],[1,1,0],[0,0,0]]
    def testChooseBlock(self):
        self.assertEqual(self.m.chooseBlock(2,2),[(2, 2),(2, 1),(1, 1),(1, 2),(2, 0),(1, 0),(1, 1),(1, 2),(0, 1),(0, 2),(1, 0)])


    def testIsClear(self):
        self.assertEqual(self.m2.isClear(),0)
        self.m2.chooseBlock(2,2)
        self.assertEqual(self.m2.isClear(),1)
        self.m3.chooseBlock(0,0)
        self.assertEqual(self.m3.isClear(),2)

if __name__ == '__main__':
    unittest.main()

