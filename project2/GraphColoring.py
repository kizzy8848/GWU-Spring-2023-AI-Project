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
        # assignment的定义:dict index=color
        # backTrack:通过递归，对assignment做尝试赋值并AC-3检查，保存副本（浪费空间，但是作为练习够用），失败则回复副本.
        # domain:当前domain assignment:当前赋值位置 csp:问题描述(static)
        # method:选择下一个变量采用的方法
        if len(assignments) == len(self.domains):  # 如果所有节点均已赋值就表示找到了结果 直接返回
            return assignments, True

        backupdomains = copy.deepcopy(self.domains)  # 备份domain
        key = self.nextVariableIndex(assignments, method)  # 通过启发式 确定下一个要赋值的节点
        for val in self.domains[key]:
            assignments[key] = val  # assignment 记录
            self.domains[key] = [val]  # 把domain更新为只有复制
            if self.AC3():  # ac3
                result, b = self.backtracking(assignments, method)
                if b:
                    return result, b
            # 运行到这里说明此路不通,回复状态,删掉val=value from domain

            self.domains = copy.deepcopy(backupdomains)
            self.domains[key].remove(val)
            del assignments[key]
        # 运行到这里说明全都不行
        return assignments, False

    def nextVariableIndex(self, assignments, method):
        # 这里实现两种方式，MRV与自然序
        if method == 'natural':
            for key in self.graph:
                if assignments.get(key) == None:
                    return key

        if method == 'MRV':
            # MRV:find the variable that has the smallest domain
            min = sys.maxsize
            min_node: int
            for node in self.domains.keys():
                # min remaining values
                if len(self.domains[node]) < min and assignments.get(node) == None:
                    min_node = node
                # tie breaking rule
                elif len(self.domains[node]) == min and assignments.get(node) == None:
                    if len(self.graph[node]) > len(self.graph[min_node]):
                        min_node = node
            return min_node

    def AC3(self):
        queue = copy.deepcopy(self.edges)
        # loop
        while (len(queue) != 0):

            edge = queue.pop()  # 一条边
            # 一次梳理一对
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
        if len(y) > 1:  # 如果y的可能去值大于2 说明y还没确定 return
            return False
        # y cannot be 0.
        for i in x:
            if i == y[0]:
                x.remove(i)
                flag = True
        return flag


if __name__ == '__main__':
    graphColoring = GraphColoring()
    graphColoring.read_file('project2/input7.txt')
    assignments, is_have_solution = graphColoring.backtracking({}, 'MRV')
    print(assignments)
