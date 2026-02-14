# mostenire, pentru clase
# overwrite


class Animal:
    def __init__(self, name = "Amoeba"):
        self.name = name

    def action(self):
        print("I am seraching for food!")


class Cat(Animal):
    def __init__(self, stripes,name = "Cat"):
        # parametrii non default tb sa fie in stanga, parametrii default tb sa fie in dreapta
        super().__init__(name)
        self.stripes = stripes





    def purr(self):
        print("Prrrrrrrrrrrr")

    def action(self):
        # putem sa accesam metoda originala action() din clasa din care mostenim, cu super()
        super().action()
        print("Hunting for mice and rats")


class Dog(Animal):
    def action(self):
        print("Runs around, looking for....")
        print("Licks yor face afterwards.")

print("Animal::")
anim1 = Animal("Lizard")
anim1.action()
print(anim1.name)

print("Cat::")
cat1 = Cat("Red", name = "Leo")
cat1.action()
cat1.purr()
cat1.action()

print(cat1.name)
print(cat1.stripes)


# polimorfism
# cand ai doua clase, una o mosteneste pe cealalta, dar au comportamente diferite

animal_park = []
cat2 = Cat("Orange", "skitty")
cat3 = Cat("Black", "Skittesls")
dog1 = Dog("Hunter")
dog2 = Dog("PawPaw")

animal_park = [cat2, cat3, dog1, dog2]

print ("Animal Park::")


for v in animal_park:
    print(v.name)
    v.action()
