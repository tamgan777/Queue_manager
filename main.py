import json
from queue import Queue

# ---------- Task ----------
class Task:
    def __init__(self, task_id, execution_time):
        self.id = task_id
        self.execution_time = execution_time
        self.status = "PENDING"
        self.assigned_worker = None

# ---------- Worker ----------
class Worker:
    def __init__(self, worker_id):
        self.id = worker_id
        self.status = "IDLE"
        self.current_load = 0
        self.tasks_completed = 0
        self.total_execution_time = 0

    def assign_task(self, task):
        self.status, task.status = "BUSY", "RUNNING"
        task.assigned_worker = self.id
        print(f"\nWorker {self.id} -> Task {task.id} ({task.execution_time}s)")
        self.current_load += task.execution_time
        self.total_execution_time += task.execution_time
        self.tasks_completed += 1
        task.status, self.status = "COMPLETED", "IDLE"
        print(f"Task {task.id} Completed")

# ---------- Load Balancer ----------
class LoadBalancer:
    @staticmethod
    def select_worker(workers):
        return min(workers, key=lambda w: w.current_load)

# ---------- Input ----------
def positive_int(msg):
    while True:
        try:
            val = int(input(msg))
            if val > 0: return val
            print("Enter a positive number.")
        except ValueError: print("Invalid input.")

def manual_input():
    workers, total_tasks = positive_int("Number of Workers : "), positive_int("Number of Tasks   : ")
    tasks = [{"id": i+1, "execution_time": positive_int(f"Task {i+1} Time : ")} for i in range(total_tasks)]
    return {"workers": workers, "tasks": tasks}

def read_json():
    with open("input.json", "r") as f: return json.load(f)

def get_input():
    print("\nQueue Based Task Distribution Simulator\n1. Manual Input\n2. Read input.json")
    return manual_input() if input("Choice : ") == "1" else read_json()

# ---------- Scheduler ----------
class Scheduler:
    def __init__(self, workers, tasks):
        self.queue, self.workers, self.tasks = Queue(), [Worker(i+1) for i in range(workers)], []
        self.completed_tasks, self.total_execution_time = 0, 0
        for t in tasks:
            task = Task(t["id"], t["execution_time"])
            self.tasks.append(task)
            self.queue.put(task)

    def run(self):
        print("\n========== Simulation Started ==========")
        while not self.queue.empty():
            self.show_queue()
            task, worker = self.queue.get(), LoadBalancer.select_worker(self.workers)
            print(f"\nAssigning Task {task.id} to Worker {worker.id}")
            worker.assign_task(task)
            self.completed_tasks += 1
            self.total_execution_time += task.execution_time
        print("\n========== Simulation Completed ==========")

    def show_queue(self):
        print("\nPending Queue")
        print("Queue Empty" if self.queue.empty() else "\n".join([f"Task {t.id} ({t.execution_time}s)" for t in list(self.queue.queue)]))

    def worker_summary(self):
        print("\nWorker Summary\n" + "-"*40)
        for w in self.workers:
            print(f"Worker {w.id}\nStatus          : {w.status}\nCompleted Tasks : {w.tasks_completed}\nCurrent Load    : {w.current_load}\nExecution Time  : {w.total_execution_time}\n" + "-"*40)

    def task_summary(self):
        print("\nTask Summary\n" + "-"*40)
        for t in self.tasks:
            print(f"Task {t.id}\nExecution Time : {t.execution_time}\nStatus         : {t.status}\nWorker         : {t.assigned_worker}\n" + "-"*40)

    def statistics(self):
        loads = [w.current_load for w in self.workers]
        print("\nProject Statistics\n" + "-"*40)
        print(f"Workers Used        : {len(self.workers)}\nCompleted Tasks     : {self.completed_tasks}\nTotal Time          : {self.total_execution_time}\nAverage Load        : {sum(loads)/len(loads):.2f}\nMaximum Load        : {max(loads)}\nMinimum Load        : {min(loads)}")

    def export_json(self):
        output = {
            "completed_tasks": self.completed_tasks,
            "workers_used": len(self.workers),
            "workers": [{"worker_id": w.id, "status": w.status, "tasks_completed": w.tasks_completed, "current_load": w.current_load, "total_execution_time": w.total_execution_time} for w in self.workers],
            "tasks": [{"task_id": t.id, "execution_time": t.execution_time, "status": t.status, "assigned_worker": t.assigned_worker} for t in self.tasks],
            "statistics": {
                "completed_tasks": self.completed_tasks,
                "total_execution_time": self.total_execution_time,
                "average_worker_load": sum(w.current_load for w in self.workers)/len(self.workers),
                "maximum_worker_load": max(w.current_load for w in self.workers),
                "minimum_worker_load": min(w.current_load for w in self.workers)
            }
        }
        with open("output.json", "w") as f: json.dump(output, f, indent=4)
        print("\noutput.json created successfully.")

# ---------- Main ----------
def main():
    try:
        data = get_input()
        s = Scheduler(data["workers"], data["tasks"])
        s.run(); s.worker_summary(); s.task_summary(); s.statistics(); s.export_json()
    except FileNotFoundError: print("\nError: input.json not found.")
    except ValueError: print("\nError: Invalid input.")
    except KeyboardInterrupt: print("\nProgram Interrupted.")
    except Exception as e: print(f"\nUnexpected Error: {e}")

if __name__ == "__main__":
    main()
