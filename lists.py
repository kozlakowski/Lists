import random
import math

numList = []

for i in range(5):
    numList.append(random.randrange(1,10))

i = len(numList) - 1

while i > 0:

    j = 0

    while j < i:

        if numList[j] > numList[j + 1]:

            tymczasowe = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = tymczasowe


        else:
            print()

        j += 1

    i -= 1

for k in numList:
    print(k, end=", ")

print()

