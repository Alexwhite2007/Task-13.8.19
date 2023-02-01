number_of_tickets = int(input("Сколько нужно билетов: "))  # количество билетов к покупке
ages = []  # список возрастов для каждого билета
# запрашиваем возраст и заполняем ages числами, которые вводит пользователь
for i in range(0, number_of_tickets):
    input_age = int(input(f'Введите возраст участника № {i + 1}:\n'))
    ages.append(input_age)

# считаем стоимость билетов в зависимости от возраста
prices = []
for i in ages:
    if i < 18 in ages:
        prices.append(0)
    elif 18 <= i <= 25:
        prices.append(990)
    elif i > 25:
        prices.append(1390)
total_price = sum(prices)  # стоимость всех билетов

# проводим скидку если количество билетов больше 3
discount_price = int(total_price * 0.9)  # расчет скидки 10% если регистрируется больше трёх человек
if number_of_tickets > 3:
    print('Стоимость всех билетов со скидкой: ', discount_price, "руб.")
else:
    print('Стоимость всех билетов: ', total_price, "руб.")
