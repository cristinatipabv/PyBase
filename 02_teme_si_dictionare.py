raw_logs = [
" ERROR | Voltage too LOW | code=E12 ", #index1 - randul1
" info | System started successfully ", #index2 - randul2
" WARNING | High temperature detected | code=W07 ", #index3 - randul3
" ERROR | Communication timeout | code=E99 ", #index4 - randul4
" info | System shutdown complete " #index5 - randul5
]

# for elem in raw_logs:
#     print(elem)


for i in range(len(raw_logs)):
    #for i -> creaza o variabila i
    #len(raw_logs) -> 5
    #range(len(raw_logs) -> range(5) -> [0,1,2,3,4]
    #i -> index

    # 1.Clean each log line
    #stripul sterge spatiile de la inceput si la sf
    raw_logs[i] = raw_logs[i].strip().lower()
    #print(raw_logs[i])
    # print (i) - genereaza 5 printuri

    ###########################ex ptr strip si lower
    #var1 = "     EU sunt     Un sir de Caractere       E  cu cateva   spatii"
    #var2 = var1.strip().lower()
    #var2 = var2.lower()
    #print(var1)
    #print(var2)


    # 2.Split log fields
    # now i
    raw_logs[i] = raw_logs[i].split("|")
    print(raw_logs[i])

    ##ex
    #var1 = "error  |  lightning   strike | system shutdown"
    #var2=var1.split("|")
    #print(var2)

print ("Starting Identification:")

log_type_counts = []

for i in range(len(raw_logs)):
    #raw_logs[i] -> ['error ', ' voltage too low ', ' code=e12']
    #raw_logs[i][0] -> 'error '
    # raw_logs[i][0][0] -> 'e'
    #print(raw_logs[i][0]) printul afiseaza:
    # error
    # info
    # warning
    # error
    # info
    #raw_logs[i][0].startswith("error")
    #print(raw_logs[i][0].startswith("error"))
    #ptr a numara valorile dintr-o lista tb adaugate intai
    # ex de creare de adaugare elemente intr-o lista goala si numararea lor utilizand count
    # lista1 = []
    # print(lista1)
    # lista1.append(30)
    # lista1.append(100)
    # lista1.append(30)
    # lista1.append(350)
    # lista1.append(30)
    #
    # print(lista1.count(30))

    if raw_logs[i][0].startswith("error"):
        log_type_counts.append(raw_logs[i][0].strip())

    if raw_logs[i][0].startswith("info"):
        log_type_counts.append(raw_logs[i][0].strip())

    if raw_logs[i][0].startswith("warning"):
        log_type_counts.append(raw_logs[i][0].strip())


error_count = log_type_counts.count("error")
warning_count = log_type_counts.count("warning")
info_count = log_type_counts.count("info")

output_string = f"""
OUTPUT
LOG SUMMARY
-----------
Errors : {error_count}
Warnings : {warning_count}
Info : {info_count}

Error Codes: E12, E99
Warning Codes: W07
"""
print(output_string)



# print('OUTPUT')
# print("LOG SUMMARY")
# print("----------")
# print("Errors   :")
# print(log_type_counts.count("error"))
# print("Warnings   :")
# print(log_type_counts.count("info"))
# print("Info   :" )
# print(log_type_counts.count("warning"))

########### ex de functie f-strings
# print("---------F-Strings------------")
#
# string2 = "Horatiu"
# var3 = f"{string2} are 30 de mere"
# print(var3)