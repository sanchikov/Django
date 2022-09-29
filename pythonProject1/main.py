q = int(input('Введите нужное количество билетов'))
q = int(q)
if type(q) == int:

    for i in range(q):
     i += 1
    while True:
       try:
         age = input(f'Ваш возраст #{i}')
         age = int(age)
         if age < 18:
            print("Бесплатный билет")
         elif age >= 18 <= 25 and q <= 3:
            print(q*990,'рублей')
         elif age >= 18 <= 25 and q >= 3:
            print(q*891, "рублей")
         elif age > 25 and q > 3:
            print(q*1251, "рублей")
         else:
            print(q*1390, 'рублей')




