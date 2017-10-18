
---
#  How the Linux Scheduler Works
## by Josh Aas
---

 - loc 8 - Normally the scheduler runs in its own thread, which is woken up by a timer interrupt

 - loc 8 - Schedulers tend to give I/O-bound threads priority access to CPUs

 - loc 9 - Because I/O operations usually take a long time it is good to get them started as early as possible

 - loc 9 - Kicking oﬀ the data request as quickly as possible frees up the CPU to work on something else

 - loc 11 - It is important for tasks to be treated with a certain degree of fairness, including the stipulation that no thread ever starves. Starvation happens when a thread is not allowed to run for an unacceptably long period of time due to the prioritization of other threads over it. Starvation must not be allowed to happen, though certain threads should be allowed to have a considerably higher priority level than others based on user-deﬁned values and/or heuristic indicators. Somehow, threads that are approaching the starvation threshold (which is

 - loc 12 - generally deﬁned by a scheduler’s implementors) must get a signiﬁcant priority boost or one-time immediate preemption before they starve. Fairness does not mean that every thread should have the same degree of access to CPU time with the same priority, but it means that no thread should ever starve or be able to trick the scheduler into giving it a higher priority or more CPU time than it ought to have

 - loc 13 - The Linux scheduler supports soft real-time (RT) scheduling. This means that it can eﬀectively schedule tasks that have strict timing requirements

 - loc 13 - RT scheduling modes include a ﬁrst-in-ﬁrst-out (FIFO) mode which allows RT tasks to run to completion on a ﬁrst-come-ﬁrstserve basis, and a round-robin scheduling mode that schedules RT tasks in a round-robin fashion while essentially ignoring non-RT tasks on the system

 - loc 15 - The fact that the Linux 2.4.x scheduling algorithm contained O(n) algorithms was perhaps its greatest ﬂaw, and subsequently the new scheduler’s use of only O(1) algorithms was its most welcome improvement

 - loc 15 - one runqueue is created and maintained for each CPU in a system

 - loc 16 - Only one task can modify a particular runqueue at any given time

 - loc 16 - tasks on a CPU begin in one priority array, the active one, and as they run out of their timeslices they are moved to the expired priority array. During the move, a new timeslice is calculated. When there are no more runnable tasks in the active priority arrays, it is simply swapped with the expired priority array

 - loc 18 - Obtaining multiple runqueue locks must be done by order of ascending runqueue address in order to avoid deadlocks

 - loc 18 - The Linux 2.6.8.1 scheduler always schedules the highest priority task on a system, and if multiple tasks exist at the same priority level, they are scheduled roundrobin with each other

 - loc 18 - Priority arrays make ﬁnding the highest priority task in a system a constant-time operation, and also makes round-robin behavior within priority levels possible in constant-time. Furthermore, using two priority arrays in unison (the active and expired priority arrays) makes transitions between timeslice epochs a constant-time operation. An epoch is the time between when all runnable tasks begin with a fresh timeslice and when all runnable tasks have used up their timeslices

 - loc 19 - struct list_head queue[MAX_PRIO] An array of linked lists. There is one list in the array for each priority level

 - loc 19 - The highest priority task in a priority array is always scheduled ﬁrst, and tasks within a certain priority level are scheduled round-robin

 - loc 19 - A bitmap of size MAX_PRIO + 1 (actually it might be a bit larger since it must be implemented in word-sized chunks) has bits set for each priority level that contains active tasks. In order to ﬁnd the highest priority task in a priority array, one only has to ﬁnd the ﬁrst bit set in the bitmap

 - loc 19 - after running, tasks are put at the bottom of their priority level’s list

 - loc 19 - When a task runs out of timeslice, it is removed from the active priority array and put into the expired priority array. During this move, a new timeslice is calculated. When there are no more runnable tasks in the active priority array, the pointers to the active and expired priority arrays are simply swapped

 - loc 20 - All tasks have a static priority, often called a nice value. On Linux, nice values range from -20 to 19, with higher values being lower priority

 - loc 20 - The Linux 2.6.8.1 scheduler rewards I/O-bound tasks and punishes CPU-bound tasks by adding or subtracting from a task’s static priority

 - loc 20 - Tasks that are I/O-bound tend to sleep quite a bit as they block on I/O, whereas CPU-bound task rarely sleep as they rarely block on I/O. Quite often, tasks are in the middle, and are not entirely CPU-bound or I/O-bound so the heuristic produces some sort of scale instead of a simple binary label (I/O-bound or CPU-bound

 - loc 20 - when a task is woken up from sleep, its total sleep time is added to its sleep_avg variable

 - loc 20 - In the Linux 2.6.8.1 scheduler, the maximum priority bonus is 5 and the maximum priority penalty is 5. Since the scheduler uses bonuses and penalties, adjustments to a task’s static priority are respected

 - loc 21 - When a task gives up the CPU, voluntarily or involuntarily, the time the current task spent running is subtracted from its sleep_avg. The higher a task’s sleep_avg is, the higher its dynamic priority will be

 - loc 22 - The higher the task’s static priority (the lower the task’s static_prio value) the larger the timeslice it gets

 - loc 22 - Without this check, highly interactive tasks could keep spawning new tasks in order to hog the CPU. With this check, sleep_avg and subsequently priority are decreased

 - loc 22 - scheduler_tick() will reinsert interactive tasks into the active priority array with their new timeslice so long as nothing is starving in the expired priority array

 - loc 23 - Essentially, tasks get an interactive credit when they sleep for a long time, and lose an interactive credit when they run for a long time

 - loc 23 - High interactivity credit tasks get less run time subtracted from their sleep avg in order to prevent them from losing interactive status too quickly. If a task got high credit, it must have slept quite a bit at least 100 times recently and thus it should not lose interactive status just because it used up a lot of CPU time once

 - loc 23 - uninterruptible. A task in the interruptible state can wake up prematurely to 23

 - loc 23 - When a task goes to sleep, it is usually in one of two states - interruptible or uninterruptible

 - loc 24 - the kill command will attempt to do its job by sending a SIGTERM signal to the task. If the task is in the uninterruptible state, it will ignore the signal until the event it was originally waiting for occurs

 - loc 24 - When that event occurs, code controlling that event will tell the waitqueue to wake up all of the tasks in it.

 - loc 27 - Once the busiest group has been identiﬁed, load_balance() attempts to move tasks from the busiest group’s busiest runqueue to the current CPU’s runqueue via move_tasks

 - loc 31 - If another task has not run for longer than STARVATION_LIMIT speciﬁes, then interactive tasks stop running in order for the starving tasks to get CPU time. Decreasing this value hurts interactivity since interactive tasks will more often be forced to give up the CPU for the sake of starving tasks, but fairness will increase

 - loc 31 - Timeslices are computed for all tasks when epochs begin, which means that the scheduler’s algorithm for timeslice calculation runs in O(n) time since it must iterate over every task

 - loc 31 - The Linux 2.4.x scheduling algorithm divides time into “epochs,” which are periods of time during which every task is allowed to use up its timeslice. Timeslices are computed for all tasks when epochs begin, which means that the scheduler’s algorithm for timeslice calculation runs in O(n) time since it must iterate over every task.

 - loc 31 - tasks that do not use up their timeslices due to being I/O-bound get longer a longer timeslice in the next epoch. If a task suddenly becomes CPU-bound and uses up its whole timeslice, it quickly drops back to a base timeslice in the next epoch

 - loc 33 - large timeslices can cause the time between executions of low-priority tasks (or simply unlucky ones if all priorities are equal) to grow quite large. For example - with 100 threads using all of their 210ms timeslices without pause, the lowest priority thread in the group might have to wait more than 20 seconds before it executes (an unlikely situation, but it illustrates the point). This problem does not appear to be mitigated by starvation checks or taking system load into account when calculating timeslices, which might not help anyway

 - loc 33 - The problem is lessened by the Linux 2.6.8 scheduler’s lower average timeslices, but it is not entirely done away with. Essentially the system load just needs to be twice as much to create the same problem

