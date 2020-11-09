# task:  implement two stacks using one array

import sys


class TwoStacks:
    def __init__(self, n):
        self.array = [0] * n
        self.array_len = n
        self.index1 = 0
        self.index2 = n - 1

    def __repr__(self):
        stack1 = [self.array[i] for i in range(0, self.index1)]
        stack2 = [self.array[self.index2 - 1 - i] for i in range(self.index2, self.array_len - 1)]
        return 'stack 1: ' + str(stack1) + ' stack 2: ' + str(stack2)

    def insert_stack1(self, data):
        if self.index1 >= self.array_len // 2:
            print("cannot insert, stack overflow")
            exit(1)
        else:
            self.array[self.index1] = data
            self.index1 += 1 

    def insert_stack2(self, data):
        if self.index2 < self.array_len // 2:
            print("cannot insert, stack overflow")
            exit(1)
        else:
            self.array[self.index2] = data
            self.index2 -= 1 
    
    def pop_stack1(self):
        self.index1 -= 1
        val = self.array[self.index1]
        if self.index1 < 0:
            print("cannot pop, stack underflow")
            exit(1)
        else:
            return val
    
    def pop_stack2(self):
        self.index2 += 1
        val = self.array[self.index2]
        if self.index2 >= self.array_len:
            print("cannot pop, stack underflow")
            exit(1)
        else:
            return val

    def top_stack1(self):
        val = self.array[self.index1 - 1]
        return val

    def top_stack2(self):
        val = self.array[self.index2 + 1]
        return val


def main():
    data_stack1_stack2 = sys.stdin.readlines()
    n = int(data_stack1_stack2[0].rstrip())
    two_stacks = TwoStacks(n)
    for data in data_stack1_stack2[1:]:
        data = list(map(int, data.rstrip().split()))
        if len(data) > 1:
            data1 = data[0]
            data2 = data[1]
            two_stacks.insert_stack1(data1)
            two_stacks.insert_stack2(data2)
        else:
            data2 = data[0]
            two_stacks.insert_stack2(data2)
    
    print(two_stacks)
    val = two_stacks.pop_stack1()
    print("popped value for stack 1:", val)
    val = two_stacks.pop_stack2()
    print("popped value for stack 2:", val)
    print("top of stack 1 is", two_stacks.top_stack1())
    print("top of stack 2 is", two_stacks.top_stack2())
    print(two_stacks)


if __name__ == '__main__':
    main()

