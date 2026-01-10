from itertools import combinations

from pyexpat.errors import messages

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

# test_name = "VoltageCheck"
# duration = 1.237
#
# # test VoltageCheck finished in 1.23
# print(f"test {test_name} finished in {duration:.2f} ")
#
#
# test_name = "VoltageCheck"
# duration = 1.237
#
# # test VoltageCheck finished in 1.23
# print(f"test {test_name} finished in {duration:.3f} ")

#print(test_name.upper())

#print(test_name.lower())

# command = 'Start'
#
# if command == 'StaRt':
#     print ('Starting system')
#
# if command.lower() == 'start':
#     print ('Starting system')

# word = 'Python'

# print(word[0])
# print(word[3])
#
# print(word[-1])

# text = 'Programming'
# print(text[0:6])
#
# print(text[:4])
#
# print(text[4:])

# message = 'hello Python'
# # len
# print(len(message))

# a= 'Hello'
# b= 'World'
#
# print(a + ' ' + b)

# raw = '    ERROR_CODE_12  '
# print(raw)
# # strip
# clean_string = raw.strip()
# print(clean_string)

# replace ()
# log = 'Voltage=12,5V   new text1, text2'
#  float 12.5 <- 12,5
# print(log)
# log = log.replace(',', '.')
# print(log)

# sdsds.txt
# sdsd.exe
# file.log

# filename = 'report_2025.log'
#
# if filename.endswith('.log'):
#     print('Log file detected')
#
# if filename.startswith('report'):
#     print('Report file detected')
#

# find
# message = 'CAN timeout detected'
# print(message)
# index = message.find('timeout')
# print(index)
#
# index = message.find('exe')
# print(index)

# in vs find

# Timeout_flag = False
# if 'timeout' in message:
#     timeout_flag = True
#     print('Timeout found!')

# split

# data = '12.5, 3.7, OK'
# print(data)
# values = data.split(',')
# print(values)

# my_strings = ['Ana ', 'are ', 'mere ', '!']
# final_string = ''.join(my_strings)
# print(final_string)



# problema: parti dintr-un path intr-un fisier, vreau sa gasesc un anumit path
# parts = ['c:', 'logs', '2026', 'run_01.txt']
# path = '/'.join(parts)
# print(path)

# Password Generator

# import random
#
# s ='Ana are mere!'
# s_random = random.sample(s,3)
# print(s_random)

####### generare parola utilizand mai multe conditii
# import random
# lower = 'abcdefghijklmnopqestuvwyz'
# upper = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
# numbers = '0123456789'
# symbols = '!@#$%^&*()'
#
# all_string = lower+upper+numbers+symbols
# print(all_string)
#
# length = 16
# password = ''.join(random.sample(all_string, length))
# print(password)

######### vreau sa intreb utilizatorul care foloseste sistemul ce tb sa execute
# function input
a = ""

# while a != "STOP":
#     a = input("Add data: ")
#     print(a)
#
# print("The user sttoped entering the data!")


# ##### Liste

# my_list = [70, 5, -7, 50, 50, -7, -20.5, True, "Ana are mere", 4+7j]
# print(my_list)
#
# print(my_list[0])
# print(my_list[3])
# print(my_list[-1])

# print(len(my_list))
# sliced_list = my_list[:4]
# print(sliced_list)
# sliced_list = my_list[4:]
# print(sliced_list)
# sliced_list = my_list[-3]
# print(sliced_list)

######### o lista ca o baza de date din tastatura

# db = []
# print(db)
#
# get_data = ""
# while get_data != "STOP":
#     get_data = input("Add Data: ")
#     if get_data != "STOP": db.append(get_data)
# print(db)
