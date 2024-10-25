numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

count = 0
for num in numbers:
    if num is not None:
        count += num

none = count/len(numbers)
numbers[4] = none
print("Измененный список:", numbers)
