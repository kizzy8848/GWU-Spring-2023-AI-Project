import unittest
from toyWaterPitcherProblem import Solver

class TestCalculator(unittest.TestCase):
    def test01(self):
        solver = Solver()
        result = solver.A_star("input.txt")
        self.assertEqual(result,19)

    def test02(self):
        solver = Solver()
        result = solver.A_star("input1.txt")
        self.assertEqual(result,7)

    def test03(self):
        solver = Solver()
        result = solver.A_star("input2.txt")
        self.assertEqual(result,-1)

    def test04(self):
        solver = Solver()
        result = solver.A_star("input3.txt")
        self.assertEqual(result,-1)

    def test05(self):
        solver = Solver()
        result = solver.A_star("input4.txt")
        self.assertEqual(result,36)

    


if __name__ == '__main__':
    unittest.main()
