class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    # Step 1: Sort jobs by descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = max(job.deadline for job in jobs)
    schedule = [None] * n  # Time slots

    total_profit = 0

    for job in jobs:
        # Find a free slot from job.deadline - 1 to 0
        for i in range(min(n, job.deadline) - 1, -1, -1):
            if schedule[i] is None:
                schedule[i] = job
                total_profit += job.profit
                break

    print("Scheduled Jobs:")
    for slot in schedule:
        if slot:
            print(f"Job ID: {slot.job_id}, Profit: {slot.profit}")

    print("Total Profit:", total_profit)

# Example usage
if __name__ == "__main__":
    jobs = [
        Job('J1', 2, 100),
        Job('J2', 1, 19),
        Job('J3', 2, 27),
        Job('J4', 1, 25),
        Job('J5', 3, 15)
    ]

    job_scheduling(jobs)
