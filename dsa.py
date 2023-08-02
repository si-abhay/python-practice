class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        print("Animal class created")

    def copy(self):         # Copy constructor functionality C++
        new_animal = type(self)(self.age, self.name)
        return new_animal

ani = Animal(20, "RAT")
mni = ani.copy()

print(mni.name)
print(mni.age)
