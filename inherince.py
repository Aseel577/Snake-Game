class Blue():
    def __init__(self):
        self.eye = "Blue"
        self.skin = "White"
        


class Person(Blue):
    def __init__(self):
        super().__init__()



blue = Blue()

person = Person()

print(person.eye)