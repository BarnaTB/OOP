class Pets:
    dogs = []


class Dog:
    def __init__(self, name, age, is_hungry=True):
        self.is_hungry = is_hungry

    def eat(self):
        self.is_hungry = False
        return self.is_hungry
