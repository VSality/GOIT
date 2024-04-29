import queue

#Створити чергу заявок
q = queue.Queue()
iter = 1

class Request:
    def __init__(self, id:int):
        self.id = id
        
    def work(self):
        print(f"Оброблена заявка {self.id}")
    

def generate_request():
    global q
    global iter
    for _ in range(0, 20):
        req = Request(iter)
        print(f"Створена заявка {iter}")
        q.put(req)
        print(f"Додана до черги завка {iter}")
        iter += 1

def process_request():
    global q
    while not q.full():
        req = q.get()
        req.work()
    print("Queue is empty")

def main():
    generate_request()
    process_request()
        
        
if __name__ == "__main__":
    main() 
    