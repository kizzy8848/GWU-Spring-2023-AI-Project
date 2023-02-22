import heapq
import math
import time


class Solver:
    capacities = []  # the capacity of each jug
    target = 0  # the target

    # calculate h(n)
    def heuristicFunc(self, state, max_capacity):
        # state is the current water in the infinited jug
        remain = abs(self.target - state)
        h = math.ceil(remain / max_capacity)
        return h

    def A_star(self, filename):
        # read data in file
        fo = open(filename, mode='r')

        line = fo.readline()
        if line[-1] == '\n':
            line = line[:-1]
        self.capacities = [int(c) for c in line.split(',')]

        line = fo.readline()
        if line[-1] == '\n':
            line = line[:-1]
        self.target = int(line)
        print(self.capacities)
        print(self.target)
        fo.close()

        # if gcd is not divisible by target, return -1
        # greatest common divisor 最大公约数
        greates_common_divisor = self.capacities[0]
        for i in self.capacities:
            greates_common_divisor = math.gcd(greates_common_divisor, i)
        if self.target % greates_common_divisor != 0:
            print('Gcd is not divisible by target')
            print('Returned -1')
            return -1

        initial_state = 0  # interger Initial State

        visited = set()

        visited.add(initial_state)

        waters = [0 for _ in range(len(self.capacities))]

        heap = [(self.heuristicFunc(initial_state, max(self.capacities)), 0, self.heuristicFunc(
            initial_state, max(self.capacities)), waters, initial_state, [])]

        while heap:
            
            f, g, h, curr_water, curr_state, curr_path = heapq.heappop(heap)

            # deque the answer, return
            if curr_state == self.target:
                print("Search Successed")
                print('Steps Taken', g)
                return g

            # pour any water pitcher -> the infinite one
            for i in range(len(self.capacities)):
                # if the new state is visited, just skip
                if curr_state + self.capacities[i] in visited:
                    continue
                new_water = curr_water[:]
                if new_water[i]:
                    new_water[i] = 0
                    new_g = g + 1
                else:
                    new_g = g + 2
                # calculate the new state related variables
                new_path = curr_path[:]
                new_path.append(self.capacities[i])
                new_state = curr_state + self.capacities[i]
                new_h = self.heuristicFunc(new_state, max(self.capacities))
                new_f = new_g + new_h
                visited.add(new_state)
                heapq.heappush(heap, (new_f, new_g, new_h,
                                      new_water, new_state, new_path))

            # pour the infinite one -> any water pitcher
            for i in range(len(self.capacities)):
                # if the new state is invalid or visited, just skip
                if curr_state - self.capacities[i] < 0:
                    continue
                if curr_state - self.capacities[i] in visited:
                    continue
                new_water = curr_water[:]
                if new_water[i]:
                    new_g = g + 2
                else:
                    new_water[i] = 1
                    new_g = g + 1
                # calculate the new state related variables
                new_path = curr_path[:]

                new_path.append(-self.capacities[i])
                new_state = curr_state - self.capacities[i]
                new_h = self.heuristicFunc(new_state, max(self.capacities))
                new_f = new_g + new_h
                visited.add(new_state)
                heapq.heappush(heap, (new_f, new_g, new_h,
                                      new_water, new_state, new_path))

        print('Search Failed')
        print("Returned -1")
        return -1


if __name__ == '__main__':
    solver = Solver()
    steps = solver.A_star('input.txt')
    print(steps)
