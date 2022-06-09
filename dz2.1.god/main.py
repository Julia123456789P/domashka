year = int(input())


if year % 400 and year % 4 == 0:
    print('God visokosnyi')
else:
    print('God ne visokosnyi')