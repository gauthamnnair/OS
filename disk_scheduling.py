def output(seek_operations, total_distance, seek_sequence):
    print("Total number of seek operations:", seek_operations)
    print("Total distance traveled:", total_distance)
    print("Seek sequence:", seek_sequence)

class DiskScheduler:
    def __init__(self, initial_head_position, request_queue):
        self.initial_head_position = initial_head_position
        self.request_queue = request_queue

    def fcfs(self):
        seek_sequence = [self.initial_head_position] + self.request_queue
        total_movement = abs(self.initial_head_position - self.request_queue[0])
        for i in range(1, len(self.request_queue)):
            total_movement += abs(self.request_queue[i] - self.request_queue[i-1])
        output(len(seek_sequence), total_movement, seek_sequence)

    def sstf(self):
        request_queue = self.request_queue.copy()
        current_position = self.initial_head_position
        seek_sequence = [current_position]
        total_movement = 0

        while request_queue:
            next_request = min(request_queue, key=lambda x: abs(x - current_position))
            seek_sequence.append(next_request)
            total_movement += abs(next_request - current_position)
            current_position = next_request
            request_queue.remove(next_request)

        output(len(seek_sequence), total_movement, seek_sequence)

    def scan(self, direction):
        request_queue = sorted(self.request_queue)
        left_requests = [req for req in request_queue if req < self.initial_head_position]
        right_requests = [req for req in request_queue if req >= self.initial_head_position]
        total_movement = 0
        seek_sequence = []

        if direction == "left":
            scan_sequence = left_requests[::-1] + [0] + right_requests
        else:
            scan_sequence = right_requests + [200] + left_requests[::-1]

        seek_sequence.append(self.initial_head_position)
        previous = initial_head_position
        for request in scan_sequence:
            seek_sequence.append(request)
            total_movement += abs(request - previous)
            previous = request

        output(len(seek_sequence), total_movement, seek_sequence)

    def c_scan(self, direction):
        request_queue = sorted(self.request_queue)
        total_movement = 0
        seek_sequence = []

        left_requests = [req for req in request_queue if req < self.initial_head_position]
        right_requests = [req for req in request_queue if req >= self.initial_head_position]

        if direction == "left":
            c_scan_sequence = left_requests[::-1] + [0] + [200] + right_requests[::-1]
        else: # Reverse for proper order
            c_scan_sequence = right_requests + [200] + [0] + left_requests[::-1]

        seek_sequence.append(self.initial_head_position)
        previous = initial_head_position
        for request in c_scan_sequence:
            seek_sequence.append(request)
            total_movement += abs(request - previous)
            previous = request

        output(len(seek_sequence), total_movement, seek_sequence)




    def look(self, direction):
        request_queue = sorted(self.request_queue)
        left_requests = [req for req in request_queue if req < self.initial_head_position]
        right_requests = [req for req in request_queue if req >= self.initial_head_position]
        total_movement = 0
        seek_sequence = []

        if direction == "left":
            look_sequence = left_requests[::-1] + right_requests
        else:
            look_sequence = right_requests + left_requests[::-1]

        seek_sequence.append(self.initial_head_position)
        previous = initial_head_position
        for request in look_sequence:
            seek_sequence.append(request)
            total_movement += abs(request - previous)
            previous = request

        output(len(seek_sequence), total_movement, seek_sequence)

    def c_look(self, direction):
        request_queue = sorted(self.request_queue)
        left_requests = [req for req in request_queue if req < self.initial_head_position]
        right_requests = [req for req in request_queue if req >= self.initial_head_position]
        total_movement = 0
        seek_sequence = []

        if direction == "left":
            c_look_sequence = left_requests[::-1] + right_requests[::-1]
        else:
            c_look_sequence = right_requests + left_requests

        seek_sequence.append(self.initial_head_position)
        previous = initial_head_position
        for request in c_look_sequence:
            seek_sequence.append(request)
            total_movement += abs(request - previous)
            previous = request

        output(len(seek_sequence), total_movement, seek_sequence)



# Example usage
initial_head_position = int(input("Enter initial head position: "))
request_queue = list(map(int, input("Enter request queue: ").split(' ')))
direction = input("Enter direction (left/right): ").lower()

scheduler = DiskScheduler(initial_head_position, request_queue)

print("\nFCFS:")
scheduler.fcfs()

print("\nSSTF:")
scheduler.sstf()

print("\nSCAN:")
scheduler.scan(direction)

print("\nC-SCAN:")
scheduler.c_scan(direction)

print("\nLOOK:")
scheduler.look(direction)

print("\nC-LOOK:")
scheduler.c_look(direction)

