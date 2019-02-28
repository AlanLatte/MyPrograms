# Шукуров Фотех Фуркатович
# группа № 181-362
name = "Михаил Евграфович Салтыков"
pseudonym = "Николай Щедрин"
psUpper = pseudonym.upper()
test = input("Какой по вашему у него Михаила Евграфовича Салтыкова псведоним?\n")
upper = test.upper()
if upper == psUpper:
    print("Вы абсолютно правы!")
else:
    print("Вы не правы, его псевдоним: " + pseudonym)
input("\n\n\tPress enter to exit")
