# Шукуров Фотех Фуркатович
# группа № 181-362
import random

name: str = ""
attempts = int(10)
while attempts >= 1:
    massive = ["Кирилл", "Мефодий"]
    random.shuffle(massive)
    massiveUpper: str = massive[0].upper()
    name = input("Назовите имя одного из основателей старословянской азбуки: \n\tОтвет:")
    if massiveUpper == name.upper():
        attempts += 1
        print("Ты угадал!\nПопыток осталось: " + str(attempts))
    elif attempts == 15:
        print("\n\n\t\t\\\\\\ТЫ ВЫИГРАЛ!\\\\\\\n\n")
        break
    else:
        attempts -= 2
        print("Я загадывал не это имя!\nПравильный ответ: " + massiveUpper.title() + "\nПопыток осталось: " + str(
            attempts))
if attempts == 0:
    print("\n\n\t\t\\\\\\ТЫ ПРОИГРАЛ\\\\\\\n\n")
input("press enter for quit")
