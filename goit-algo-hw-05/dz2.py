def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    last = 0
    iter = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        iter += 1
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
            last = low
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            
        # інакше x присутній на позиції і повертаємо його
        else:
            return [iter, arr[mid]]

    if last >= len(arr):
        return [iter, arr[len(arr)-1]]
    
    # якщо елемент не знайдений
    return [iter, arr[last]]

arr = [2.2, 3.1, 4.3, 5.2, 6.2, 7, 8.3, 9.1]
x = 1

result = binary_search(arr, x)
print(result)

