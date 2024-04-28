import queue

#Створити чергу заявок
q = queue.Queue()
iter = 1

class Request:
    def __init__(self, id:int):
        self.id = id
        
    def work(self):
        pass
    

def generate_request():
    global q
    global iter
    req = Request(iter)
    q.put(req)
    iter += 1

def process_request():
    global q
    if not q.full():
        req = q.get()
        req.work()
    else:
        print("Queue is empty")

def main():

    while True:
        generate_request()
        process_request()
        
        
if __name__ == "__main__":
    main() 
    