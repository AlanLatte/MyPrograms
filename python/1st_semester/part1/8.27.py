import random
import codecs


def anagrams():
    text_1 = ""
    with open(r'\src\zdf-win.txt', 'rt', "utf-8") as TEXT:
        void = []
        for line in TEXT:
            void.append(line[:len(line) - 1])
        word = random.choice(void)
    correct_answer = word
    while word:
        pos = random.randrange(len(word))
        text_1 += word[pos]
        word = word[:pos] + word[(pos + 1):]
    return text_1, correct_answer


def answer(x, y, z):
    global text, correct
    point = 100
    health = y
    while point:
        answer_1 = input("Попробуй угадать слово: \n\t\t[" + text + "]\n\n\t\tОтвет: ")
        if answer_1.lower() == correct:
            print("Ты выиграл!1!\n\t\t[\\\\\\_У тебя " + str(point) + " очков_///]")
            break
        else:
            point -= x
            health -= 1
            print("Осталось попыток: " + "[ " + str(point) + " ]")
            if health == 1:
                tips = input("Хочешь видеть подсказку?\n1.Да\n2.Нет\n\tОтвет: \t")
                if tips.lower() == "да" or tips == "1":
                    print(correct[:z], "_" * (len(correct) - z * 2), correct[-z:])


answer_2 = input("Укажите уровень сложности игры:\n1.Легко\n2.Нормально\n3.Сложно\n\tОтвет:\t")
while True:
    answer_3 = answer_2
    anagrams_1 = anagrams()
    text = anagrams_1[0]
    correct = anagrams_1[1]
    if (answer_3 == "1" or answer_3.lower() == "легко") and answer_3:
        if 4 <= len(text) <= 6:
            print('Режим "Легкий": \n\n\n\t')
            answer(x=50, y=2, z=1)
            break
    elif (answer_3 == "2" or answer_3.lower() == "нормально") and answer_3:
        if 6 < len(text) <= 9:
            print('Режим "Нормальный": \n\n\n\t')
            answer(x=25, y=3, z=1)
            break
    elif (answer_3 == "3" or answer_3.lower() == "сложный") and answer_3:
        if 9 < len(text) <= 100:
            print('Режим "Сложный": \n\n\n\t')
            answer(x=20, y=4, z=3)
            break
    else:
        print("\n\nПробуй еще\n\n")
        answer_2 = input("Укажите уровень сложности игры:\n1.Легко\n2.Нормально\n3.Сложно\n\tОтвет:\t")
print("\n\tПравильное слово: [\t" + correct + " ]")
input("Press enter for quit")
