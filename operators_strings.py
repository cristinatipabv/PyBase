from itertools import combinations

#produs = 1

#for i in range(5):
#    produs = produs * (i+1)

#print(produs)

#import math

#produs = math.factorial(5)
#print(produs)

# doime_nr = 121
# nr=doime_nr*2
# print(nr)
# triplu_nr=3*nr
# print(triplu_nr)
#
#
# produs_numere_pare = 1
# for i in range(6):
#     if i % 2 == 0 and i !=0:
#         produs_numere_pare = produs_numere_pare*i
# print(produs_numere_pare)
#
# rezultat = triplu_nr + produs_numere_pare
# print(rezultat)

# //
# boxes = 53
# boxes_per_pallet = 10
#
# full_pallets = boxes // boxes_per_pallet
# print(full_pallets)

# **
# a=2
# b=3
# c=a**b
# print(c)

# modes = 3
# devices = 4
#
# combin= modes ** devices
# print(combin)

# door_closed = True
# emergency_stop_pressed = False
#
# start_machine = door_closed and not emergency_stop_pressed
# print(start_machine)

# door_closed = True
# emergency_stop_pressed = False
#
# start_machine = door_closed and  emergency_stop_pressed
# print(start_machine)

# door_closed = True
# emergency_stop_pressed = False
# breek_pressed = True
# start_machine = door_closed and not emergency_stop_pressed and breek_pressed
# print(start_machine)

# voltage_ok = True
# communication_ok = False
#
# test_fail = (not voltage_ok) or (not communication_ok)
# print(test_fail)
#
# voltage_ok = True
# communication_ok = True
#
# test_fail = not voltage_ok or not communication_ok
# print(test_fail)

# value = 42
# print(value)
# print(bin(value))
# print(hex(value))

# &, |, ~
# 001100101

# READ = 0b001
# WRITE = 0b010
# EXE = 0b100
#
# user_permissions = READ | WRITE
# print(bin(user_permissions))
#
# can_write = user_permissions & WRITE
# print(can_write)
#
# print("Hello World!")
#
# s= "Hello World!"
# print(s)
# print(type(s))
#
# my_string = ""
# print(my_string)
# print(type(my_string))

# my_string = "a"
# print(my_string)
#
# print(ord("a"))
# print(chr(83))
# print(chr(97))
# print(chr(36))

# print("primul rand\nal doilea rand\nal treilea rand")
# primul rand
# al doilea rand
# al treilea rand
#
# print("""primul rand
#   al doilea rand
#     al treilea rand    refefe"""
# )

test_name = "VoltageCheck"
duration = 1.237

# test VoltageCheck finished in 1.23
print(f"test {test_name} finished in {duration:.2f} ")


test_name = "VoltageCheck"
# duration = 1.237
#
# # test VoltageCheck finished in 1.23
# print(f"test {test_name} finished in {duration:.3f} ")

print(test_name.upper())




