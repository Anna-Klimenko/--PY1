money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# предположим, что расходы вычитаются после начисления зп

while money_capital + salary >= spend: # подушка и зп не должны превышать расходы
    money_capital = money_capital + salary - spend # перезаписываем остаток фин.подушки после всех фин.операций
    spend *= increase + 1
    month += 1

print(month)
