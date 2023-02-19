import copy

# open_list and closed_list are stored for each node
open_list = []
closed_list = []


class Node:
    capacities = []

    def __init__(self, state,  parent=None, g=0):
        self.state = state  # the current water storage capacity of each pitcher
        self.parent = parent # the parent node
        self.g = g
        if parent:
            self.SetParent(parent)
        self.h = self.GetH()
        self.f = self.GetF()

    def SetParent(self, parent):
        self.parent = parent
        self.g = parent.g + 1

    def GetH(self):
        remain = self.capacities[-1] - self.state[-1]  # h_star(n)
        m = remain  # h(n)
        # h(n) <= h_star(n)
        for x in self.state[:-1]:
            temp = abs(remain - x)
            if temp < m:
                m = temp

        for x in self.capacities[:-1]:
            for y in self.state[:-1]:
                if x + y + self.state[-1] == self.capacities[-1]:
                    m = 0
        return m + remain 

    # heuristic function
    def GetF(self):
        return self.g * 1.6 + self.h
    

    # Check if the state already exists in the list
def isExist(list, state):
    for i in range(len(list)):
        if list[i].state == state:
            return i
    return -1


# after every step, the list need to be updated
def update(node, state):
    if isExist(closed_list, state) == -1:
        key = isExist(open_list, state)
        if key == -1:
            open_list.append(Node(state, node))
            open_list.sort(key=lambda element: element.f)
        elif node.g + 1 < open_list[key].g:
            open_list[key].parent = node.parent
            open_list[key].g = node.g + 1


def PrintPath(current_node):
    best_path = []
    while (current_node):
        best_path.append(current_node.state)
        current_node = current_node.parent
    best_path.reverse()
    print("The shortest path has %d nodes" % (len(best_path)-1))
    print(best_path)


class Solver:
    # A _star algorithm
    def A_star(self, filename):
        fo = open(filename, mode='r')
        line = fo.readline()
        if line[-1] == '\n':
            line = line[:-1]
        capacities = [int(c) for c in line.split(',')]

        line = fo.readline()
        if line[-1] == '\n':
            line = line[:-1]
        capacities.append(int(line))
        print(capacities)
        fo.close()

        Node.capacities = capacities  # condition node
        open_list.clear()
        closed_list.clear()
        # put the initial node in open_list
        open_list.append(Node([0]*len(capacities)))

        while (open_list != []):
            # According to the value of F, get the top node of open_list
            curr_node = open_list.pop(0)

            # find the taget quantity
            if (curr_node.state[-1] == Node.capacities[-1]):
                print("Successed!")
                PrintPath(curr_node)
                return curr_node.g

            # search
            closed_list.append(curr_node)
            curr_state = curr_node.state
            pitcher_nums = len(curr_state) - 1
            # any two pitchers x and y have following 4 actions

            # 1. x has water, empty x
            for i in range(pitcher_nums):
                if curr_state[i] > 0:
                    new_state = copy.deepcopy(curr_state)
                    # new_state = copy.deepcopy(curr_state)
                    new_state[i] = 0
                    update(curr_node, new_state)

            # 2. x has water, pour to y
                    for j in range(pitcher_nums - 1):
                        if j == i:
                            break
                        gap = Node.capacities[j] - curr_state[j]
                        if gap > 0:
                            new_state = copy.deepcopy(curr_state)
                            if gap < curr_state[i]:
                                new_state[i] = curr_state[i] - gap
                                new_state[j] = Node.capacities[j]
                            else:
                                new_state[i] = 0
                                new_state[j] += curr_state[i]
                            update(curr_node, new_state)

            # 3. x has water, pour infinite pitcher
                    if curr_state[i] + curr_state[-1] <= Node.capacities[-1]:
                        new_state = copy.deepcopy(curr_state)
                        new_state[-1] += curr_state[i]
                        new_state[i] = 0
                        update(curr_node, new_state)

            # 4. x has no water, fill water
                new_state = copy.deepcopy(curr_state)
                new_state[i] = Node.capacities[i]
                update(curr_node, new_state)
        print("Failed")
        return -1 # failed return -1


if __name__ == '__main__':
    solver = Solver()
    steps = solver.A_star('input.txt')
    print(steps)
