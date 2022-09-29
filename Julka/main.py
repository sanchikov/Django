total = 0
while True:
    try:
        ticket_qty = input('Сколько билетов вы хотите приобрести на мероприятие? ')
        ticket_qty = int(ticket_qty)
        if type(ticket_qty) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_qty):
    i += 1
    while True:
        try:
            age = input(f'Для какого возраста билет №{i}? ')
            age = int(age)
            if age < 18:
                print('Билет бесплатный')
            elif 25 > age >= 18:
                total += 990
                print('Стоимость билета: 990 руб.')
            else:
                total += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_qty > 5:
    price_all = total - ((total / 100) * 20)
    print(f'Всего к оплате {total} рублей с учетом 20% скидки при регистрации больше 5-ти человек')
else:
    print(f'Всего к оплате {total} рублей')