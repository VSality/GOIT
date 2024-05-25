from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Створення задачі лінійного програмування
model = LpProblem(name="drinks", sense=LpMaximize)

# Змінні
L = LpVariable(name="Lemonade", lowBound=0, cat='Continuous')
F = LpVariable(name="Fruit_Juice", lowBound=0, cat='Continuous')

# Цільова функція
model += L + F, "Total_Production"

# Обмеження
model += (2 * L + F <= 100, "Water_Constraint")
model += (L <= 50, "Sugar_Constraint")
model += (L <= 30, "Lemon_Juice_Constraint")
model += (2 * F <= 40, "Fruit_Puree_Constraint")

# Розв'язання задачі
status = model.solve()

# Результати
print(f"Lemonade: {L.value()} units")
print(f"Fruit Juice: {F.value()} units")