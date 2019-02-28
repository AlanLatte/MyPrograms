#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random


def word():
    with open(r'src\easy.txt', 'rt') as text_:
        void = []
        for word__1 in text_:
            void.append(word__1)
        return random.choice(void)


def list__in():
    with open(r'src\correct.txt', 'w') as list_in:
        for list_item in WORD[:-1]:
            list_in.write(list_item)


def task():
    global used_wrong_Words, used_correct_Words
    used_correct_Words += answer.lower()
    print("Правильные:\n")
    for i in used_correct_Words:
        print(i, end="|")
    print("\t")
    return used_correct_Words


def task_1():
    global used_wrong_Words
    used_wrong_Words += answer.lower()
    print("Не правильные буквы: ")
    for i in used_wrong_Words:
        print(i, end="|")
    print("\t")


def test_func():
    with open(r'src\correct.txt') as test_open:
        return test_open.read()


WORD: str = word().lower()
list__in()
answer_Words = ""
used_correct_Words = ""
used_wrong_Words = ""
print("В слове ", str(len(WORD) - 1), "букв.\nУгадай их.")
print('|', ' _  ' * (len(WORD) - 1))
for i in range(len(WORD) - 1):
    print("  ", i + 1, end="")
print('   |')
health = 5
health_answer = 3
while health:
    answer = input("Введи букву: \n\t")
    if answer.isalpha() and len(answer.lower()) == 1:
        if answer.lower() in WORD and answer.lower() not in used_correct_Words:
            print("\nДа, такая буква есть")
            health -= 1
            answer_Words += answer
            if answer not in used_correct_Words:
                print("\nВы использовали такие буквы:\n\t")
                used_correct_Words = task()
        elif (answer.lower() not in used_wrong_Words) and (answer.lower() not in used_correct_Words):
            task_1()
            health -= 1
    else:
        continue
input("Угадай теперь слово целиком ;)\nНажми 'Enter' когда будешь готов. ")
with open(r'src\correct.txt') as file_in:
    text = file_in.read()
for i in text:
    if i not in answer_Words:
        text = text.replace(i, "(_)")
with open(r'src\correct.txt', "w") as file_out:
    file_out.write(text)
while health_answer:
    health_answer -= 1
    print(test_func())
    res = input("\nТвои мысли?\n\tОтвет: \t")
    if res.lower() == WORD[:-1]:
        print("Ты выиграл! Поздравляю!")
        break
    else:
        print("Пробуй еще, у тебя еще " + str(health_answer) + " попыток")
if health_answer == 0:
    print("Ты был близок, но пал в суровом бою.\n","Правильный ответ: ",WORD)
input("Нажми 'Enter' для выйхода")
