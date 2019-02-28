# Шукуров Фотех Фуркатович
# группа № 181-362
import random

mas = ["КИРИЛЛ", "МЕФОДИЙ"]
random.shuffle(mas)
name = input("Назовите одного из двух братьев, создателей старославянской азбуки: ")
nameUpper = name.upper()
if mas[0] == nameUpper:
    print("Ты выиграл!")
else:
    print("Я загадывал не это имя.\nПравильный ответ:\n\t\t" + str(mas[0].title()))
input("\n\n\tPress enter to exit")
