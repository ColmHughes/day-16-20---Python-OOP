class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def add(self, value):
        if value < self.value:
            if t.left == None:
                t.left = Tree(value)
            else:
                t.left.add(value)
        else:
            if t.right == None:
                t.right = Tree(value)
            else:
                t.right.add(value)
                
    def get_nums(self):
        
t = Tree()
t.add(7)
t.add(2)
t.add(13)
print(t.value)
print(t.left.value)
print(t.right.value)