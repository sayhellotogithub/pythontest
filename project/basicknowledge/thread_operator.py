import threading
counter = 0
# lock = threading.Lock()
def worker():
    global counter
    for _ in range(10000):
      #   with lock:
         print(counter)
         counter +=1


threads=[]
for _ in range(2):
   t= threading.Thread(target=worker)
   threads.append(t)
   t.start()
for t in threads:
   t.join()

print(f'最終カウンタ：{counter}')

