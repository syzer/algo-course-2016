# python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    height = []

    def compute_height(self):
        maxHeight = 0
        print(self.n, self.parent)

        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            print(maxHeight, height, 'v', vertex, i, self.parent[i])
            maxHeight = max(maxHeight, height)
        return maxHeight

    # def heights(t, level=0):
    #     if not t.parent:
    #         self.height.append(level)
    #     else:
    #         for c in t.parent:
    #             self.heights(c, level + 1)

    def compute_height_fast(self):
        for vertex in range(self.n):
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
        all_levs = set(sorted(self.parent))
        print(all_levs)
        print(sorted(self.parent))
        return len(all_levs)

        # heights = []

        # if not self.parent:
        #     return 1
        # else:
        #     self.parent.pop(0)
        # self.height +=1
        # return max(self.compute_height_fast() for c in self.parent) + 1


ver = [0, 1, 2, 3, 4, 5, 6]
arr = [-1, 0, 0, 1, 1, 2, 2]


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())
    print(tree.compute_height_fast())


threading.Thread(target=main).start()
