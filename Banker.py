n = int(input("Enter the number of processes: "))  # Number of processes
m = int(input("Enter the number of resources: "))  # Number of resources

# Allocation Matrix
alloc = []
print("Enter the Allocation Matrix:")
for _ in range(n):
    print(f"Process {_+1} : ")    
    row = list(map(int, input().split()))
    alloc.append(row)

# MAX Matrix
max = []
print("Enter the MAX Matrix:")
for _ in range(n):
    row = list(map(int, input().split()))
    max.append(row)

# Available Resources
avail = list(map(int, input("Enter the Available Resources: ").split()))

f = [0] * n
ans = [0] * n
ind = 0

need = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        need[i][j] = max[i][j] - alloc[i][j]

for k in range(n):
    for i in range(n):
        if f[i] == 0:
            flag = 0
            for j in range(m):
                if need[i][j] > avail[j]:
                    flag = 1
                    break
            if flag == 0:
                ans[ind] = i
                ind += 1
                for y in range(m):
                    avail[y] += alloc[i][y]
                f[i] = 1

flag = 1
for i in range(n):
    if f[i] == 0:
        flag = 0
        print("The following system is not safe")
        break

if flag == 1:
    print("Following is the SAFE Sequence")
    for i in range(n - 1):
        print(" P%d ->" % ans[i], end="")
    print(" P%d" % ans[n - 1])

