import copy

open_list = []
closed_list = []


class Node:
    capacities = []

    def __init__(self, state,  parent=None, g=0):
        self.state = state  
        self.parent = parent  
        self.g = g # steps already taken 
        if parent:
            self.SetParent(parent)
        self.h = self.GetH()
        self.f = self.GetF()

    def SetParent(self, parent):
        self.parent = parent
        self.g = parent.g + 1

    def GetH(self):
        remain = self.capacities[-1] - self.state[-1]  
        m = remain  
        
        for x in self.state[:-1]:
            t = abs(remain - x)
            if t < m:
                m = t

        for x in self.capacities[:-1]:
            for y in self.state[:-1]:
                if x + y + self.state[-1] == self.capacities[-1]:
                    m = 0
        return m + remain

   
    def GetF(self):
        return self.g * 1.6 + self.h



def isExist(list, state):
    for i in range(len(list)):
        if list[i].state == state:
            return i
    return -1



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
    optimal_path = []
    while (current_node):
        optimal_path.append(current_node.state)
        current_node = current_node.parent
    optimal_path.reverse()
    print("The shortest path has %d nodes" % (len(optimal_path)-1))
    print(optimal_path)


class Solver:
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

        Node.capacities = capacities  
        open_list.clear()
        closed_list.clear()
        
        open_list.append(Node([0]*len(capacities)))

        while (open_list != []):
            
            curr_node = open_list.pop(0)
            if (curr_node.state[-1] == Node.capacities[-1]):
                print("Successed!")
                # PrintPath(curr_node)
                return curr_node.g

           
            closed_list.append(curr_node)
            curr_state = curr_node.state
            pitcher_nums = len(curr_state) - 1
            

            #  empty x
            for i in range(pitcher_nums):
                if curr_state[i] > 0:
                    new_state = copy.deepcopy(curr_state)
                    # new_state = copy.deepcopy(curr_state)
                    new_state[i] = 0
                    update(curr_node, new_state)

            # pour x to y
                    for j in range(pitcher_nums - 1):
                        if j == i:
                            break
                        remain = Node.capacities[j] - curr_state[j]
                        if remain > 0:
                            new_state = copy.deepcopy(curr_state)
                            if remain < curr_state[i]:
                                new_state[i] = curr_state[i] - remain
                                new_state[j] = Node.capacities[j]
                            else:
                                new_state[i] = 0
                                new_state[j] += curr_state[i]
                            update(curr_node, new_state)

            # pourx to infinite pitcher
                    if curr_state[i] + curr_state[-1] <= Node.capacities[-1]:
                        new_state = copy.deepcopy(curr_state)
                        new_state[-1] += curr_state[i]
                        new_state[i] = 0
                        update(curr_node, new_state)

            # fill x
                new_state = copy.deepcopy(curr_state)
                new_state[i] = Node.capacities[i]
                update(curr_node, new_state)
        print("Failed")
        return -1  # failed return -1


if __name__ == '__main__':
    solver = Solver()
    steps = solver.A_star('input.txt')
    print(steps)
