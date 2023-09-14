class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name=''):
        self._name = name
        self._breed = None

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in Dog.approved_breeds:
            self._breed = breed
        else:
            raise ValueError("Breed must be in the list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
