
---
#  Computer Security
## by Stallings & Brown
---

 - loc 355 - The next issue is ensuring that no NULLs occur in the shellcode. This means a zero value cannot be used in any instruction argument or in any constant data (such as the terminating NULL on the end of the ”/bin/sh” string).Instead, any required zero values must be generated and saved as the code runs. The logical XOR instruction of a register value with itself generates a zero value, as is done here with the %eax register. This value can then be copied anywhere needed, such as the end of the string, and also as the value of args[1].

 - loc 367 - Memory is requested from the heap by programs for use in dynamic data structures, such as linked lists of records. If such a record contains a buffer vulnerable to overflow, the memory following it can be corrupted. Unlike the stack, there will not be return addresses here to easily

 - loc 368 - cause a transfer of control. However, if the allocated space includes a pointer to a function, which the code then subsequently calls, an attacker can arrange for this address to be modified to point to shellcode in the overwritten buffer

 - loc 370 - if unsafe buffer operations are used, data may overflow a global buffer and change adjacent memory locations, including perhaps one with a function pointer, which is then subsequently called

 - loc 429 - Unix and Linux systems provide a mechanism to run such services in a chroot jail, which restricts the server’s view of the file system to just a specified portion. Thisis done using the chroot system call that confines a process to some subset ofthefile system by mapping the root of the filesystem “/” to some other directory (e.g.,/srv/ftp/public

 - loc 430 - Tripwire” is a well-known file integrity checking tool that maintains a database of cryptographic hashes of monitored files, and scans to detect any changes, whether

 - loc 430 - Tripwire” is a well-known file integrity checking tool that maintains a database of cryptographic hashes of monitored files, and scans to detect any changes, whether as a result of malicious attack, or simply accidental or incorrectly managed update.

