import threading
import time

def worker(num):
    print(f"Threat {num}: Starting")
    time.sleep(2)
    print(f"Threat {num}: Finishing")
    
threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads completed.")