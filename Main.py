    #Task 1
# name_film = input();
# name_cinema = input();
# time = input();
# print("Билет на '" + name_film + "' в '" + name_cinema + "' на " + time + " забронирован.")

    #Task 2
# word_first = input()
# word_second = input()
# if word_first == "да" or word_first == "нет":
#     if word_second == "да" or word_second == "нет":
#         print("True")
# else:
#     print("False")

    #Task 3
# user_login = input()
# user_email = input()
# if "@" not in user_login and "@" in user_email:
#     print("Input is correct!")
# else:
#     print("Input is wrong!")

    #Task 4
#print(input())

    #Task 5
# if input() == "":
#     print("YES")
# else: print("NO")

    #Task 6
num = int(input())
max, min = 0, 9
sum = 0
vart = "13"
i = 3

while num:
    if num % 10 > max:
        max = num % 10
    if num % 10 < min:
        min = num % 10
    sum += num % 10
    num = num // 10

if (max+min)/2 == (sum - (max+min)):
    print("Вы ввели красивое число")
else: print("Жаль, вы ввели обычное число")