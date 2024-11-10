numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


summa = 0
count = 0

for i in range(len(numbers)):
    if type(numbers[i]) == int:
        summa += numbers[i]
        count += 1

average = summa / len(numbers)


for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = average

print("Измененный список:", numbers)







