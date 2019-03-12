BEFORE = ['1> Дороро / Dororo [08 из 12+]<', '2> Моб Психо 100 ТВ-2 / Mob Psycho 100 TV-2 [10 из 12]<', '3> О моём перерождении в слизь / Tensei Shitara Slime Datta Ken [22 из 25]<', '4> Восхождение Героя щита / Tate no Yuusha no Nariagari [09 из 25]<']

AFTER = ['1> Дороро / Dororo [09 из 12+]<', '2> Моб Психо 100 ТВ-2 / Mob Psycho 100 TV-2 [10 из 12]<', '3> О моём перерождении в слизь / Tensei Shitara Slime Datta Ken [22 из 25]<', '4> Восхождение Героя щита / Tate no Yuusha no Nariagari [09 из 25]<']


result=list(set(AFTER) - set(BEFORE))
print(result[0][0])
