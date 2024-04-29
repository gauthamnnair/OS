def firstFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    print("First Fit Allocation:")
    print("Process No.\tProcess Size\tBlock no.\tMemory Wastage")
    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                memory_wastage = blockSize[j]
                print(f"{i + 1}\t\t{processSize[i]}\t\t{j + 1}\t\t{memory_wastage}")
                break
            elif j == m - 1:
                print(f"{i + 1}\t\t{processSize[i]}\t\tNot Allocated\t\t-")

def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    print("\nBest Fit Allocation:")
    print("Process No.\tProcess Size\tBlock no.\tMemory Wastage")
    for i in range(n):
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1 or blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j
        if bestIdx != -1:
            allocation[i] = bestIdx
            blockSize[bestIdx] -= processSize[i]
            memory_wastage = blockSize[bestIdx]
            print(f"{i + 1}\t\t{processSize[i]}\t\t{bestIdx + 1}\t\t{memory_wastage}")
        else:
            print(f"{i + 1}\t\t{processSize[i]}\t\tNot Allocated\t\t-")

def worstFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    print("\nWorst Fit Allocation:")
    print("Process No.\tProcess Size\tBlock no.\tMemory Wastage")
    for i in range(n):
        wstIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if wstIdx == -1 or blockSize[wstIdx] < blockSize[j]:
                    wstIdx = j
        if wstIdx != -1:
            allocation[i] = wstIdx
            blockSize[wstIdx] -= processSize[i]
            memory_wastage = blockSize[wstIdx]
            print(f"{i + 1}\t\t{processSize[i]}\t\t{wstIdx + 1}\t\t{memory_wastage}")
        else:
            print(f"{i + 1}\t\t{processSize[i]}\t\tNot Allocated\t\t-")

# Driver code
if __name__ == '__main__':
    process_num = int(input("Enter the Number of Process: "))
    processSize = list(map(int, input("Enter the Memory size of each process: ").split()))
    block_num = int(input("Enter the Number of blocks: "))
    blockSize = list(map(int, input("Enter the Memory size of each block: ").split()))
    firstFit(blockSize[:], block_num, processSize[:], process_num)
    bestFit(blockSize[:], block_num, processSize[:], process_num)
    worstFit(blockSize[:], block_num, processSize[:], process_num)

