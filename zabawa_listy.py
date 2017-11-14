import random

numList = []

for i in range(5):
    numList.append(random.randrange(1,10))

i = len(numList) - 1

print("Przed zamianą:", numList)

while i > 0:

    j = 0

    while j < i:

        if numList[j] > numList[j + 1]:
            temporary = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temporary

        j += 1

    i -= 1


print("Po posortowaniu:", numList)

