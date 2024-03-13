from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Визначаємо модель
model = LpProblem(name="production-planning", sense=LpMaximize)

# Визначаємо змінні
lemonade = LpVariable(name="lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

# Додаємо обмеження ресурсів
model += (2 * lemonade + 1 * fruit_juice <= 100, "water_constraint")
model += (1 * lemonade <= 50, "sugar_constraint")
model += (1 * lemonade <= 30, "lemon_juice_constraint")
model += (2 * fruit_juice <= 40, "fruit_puree_constraint")

# Функція цілі: максимізувати загальну кількість продуктів
model += lpSum([lemonade, fruit_juice])

# Вирішуємо задачу
status = model.solve()

# Виводимо результат
print(f"Виробництво лимонаду: {lemonade.value()}")
print(f"Виробництво фруктового соку: {fruit_juice.value()}")
print(f"Загальна кількість продуктів: {lemonade.value() + fruit_juice.value()}")
