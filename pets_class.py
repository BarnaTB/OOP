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
                return 'My dogs are hungry'
            return 'My dogs are not hungry'

print('I have {0} dogs'.format(len(Pets.dogs)))
print('And they\'re all mammals, of course.')
