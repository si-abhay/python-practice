class Animal:
    def __init__(self):
        print("Animal class created")
    def name(self,name):
        self.name=name
        print("Name of animal is {}".format(self.name))
    def do(self):
        print("Runs")

ani=Animal()
ani.name("Dog")
print(ani.name)

class Kangaroo(Animal):
    def __init__(self):
        super().__init__()
        print("Kangaroo class created")

    def jumps(self):
        print("jumps around")

kang=Kangaroo()
kang.jumps()
kang.name("kang1")
