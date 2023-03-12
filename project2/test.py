import unittest
from GraphColoring import GraphColoring


class TestGraphColoring(unittest.TestCase):
    def test01(self):
        print("Test01")
        graphColoring = GraphColoring()
        graphColoring.read_file('project2/input1.txt')
        assignments, is_have_solution = graphColoring.backtracking({}, 'MRV')
        self.assertEqual(is_have_solution, True)
        print(assignments)
        print('****************')

    def test02(self):
        print("Test02")
        graphColoring = GraphColoring()
        graphColoring.read_file('project2/input2.txt')
        assignments, is_have_solution = graphColoring.backtracking({}, 'MRV')
        self.assertEqual(is_have_solution, True)
        print(assignments)
        print('****************')

    def test03(self):
        print("Test03")
        graphColoring = GraphColoring()
        graphColoring.read_file('project2/input3.txt')
        assignments, is_have_solution = graphColoring.backtracking({}, 'MRV')
        self.assertEqual(is_have_solution, True)
        print(assignments)
        print('****************')

    def test04(self):
        print("Test04")
        graphColoring = GraphColoring()
        graphColoring.read_file('project2/input4.txt')
        assignments, is_have_solution = graphColoring.backtracking({}, 'MRV')
        self.assertEqual(is_have_solution, True)
        print(assignments)
        print('****************')

    def test05(self):
        print("Test05")
        graphColoring = GraphColoring()
        graphColoring.read_file('project2/input5.txt')
        assignments, is_have_solution = graphColoring.backtracking({}, 'MRV')
        self.assertEqual(is_have_solution, False)
        print(assignments)
        print('****************')

    def test06(self):
        print("Test06")
        graphColoring = GraphColoring()
        graphColoring.read_file('project2/input6.txt')
        assignments, is_have_solution = graphColoring.backtracking({}, 'MRV')
        self.assertEqual(is_have_solution, True)
        print(assignments)
        print('****************')

    def test07(self):
        print("Test07")
        graphColoring = GraphColoring()
        graphColoring.read_file('project2/input6.txt')
        assignments, is_have_solution = graphColoring.backtracking({}, 'MRV')
        self.assertEqual(is_have_solution, True)
        print(assignments)
        print('****************')


if __name__ == '__main__':
    unittest.main()
