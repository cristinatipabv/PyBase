from doctest import Example
Example = 1
example = 2

example += 3
example = example + 3

example +=1

print(example)

a=3

aux = 55

a=aux*5
PI = 3.14
TIMEOUT_MSG_X = 500

print(a)
print(id(a))

suma_doua_numere = 0

check_flag = False
print(type(check_flag))





b=6
c=b+a
#print(c)

#0,1,2,3,4,...9
#This is a for statement
#suma = 1+2+3+4+5
#produs = 1*2*3...*9
suma1 = 0
produs = 1

for i in range(5):
    suma1 = suma1 + i
    produs = produs * (i+1)
    #print(suma)
    #print(2*i)

print(suma1)

#suma = n*(n+1)/2
suma2 = 9*(9+1)/2
#print(suma2)

print(produs)

print(type(suma2))

var_flag = True

if var_flag == False:
    print("Ästazi este miercuri!")
else:
    print("Astazi o zi de weekend!")


for i in range(20):
    if i % 2 == 1:
        print(f"Numarul {i} este par: ")
    #else:
     #  print("Numarul este impar: ", i)
