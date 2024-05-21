import pulp

# Створення моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Змінні
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit Juice', lowBound=0, cat='Continuous')

# Функція мети
model += lemonade + fruit_juice, "Total Products"

# Обмеження
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint"
model += 1 * lemonade <= 50, "Sugar Constraint"
model += 1 * lemonade <= 30, "Lemon Juice Constraint"
model += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Розв'язання моделі
model.solve()

# Виведення результатів
print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Кількість виробленого лимонаду: {lemonade.varValue}")
print(f"Кількість виробленого фруктового соку: {fruit_juice.varValue}")
print(f"Максимальна кількість продуктів: {pulp.value(model.objective)}")
