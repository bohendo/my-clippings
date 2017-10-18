
---
#  Xinu
## by Douglas Comer
---

 - loc 9 - In source code, a system call appears to be a conventional function invocation. At runtime, however, a system call and a conventional function call differ. Instead of transferring control to another function, a system call transfers control to the operating system, which performs the requested service for the application. Taken as a set, system calls establish a well-defined boundary between applications and the underlying operating system that is known as an Application Program Interface (API

 - loc 16 - A synchronous event loop uses a single, large iteration to handle coordination. During a given iteration of the loop, the code checks each possible activity and invokes the appropriate handler

 - loc 16 - An asynchronous paradigm is used in systems where the hardware can be configured to invoke a handler for each event. For example, the code to adjust volume might be placed in memory at location 100, and the hardware is configured so that when the volume button is pressed, control transfers to location 100

 - loc 17 - The third paradigm used to organize multiple activities is the most significant: software is organized as a set of programs that each operate concurrently. The model is sometimes called run-to-completion because each computation appears to run until it chooses to stop

 - loc 18 - . A timesharing system gives equal priority to all computations, and permits computations to start or terminate at any time. Because they allow computations to be created dynamically, timesharing systems are popular for computers that human users operate

 - loc 18 - A timesharing system gives equal priority to all computations, and permits computations to start or terminate at any time

 - loc 18 - Because it is designed to meet performance constraints, a real-time system does not treat all computations equally. Instead, a real-time system assigns priorities to computations, and schedules the processor carefully to ensure that each computation meets its required schedule

 - loc 18 - The terms process and job often connote a single computation that is self-contained and isolated from other computations

 - loc 19 - . The term task refers to a process that is declared statically. That is, a programming language allows a programmer to declare a task similar to the way one declares a function. The term thread refers to a type of concurrent process that shares an address space with other threads

 - loc 19 - The term task refers to a process that is declared statically. That is, a programming language allows a programmer to declare a task similar to the way one declares a function. The term thread refers to a type of concurrent process that shares an address space with other threads.

 - loc 21 - A normal function call does not return until the called function completes. Process creation functions create and resume return to the caller immediately after starting a new process, which allows execution of both the existing process and the new process to proceed concurrently.

 - loc 23 - Storage for local variables, function arguments, and a function call stack is associated with the process executing a function, not with the code for the function

 - loc 26 - In a concurrent programming system, no process should use the processor while waiting for another process. A process that executes instructions while waiting for another is said to engage in busy waiting. To understand our prohibition on busy waiting, think of the implementation. If a process uses the processor while waiting, the processor cannot be executing other processes. At best, the computation will be delayed unnecessarily, and at worst, the waiting process will use all the available processor cycles in a single-core system, and will wind up waiting forever

 - loc 26 - A semaphore consists of an integer value that is initialized when the semaphore is created and a set of zero or more processes that are waiting on the semaphore. The system call wait decrements a semaphore and adds the calling process to the set of waiting processes if the result is negative. The system call signal performs the opposite action by incrementing the semaphore and allowing one of the waiting process to continue, if any are waiting. To synchronize, a producer and consumer need two semaphores: one on which the consumer waits and one on which the producer waits

 - loc 32 - Although it is not important to understand the exact details of how polled I/O operates, it is essential to use polled I/O when debugging: Whenever they modify or extend the operating system, programmers should use kprintf to display messages rather than printf

 - loc 38 - Physically, the platforms we are using each consist of a single, self-contained circuit board that uses a separate power cube. Most of the major components are contained in a single VLSI chip that is known as a System on Chip (SoC)

 - loc 40 - That is, instructions can access the low-order 16 bits or the high-order 16 bits of a register without changing the other part. In fact, some instructions allow a programmer to reference individual bytes of a register

 - loc 40 - Name Use  EAX Accumulator  EBX Base  ECX Count  EDX Data  ESI Source Index  EDI Destination Index  EBP Base Pointer  ESP Stack Pointer  Figure 3.2 The general-purpose registers in the Galileo board (Intel) and the meaning of each

 - loc 41 -  R0 – R3 a1 – a4 Argument registers  R4 – R11 v1 – v8 Variables and temporaries  R9 sb Static base register  R12 ip Intra procedure call scratch register  R13 sp Stack pointer  R14 lr Link register used for return address  R15 pc Program counter

 - loc 41 -  R0 – R3 a1 – a4 Argument registers  R4 – R11 v1 – v8 Variables and temporaries  R9 sb Static base register  R12 ip Intra procedure call scratch register  R13 sp Stack pointer  R14 lr Link register used for return address  R15 pc Program counter  Figure 3.3 The general-purpose registers and the program counter in the BeagleBone Black (ARM) and the meaning of each

 - loc 41 - We use the term bus to refer to a mechanism that provides the primary path between the processor and other components, namely the memory, I/O devices, and other interface controllers. Bus hardware uses a fetch-store paradigm in which the only operations are fetch, to move data from a component across the bus to the processor, and store, to move data from the processor across the bus to a component

 - loc 42 - Higher-speed I/O devices (e.g., an Ethernet device) offer Direct Memory Access (DMA), which means the device contains hardware that can use the bus to communicate directly with memory

 - loc 42 - Each of the platforms uses a 32-bit bus address space, with addresses ranging from 0x00000000 through 0xFFFFFFFF. Some of the addresses in the bus address space correspond to memory, some to FlashROM, and others to I/O devices

 - loc 43 - Referencing an unassigned bus address, such as an address beyond the physical memory, will cause the hardware to create an exception

 - loc 43 - Static address assignment. Often used by small, embedded systems, static means that all details of the hardware configuration are chosen when the hardware is designed

 - loc 43 - Static configuration has the advantage of increased runtime efficiency, but the disadvantages of less generality and susceptibility to human error.

 - loc 43 - Dynamic address assignment. Dynamic assignment means that when a system boots, an operating system, with the support of the bus hardware and platform firmware, must discover devices and memories attached to the bus

 - loc 43 - Static configuration has the advantage of increased runtime efficiency

 - loc 44 - The steps taken during a function call and return are known as calling conventions. The term convention arises because the hardware does not dictate all details. Instead, the hardware design places some constraints on possible approaches, and leaves final choices to a compiler writer

 - loc 44 - When a function is called, the caller supplies a set of actual arguments that correspond to formal parameters

 - loc 44 - A statically scoped language, such as C, uses a runtime stack to store the state associated with a function call. The compiler allocates enough space on the stack to hold an activation record for the called function. The allocated space is known as a stack frame

 - loc 48 - The operating system creates an array of pointers in memory known as an interrupt vector, where the i th entry in the interrupt vector array points to the code that handles interrupts for the device with vector number i.

 - loc 48 - We think of an interrupt as occurring between two instructions. Thus, one instruction has completed and the next instruction has not begun. However, an exception occurs during an instruction. Thus, when the processor returns from the exception, the program counter has not advanced, and the instruction can be restarted. Restarting is especially important for page fault exceptions

 - loc 50 - The alternative to interrupt-driven I/O is known as polled I/O. When using polled I/O, the processor starts an I/O operation, but does not enable interrupts.Instead, the processor enters a loop that repeatedly checks a device status register to determine whether the operation has completed

 - loc 59 - A process appears on at most one list at any time. To omit the process ID, use an array implementation and use the i th element of the array for process ID i.

 - loc 60 - a relative pointer (i.e. , an array index

 - loc 62 - The functions isempty and nonempty are predicates (i.e., Boolean functions) that test whether a list is empty or not empty, given the index of its head as an argument

 - loc 63 - the implementation has a useful property: a list always has a head and tail, even if the list is empty. Thus, the functions described above can be applied to an empty list without causing a runtime error

 - loc 70 - the general paradigm can be stated as follows: first, design the data structures needed when the system is running, and then figure out how to initialize the data structures. Partitioning the “steady state” aspect of the system from the “transient state” helps focus the designer’s attention on the most important aspect, and avoids the temptation of sacrificing good design for easy initialization

 - loc 70 - head. In the code, newqueue allocates a pair of adjacent positions in the queuetab array to use as head and tail nodes, and initializes the list to empty by pointing the successor of the head to the tail and the predecessor of the tail to the head. Newqueue assigns the value EMPTY to unused pointers (i.e., the successor of the tail and the predecessor of the head). When it initializes a list, newqueue also sets the key fields in the head and the tail to the maximum and minimum integer values, respectively, with the assumption that neither value will be used as a key. Only one allocation function is needed because a list can be used to implement a FIFO queue or a priority queue. Once it finishes with initialization, newqueue returns the index of the list head to its caller. The caller only needs to store one value because the ID of the tail can be computed by adding 1 to the ID of the head

 - loc 70 - The head and tail nodes for a list, X, are allocated from successive locations in the queuetab array, and list X is identified by the index of the head.

 - loc 76 - Because exactly one process is executing at any time, exactly one of the entries in a process table corresponds to an active process — the saved state information in the process table is out of date for the executing process

 - loc 76 - when it executes, a process will change the hardware stack pointer register. Therefore, the contents of the stack pointer register must be saved when a process temporarily stops executing, and must be restored when the process resumes execution. Similarly, copies of other general-purpose registers must be saved and restored

 - loc 77 - prstate The current status of the process (e.g. , whether the process is currently executing or waiting)  prprio The scheduling priority of the process  prstkptr The saved value of the process’s stack pointer when the process is not executing  prstkbase The address of the highest memory location in the memory region used as the process’s stack  prstklen A limit on the maximum size that the process’s stack can grow  prname A name assigned to the process that humans use to identify the process’s purpose

 - loc 80 - At any time, the highest priority eligible process is executing. Among processes with equal priority scheduling is round-robin

 - loc 81 - A scheduler consists of a function that a running process calls to willingly give up the processor

 - loc 82 - In Xinu, the scheduler does not receive an explicit argument that specifies the disposition of the current process. Instead, the system functions use an implicit argument: if the current process should not remain ready, before calling resched, the current process’s prstate field must be set to the desired next state

 - loc 92 - if one were to freeze the system at an arbitrary instant and examine memory, the saved information for each ready process will have the same value for a return address — an address just after the call to ctxsw in resched

 - loc 93 - Because an operating system can only switch the processor from one process to another, at least one process must remain ready to execute at all times. To ensure that at least one process always remains ready to execute, Xinu uses a standard technique: it creates an extra process, called the null process, when the system boots

 - loc 93 - Because an operating system can only switch the processor from one process to another, at least one process must remain ready to execute at all times. To ensure that at least one process always remains ready to execute, Xinu uses a standard technique: it creates an extra process, called the null process, when the system boots. The null process has process ID zero and priority zero (a lower priority than any other process

 - loc 93 - if a function changes the state of processes, the function must call resched to reestablish the invariant. Thus, when it places a high priority process on the ready list, ready calls resched to ensure that the policy is followed

 - loc 94 - many scheduling algorithms have been proposed as alternatives to the round-robin scheduler

 - loc 95 - instead of the operating system being implemented separately from the processes it controls, the operating system code is executed by the processes themselves

 - loc 101 - The present implementation of getpid merely returns the value of currpid, which may seem like unnecessary overhead. However, the advantage of information hiding becomes clear when one considers modifying the operating system. If all processes call getpid, a designer can change the details of where and how the current process ID is stored without changing other code

 - loc 101 - The present implementation of getpid merely returns the value of currpid, which may seem like unnecessary overhead. However, the advantage of information hiding becomes clear when one considers modifying the operating system. If all processes call getpid, a designer can change the details of where and how the current process ID is stored without changing other code. The point is: A good system design follows the principle of information hiding, which states that implementation details are not revealed unless necessary

 - loc 101 - System calls, which define operating system services for applications, protect the system from illegal use and hide information about the underlying implementation

 - loc 102 - complete. In Chapter 13, we will understand the reason: hardware interrupts can result in rescheduling because some interrupt routines call resched. An example system call will help clarify the two aspects. Consider the code for resume that is contained in file resume.c. //** rreessuummee..cc -- rreessuummee **// ##iinncclluuddee <<xxiinnuu..hh>>

 - loc 102 - while changes are in progress, a system call cannot invoke resched directly and cannot invoke any function that calls resched. To prevent involuntarily relinquishing the processor, a system call disables interrupts until a change is complete

 - loc 103 - d Function disable disables interrupts and returns the previous interrupt status to its caller. d Function restore reloads an interrupt status from a previously saved value

 - loc 107 - when suspending the current process, suspend must call resched

 - loc 107 - the currently executing process will stop executing, at least temporarily. Thus, before suspending itself, the current process must prearrange for some other process to resume it (or it will remain suspended forever)

 - loc 107 - the currently executing process will stop executing, at least temporarily. Thus, before suspending itself, the current process must prearrange for some other process to resume it (or it will remain suspended forever). Second, because it will be suspended, the current process must allow another process to execute. Thus, when suspending the current process, suspend must call resched

 - loc 107 - Because the system never searches through suspended processes looking for one to resume, the set of suspended processes need not be kept on a list

 - loc 107 - Because the system never searches through suspended processes looking for one to resume, the set of suspended processes need not be kept on a list. Thus, before suspending a process, a programmer must arrange a way for another process to find the ID of the suspended process so it can be resumed

 - loc 107 - points. First, the currently executing process will stop executing, at least temporarily. Thus, before suspending itself, the current process must prearrange for some other process to resume it (or it will remain suspended forever). Second, because it will be suspended, the current process must allow another process to execute. Thus, when suspending the current process, suspend must call resched

 - loc 107 - To understand one possible motivation for returning the priority at the time of resumption, consider how the priority can be used to convey information. Suppose, for example, that a process needs to suspend until one of two events occurs. A programmer can assign a unique priority value to each event (e.g., priorities 25 and 26), and arrange the calls to resume to set the priority accordingly. The process can then use the priority to determine why it was resumed

 - loc 108 - The actions taken by kill depend on the process state. Before writing the code, a designer needs to consider each possible process state and what it means to terminate a process in that state. We will see, for example, that a process in the ready, sleeping, or waiting states is stored on one of the linked lists in the queue structure, which means kill must dequeue the process. In the next chapter, we will see that if a process is waiting for a semaphore, kill must adjust the semaphore count

 - loc 111 - If a process returns from the initial (top-level) function in which its execution started, the process exits

 - loc 111 - The first argument to create specifies the initial function at which the process should start execution. Create forms a saved environment on the process’s stack as if the specified function had been called. Consequently, we refer to the initial configuration as a pseudo call.

 - loc 125 - From the point of view of the process, the call to wait does not return for a while

 - loc 125 - A process calls wait(s) to decrement the count of semaphore s, and signal(s) to increment the count. If the semaphore count becomes negative when a process executes wait(s), the process is temporarily blocked and placed in the semaphore’s set of blocked processes. From the point of view of the process, the call to wait does not return for a while

 - loc 126 - While a process waits on a semaphore, the process does not execute instructions

 - loc 126 - when signal is called on semaphore s, the semaphore count is incremented. In addition, the signal examines the process list associated with s. If the list is not empty (i.e., at least one process is waiting on the semaphore), signal extracts a process from the list and moves the process back to the ready list. A question arises: if multiple processes are waiting, which one should signal select? Several policies have been used: d Highest scheduling priority d First-come-first-served (longest waiting time) d Random

 - loc 126 - A first-come-first-served policy can lead to a priority inversion in the sense that a high-priority process can be blocked on a semaphore while a low-priority process executes.

 - loc 128 - A semaphore is identified by its index in the global semaphore table, semtab

 - loc 130 - Semaphore invariant: a nonnegative semaphore count means that the queue is empty; a semaphore count of negative N means that the queue contains N waiting processes

 - loc 136 - As with semdelete, semreset must be sure that no processes are already waiting on the semaphore. Thus, after checking its arguments and verifying that the semaphore exists, semreset iterates through the list of waiting processes, removing each from the semaphore queue and making the process ready to execute. As expected, semreset uses resched_cntl to defer rescheduling during the time processes are placed on the ready list.

 - loc 136 - Communication among cores often involves raising an interrupt

 - loc 136 - Some multiprocessor systems supply hardware primitives, known as spin locks, that allow multiple processors to contend for mutually exclusive access

 - loc 137 - If multiple processors are all trying to set spin lock 5 at the same time, the hardware guarantees that only one will be granted access. Thus, test_and_set is analogous to wait

 - loc 137 - It may seem that a spin lock is wasteful because a processor merely blocks (i.e., busy waits) in a loop until access is granted. However, if the probability of two processors contending for access is low, a spin lock mechanism is much more efficient than a system call

 - loc 144 - Although it may lack generality and convenience, a synchronous message passing facility can serve in place of a semaphore mechanism

 - loc 144 - , an asynchronous message passing system either requires a process to poll (i.e., check for a message periodically) or requires a mechanism that allows the operating system to stop a process temporarily, allows the process to handle a message, and then resumes normal execution

 - loc 156 - The text segment, which begins at the lowest usable memory address, contains compiled code for each of the functions that are part of the memory image

 - loc 156 - The data segment, which follows the text segment, contains storage for all global variables that are assigned an initial value. In C, such variables are declared to be global by placing the declarations outside of function declarations

 - loc 156 - The bss segment, which follows the data segment, contains global variables that are not initialized explicitly. Following C conventions, Xinu writes zero into each bss location before execution begins

 - loc 156 - Addresses beyond the bss segment are considered free (i.e., unallocated) when execution begins

 - loc 157 - Stack. Each process needs space for a stack that holds the activation record associated with each function the process invokes. In addition to arguments, an activation record contains storage for local variables.Heap. A process or set of processes may also use heap storage. Items from the heap are allocated dynamically and persist independent of specific function calls

 - loc 158 - Functions getstk and freestk are not intended for general use.Instead, when it forms a new process, create calls getstk to allocate a stack. Getstk obtains a block of memory from the highest address of free space, and returns

 - loc 158 - Functions getstk and freestk are not intended for general use.Instead, when it forms a new process, create calls getstk to allocate a stack

 - loc 158 - kill calls function freestk to release the process’s stack and return the block to the free list.

 - loc 158 - Functions getmem and freemem perform analogous functions for heap storage. Unlike the stack allocation functions, getmem and freemem allocate heap space from the lowest available free memory address

 - loc 159 - Heap space persists independent of the process that allocates the space. Before it exits, a process must explicitly release storage that it has allocated from the heap, or the space will remain allocated

 - loc 159 - the memory manager forms a list, where each item on the list specifies a memory address at which a block starts and a length

 - loc 160 - When a block is released, the memory manager scans the list to see if the released block is adjacent to the end of one of the existing free blocks. If so, the size of the existing block can be increased without adding a new entry to the list.Similarly, if the new block is adjacent to the beginning of an existing block, the entry can be updated.Finally, if a released block exactly fills the gap between two free blocks on the list, the memory manager will combine the two existing entries on the list into one giant block that covers all the memory from the two on the list plus the released block. We use the term coalesce to describe combining entries

 - loc 160 - free memory blocks can be chained together to form a linked list by placing a pointer in each block to the next block

 - loc 160 - global variable memlist contains a pointer to the first free block

 - loc 162 - Note that each block on the free list must hold a complete memblk structure (i.e., eight bytes). The design choice has a consequence: our free list cannot store a free block of less then eight bytes

 - loc 164 - adding nbytes to pointer curr will not produce the desired result because C performs pointer arithmetic. To force C to use integer arithmetic instead of pointer arithmetic, variable curr is cast to an unsigned integer before adding nbytes

 - loc 165 - Because the free list is kept in order by memory address and stack space is allocated from the highest available block, getstk must search the entire list of free blocks. During the search, getstk records the address of any block that satisfies the request, which means that after the search completes, the last recorded address points to the free block with the highest address that satisfies the request

 - loc 177 - The data structure used to hold information about buffer pools consists of a single table. Each entry in the table holds a buffer size, a semaphore ID, and a pointer to a linked list of buffers for the pool

 - loc 179 - getbuf stores the pool ID in the first four bytes of the allocated space, and returns the address just beyond the ID

 - loc 184 - Swapping refers to an approach that moves all code and data associated with a particular computation into main memory when the scheduler makes the computation current. Swapping works best for a long-running computation, such as a word processor

 - loc 184 - Segmentation refers to an approach that moves pieces of the code and data associated with a computation into main memory as needed. One can imagine, for example, placing each function and the associated variables in a separate segment. When a function is called, the operating system loads the segment containing the function into main memory

 - loc 184 - Paging refers to an approach that divides each program into small, fixed-size pieces called pages. The system keeps the most recently referenced pages in main memory, and moves copies of other pages to secondary storage. Pages are fetched on demand — when a running program references memory location i, the memory hardware checks to see whether the page containing location i is resident (i.e., currently in memory). If the page is not resident, the operating system suspends the process (allowing other processes to execute), and issues a request to the disk to obtain a copy of the needed page

 - loc 185 - we use the term physical address space or real address space to define the set of addresses that the memory hardware provides, and the term virtual address space to describe the set of addresses available to a given computation

 - loc 186 - An operating system that maps between virtual and real addresses cannot operate without hardware support

 - loc 186 - The hardware needed for demand paging consists of a page table and an address translation unit. A page table resides in kernel memory, and there is one page table for each process. Typically, the hardware contains a register that points to the current page table and a second register that specifies the length; after it has created a page table in memory, the operating system assigns values to the registers and turns on demand paging. Similarly, when a context switch occurs, the operating system changes the page table registers to point to the page table for the new process

 - loc 187 - If memory is divided into a set of 4096-byte frames, the starting address of each frame (i.e. , the address of the first byte in the frame) will have zeroes in the 12 low-order bits.Therefore, to point to a frame in memory, a page table entry only needs to contain the upper 20 bits

 - loc 187 - Translation consists of array lookup: the hardware treats the high-order bits of an address as a page number, uses the page number as an index into the page table, and follows the pointer to the location of the page in memory

 - loc 187 - a page table consists of an array of pointers to memory locations

 - loc 188 - To make translation efficient, a processor employs a special-purpose hardware unit known as a Translation Look-aside Buffer (TLB). The TLB caches recently accessed page table entries, and can look up the answer much faster than a conventional memory access. To achieve high speed, a TLB uses a form of parallel hardware known as a ContentAddressable Memory (CAM). Given an address, CAM hardware searches a set of stored values in parallel, returning the answer in only a few clock cycles

 - loc 189 - Special processor hardware is required to support demand paging: if a process attempts to access a page that is not resident in memory, the hardware must suspend execution of the current instruction and notify the operating system by signaling a page fault exception. When a page fault occurs, the operating system finds an unused frame in memory, reads the needed page from disk, and then instructs the processor to resume the instruction that caused the fault

 - loc 189 - The selection of a page to move back to disk forms a key problem for operating systems designers

 - loc 190 - In terms of practical systems, a single algorithm has become the de facto standard for page replacement. Known as global clock or second chance

 - loc 190 - To determine whether to select a frame, global clock checks the Use and Modify bits in the page table of the frame. If the Use / Modify bits have value (0,0), global clock chooses the frame. If the bits are (1,0), global clock resets them to (0,0) and bypasses the frame. Finally, if the bits are (1,1), global clock changes them to (1,0) and bypasses the frame

 - loc 190 - the algorithm continues to run, and collects a small set of candidate pages. Collecting a set allows subsequent page faults to be handled quickly

 - loc 191 - a demand paging system works well not because we have devised excellent replacement algorithms, but because memories have grown so large that replacement algorithms are seldom invoked

 - loc 195 - Xinu uses the term inter-process communication port to refer to a rendezvous point through which processes can exchange messages

 - loc 196 - Each port consists of a queue to hold messages and two semaphores. One of the semaphores controls producers, blocking any process that attempts to add messages to a full port. The other semaphore controls consumers, blocking any process that attempts to remove a message from an empty port

 - loc 196 - To guarantee a limit on the total space used, the port functions allocate a fixed number of nodes to hold messages, and share the set among all ports

 - loc 202 - . The idea is to have waiting processes verify that the wait did not terminate because the port was deleted. If it did, the port will either remain unused or the sequence number will be incremented

 - loc 212 - Instead of relying on the processor to provide complete control over I/O, each I/O device contains hardware that can operate independently

 - loc 212 - Hardware in a processor performs three basic steps when an interrupt occurs: d Set the hardware to prevent further interrupts from occurring while an interrupt is being processed d Save sufficient state to allow the processor to resume execution transparently once the interrupt has been handled d Branch to a predetermined memory location where the operating system has placed code to process the interrupt

 - loc 213 - How should a device identify itself? The most popular technique is known as a vectored interrupt. Each device is assigned a unique integer, 0, 1, 2, and so on. Using terminology that has become popular, the integer is called an Interrupt Request Number (IRQ). When an interrupt occurs, the device specifies its IRQ

 - loc 213 - IRQ can be used as an index into an interrupt vector array

 - loc 213 - the IRQ can be used as an index into an interrupt vector array. The operating system preloads each location in the interrupt vector with a pointer to a function that handles the interrupt.

 - loc 214 - The processor hardware is constructed such that it generates an exception when an error occurs. In fact, exception processing is so fundamental that some platforms use the term exception vector to refer to the array of pointers instead of the term interrupt vector

 - loc 214 - Although the vectored approach was invented to handle interrupts from I/O devices, the scheme has been extended to handle exceptions

 - loc 214 - The Galileo uses a single, large vector that contains entries for both exceptions and device interrupts. The first entries in the array correspond to exceptions, and devices are assigned IRQ values above the exceptions. For example, vector position zero is reserved for arithmetic division errors

 - loc 214 - Exceptions, such as divide-by-zero and page faults, follow a vectored approach. The Galileo illustrates how interrupts and exceptions are integrated into a single exception vector. The BeagleBone Black illustrates a two-level scheme in which device interrupts correspond to one particular exception and the operating system must use a second level of indirection to reach the handler for a specific device

 - loc 219 - Manual device configuration. On early hardware, a human had to assign a unique IRQ to each device before the device was connected to a computer

 - loc 219 - Automated assignment during bootstrap. As bus hardware became more sophisticated, techniques were developed that automated interrupt vector assignments. Automated assignment requires programmable devices. That is, the operating system uses the bus to find devices that are attached to the bus, and assigns each device an IRQ. In essence, programmable devices allow the paradigm to be reversed: instead of assigning an IRQ to a device and then configuring the operating system to match the assignment, programmable devices allow the operating system to choose an IRQ and then assign the number to the device

 - loc 219 - Dynamic assignment for pluggable devices. A final approach is used to accommodate devices that can be plugged into a computer while the operating system is running

 - loc 220 - We will use the term master driver to describe the software that handles USB host controller interrupts. At runtime, when a user plugs a device into a USB port, a second level binding occurs. The USB controller hardware detects the new device, and generates an interrupt. The master driver receives control, and communicates across the USB to obtain the type and model of the new device. The master dynamically loads a driver for the new device, and records the driver location. Later, when the USB device interrupts, the master obtains control, determines which of the devices plugged into the USB generated the interrupt, and forwards control to the appropriate driver

 - loc 220 - We use the term interrupt dispatching to refer to the steps that are taken to obtain a device number, use the device number as an index into a vector, extract the address of a handler, and pass control to the handler. To make dispatching efficient and to separate I/O details from the processor, many systems use a special-purpose hardware device known as an interrupt controller

 - loc 221 - we follow an approach used in most systems: interrupt code is divided into two parts: a low-level piece written in assembly language and a high-level piece written in C. We use the term dispatcher for the low-level piece and handler for the high-level piece

 - loc 223 - Interrupts are disabled when an interrupt occurs, and remain disabled until the code returns from an interrupt

 - loc 224 - The maximum time that an interrupt handler for device D can leave interrupts disabled cannot be computed by examining device D. Instead, the time is computed by choosing the smallest constraint across all devices in the system

 - loc 225 - interrupt code is executed by whichever process is running when the interrupt occurs

 - loc 225 - an interrupt can be thought of as occurring “between” two successive instructions

 - loc 225 - Interrupt routines can only call operating system functions that leave the executing process in the current or ready states

 - loc 225 - The scheduling invariant specifies that at any time, a highest priority eligible process must be executing. d When an I/O operation completes, a high-priority process may become eligible to execute

 - loc 226 - To ensure that processes are notified promptly when an I/O operation completes and to maintain the scheduling invariant, an interrupt handler must reschedule whenever it makes a waiting process ready

 - loc 227 - Rescheduling during interrupt processing is safe provided that (1) interrupt code leaves global data in a valid state before rescheduling, and (2) no function enables interrupts unless it disabled them

 - loc 227 - only one interrupt can be in progress for a given process at any time. Because only a finite number of processes exist in the system at a given time and each process can have at most one outstanding interrupt, the number of outstanding interrupts is bounded

 - loc 234 - The term processor clock refers to a hardware device that emits pulses (i.e., square waves) at regular intervals with high precision. The processor clock controls the rate at which the processor executes instructions

 - loc 234 - A real-time clock operates independent of the processor, and pulses in fractions of a second (e.g., 1000 times per second), generating an interrupt for each pulse. Usually, real-time clock hardware does not count pulses — if an operating system needs to compute an elapsed time, the system must increment a counter when each clock interrupt occurs

 - loc 235 - Technically, a time-of-day clock is a chronometer that computes elapsed time. The hardware consists of an internal real-time clock connected to a counter that tallies the pulses. Like a normal clock, the time can be changed. Once set, however, the mechanism runs independent of the processor, and continues as long as the system receives power (some units include a small battery to keep the clock active even if the external power is removed temporarily). Unlike other clocks, a time-of-day clock does not interrupt — the processor must set or interrogate the clock

 - loc 235 - An interval timer, sometimes called a count-down timer or simply a timer, also consists of an internal real-time clock and a counter. To use an interval timer, the system initializes the counter to a positive value. The timer decrements the count once for each real-time clock pulse, and generates an interrupt when the count reaches zero

 - loc 235 - a time-of-day clock is a chronometer that computes elapsed time. The hardware consists of an internal real-time clock connected to a counter that tallies the pulses

 - loc 235 - Unlike other clocks, a time-of-day clock does not interrupt — the processor must set or interrogate the clock

 - loc 236 - If a processor takes too long to service a real-time clock interrupt or if it operates with interrupts disabled for more than one clock cycle, a clock interrupt will be missed and no error will be reported

 - loc 236 - The process manager in an operating system uses a preemption mechanism to implement time slicing that guarantees equal-priority processes receive service round-robin, as specified by the scheduling policy in Chapter 5. The system defines a maximum time slice, T, that a process can execute without allowing other processes to execute

 - loc 236 - When a preemption event occurs, the event handler simply calls resched

 - loc 236 - An operating system allows any process to request a timed delay. When a process requests a timed delay, the operating system moves the process from the current state into a new state (which we call sleeping), and schedules a wakeup event to restart the process at the specified time

 - loc 237 - Without a preemptive capability, an operating system cannot regain control from a process that executes an infinite loop

 - loc 237 - Each time the clock ticks, the clock interrupt handler decrements preempt. When preempt reaches zero, the clock interrupt handler resets preempt to QUANTUM and calls resched. Following the call to resched, the handler returns from the interrupt

 - loc 238 - The key of the first process on a delta list specifies the number of clock ticks a process must delay beyond the current time; the key of each other process on a delta list specifies the number of clock ticks the process must delay beyond the preceding process on the list

 - loc 244 - The fundamental concept behind timed message reception is disjunctive wait: a process blocks until one of two events occurs

 - loc 260 - The I/O subsystem can be divided into three conceptual pieces: an abstract interface consisting of high-level I/O functions that processes use to perform I/O, a set of physical devices, and device driver software that connects the two

 - loc 261 - Unix: choose a small set of abstract I/O operations that are sufficient for all I/O.

 - loc 262 - When using a synchronous I/O interface, a process is blocked until the operation completes. When using an asynchronous I/O interface, a process continues to execute and is notified when the operation completes

 - loc 263 -  Operation Purpose  close Terminate use of a device  control Perform operations other than data transfer  getc Input a single byte of data  init Initialize the device at system startup  open Prepare the device for use  putc Output a single byte of data  read Input multiple bytes of data  seek Move to specific data (usually a disk)  write Output multiple bytes of data

 - loc 263 - The open-read-write-close paradigm requires a process to open a device before use and close a device after use

 - loc 263 - Open and close allow the operating system to manage devices that require exclusive use, prepare a device for data transfer, and stop a device after transfer has ended. Closing a device may be useful, for example, if a device needs to be powered down or placed in a standby state when not in use. Read and write handle the transfer of multiple data bytes to or from a buffer in memory. Getc and putc form a counterpart for the transfer of a single byte (usually a character). Control allows a program to control a device or a device driver (e.g. , to check supplies in a printer or select the channel on a wireless radio). Seek is a special case of control that applies to randomly accessible storage devices, such as disks.Finally, init initializes the device and driver at system startup

 - loc 265 - Xinu uses a static binding for device names. Each device name is bound to an integer descriptor at configuration time before the operating system is compiled

 - loc 265 - The integer descriptor assigned to a device is an index into the device switch table.

 - loc 266 - if a system contains two Ethernet interfaces, each will have its own row in the device switch table. Most entries in the two rows will be identical.However, one column will specify a unique Control and Status Register (CSR) address for each device

 - loc 275 - most drivers employ a technique known as reference counting. That is, a driver maintains an integer variable

 - loc 276 - that counts the number of processes using the device. During initialization, the reference count is set to zero. Whenever a process calls open, the driver increments the reference count, and whenever a process calls close, the driver decrements the reference count. When the reference count reaches zero, the driver powers down the device.

 - loc 277 - What value can be used in devtab for operations that are not meaningful? The answer lies in two special routines that can be used to fill in entries of devtab that have no driver functions: d ionull — return OK without performing any action d ioerr — return SYSERR without performing any action

 - loc 287 - The console line on most embedded systems uses a Universal Asynchronous Transmitter and Receiver (UART) chip that implements serial communication according to the RS-232 standard. UART hardware is primitive — it only provides the ability to send and receive individual bytes. It does not interpret the meaning of bytes or provide functions such as the use of backspace to erase previous input

 - loc 288 - a tty device supports two-way communication: a process can send characters to the output side and/or receive characters from the input side. Although the underlying serial hardware mechanism operates the input and output independently, the tty abstraction allows the two to be treated as a single mechanism

 - loc 288 - Mode Meaning  The driver delivers each incoming character as it arrives raw without echoing the character, buffering a line of text, performing translation, or controlling the output flow  The driver buffers input, echoes characters in a readable cooked form, honors backspace and line kill, allows type-ahead, handles flow control, and delivers an entire line of text  The driver handles character translation, echoing, and cbreak flow control, but instead of buffering an entire line of text, the driver delivers each incoming character as it arrives

 - loc 289 - In general, upper-half functions move data to or from the shared structure and have minimal interaction with the device hardware

 - loc 289 - In general, upper-half functions move data to or from the shared structure and have minimal interaction with the device hardware. For example, an upper-half function places outgoing data in the shared structure where a lower-half function can access and send the data to the device. Similarly, the lower half places incoming data in the shared structure where an upper-half function can extract it

 - loc 289 - upper-half functions are called by application processes and lower-half functions are invoked by interrupts

 - loc 290 - In most drivers, the shared data structure contains two key items: d Request queue d Buffered I/O

 - loc 290 - Each driver has its own set of requests, and the contents of elements on a request queue depend on the underlying device as well as the operations to be performed

 - loc 290 - a queue into which the upper half places requests

 - loc 290 - Output buffering allows an application to deposit an outgoing item in a buffer, and then continue processing. The item remains in the buffer until the hardware is ready to accept the item. Input buffering allows a driver to accept data from a device before an application is ready to receive it

 - loc 291 - Upper-half functions transfer data between processes and buffers; the lower half transfers data between buffers and the device hardware

 - loc 292 - Semaphores can be used to coordinate the upper half and lower half of a device driver. To avoid having lower-half functions block, output is handled by arranging for upper-half functions to wait for buffer space

 - loc 292 - we do not view the lower half as a consumer. Instead, a lower-half output function acts as a producer to generate space (i.e., slots) in the buffer, and signals the output semaphore for each slot

 - loc 292 - because it can be executed by the null process, an interrupt function cannot call a function that moves the executing process to any state other than ready or current. In particular, lower-half routines cannot call wait

 - loc 292 - The UART device contains two onboard buffers, known as FIFOs. One FIFO handles incoming characters, and the other handles outgoing characters. Each FIFO holds up to sixteen characters. The device does not interrupt each time a character arrives. Instead, the hardware generates an interrupt when the first character arrives, but continues to add characters to the input FIFO if they arrive before the interrupt has been serviced. Thus, when it receives an input interrupt, the driver must repeatedly extract characters from the FIFO until the hardware FIFO is empty

 - loc 293 - our driver uses resched_cntl to defer rescheduling temporarily.† After all characters have been extracted from the input FIFO and processed, the driver again calls resched_cntl to permit other processes to run

 - loc 293 - We use the term control block to refer to the shared data structure associated with a device. More specifically, the control block is associated with a driver for the device, and holds data that the driver uses as well as data needed by the hardware. For example, if a driver uses semaphores to coordinate the upper-half and lower-half functions, the semaphore IDs will be placed in the control block

 - loc 293 - the system must have a separate control block for each physical copy of the device

 - loc 293 - When it runs, a device driver function receives an argument that identifies the control block to use. Thus, if a particular system has three serial devices that use the tty abstraction, the operating system contains only one copy of the functions that read and write to a tty device, but contains three separate copies of a tty control block

 - loc 293 - tty control block structure, which is named ttycblk. The key components of the ttycblk structure consist of the input buffer, tyibuff, an output buffer, tyobuff, and a separate echo buffer, tyebuff

 - loc 296 - A character is always inserted at the tail and taken from the head, independent of whether a buffer is used for input or output

 - loc 296 - if a system contains three tty devices, they will be assigned minor device numbers 0, 1, and 2. Unlike device IDs, the assignment of minor device numbers is guaranteed to be contiguous

 - loc 296 - A minor device number serves as an index into the array of control blocks for the device

 - loc 296 - Each function in the upper half has an argument that specifies one of the device table entries. Similarly, when an interrupt occurs, the operating system associates the interrupt with a specific device in the device table

 - loc 301 - To avoid the race condition, device hardware is designed to allow an operating system to request an interrupt without testing the device

 - loc 302 - Setting the interrupt bit in the device only requires a single assignment statement; the code can be found in file ttykickout.c

 - loc 303 - the handler will be invoked whenever the device has received one or more incoming characters, or when the device has sent all the characters in its output FIFO and is ready for more. The handler must check a control register in the device to determine whether an input or output interrupt has occurred

 - loc 325 - The motivation for Direct Memory Access (DMA) is parallelism: adding intelligence to an I/O device allows the device to perform multiple bus transfers without interrupting the processor.

 - loc 326 - To write a disk block, the operating system places the data in a buffer, creates a write request in memory, and passes a pointer to the request to the device. Once a request has been passed to the device, the processor is free to continue executing other processes. While the processor executes, the disk DMA hardware uses the bus to access the write request, obtain the buffer address, and transfer successive words of data from the buffer to the disk

 - loc 326 - DMA input works the other way around. To read a disk block, the operating system allocates a buffer to hold the incoming data, creates a read request in memory, and passes the address of the request to the disk device

 - loc 326 - To write a disk block, the operating system places the data in a buffer, creates a write request in memory, and passes a pointer to the request to the device. Once a request has been passed to the device, the processor is free to continue executing other processes. While the processor executes, the disk DMA hardware uses the bus to access the write request, obtain the buffer address, and transfer successive words of data from the buffer to the disk. Once the device has read an entire block of data from memory and written the block to disk, the disk interrupts the processor

 - loc 326 - with DMA, only one interrupt occurs per block transferred

 - loc 326 - Interestingly, most DMA devices never reach the end of the linked list because the hardware uses a circular linked list, called a request ring (or informally, a buffer ring

 - loc 326 - Instead of passing the device the address of a single request, the hardware requires the operating system to allocate multiple request blocks (each with its own buffer), link them together on a linked list, and pass the address of the list.

 - loc 327 - If it travels completely around the ring and encounters a full buffer, the DMA hardware sets an error indicator (typically an overflow bit) and generates an interrupt to inform the operating system

 - loc 327 - Most DMA hardware also uses a circular linked list for output

 - loc 346 - Ethread consists of a loop that reads packets until it finds a packet that should be processed (i.e., valid). A packet is accepted if the packet is addressed to the computer’s unicast address, the network broadcast address, or is one of the multicast addresses to which the computer is listening. Other packets are discarded

 - loc 348 - Ethwrite waits on the output semaphore, which blocks the calling process until an output ring descriptor is empty and available. The code then copies a packet from the caller’s buffer into the packet buffer associated with the descriptor. If the device is currently idle, ethwrite must start the device. Starting the device is trivial: ethwrite assigns 1 to the tpdr register in the device’s transmit control register

 - loc 353 - DMA devices have a steep learning curve, but offer the reward of both higher performance and smaller driver code

 - loc 357 - Although an Ethernet device can transfer packets across a single network, additional communication software is required to permit applications to communicate across the Internet. In particular, the TCP/Internet Protocol Suite defines the protocols used for Internet communication. The protocols are organized into conceptual layers, and an implementation is known as a protocol stack

 - loc 358 - The Internet Protocol (IP) defines the format of an internet packet, which is known as a datagram. Each datagram is carried in the data area of an Ethernet frame. The Internet Protocol also defines the address format

 - loc 358 - The User Datagram Protocol (UDP) defines a set of 16-bit port numbers that an operating system uses to identify a specific application program

 - loc 358 - The Address Resolution Protocol (ARP) provides two functions. Before another computer can send IP packets to our system, the computer must send an ARP packet that requests our Ethernet address and our system must respond with an ARP reply. Similarly, before our system can send IP packets to another computer, it first sends an ARP request to obtain the computer’s Ethernet address, then uses the Ethernet address to send IP packets

 - loc 358 - The Dynamic Host Configuration Protocol (DHCP) provides a mechanism that a computer can use to obtain an IP address, an address mask for the network, and the IP address of a default router. The computer broadcasts a request, and a DHCP server running on the network sends a response. Usually, DHCP is invoked at startup because the information must be obtained before normal Internet communication is possible

 - loc 359 - the netin process places an incoming UDP packet in a queue associated with a UDP port number, and uses an incoming ARP packet to supply information for an ARP table entry

 - loc 359 - The Internet Control Message Protocol (ICMP) provides error and informational messages that support IP. Our implementation only handles the two ICMP messages used by the ping program: Echo Request and Echo Reply

 - loc 360 - Because the netin process must remain running to receive incoming packets, netin must never execute code that blocks waiting for a packet to arrive. In particular, netin cannot execute code that sends an IP packet, such as a ping reply

 - loc 370 - Function arp_resolve is called when an IP packet is ready to be sent. Arp_resolve takes two arguments: the first specifies the IP address of a computer for which an Ethernet address is needed; the second is a pointer to an array that will hold the Ethernet address. Although the code may seem complex, there are only three cases: the IP address is a broadcast address, the information is already in the ARP cache, or the information is not known. For an IP broadcast address, arp_resolve copies the Ethernet broadcast address into the array specified by the second argument. If the information is present in the cache, arp_resolve finds the correct entry, copies the Ethernet address from the entry into the caller’s array, and returns to the caller without sending any packets over the network. In the case where the requested mapping is not in the cache, arp_resolve must send packets over the network to obtain the information

 - loc 371 - If it finds the ARP packet type (0x806), netin calls function arp_in to handle the packet. Arp_in must handle two cases: either the packet is a request that was initiated by another computer or it is a reply, possibly to a request that we have sent. The protocol specifies that when either type of packet arrives, ARP must examine the sender’s information (IP address and Ethernet address), and update the local cache accordingly. If a process is waiting for the reply, arp_in sends a message to the process. Because an ARP request is broadcast, all computers on the network receive each request. Therefore, after it updates the sender’s information, arp_in checks the target IP address in a request to determine whether the request is for the local system or some other computer on the network. If the request is for another computer, arp_in returns without taking further action. If the target IP address in the incoming request matches the IP address of the local system, arp_in sends an ARP reply. Arp_in forms a reply in variable apkt. Once all fields of the packet have been filled in, the code calls write on the Ethernet device to transmit the reply back to the requester

 - loc 373 - After it creates the network buffer pool and initializes global variables, net_init calls arp_init, udp_init, and icmp_init. It then initializes the IP output queue to empty, and creates the netin and netout processes

 - loc 373 - The netin process repeatedly allocates a buffer, waits for the next packet, and then performs packet demultiplexing. That is, netin uses information in each incoming packet to decide which protocol to use to process the packet

 - loc 377 - On input, ip_in passes valid datagrams to ip_local, which examines the type field in the datagram. Datagrams carrying UDP are passed to udp_in, datagrams carrying ICMP are passed to icmp_in, and other datagrams are dropped

 - loc 418 - The industry has settled on a de facto standard block size of 512 bytes

 - loc 418 - to keep the interface simple, we will stretch the usual meaning of arguments to read and write: instead of interpreting the third argument as a buffer size, we will assume the buffer is large enough to hold a disk block, and use the third argument to specify a block number

 - loc 420 - Because disk access is slow and file system functions often read or write partial blocks, a disk driver must cache copies of blocks to achieve high performance

 - loc 420 - A block is cached whenever a read or write operation occurs. Furthermore, when it receives a subsequent operation for a block, the driver always searches the cache before requesting a transfer

 - loc 420 - A list of pending requests. Like a traditional driver, our remote disk system allows multiple processes to access a disk, and implements synchronous read operations and asynchronous write operations

 - loc 421 - we assume an implicit write occurs at time zero before the system starts

 - loc 421 - The example driver uses a FIFO queue to enforce last-write semantics: Items are inserted at the tail of the request queue; the lower-half process continually selects and performs the item at the head of the queue

 - loc 421 - We use the term last-write semantics to capture the concept, and insist that: A disk driver can use techniques such as caching to

 - loc 421 - We use the term last-write semantics to capture the concept, and insist that: A disk driver can use techniques such as caching to optimize performance provided the driver guarantees last-write semantics

 - loc 421 - if process A reads block five and process B writes block five later, the two requests will appear in the correct order in the queue. The read request will be serviced first, followed by the write request

 - loc 421 - example driver uses a FIFO queue to enforce last-write semantics

 - loc 421 - A disk driver can use techniques such as caching to optimize performance provided the driver guarantees last-write semantics

 - loc 421 - If opt is a read operation for block i, the driver must deliver the data that was written to the block in opk , where k is the highest index of a write operation less than t (i.e., all the operations between opk and opt are read operations). To complete the definition, we assume an implicit write occurs at time zero before the system starts. Thus, if a system attempts to read a block before any calls to write the block, the driver returns whatever data was on the disk when the system booted. We use the term last-write semantics to capture the concept

 - loc 429 - rdsinit performs three important tasks. It allocates a set of disk buffers and links them onto the free list, it creates two semaphores that control processing, and it creates the high-priority process that communicates with the server

 - loc 429 - rd_reqsem, guards the request list. The semaphore starts with count zero, and is signaled each time a new request is added to the request queue. The communication process waits on rd_reqsem before extracting an item from the list, which means the process will block if the list is empty

 - loc 429 - rd_availsem, counts the number of buffers that are available for use (i.e., free or in the cache). Initially, RD_BUFFS buffers are on the free list and rd_availsem has a count equal to RD_BUFFS. When a buffer is needed, a caller waits on the semaphore

 - loc 430 - Each client supplies a unique identification string which allows the server to distinguish among clients. Instead of using a hardware value (e.g., an Ethernet address) as the unique string, the example code allows a user to specify the ID string by calling open on the disk device. The chief advantage of separating the ID from the hardware is portability

 - loc 435 - First, rdscomm checks to see whether the UDP port has already been registered, and calls udp_register if it has not. It may seem that the check is unnecessary because the port will not be registered until rdscomm runs. However, checking at runtime allows the remote disk system to be restarted. Second, rdscomm checks to see whether the computer has already obtained an IP address (which is required for Internet communication). If an address has not been assigned, rdscomm calls getlocalip to obtain an address. Once the two steps are complete, rdscomm is ready to communicate with the remote disk server

 - loc 435 - On each iteration, rdscomm calls udp_sendto to transmit a copy of the message to the server, and calls udp_recv to receive a reply

 - loc 441 - Rdsread begins by handling two special cases. First, if the requested block is found in the cache, rdsread extracts a copy of the data and returns. Second, if the request list contains a request to write the specified block, rdsread extracts a copy of the data from the buffer and returns. Finally, rdsread creates a read request, enqueues the request at the tail of the request queue, and waits for a message from the communication process as described above

 - loc 441 - Rdsread begins by handling two special cases. First, if the requested block is found in the cache, rdsread extracts a copy of the data and returns. Second, if the request list contains a request to write the specified block, rdsread extracts a copy of the data from the buffer and returns. Finally, rdsread creates a read request, enqueues the request at the tail of the request

 - loc 453 - When examining the code, remember that the remote disk process has higher priority than any application process. Thus, the code does not need to disable interrupts or use a mutual exclusion semaphore when accessing the request queue, cache, or free list

 - loc 453 - In the case of a read operation, rdsprocess leaves the buffer on the request queue until the request can be satisfied. In the case of a write operation, rdsprocess extracts a copy of the data and moves the buffer to the cache before calling rdscomm

 - loc 460 - File semantics are taken from Unix according to the following principle: The file system considers each file to be a sequence of zero or more bytes; any further structure must be enforced by application programs that use the file

 - loc 460 - File semantics are taken from Unix according to the following principle: The file system considers each file to be a sequence of zero or more bytes; any further structure must be enforced by application programs that use the file. Treating a file as a sequence of bytes has several advantages. First, the file system does not impose a type on the file and does not need to distinguish among file types. Second, the code is small because a single set of file system functions suffices for all files. Third, the file semantics can be applied to devices and services as well as to conventional files. Fourth, application programs can choose an arbitrary structure for data without changing the underlying system. Finally, file contents are independent of the processor or memory (e.g., an application may need to distinguish among a 32-bit and

 - loc 460 - File semantics are taken from Unix according to the following principle: The file system considers each file to be a sequence of zero or more bytes; any further structure must be enforced by application programs that use the file. Treating a file as a sequence of bytes has several advantages. First, the file system does not impose a type on the file and does not need to distinguish among file types. Second, the code is small because a single set of file system functions suffices for all files. Third, the file semantics can be applied to devices and services as well as to conventional files. Fourth, application programs can choose an arbitrary structure for data without changing the underlying system. Finally, file contents are independent of the processor or memory (e.g., an application may need to distinguish among a 32-bit and 64-bit integer stored in a file, but the file system does not

 - loc 460 - Opening a named file connects an executing process with the data on disk, and establishes a pointer to the first byte. Operations getc and read retrieve data from the file and advance the pointer; getc retrieves one byte, and read can retrieve multiple bytes. Operations putc and write change bytes in the file and move the pointer along, extending the file length if new data is written beyond the end; putc changes one byte, and write can change multiple bytes. The seek operation moves the pointer to a specified byte position in the file; the first byte is at position zero. Finally, close detaches the running process from the file, leaving the data in the file on permanent storage

 - loc 461 - Each file has a mutual exclusion semaphore to guarantee that only one process at a time can attempt to write a byte to the file, read a byte from the file, or change the current file position. Furthermore, the directory has a mutual exclusion semaphore to guarantee that only one process at a time can attempt to create a file or otherwise change a directory entry.

 - loc 461 - Large systems usually allow arbitrary numbers of processes to read and write arbitrary numbers of files concurrently. The chief difficulty with multiple access lies in specifying exactly what it means to have

 - loc 461 - Large systems usually allow arbitrary numbers of processes to read and write arbitrary numbers of files concurrently. The chief difficulty with multiple access lies in specifying exactly what it means to have multiple processes writing and reading a file at the same time

 - loc 462 - The first sector of the disk holds a directory that contains a list of file names along with a pointer to the list of index blocks for the file. The directory also contains two other pointers: one to a list of free (unused) index blocks and another to a list of free data blocks

 - loc 462 - Following the directory, the disk contains an index area that holds a set of index blocks, abbreviated i-blocks. Each file has its own index, which consists of a singlylinked list of index blocks. Initially, all index blocks are linked onto a free list from which the system allocates one as needed

 - loc 462 - Following the index area, remaining blocks of the disk comprise a data area. Each block in the data area is referred to as a data block, abbreviated d-block, because a block contains data that has been stored in a file

 - loc 462 - data block does not contain pointers to other data blocks, nor does it contain information that relates the block to the file of which it is a part; all such information resides in the file’s index

 - loc 462 - Similar to index blocks, when a disk is initialized, the data blocks are linked onto a free list

 - loc 463 - each index block contains a pointer to the next index block, an offset that specifies the lowest position in the file indexed by the block, and an array of sixteen pointers to data blocks

 - loc 474 - After the file has been opened, the process uses the device ID with operations getc, read, putc, write, and seek. The device switch table maps each high-level operation to the appropriate driver function for file pseudo-devices exactly as it maps high-level operations onto device drivers for physical devices

 - loc 474 - Conceptually, the control block contains two types of items: fields that hold information about the pseudo-device and fields that hold information from the disk. Fields lfstate and lfmode are the former type: the state field specifies whether the device is currently in use, and the mode field specifies whether the file has been opened for reading, writing, or both. Fields lfiblock and lfdblock are of the latter type: when a file is being read or written they contain a copy of the index block and the data block for the current position in the file measured in bytes (which is given by field lfpos

 - loc 485 - llffppttrr-->>llffiinnuumm,, &&llffppttrr-->>llffiibblloocckk

