a = int(input())
b = int(input())
c = int(input())


if a + b > c and b + c > a and a + c > b:
    print('Eto treugol\'nik')
else:
    print('Eto ne treygol\'nik')