class Pets:
    dogs = []

    def walk(self):
        for dog in Pets.dogs:
            self.walk()


class Dog:
    def __init__(self, name, age, is_hungry=True):
        self.is_hungry = is_hungry
        self.name = name
        self.age = age

    def eat(self):
        self.is_hungry = False
        return self.is_hungry

    def check_for_hunger(self):
        for dog in Pets.dogs:
            if dog.is_hungry:
                return 'My dogs are hungry'
            return 'My dogs are not hungry'

    def walk(self):
        for dog in Pets.dogs:
            print('{0} is walking!'.format(dog.name))
