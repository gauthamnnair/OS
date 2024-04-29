class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=None):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0


def srtf(processes):
    current_time = 0
    remaining_processes = processes[:]
    completion_time = [0] * len(processes)
    print("\nSRTF Scheduling:")
    print("PID\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    while remaining_processes:
        remaining_processes.sort(key=lambda x: x.remaining_time)
        shortest_process = remaining_processes[0]
        if shortest_process.arrival_time > current_time:
            current_time = shortest_process.arrival_time
        current_time += 1
        shortest_process.remaining_time -= 1
        if shortest_process.remaining_time == 0:
            completion_time[shortest_process.pid - 1] = current_time
            remaining_processes.remove(shortest_process)
            shortest_process.completion_time = current_time
            shortest_process.turnaround_time = shortest_process.completion_time - shortest_process.arrival_time
            shortest_process.waiting_time = shortest_process.turnaround_time - shortest_process.burst_time
            print(f"{shortest_process.pid}\t{shortest_process.arrival_time}\t\t{shortest_process.burst_time}\t\t{shortest_process.completion_time}\t\t{shortest_process.waiting_time}\t\t{shortest_process.turnaround_time}")


def priority_scheduling(processes):
    current_time = 0
    remaining_processes = processes[:]
    completion_time = [0] * len(processes)
    print("\nPriority Scheduling:")
    print("PID\tArrival Time\tBurst Time\tPriority\tCompletion Time\tWaiting Time\tTurnaround Time")
    while remaining_processes:
        remaining_processes.sort(key=lambda x: (x.priority, x.arrival_time))
        current_process = remaining_processes[0]
        if current_process.arrival_time > current_time:
            current_time = current_process.arrival_time
        current_time += current_process.burst_time
        completion_time[current_process.pid - 1] = current_time
        remaining_processes.remove(current_process)
        current_process.completion_time = current_time
        current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
        current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
        print(f"{current_process.pid}\t{current_process.arrival_time}\t\t{current_process.burst_time}\t\t{current_process.priority}\t\t{current_process.completion_time}\t\t{current_process.waiting_time}\t\t{current_process.turnaround_time}")


def round_robin(processes, quantum):
    print("\nRound Robin Scheduling:")
    print("PID\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    remaining_processes = processes[:]
    current_time = 0
    while remaining_processes:
        executed = False  # Flag to check if any process was executed in this iteration
        for process in remaining_processes:
            if process.arrival_time <= current_time and process.remaining_time > 0:
                executed = True
                if process.remaining_time <= quantum:
                    current_time += process.remaining_time
                    process.completion_time = current_time
                    process.remaining_time = 0
                else:
                    current_time += quantum
                    process.remaining_time -= quantum
            elif process.remaining_time == 0:
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
                remaining_processes.remove(process)
                break
        
        if not executed:
            current_time += 1  # Increment time if no process is executed

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))

    processes_srtf = []
    processes_priority = []
    processes_rr = []

    for i in range(1, num_processes + 1):
        arrival_time = int(input(f"Enter arrival time for process {i}: "))
        burst_time = int(input(f"Enter burst time for process {i}: "))
        priority = int(input(f"Enter priority for process {i}: "))

        processes_srtf.append(Process(i, arrival_time, burst_time))
        processes_priority.append(Process(i, arrival_time, burst_time, priority))
        processes_rr.append(Process(i, arrival_time, burst_time))

    quantum_rr = int(input("Enter the time quantum for Round Robin: "))

    srtf(processes_srtf)
    priority_scheduling(processes_priority)
    round_robin(processes_rr, quantum_rr)

