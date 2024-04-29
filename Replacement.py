page_frame=[]
page_ref=[]
time = []
index = 0
hit_fifo = 0
hit_lru = 0
hit_optimal = 0

num_frame = int(input("Enter the Size of Page Frame: "))
num_ref = int(input("Enter the Size of Page Reference: "))

# Initialize time for LRU algorithm
for _ in range(num_frame):
    time.append(0)

print(f"Enter {num_ref} values of Page references:")
# Use split to separate the digits and convert them to integers
page_ref = list(map(int, input().split()))

# FIFO Algorithm
print("\nFIFO Algorithm:")
for _ in range(num_frame):
    page_frame.append(-1)

for i in page_ref:
    if i not in page_frame:
        if -1 in page_frame:  # If there is an empty slot
            index = page_frame.index(-1)
            page_frame[index] = i
        else:
            page_frame.pop(0)
            page_frame.append(i)
    else:
        hit_fifo += 1
    for j in page_frame:
        if j == -1:
            print('-', end="\t")
        else:
            print(j, end="\t")
    print()

print("\nFIFO Hit Ratio: ", hit_fifo/num_ref)
print("FIFO Miss Ratio: ", 1-(hit_fifo/num_ref))

# LRU Algorithm
page_frame.clear()  # Clearing the page frame for the LRU algorithm
print("\nLRU Algorithm:")
for _ in range(num_frame):
    page_frame.append(-1)

for i in page_ref:
    if i not in page_frame:
        if -1 in page_frame:  # If there is an empty slot
            index = page_frame.index(-1)
            page_frame[index] = i
        else:
            least_recently_used = min(time)
            index = time.index(least_recently_used)
            page_frame[index] = i
        time[index] = 0
    else:
        hit_lru += 1
        index = page_frame.index(i)
        time[index] = 0
    for j in page_frame:
        if j == -1:
            print('-', end="\t")
        else:
            print(j, end="\t")
    print()
    
    for j in range(num_frame):
        time[j] += 1

print("\nLRU Hit Ratio: ", hit_lru/num_ref)
print("LRU Miss Ratio: ", 1-(hit_lru/num_ref))

# Optimal Algorithm
page_frame.clear()  # Clearing the page frame for the Optimal algorithm
print("\nOptimal Algorithm:")
for _ in range(num_frame):
    page_frame.append(-1)

for i in range(len(page_ref)):
    if page_ref[i] not in page_frame:
        if -1 in page_frame:  # If there is an empty slot
            index = page_frame.index(-1)
            page_frame[index] = page_ref[i]
        else:
            page_frame_full = True
            farthest = i + 1
            replace_index = None
            for j in range(num_frame):
                if page_frame[j] not in page_ref[i:]:
                    replace_index = j
                    break
                else:
                    temp = page_ref[i:].index(page_frame[j])
                    if temp > farthest:
                        farthest = temp
                        replace_index = j
            if replace_index is not None:  # Ensure replace_index is assigned
                page_frame[replace_index] = page_ref[i]
    else:
        hit_optimal += 1
    for j in page_frame:
        if j == -1:
            print('-', end="\t")
        else:
            print(j, end="\t")
    print()

print("\nOptimal Hit Ratio: ", hit_optimal/num_ref)
print("Optimal Miss Ratio: ", 1-(hit_optimal/num_ref))
