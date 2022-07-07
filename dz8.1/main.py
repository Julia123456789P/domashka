#Найти самое длинное слово в строке.

a = str(input('Vvedite stroku: '))
b = (a.split())

print(max(b, key=len))