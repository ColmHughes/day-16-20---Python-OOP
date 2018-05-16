class Vehicle():
    
    vehicles_running = 0
    
    def __init__(self):
        self.fuel = 100
        self.running = False
   
    def start(self):
        print("Starting up the Vehicle")
        self.fuel -= 1
        self.running = True
        Vehicle.vehicles_running += 1
        
    def stop(self):
        print("Stopping the Vehicle")
        self.running = False
        Vehicle.vehicles_running -= 1
        print("You have {0} vehicles running".format(Vehicle.vehicles_running))
        
    
    def fuelgauge(self):
        print("You have {0} litres of fuel left".format(self.fuel))
        
        
v = Vehicle()
v.start()
print(v.running)

