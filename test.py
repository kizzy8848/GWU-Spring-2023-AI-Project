import unittest
from toyWaterPitcherProblem import Solver, read_file

class TestCalculator(unittest.TestCase):
    def test01(self):
        
        print("Test01")
        capacities, target = read_file("input.txt")
        solver = Solver(capacities,target)
        result = solver.A_star()
        self.assertEqual(result,19)
        print('****************')
        
        

    def test02(self):
        print()
        print()
        print("Test02")
        capacities, target = read_file("input1.txt")
        solver = Solver(capacities,target)
        result = solver.A_star()
        self.assertEqual(result,7)
        print('****************')
        

    def test03(self):
        print()
        print()
        print("Test03")
        capacities, target = read_file("input2.txt")
        solver = Solver(capacities,target)
        result = solver.A_star()
        self.assertEqual(result,-1)
        print('****************')
        

    def test04(self):
        print()
        print()
        print("Test04")
        capacities, target = read_file("input3.txt")
        solver = Solver(capacities,target)
        result = solver.A_star()
        self.assertEqual(result,-1)
        print('****************')
        

    def test05(self):
        print()
        print()
        print("Test05")
        capacities, target = read_file("input4.txt")
        solver = Solver(capacities,target)
        result = solver.A_star()
        self.assertEqual(result,36)
        print('****************')
        


if __name__ == '__main__':
    unittest.main()
