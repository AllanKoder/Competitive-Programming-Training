
class UnionNode:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0
    
    def find(self):
        if self != self.parent:
            self.parent = self.parent.find()
        return self.parent

    def union(self, other):
        group1 = self.find()
        group2 = other.find()

        if group1 != group2:
            if group1.rank > group2.rank:
                group2.parent = group1
            elif group1.rank < group2.rank:
                group1.parent = group2
            else:
                group2.parent = group1
                group1.rank += 1
        

nodes = [UnionNode(i) for i in range(8)]

nodes[0].union(nodes[1])
nodes[2].union(nodes[3])
nodes[3].union(nodes[0])

for n in range(8):
    print(nodes[n].find().value)
