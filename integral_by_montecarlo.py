import numpy as np
import scipy.integrate as spi

def monte_carlo_integral(a, b, num_points=10000):
    # Генеруємо випадкові точки для x в інтервалі від a до b
    x_random = np.random.uniform(a, b, num_points)
    
    # Обчислюємо y для кожної точки x
    y_random = x_random ** 3
    
    # Знаходимо максимальне та мінімальне значення y для визначення меж прямокутника
    y_max = max(y_random)
    y_min = min(y_random)  # Використовується, якщо функція приймає від'ємні значення
    
    # Генеруємо випадкові точки y в інтервалі від y_min до y_max
    y_random = np.random.uniform(y_min, y_max, num_points)
    
    # Підрахунок точок, що потрапили під криву
    under_curve = y_random <= x_random ** 3
    
    # Обчислення площі під кривою
    area = ((b - a) * (y_max - y_min)) * np.mean(under_curve)
    
    return area

# Визначимо інтервал інтегрування, наприклад, від 0 до 1
a = 0
b = 1

# Обчислюємо інтеграл
integral_value = monte_carlo_integral(a, b)
print(f"Значення інтегралу функції y = x^3 на інтервалі від {a} до {b} методом Монте-Карло: {integral_value}")

# Обчислюємо інтеграл через spi
def f(x):
    return x**3

result, error = spi.quad(f, a, b)
print("Інтеграл scipy: ", result, error)
