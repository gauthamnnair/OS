def fifo_algorithm(pages, num_frames):
    print("FIFO Algorithm : ")
    frames = [-1] * num_frames
    page_faults = 0
    hits = 0
    for i, page in enumerate(pages):
        page_found = False

        # Check if page is already in memory
        for j in range(num_frames):
            if frames[j] == page:
                page_found = True
                hits += 1
                break

        # If page is not in memory, replace oldest page with new page
        if not page_found:
            frame_pointer = i % num_frames
            frames[frame_pointer] = page
            page_faults += 1

        # Print current state of frames
        print('\t'.join(str(frame) if frame != -1 else '-' for frame in frames))

    print("\nPage Faults: ", page_faults)
    print("Total Hits : ", hits)

def lru_algorithm(pages, num_frames):
    print("\nLRU Algorithm : ")
    frames = [-1] * num_frames
    page_faults = 0
    hits = 0
    used = [0] * num_frames

    for i, page in enumerate(pages):
        page_found = False

        # Check if page is already in memory
        for j in range(num_frames):
            if frames[j] == page:
                page_found = True
                hits += 1
                used[j] = i
                break

        # If page is not in memory, find least recently used page to replace
        if not page_found:
            # If there is an empty frame, use it
            if -1 in frames:
                frame_to_replace = frames.index(-1)
            else:
                # Otherwise, find least recently used frame to replace
                frame_to_replace = used.index(min(used))
            frames[frame_to_replace] = page
            used[frame_to_replace] = i
            page_faults += 1

        # Print current state of frames
        print('\t'.join(str(frame) if frame != -1 else '-' for frame in frames))
    print("\nPage Faults: ", page_faults)
    print("Total Hits : ", hits)

def optimal_algorithm(pages, num_frames):
    print("\nOptimal Algorithm : ")
    frames = [-1] * num_frames
    page_faults = 0
    hits = 0

    for i, page in enumerate(pages):
        page_found = False

        # Check if page is already in memory
        if page in frames:
            page_found = True
            hits += 1
        else:
            # If there is an empty frame, use it
            if -1 in frames:
                frame_to_replace = frames.index(-1)
            else:
                # Find the page with the longest future distance
                future_distances = [pages[i+1:].index(frames[j]) if frames[j] in pages[i+1:] else len(pages) for j in range(num_frames)]
                frame_to_replace = future_distances.index(max(future_distances))
            frames[frame_to_replace] = page
            page_faults += 1

        # Print current state of frames
        print('\t'.join(str(frame) if frame != -1 else '-' for frame in frames))

    print("\nPage Faults: ", page_faults)
    print("Total Hits : ", hits)

# Take input from user
reference_string = input("Enter the reference string separated by spaces: ").split()
reference_string = [int(page) for page in reference_string]
num_frames = int(input("Enter the number of frames: "))

fifo_algorithm(reference_string, num_frames)
lru_algorithm(reference_string, num_frames)
optimal_algorithm(reference_string, num_frames)

