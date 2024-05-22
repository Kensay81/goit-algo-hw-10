import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return np.sin(x) * np.exp(-x/2)

a = 0  # Нижня межа
b = 5  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-1, 6, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([min(y) - 0.1, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = sin(x) * exp(-x/2) від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Обчислення інтеграла з використанням scipy
result, error = spi.quad(f, a, b)
print("Результат при використанні аналітичного метода (quad) : ", result)
print(f"Похибка аналітичного обчислення: {error:.2e}")

# Метод Монте-Карло для обчислення інтеграла
x_random = np.random.uniform(a, b, 10000)
y_random = f(x_random)

# Обчислення значення інтегралу
integral_value = (b - a) * np.mean(y_random)
print("Результат при використанні метода Монте-Карло: ", integral_value)

print(f"Різниця між результатами: {abs(integral_value - result):.6f}")
