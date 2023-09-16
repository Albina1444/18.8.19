# Шаг 1: Ввод количества билетов
num_tickets = int(input("Введите количество билетов: "))

# Шаг 2: Ввод возраста и подсчет стоимости для каждого билета
total_cost = 0
for i in range(num_tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        # бесплатный проход на конференцию
        cost = 0
    elif age >= 18 and age <= 25:
        # стоимость для возраста от 18 до 25 лет
        cost = 990
    else:
        # полная стоимость для возраста от 25 лет и старше
        cost = 1390

    total_cost += cost

# Шаг 3: Применение скидки при необходимости
if num_tickets > 3:
    discount = 0.1 * total_cost
    total_cost -= discount

# Вывод суммы к оплате
print("Сумма к оплате:", total_cost)

