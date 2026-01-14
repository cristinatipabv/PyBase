#print("Hello")
#
# l = "hello"
# print(l)

#exemple de variabile. O variabila nu poate incepe de genul "10var"
# var1 = "Adrian"
# var2 = [0,1,2,3]
#daca sirul de caractere nu se pune in "" o sa considere sirul de caractere o variabila. Nu se poate crea o variabila True sau False.
#se poate crea variabila true sau false doar daca sunt scrise cu litere mici. Au index.


#################################
# Tuplu - structura de date imutabila (este fixa, nu isi schimba forma), o lista de date care nu poate fi schimbata. Au index


coordonate_punct1 = (3,5)
coordonate_punct2 = (0,10)
#                     0, 1
persoana1 = ("Adrian", 32, "Brasov", "Tutore", True, 300, 185, 70)
#persoana1 = [("Adrian", 32, "Brasov", "Tutore", True, 300, 185, 70)]
#               0       1   2           3       4       5   6   7
#
# print(coordonate_punct1)
# print(coordonate_punct2)
print(persoana1[3])

#assign
#error - TypeError: 'tuple' object does not support item assignment = apare ok, deoarece nu se poate schimba un tuplu (tuple)

#persoana1[3]="Student"
#print(persoana1[3])

# CTRL + SPACE - afiseaza formulale sau functiile pe care le poti utiliza

tuplu2 = ("Tudor", (30, "Cluj","Tamplar", ("Universitate", "Europa",("Sursa Divina",("Pur Existenta")))))

# tuplu2[1]   -> (30, "Cluj","Tamplar", ("Universitate", "Europa",("Sursa Divina",("Pur Existenta")))))
# tuplu2[1] [3]  -> ("Universitate", "Europa",("Sursa Divina",("Pur Existenta")))))
# tuplu2[1] [3][2]  -> ("Sursa Divina",("Pur Existenta")))))
# tuplu2[1][3][2][1])  -> Pur Existenta
print(tuplu2[1][3][2][1])
print("=========END TUPLUS=========")

# END TUPLES

#######################################
#SETS
# sets - data structures. Setturile nu sunt ordinate si nu au index
#{3,4,100,200,5,9,0}
#{}
#{3,4,3} - nu este un set deoarece un set contine doar date unice

var2={3,4,10,0}
print(var2)

var2.add(100)
print(var2)

var2.remove(100)
print(var2)


# complexitate
# 0(n)

persoane = ["Tudor","Maria","Vlad","Adrian","Flavia","Vlad","Marius"]
#persoane = ["Tudor","Maria","Vlad","Popa","Adrian","Flavia","Vlad"]

print(persoane)

var4=set(persoane)
print(var4)
#la creare set s-au eliminat duplicatele
#in este un operator de comparare, compara datele

#7 pasi pana a ajuns la Marius
# Complexitatea codului astuia este 0(n), adica in acest caz o sa fie 0(7) -> Liniar
if "Marius" in persoane:
    print("Marius este printre noi")
else:
    print("Marius nu este printre noi")

#1 Pas
# Complexitatea este 0(1) -> Constant
# Daca elementul este unic atunci H (hashes) este unic, timpul de procesare este rapid
if "Marius" in var4:
    print("Marius este printre noi")
else:
    print("Marius nu este printre noi")

# END SETS

print("=========END SETS========")

##########################

# Liste + Strings

str1 = "LOG: Hello this is Vlad the Impaler."
str2 = "WARN: My story is way overblown"
str3 = "ERROR:  )((^%%$##"
list3 = ["adrian", "client", "student"]
list4 = [str1,str2,str3]
#list4 = ["Hello this is Vlad the Impaler.","My story is way overblown",")((^%%$##"]

print(list4)
#task: split all the strings in our lists, split them using ":"
# example: "LOG: Hello this is Vlad the Impaler."  -> ["LOG", "Hello this is Vlad the Impaler."]

#print(list4[0].split(":"))
# ex: o metoda de splitare
# print(list4[0].split(":"))
# print(list4[1].split(":"))
# print(list4[2].split(":"))
#split daca nu indic caracterul face automat split dupa spatiu

####o metoda automata de a trece pas cu pas prin elementele dintr-o lista
# 0,1,2 - lista are 3 numere, in acest caz este 3
# len returneaza nr de numere
print(len(list4))
print(list(range(len(list4))))




for i in range(len(list4)):
    # print("Elementul de pe pozitia: ")
    # print(i)
    # print(list4[i])
    list4[i] = list4[i].split(":")

print(list4)
#list4:
#[
# ["LOG: Hello this is Vlad the Impaler."]
# ["WARN: My story is way overblown"]
# ["ERROR:  )((^%%$##"]
#]
#
print("===========")

## metoda de schimbare element din lista
# list5 = [10,20,30]
# list5[1] = 100
# print(list5)













