class Animal:
    def does(self):
        print("speaks")

class Dog(Animal):
    pass
    #def does(self):
    #    print("barks")

d=Dog()
d.does()