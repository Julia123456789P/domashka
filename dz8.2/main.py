#Преобразовать текст в кортеж слов с удалением знаков препинания.


a = [input('Vvedite text: ')]
i = 0

if i == ',':
    a.pop(i)
    i += 1

b = tuple(a)

print(b)