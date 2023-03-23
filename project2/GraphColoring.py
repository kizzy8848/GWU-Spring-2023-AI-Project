import collections
import copy
import sys


class GraphColoring:
    def __init__(self):
        self.edges = []
        self.graph = collections.defaultdict(set)
        self.domain = []
        self.domains = {}

    def read_file(self, filename):
        # read file
        with open(filename, 'r') as file:
            for line in file:
                if line[0] == "#":
                    continue
                elif line[0] == "c":
                    number_of_available_color = int(line[-2])
                else:
                    edge = [int(i) for i in line.split(',')]
                    self.edges.append(edge)
                    self.graph[edge[0]].add(edge[1])
                    self.graph[edge[1]].add(edge[0])
        file.close()
        for i in range(number_of_available_color):
            self.domain.append(i)
        for node in self.graph.keys():
            self.domains[node] = copy.deepcopy(self.domain)

    def backtracking(self, assignments, method):
        if len(assignments) == len(self.domains):
            return assignments, True
        backupdomains = copy.deepcopy(self.domains)
        key = self.nextVariableIndex(assignments, method)
        for val in self.domains[key]:
            assignments[key] = val
            self.domains[key] = [val]
            if self.AC3():  # ac3
                result, b = self.backtracking(assignments, method)
                if b:
                    return result, b
            self.domains = copy.deepcopy(backupdomains)
            self.domains[key].remove(val)
            del assignments[key]

        return assignments, False

    def nextVariableIndex(self, assignments, method):

        if method == 'natural':
            for key in self.graph:
                if assignments.get(key) == None:
                    return key

        if method == 'MRV':

            min = sys.maxsize
            min_node: int
            for node in self.domains:

                if len(self.domains[node]) < min and assignments.get(node) == None:
                    min_node = node

                elif len(self.domains[node]) == min and assignments.get(node) == None:
                    if len(self.graph[node]) > len(self.graph[min_node]):
                        min_node = node
            return min_node

    def AC3(self):
        queue = copy.deepcopy(self.edges)

        while (len(queue) != 0):
            edge = queue.pop()

            for c in range(2):
                if c == 1:
                    edge = [edge[1], edge[0]]
                if self.revise(edge):
                    if len(self.domains[edge[0]]) == 0:
                        return False
                    for vertex in self.graph[edge[0]]:
                        queue.append([vertex, edge[0]])
        return True

    def revise(self, edge):
        x = self.domains[edge[0]]
        y = self.domains[edge[1]]
        flag = False
        if len(y) > 1:
            return False
        for i in x:
            if i == y[0]:
                x.remove(i)
                flag = True
        return flag


if __name__ == '__main__':
    graphColoring = GraphColoring()
    graphColoring.read_file('project2/input.txt')
    assignments, is_have_solution = graphColoring.backtracking({}, 'MRV')
    if assignments:
        print("Successed")
        for key in assignments.keys().__reversed__(): 
            print('Node',key,':',assignments[key])
    else:
        print("Failed")
    
