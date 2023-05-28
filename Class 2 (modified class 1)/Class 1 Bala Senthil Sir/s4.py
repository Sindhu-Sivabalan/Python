class Human:
    def __init__(self):
        self.energy=0
    def eat(self):
        self.energy+=5
    def walk(self):
        self.energy-=2

x=Human()
print(x.energy)
x.eat()
x.eat()
x.walk()
print(x.energy)