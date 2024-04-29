class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0


def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sort processes based on arrival time
    waiting_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    print("FCFS Scheduling:")
    print("PID\tArrival Time\tBurst Time\tCT\tTAT\tWT")
    for process in processes:
        waiting_time = max(waiting_time, process.arrival_time)  # Wait until the process arrives
        total_waiting_time += waiting_time - process.arrival_time
        process.completion_time = waiting_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        total_turnaround_time += process.turnaround_time
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.turnaround_time}\t\t{waiting_time - process.arrival_time}")
        waiting_time += process.burst_time  # Update WT for next process

    print("Average WT:", total_waiting_time / len(processes))
    print("Average TAT:", total_turnaround_time / len(processes))


def sjf(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))  # Sort processes based on arrival and burst time
    waiting_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    print("\nSJF Scheduling:")
    print("PID\tArrival Time\tBurst Time\tCT\tTAT\tWT")
    for process in processes:
        waiting_time = max(waiting_time, process.arrival_time)  # Wait until the process arrives
        total_waiting_time += waiting_time - process.arrival_time
        process.completion_time = waiting_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        total_turnaround_time += process.turnaround_time
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.turnaround_time}\t\t{waiting_time - process.arrival_time}")
        waiting_time += process.burst_time  # Update WT for next process

    print("Average WT:", total_waiting_time / len(processes))
    print("Average TAT:", total_turnaround_time / len(processes))


if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    for i in range(1, num_processes + 1):
        arrival_time = int(input(f"Enter arrival time for process {i}: "))
        burst_time = int(input(f"Enter burst time for process {i}: "))
        processes.append(Process(i, arrival_time, burst_time))
        
    fcfs(processes)
    sjf(processes)

