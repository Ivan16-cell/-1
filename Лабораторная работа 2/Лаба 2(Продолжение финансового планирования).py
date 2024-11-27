salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы  протянуть 10 месяцев без долгов

#print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", ...)


money_capital = 0

for months in range(1, months+1):
  current = spend * (1+increase)**(months-1)
  lack = current - salary
  if lack > 0:
      money_capital += lack

money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)

