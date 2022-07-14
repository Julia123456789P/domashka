#У вас есть словарь, где ключ – название продукта. Значение – список, который содержит цену и кол-во товара.
#Выведите через ‘’–’’ название – цену – количество.
#С клавиатуры вводите название товара и его кол-во. n – выход из программы. Посчитать цену выбранных товаров
# и сколько товаров осталось в изначальном списке.

dict = {'milk': [2.1, 100],
        'apple': [3.5, 200],
        'water': [1.5, 1000],
        'beer': [4.2, 500]}

for key, value in dict.items():
    print(key, '-', value[0], '-', value[1])
i = 0

while True:
    d = input('Tovar ili vuhod (n): ')
    if d == 'n' or d not in dict.keys():
        break
    k = int(input('Kol-vo: '))
    if k > dict[d][1]:
        print('No')
        continue
    i += dict[d][0] * k
    dict[d][1] -= k
print('Chek: ', i)
print('--------------------')

for key, value in dict.items():
    print(key, '-', value[0], '-', value[1])




