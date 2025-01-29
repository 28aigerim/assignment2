class Animal:

    def __init__(self, species, age, food, color=None):
        self.species = species
        self.age = age
        self.color = color
        self.food = food

    #methods
    def display_info(self):
        print(f'The animal {self.species} is {self.age} years old. Its color is {self.color} and it eats {self.food}.')

    def eat(self):
        print(f'The animal of species {self.species} is eating {self.food}.')