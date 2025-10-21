class mammal:
    def __init__(self):
        print("mammal class constructor")

    def walk(self):
        print("mammal do walk tho")

class dog(mammal):
    def __init__(self):
        super().__init__()
        print("dog class constructor")

    def bark(self):
        print("dogs do fucking bark")

dog1 = dog()
dog1.bark()
dog1.walk()
