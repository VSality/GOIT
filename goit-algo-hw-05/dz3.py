import timeit
from knut_search import kmp_search
from boer_search import boyer_moore_search
from rabin_search import rabin_karp_search


# Открываем файл и читаем его содержимое
with open('goit-algo-hw-05/page1.txt', 'r', encoding='windows-1251') as file:
    page1_string = file.read()
    
with open('goit-algo-hw-05/page2.txt', 'r', encoding='windows-1251') as file:
    page2_string = file.read()


pattern_yes_page1 = "бібліотеках"
pattern_no_page1 = "блабла"

pattern_yes_page2 = "даних"
pattern_no_page2 = "блабла"

print("----- Knut -------------")
execution_time = timeit.timeit(f'{kmp_search(page1_string, pattern_yes_page1)}', number=1000000)
print("Время выполнения YES Knut page1:", execution_time, "секунд", "найдено ", kmp_search(page1_string, pattern_yes_page1))
execution_time = timeit.timeit(f'{kmp_search(page1_string, pattern_no_page1)}', number=1000000)
print("Время выполнения NO Knut page1:", execution_time, "секунд", "найдено ", kmp_search(page1_string, pattern_no_page1))

execution_time = timeit.timeit(f'{kmp_search(page2_string, pattern_yes_page2)}', number=1000000)
print("Время выполнения YES Knut page2:", execution_time, "секунд", "найдено ", kmp_search(page2_string, pattern_yes_page2))
execution_time = timeit.timeit(f'{kmp_search(page2_string, pattern_no_page2)}', number=1000000)
print("Время выполнения NO Knut page2:", execution_time, "секунд", "найдено ", kmp_search(page2_string, pattern_no_page2))

print("----- Boer -------------")
execution_time = timeit.timeit(f'{boyer_moore_search(page1_string, pattern_yes_page1)}', number=1000000)
print("Время выполнения YES Boer page1:", execution_time, "секунд", "найдено ", boyer_moore_search(page1_string, pattern_yes_page1))
execution_time = timeit.timeit(f'{boyer_moore_search(page1_string, pattern_no_page1)}', number=1000000)
print("Время выполнения NO Boer page1:", execution_time, "секунд", "найдено ", boyer_moore_search(page1_string, pattern_no_page1))

execution_time = timeit.timeit(f'{boyer_moore_search(page2_string, pattern_yes_page2)}', number=1000000)
print("Время выполнения YES Boer page2:", execution_time, "секунд", "найдено ", boyer_moore_search(page2_string, pattern_yes_page2))
execution_time = timeit.timeit(f'{boyer_moore_search(page2_string, pattern_no_page2)}', number=1000000)
print("Время выполнения NO Boer page2:", execution_time, "секунд", "найдено ", boyer_moore_search(page2_string, pattern_no_page2))

print("----- Rabin -------------")
execution_time = timeit.timeit(f'{rabin_karp_search(page1_string, pattern_yes_page1)}', number=1000000)
print("Время выполнения YES Rabin page1:", execution_time, "секунд", "найдено ", rabin_karp_search(page1_string, pattern_yes_page1))
execution_time = timeit.timeit(f'{rabin_karp_search(page1_string, pattern_no_page1)}', number=1000000)
print("Время выполнения NO Rabin page1:", execution_time, "секунд", "найдено ", rabin_karp_search(page1_string, pattern_no_page1))

execution_time = timeit.timeit(f'{rabin_karp_search(page2_string, pattern_yes_page2)}', number=1000000)
print("Время выполнения YES Rabin page2:", execution_time, "секунд", "найдено ", rabin_karp_search(page2_string, pattern_yes_page2))
execution_time = timeit.timeit(f'{rabin_karp_search(page2_string, pattern_no_page2)}', number=1000000)
print("Время выполнения NO Rabin page2:", execution_time, "секунд", "найдено ", rabin_karp_search(page2_string, pattern_no_page2))

