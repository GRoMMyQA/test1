class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self):
        print(self.name + "Singing")

man = Person("Roman", 29)
man.sing()