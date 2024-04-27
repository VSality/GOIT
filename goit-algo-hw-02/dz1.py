import queue

#Створити чергу заявок
q = queue.Queue()
iter = 1

class Request():
    

def generate_request():
    global q
    #Створити нову заявку
    q.put(iter)
    #Додати заявку до черги

def process_request():
    pass
    #Якщо черга не пуста:
        #Видалити заявку з черги
        #Обробити заявку
    #Інакше:
        #Вивести повідомлення, що черга пуста

def main():

    while True:
        generate_request()
        process_request()
        
        
if __name__ == "__main__":
    main() 
    