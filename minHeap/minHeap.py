class minHeap():
    def __init__(self):
        self.tree = []
    def add(self, value):
        index = len(self.tree)
        self.tree.append(value)
        self.bubbleUpR(index)
    def printer(self):
        for x in range(len(self.tree)):
            print(str(self.tree[x]) + " ")
    def bubbleUpR(self, index):
        if 