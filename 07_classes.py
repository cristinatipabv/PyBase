student = {
    "name": "Adrian",
    "age": 32,
    "weight": 70.0,
    "backpack": ["keys", "wallet", "camera", "phone"],
    0: "nothing at all",
    (1, 2): "alpha and omega"
}
student2 = {
    "name": "Marius",
    "age": 25,
    "weight": 65.0,
    "backpack": [],
}

student3 = {
    "name": "Catalin",
    "age": 30,
    "weight": 80.0,
    "backpack": ["keys", "wallet", "camera"],
    0: "nothing at all",
    (1, 2): "alpha and omega"
}

def get_backpack(param1):
    return param1["backpack"]

print(get_backpack(student3))
#print(get_backpack(100))

def func_goala():
    pass

# Clase

class Dog:
    pass


# Dog este o clasa

var1 = Dog()
var2 = Dog()
var3 = Dog()

# var1, var2, var3 -> instante a clasei Dog

print(var1)
print(var1)
print(var2)
print(var3)

print ("==================Class Properties==================")

var4 = Dog()
var4.name = "Spot"
var4.owner = "Iulian"
var4.legs = 4
var4.last_vaccine = 2025

print(var4.name)
print(var4.owner)
print(var4.legs)
print(var4.last_vaccine)

print(var4.__dict__)

var5 = Dog()
var5.name = "Shadow"
print(var5.__dict__)
print(var5.__class__)

# in javascripts , java, self -> this
# self este o referinta la instanta / obiect curent, cu care lucram noi acum
class Cat():
    def __init__(self, name, owner, legs, last_vaccine=None):
        self.name = name
        self.owner = owner
        self.legs = legs
        self.last_vaccine = last_vaccine

    #methoda
    # self -> instanta care apeleaza aceasta methoda
    def make_sound(self):
        print(self.name, "Meowwwww!")


    def take_a_bite(self, param1):
        a_bite = param1.pop(0)
        print(f"{self.name} took a bite of {a_bite}")

var6 = Cat("Missy", "Vlad", 4, 2025)
print(var6.__dict__)

var7 = Cat("KitKat", "Ana-Maria", 4)
print(var7.owner)

var6.make_sound()
var7.make_sound()


print(var6.name)
print(var7.name)
print(var7.owner)


# def take_a_bite(self, param1):
#     a_bite = param1.pop()
#     print(f"{self.name} took a bite of {a_bite}")

snacks = ["fish_snack", "meat_pop..", "milk", "fresh_nat", "catnip"]

var7.take_a_bite(snacks)
var7.take_a_bite(snacks)
var7.take_a_bite(snacks)
var7.take_a_bite(snacks)
var7.take_a_bite(snacks)


#snacks.pop() -> afiseaza de la coada valorile din lista
#snacks.pop(0) -> afiseaza de la primul element din lista