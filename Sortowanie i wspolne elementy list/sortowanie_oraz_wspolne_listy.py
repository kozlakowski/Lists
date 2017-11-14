import random

list1 = []

for i in range(10):
    list1.append(random.randrange(1,21))

list2 = []

for i in range(10):
    list2.append(random.randrange(1,21))

print("list1 :", list1)
print()
print("list2 :", list2)



wspolna_lista = []

for num in list1:

    if (num in list1) and (num in list2) and (num not in wspolna_lista ):
        wspolna_lista.append(num)



print()
print("Wspolna lista:", wspolna_lista)


i = len(wspolna_lista) - 1

while i > 0:

    j = 0

    while j < i:

        if wspolna_lista[j] > wspolna_lista[j + 1]:

            tymczasowe = wspolna_lista[j]
            wspolna_lista[j] = wspolna_lista[j + 1]
            wspolna_lista[j + 1] = tymczasowe

        j += 1

    i -= 1


print("Posortowana lista wspólna :", wspolna_lista)

