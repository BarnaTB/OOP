class Pets:
    dogs = []


class Dog:
    def __init__(self, name, age, is_hungry=True):
        self.is_hungry = is_hungry

    def eat(self):
        self.is_hungry = False
        return self.is_hungry

    def check_for_hunger(self):
        for dog in Pets.dogs:
            if dog.is_hungry:
                print('My dogs are hungry')
            else:
                print('My dogs are not hungry')

dog = Dog('Tom', 10)
Pets.dogs = [dog]
dog.eat()
dog.check_for_hunger()
