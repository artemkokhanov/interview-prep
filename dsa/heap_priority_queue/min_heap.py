# leftChild of i = heap[2 * i]
# rightChild of i = heap[(2 * i) + 1]
# parent of i = heap[i // 2]

class Heap:
    def __init__(self):
        self.heap = [0]  # initializing an array with the first value being 0

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1  # we omit the 0 index since we are not using it

        # percolate up
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()  # move last value to root
        i = 1
        while 2 * i < len(self.heap):  # while there is a left child, do downward percolation
            if ((2 * i + 1) < len(self.heap)) and (self.heap[2 * i + 1] < self.heap[2 * i]) and (
                    self.heap[i] > self.heap[2 * i + 1]):
                # swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def heapify(self, arr):
        # 0-th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # percolate down
            i = cur
            while 2 * i < len(self.heap):
                if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[
                    2 * i + 1]:
                    # swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    # swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1
