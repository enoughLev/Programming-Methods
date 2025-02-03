import math

    #Task 1
name_film = input()
name_cinema = input()
time = input()
print("Билет на '" + name_film + "' в '" + name_cinema + "' на " + time + " забронирован.")

    #Task 2
word_first = input()
word_second = input()
if word_first == "да" or word_first == "нет":
    if word_second == "да" or word_second == "нет":
        print("True")
else:
    print("False")

    #Task 3
user_login = input()
user_email = input()
if "@" not in user_login and "@" in user_email:
    print("Input is correct!")
else:
    print("Input is wrong!")

    #Task 4
print(input())

    #Task 5
if input() == "":
    print("YES")
else: print("NO")

    #Task 6
num = int(input())
maximum, minimum = 0, 9
summary = 0

while num:
    if num % 10 > maximum:
        maximum = num % 10
    if num % 10 < minimum:
        minimum = num % 10
    summary += num % 10
    num = num // 10

if (maximum+minimum)/2 == (summary - (maximum+minimum)):
    print("Вы ввели красивое число")
else: print("Жаль, вы ввели обычное число")

    #Task 7
num7 = int(input())

a = num7 // 1000
b = (num7 // 100) % 10
c = (num7 // 10) % 10
d = num7 % 10

min_digit = min(a, b, c, d)

if min_digit == a:
    second_min = min(b, c, d)
    if second_min == b:
        third_min = min(c, d)
        fourth_min = max(c, d)
    elif second_min == c:
        third_min = min(b, d)
        fourth_min = max(b, d)
    else:
        third_min = min(b, c)
        fourth_min = max(b, c)
elif min_digit == b:
    second_min = min(a, c, d)
    if second_min == a:
        third_min = min(c, d)
        fourth_min = max(c, d)
    elif second_min == b:
        third_min = min(a, d)
        fourth_min = max(a, d)
    else:
        third_min = min(a, c)
        fourth_min = max(a, c)
elif min_digit == c:
    second_min = min(a, b, d)
    if second_min == a:
        third_min = min(b, d)
        fourth_min = max(b, d)
    elif second_min == b:
        third_min = min(a, d)
        fourth_min = max(a, d)
    else:
        third_min = min(a, b)
        fourth_min = max(a, b)
else:
    second_min = min(a, b, c)
    if second_min == a:
        third_min = min(b, c)
        fourth_min = max(b, c)
    elif second_min == b:
        third_min = min(a, c)
        fourth_min = max(a, c)
    else:
        third_min = min(b, a)
        fourth_min = max(b, a)

print((min_digit * 1000) + (second_min * 100) + (third_min * 10) + fourth_min)

    #Task 8
heights = []
correct_heights = []
count8 = 0

while True:
    height = input()
    if height == "!": break
    else:
        heights.append(height)

for var8 in heights:
    if (int(var8) >= 150) & (int(var8) <= 190):
        count8 += 1
        correct_heights.append(var8)

while count8 >= 0:
    count8 -= 1
    print(correct_heights[count8])

    #Task 9
while True:
    first_pass = input()
    second_pass = input()

    if len(first_pass) < 8:
        print("Короткий!")
        continue
    if "123" in first_pass:
        print("Простой!")
        continue
    if first_pass != second_pass:
        print("Различаются")
        continue
    else:
        print("ОК")
        break

    #Task 10
result = 0

while True:
    first_num = int(input())
    operation = input()
    match operation:
        case "+":
            sec_num = int(input())
            result = first_num + sec_num
            print(result)
            continue
        case "-":
            sec_num = int(input())
            result = first_num - sec_num
            print(result)
            continue
        case "*":
            sec_num = int(input())
            result = first_num * sec_num
            print(result)
            continue
        case "/":
            sec_num = int(input())
            if sec_num == 0: continue
            result = first_num / sec_num
            print(result)
            continue
        case "%":
            sec_num = int(input())
            result = first_num % sec_num
            print(result)
            continue
        case "!":
            if first_num < 0: continue
            result = math.factorial(first_num)
            print(result)
            continue
        case "x":
            print(first_num)
            break

    #Task 11
height11 = int(input())
for i in range(height11):
    print(' ' * (height11 - i - 1) + '*' * (2 * i + 1))

    #Task 12
number12 = int(input())
current = 1
row = 1

while current <= number12:
    for var12 in range(row):
        if current > number12:
            break
        print(current, end=" ")
        current += 1
    print()
    row += 1

    #Task 13
n = int(input())
m = int(input())
symb = input()

for i in range(n):
    if i == 0 or i == n - 1:
        print(symb * m)
    else: print(symb + ' ' * (m -2) + symb)


