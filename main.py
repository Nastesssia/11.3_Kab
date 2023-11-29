import random

class Human:
    def __init__(self, name, age, shooting_experience):
        self.name = name
        self.age = age
        self.shooting_experience = shooting_experience

    def shoot(self):
        return False

class Novice(Human):
    def shoot(self):
        probability = 0.01 * self.shooting_experience
        return random.random() < probability

class Experienced(Human):
    def shoot(self):
        probability = 0.05 * self.shooting_experience
        return random.random() < probability

class Veteran(Human):
    def shoot(self):
        probability = 0.9 - 0.01 * self.age
        return random.random() < probability

# массив из 7 человек
people = [
    Novice("Новичок Иван", 25, 3),
    Novice("Новичок Ильюша", 25, 3),
    Experienced("Опытный Дядя", 30, 7),
    Veteran("Ветеран Игорь", 40, 15),
    Experienced("Опытный Гюнтер", 35, 5),
    Novice("Новичок Гоша", 20, 2),
    Human("Просто человек Маша", 22, 1)  #без опыта стрельбы
]

# стрельба
shot_fired = False
for person in people:
    result = person.shoot()
    print(f"{person.name} ({type(person).__name__}): {'Попал' if result else 'Промах'}")
    if result:
        shot_fired = True
        break

if not shot_fired:
    print("Никто не попал")

