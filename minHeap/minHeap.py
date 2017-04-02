class minHeap():
    def __init__(self):
        self.tree = []
    def add(self, value):
        index = len(self.tree)
        self.tree.append(value)
        self.bubbleUpR(index)
    def remove(self, value):
        index = 0
        for x in range(len(self.tree)):
            if self.tree[x] == value:
                index = x
                break
        self.bubbleDownR(index)
        self.tree.remove(self.tree[len(self.tree)-1])
    def printer(self):
        for x in range(len(self.tree)):
            print(str(self.tree[x]) + " ")
    def bubbleUpR(self, index):
        p = self.getParent(index)
        if int(self.tree[p]) > self.tree[index]:
            temp = self.tree[p]
            self.tree[p] = self.tree[index]
            self.tree[index] = temp 
            self.bubbleUpR(p)
    def bubbleDownR(self, index):
        p = self.getChild(index)
        if p > len(self.tree) - 1:
            pass
        else:
            left = self.tree[p]
            right = self.tree[p] + 1
            if left < self.tree[index]:
                if left < right:
                    self.bubbleDown(p)
                else:
                    self.bubbleDownR(p+1)
            elif right < self.tree[index]:
                if left < right:
                    self.bubbleDown(p)
                else:
                    self.bubbleDownR(p+1)
            temp = self.tree[p]
            self.tree[len(self.tree)] = self.tree[index]
            self.tree[index] = temp
    def getParent(self, index):
        parent = 0
        if index % 2 == 0:
            parent = (index/2)-1
        else:
            parent = (index-1)/2
        return int(parent)
    def getChild(self, index): # Returns left child index, add one for right child index
        return int(index*2+1)
    def getMin(self):
        x = self.tree[0]
        self.remove(x)
        return x