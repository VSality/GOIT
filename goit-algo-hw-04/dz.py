import timeit
import random
from insert_sort import insertion_sort
from merge_sort import merge_sort

# Генерация массива случайных чисел

min_value = 1  # Минимальное значение
max_value = 10000  # Максимальное значение

numbers_short = [random.randint(min_value, max_value) for _ in range(20)]
numbers_middle = [random.randint(min_value, max_value) for _ in range(500)]
numbers_long = [random.randint(min_value, max_value) for _ in range(1000)]


print("----- short array -------------")
execution_time = timeit.timeit(f'{insertion_sort(numbers_short)}', number=100000)
print("Время выполнения insertion_sort:", execution_time, "секунд")
execution_time = timeit.timeit(f'{merge_sort(numbers_short)}', number=100000)
print("Время выполнения merge_sort:", execution_time, "секунд")
execution_time = timeit.timeit(f'{sorted(numbers_short)}', number=100000)
print("Время выполнения TimSort:", execution_time, "секунд")


print("----- middle array -------------")
execution_time = timeit.timeit(f'{insertion_sort(numbers_middle)}', number=100000)
print("Время выполнения insertion_sort:", execution_time, "секунд")
execution_time = timeit.timeit(f'{merge_sort(numbers_middle)}', number=100000)
print("Время выполнения merge_sort:", execution_time, "секунд")
execution_time = timeit.timeit(f'{sorted(numbers_middle)}', number=100000)
print("Время выполнения TimSort:", execution_time, "секунд")

print("----- large array -------------")
execution_time = timeit.timeit(f'{insertion_sort(numbers_long)}', number=100000)
print("Время выполнения insertion_sort:", execution_time, "секунд")
execution_time = timeit.timeit(f'{merge_sort(numbers_long)}', number=100000)
print("Время выполнения merge_sort:", execution_time, "секунд")
execution_time = timeit.timeit(f'{sorted(numbers_long)}', number=100000)
print("Время выполнения TimSort:", execution_time, "секунд")
