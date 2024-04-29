import threading
import time
import random

# Buffer size
BUFFER_SIZE = 5

# Semaphore to control access to the buffer
mutex = threading.Semaphore(1)

# Semaphores to control the number of empty and full slots in the buffer
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)

# Buffer to store items
buffer = []

# Producer function
def producer(items):
    global buffer
    for item in items:
        empty.acquire()  # Wait if buffer is full
        mutex.acquire()  # Acquire the mutex to access the buffer
        buffer.append(item)  # Produce the item
        print(f"Produced {item}, Buffer: {buffer}")
        mutex.release()  # Release the mutex
        full.release()  # Signal that buffer is not empty
        time.sleep(random.uniform(0.1, 0.5))  # Simulate some processing time

# Consumer function
def consumer(num_items):
    global buffer
    for _ in range(num_items):
        full.acquire()  # Wait if buffer is empty
        mutex.acquire()  # Acquire the mutex to access the buffer
        item = buffer.pop(0)  # Consume the item
        print(f"Consumed {item}, Buffer: {buffer}")
        mutex.release()  # Release the mutex
        empty.release()  # Signal that buffer is not full
        time.sleep(random.uniform(0.1, 0.5))  # Simulate some processing time

# Take user input for the items to produce
num_produce = int(input("Enter the number of items to produce: "))
produce_items = []
print("Enter the items to produce:")
for _ in range(num_produce):
    produce_items.append(input())

# Take user input for the number of items to consume
num_consume = int(input("Enter the number of items to consume: "))

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(produce_items,))
consumer_thread = threading.Thread(target=consumer, args=(num_consume,))

# Start the threads
producer_thread.start()
consumer_thread.start()

# Join the threads to main thread
producer_thread.join()
consumer_thread.join()

