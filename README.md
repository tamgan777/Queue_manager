# Queue-Based Task Distribution Simulator

## Overview

The Queue-Based Task Distribution Simulator is a Python application that demonstrates how a scheduler distributes tasks among multiple workers using a **FIFO (First-In, First-Out) queue** and a **Least Loaded Load Balancing Algorithm**.

The project simulates a simplified distributed task scheduling system similar to those used in cloud computing, job scheduling systems, print servers, and backend processing applications.

Although this is a simulation, it introduces important software engineering concepts such as scheduling, load balancing, queue management, worker monitoring, and task lifecycle management.

---

# Objectives

* Simulate task scheduling using a queue.
* Assign tasks efficiently to workers.
* Balance workload among workers.
* Track worker and task status.
* Generate scheduling statistics.
* Export results to a JSON file.

---

# Features

* Dynamic worker creation.
* Dynamic task creation.
* FIFO Queue implementation.
* Least Loaded load balancing.
* Worker status tracking.
* Task status tracking.
* Queue visualization.
* Worker performance summary.
* Task summary.
* Statistics generation.
* JSON output.

---

# Technologies Used

* Python 3
* queue.Queue
* JSON
* Object-Oriented Programming (OOP)

---

# Concepts Used

## Queue (FIFO)

The project uses Python's `queue.Queue()`.

FIFO means:

**First In → First Out**

The first task added to the queue is always processed first.

Example:

Queue

Task1

Task2

Task3

↓

Execution Order

Task1

Task2

Task3

---

## Task

Every task contains:

* Task ID
* Execution Time
* Status
* Assigned Worker

Task Life Cycle

PENDING

↓

RUNNING

↓

COMPLETED

---

## Worker

Every worker contains:

* Worker ID
* Status
* Current Load
* Completed Tasks
* Total Execution Time

Worker States

IDLE

↓

BUSY

↓

IDLE

---

## Scheduler

The Scheduler is the core of the project.

Responsibilities:

* Read tasks from queue
* Select worker
* Assign task
* Update status
* Collect statistics

---

## Load Balancing

The project uses the **Least Loaded Algorithm**.

The scheduler always assigns a task to the worker with the smallest current workload.

Example

Worker 1 → Load = 15

Worker 2 → Load = 6

Worker 3 → Load = 9

New Task

↓

Assigned to Worker 2

because Worker 2 has the minimum load.

---

# Project Workflow

1. User enters workers and tasks.
2. Task objects are created.
3. Worker objects are created.
4. Tasks are inserted into the queue.
5. Scheduler starts.
6. Least Loaded worker is selected.
7. Task is assigned.
8. Worker status changes to BUSY.
9. Task status changes to RUNNING.
10. Task completes.
11. Worker becomes IDLE.
12. Statistics are updated.
13. Queue becomes empty.
14. Results are exported to output.json.

---

# Architecture

```
User Input
     │
     ▼
Create Tasks
     │
     ▼
Queue (FIFO)
     │
     ▼
Scheduler
     │
     ▼
Load Balancer
     │
     ▼
Least Loaded Worker
     │
     ▼
Execute Task
     │
     ▼
Update Statistics
     │
     ▼
Generate output.json
```

---

# Algorithms Used

## FIFO Queue

Time Complexity

* Insert : O(1)
* Remove : O(1)

---

## Least Loaded Scheduling

The scheduler checks every worker and selects the worker with the minimum load.

Time Complexity

O(w)

where

w = Number of Workers

---

# Overall Complexity

Adding Tasks

O(n)

Scheduling

O(n × w)

Statistics

O(n + w)

Space Complexity

O(n + w)

where

n = Number of Tasks

w = Number of Workers

---

# Sample Input

Workers

3

Tasks

Task 1 → 4

Task 2 → 2

Task 3 → 6

Task 4 → 3

Task 5 → 5

---

# Sample Execution

Queue

Task1

Task2

Task3

Task4

Task5

↓

Worker 1 ← Task1

Worker 2 ← Task2

Worker 3 ← Task3

↓

Task2 finishes

↓

Worker2 receives Task4

↓

Task1 finishes

↓

Worker1 receives Task5

↓

Queue Empty

↓

Simulation Ends

---

# Output

The program generates an `output.json` file containing:

* Completed Tasks
* Workers Used
* Worker Statistics
* Task Statistics
* Total Execution Time
* Average Worker Load
* Maximum Worker Load
* Minimum Worker Load

---

# Real-World Applications

* Cloud Computing
* Distributed Systems
* Operating System Scheduling
* CPU Job Scheduling
* Web Servers
* Print Servers
* Email Processing Systems
* Task Queues
* Background Job Processing
* Microservices

---

# Advantages

* Easy to understand.
* Demonstrates queue operations.
* Demonstrates scheduling.
* Demonstrates load balancing.
* Uses Object-Oriented Programming.
* Scalable for additional scheduling algorithms.

---

# Limitations

* Tasks complete instantly (no real execution delay).
* Uses a simulated environment.
* Does not implement multithreading.
* Uses only the Least Loaded scheduling algorithm.
* Does not consider task priority.

---

# Future Enhancements

* Add multithreading.
* Add task priorities.
* Implement Round Robin scheduling.
* Use a min-heap for O(log w) worker selection.
* Add execution delay simulation.
* Develop a graphical user interface.
* Store task history in a database.

---

# Conclusion

This project demonstrates the fundamental concepts of queue-based task scheduling and load balancing. It shows how tasks can be distributed efficiently among multiple workers while maintaining a balanced workload. Although simplified, the project provides a strong foundation for understanding distributed scheduling systems and can be extended into more advanced implementations involving concurrency, networking, or cloud-based execution.
