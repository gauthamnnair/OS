total_memory = int(input("Enter size of physical memory: "))
frame_size = int(input("Enter the size of frame: "))
frame_occupied = int(input("Enter the number of frames occupied: "))
fmax = total_memory // frame_size

if frame_occupied > fmax:
    print("Memory thrash")
else:
    page_table = []
    print(f"Enter the frames used by pages (less than {fmax}):")
    for i in range(frame_occupied):
        page_table.append(int(input()))

    print(f"Virtual memory locations available are 0 to {frame_size * frame_occupied}")

    ans = 'y'
    while ans == 'y':
        vm = int(input("Enter the virtual memory address: "))
        if vm >= frame_size * frame_occupied:
            print("Invalid address!!!")
        else:
            r = vm // frame_size
            pm = page_table[r] * frame_size + vm % frame_size
            print("Physical Address is", pm)
        ans = input("Enter more (y/n)? ").lower()

