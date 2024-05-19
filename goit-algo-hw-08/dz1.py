
import heapq

def heap_sort(arr):
    # Створюємо мінімальну купу з усіх елементів ітерабельного об'єкта.
    h = []
    for value in arr:
        heapq.heappush(h, value)
    #print('heap', h)
    return h

    # Витягуємо елементи впорядковано, формуючи відсортований масив.
    l = []
    for _ in range(len(h)):
      root_e = heapq.heappop(h)
      print(root_e, '<--', h)
      l.append(root_e)
    return l

# Масив із дротами різної довжини
arr = [12, 11, 13, 5, 6, 7]
print('heap', arr)
heapq.heapify(arr)

l = []
while len(arr) > 1:
    print('heap', arr)
    one = heapq.heappop(arr)
    print('one', one)
    heapq.heapify(arr)
    two = heapq.heappop(arr)
    print('two', two)
    print('connect ', one+two)
    l.append(one+two)
    heapq.heapify(arr)
    heapq.heappush(arr, one+two)
    heapq.heapify(arr)
    print('heap marge', arr)
    print('-------------')

s = ""    
for i in l:
    s += f'{i} -> '
print(s)