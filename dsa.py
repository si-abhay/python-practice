class duck:
    def walk(self):
        print("duck: thapak thapak")

class horse:
    def walk(self):
        print("horse: tabdak tabdak")

def fun(obj):
    obj.walk()

d=duck()
h=horse()

fun(d)
fun(h)
