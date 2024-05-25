import numpy as np
import scipy.integrate as spi

# Кількість випадкових точок
N = 1000

# Генеруємо N випадкових точок (x, y) в межах прямокутника [0, 2] x [0, 4]
x_random = np.random.uniform(0, 2, N)
y_random = np.random.uniform(0, 4, N)

# Визначаємо, скільки точок лежить під графіком y = x^2
under_curve = y_random <= x_random**2
M = np.sum(under_curve)

# Площа прямокутника [0, 2] x [0, 4]
rect_area = 2 * 4

# Оцінка площі під кривою
area_under_curve = (M / N) * rect_area

print(f"Оцінена площа під графіком: {area_under_curve}")

def f(x):
    return x**2

# Визначте межі інтегрування, наприклад, від 0 до 1
a = 0  # нижня межа
b = 2  # верхня межа

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл: ", result)