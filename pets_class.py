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

dog1 = Dog('Tom', 10)
dog2 = Dog('Fletcher', 11)
dog3 = Dog('Larry', 9)
Pets.dogs = [dog1]
dog1.eat()
dog1.check_for_hunger()
