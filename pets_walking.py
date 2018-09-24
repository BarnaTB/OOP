class Pets:
    dogs = []

    def walk(self):
        for dog in Pets.dogs:
            dog.self.walk()


class Dog:
    def __init__(self, name, age, is_hungry=True):
        self.is_hungry = is_hungry
        self.name = name
        self.age = age

    def eat(self):
        self.is_hungry = False
        return self.is_hungry

    def get_dog_info(self):
        for dog in Pets.dogs:
            print('{0} is {1}'.format(dog.name, dog.age))

    def check_for_hunger(self):
        for dog in Pets.dogs:
            if dog.is_hungry:
                print('My dogs are hungry')
            else:
                print('My dogs are not hungry')

    def walk(self):
        for dog in Pets.dogs:
            print('{0} is walking!'.format(dog.name))


dog1 = Dog('Tom', 10)
dog2 = Dog('Fletcher', 11)
dog3 = Dog('Larry', 9)
Pets.dogs = [dog1]
dog1.get_dog_info()
# dog1.eat()
dog1.walk()
dog1.check_for_hunger()
