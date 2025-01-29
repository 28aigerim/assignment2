from animal import Animal

animals = []
n = int(input('How many animals will you add? '))

for i in range(n):
    species = input('What species is the animal? ')
    age = int(input('How old is the animal? '))
    food = input('What does it eat? ')
    color = input('What is the color of the animal? ')

    animal = Animal(species, age, food, color)

    animals.append(animal)

print(f"You have added {n} animals: ")
for animal in animals:
    animal.display_info()


does_eat = int(input('Do you give animals food? (1/0) '))
if does_eat == 1:
    for animal in animals:
        animal.eat()