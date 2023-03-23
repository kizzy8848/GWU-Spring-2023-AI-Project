import heapq
import math

def read_file(filename):
    # read data from file
    fo = open(filename, mode='r')
    line = fo.readline()
    if line[-1] == '\n':
        line = line[:-1]
    capacities = [int(c) for c in line.split(',')]

    line = fo.readline()
    if line[-1] == '\n':
        line = line[:-1]
    target = int(line)
    fo.close()
    return capacities, target

class Solver:
    capacities = []  # the capacity of each jug
    target = 0  # the target

    def __init__(self, capacities, target):
        self.capacities = capacities
        self.target = target

    # calculate h(n)
    def heuristicFunc(self, state, max_capacity):
        # state is the current water in the infinited jug
        remain = abs(self.target - state)
        h = math.ceil(remain / max_capacity)
        return h

    def A_star(self):
        

        # if gcd is not divisible by target, return -1
        # greatest common divisor 最大公约数
        # 例如 2 4 凑个 11 target 11 与 2 4的最大公约数 2 的余数是 1 不是0

        greates_common_divisor = self.capacities[0]
        for i in self.capacities:
            greates_common_divisor = math.gcd(greates_common_divisor, i)
        if self.target % greates_common_divisor != 0:
            print('Fail')
            print('Result -1')
            return -1

        initial_state = 0  # interger Initial State 

        visited = set() 
        visited.add(initial_state)
        waters = [0 for _ in range(len(self.capacities))] #把所有罐子里的水初始化为0
        heap = [(self.heuristicFunc(initial_state, max(self.capacities)), 0, self.heuristicFunc(
            initial_state, max(self.capacities)), waters, initial_state)]
        while heap:
            # curr_water 是每个罐子里现有的水
            # curr_state 是无限水壶中现有的水
            f, g, h, curr_water, curr_state = heapq.heappop(heap)
            # deque the answer, return
            if curr_state == self.target:
                print("Success")
                print('Result', g)
                return g
            # pour any water pitcher -> the infinite one
            for i in range(len(self.capacities)):
                # if the new state is visited, just skip
                if curr_state + self.capacities[i] in visited:
                    continue
                new_water = curr_water[:]
                if new_water[i]:  # 如果水壶有水 清空
                    new_water[i] = 0
                    new_g = g + 1  # 步数加一
                else:
                    new_g = g + 2  # 水壶装水 然后装到无限水壶
                # calculate the new state related variables
                new_state = curr_state + self.capacities[i]
                new_h = self.heuristicFunc(new_state, max(self.capacities))
                new_f = new_g + new_h
                visited.add(new_state)
                heapq.heappush(heap, (new_f, new_g, new_h,
                                      new_water, new_state))
            # pour the infinite one -> any water pitcher
            for i in range(len(self.capacities)):
                # if the new state is invalid or visited, just skip
                # 罐子的容量比无限水壶里面现有的水要大 把无限水壶里的水倒到罐子里没有意义
                if curr_state - self.capacities[i] < 0:
                    continue
                # 已访问的状态
                if curr_state - self.capacities[i] in visited:
                    continue
                new_water = curr_water[:]
                # 罐子里有水先清空 再把无限水壶里的水倒进去
                if new_water[i]:
                    new_g = g + 2
                else:
                    # 没水 直接把无限水壶里的水倒进去
                    new_water[i] = 1
                    new_g = g + 1
                # 更新状态
                # calculate the new state related variables
                new_state = curr_state - self.capacities[i]
                new_h = self.heuristicFunc(new_state, max(self.capacities))
                new_f = new_g + new_h
                visited.add(new_state)
                heapq.heappush(heap, (new_f, new_g, new_h,
                                      new_water, new_state))
        print('Fail')
        print("Result: -1")
        return -1

if __name__ == '__main__':
    capacities, target = read_file("project1/input1.txt")
    solver = Solver(capacities,target)
    steps = solver.A_star()
    print(steps)
