class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi my name is {self.name}")


person = Person("Greg")

print(person.name)

person.talk()
