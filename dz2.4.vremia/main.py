print('Vvedite vremia ot 0 do 24: ')


x = int(input())


if x >= 6 and x < 12:
    print('Eto utro!')
elif x >= 12 and x < 18:
    print('Eto den\'!')
elif x >= 18 and x < 24:
    print('Eto vecher!')
elif x >= 0 and x < 6:
    print('Eto noch\'!')
else:
    print('Ne verno vveli vremia!')
