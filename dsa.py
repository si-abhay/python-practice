class animal:
    def __init__(self):
        print("Animal called")

class snake:
    def __init__(self):
        print("Snake called")
    
class snail(animal,snake):
    def __init__(self):
        super().__init__()
        print("snail called")

obj=snail()  