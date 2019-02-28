# Шукуров Фотех Фуркатович
# группа № 181-362
name = "Доменико Теотокопули "
pseudonym = "Эль Греко "
work = "Живописец, скульптор и архитектор эпохи Испанского Ренессанса "
placeOfBirth = "деревне Фоделе, близ Ираклиона "
dateofBirthday: int = 1541
dateOfDeath: int = 1614
lived: int = (dateOfDeath - dateofBirthday)
print(name + "более известный как " + pseudonym + "--- " + work + "\n\tРодился: " + str(
    dateofBirthday) + "\n\tВ " + placeOfBirth + "\n\tУмер: " + str(dateOfDeath) + "\n\tВ возрасте: " + str(lived))
input("\n\n\tPress enter to exit")
