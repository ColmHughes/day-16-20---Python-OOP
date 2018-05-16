class Donut():
    
    
    def __init__(self):
        self.donut_size = 100
    
    def bite_donut(self):
        if self.donut_size > 0:
            self.donut_size -= 25
            
t = Donut()
t.bite_donut()
t.bite_donut()
t.bite_donut()
t.bite_donut()
t.bite_donut()
print(t.donut_size)

print("------------------------")

e = Donut()
e.bite_donut()
print(e.donut_size)