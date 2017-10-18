
---
#  Programming from the Ground Up
## by Jonathan Bartlett
---

 - loc 16 - The data bus is the connection between the CPU and memory. It is the actual wire that connects them

 - loc 18 - the computer can’t tell the difference between a value that is an address, a value that is a number, a value that is an ASCII code, or a value that you have decided to use for another purpose. A number becomes an ASCII code when you attempt to display it. A number becomes an address when you try to look up the byte it points to

 - loc 19 - If the instruction pointer points to a memory word, it is loaded as an instruction. Other than that, the computer has no way of knowing the difference between programs and other types of data

 - loc 21 - if we want to initialize a register to 0, instead of giving the computer an address to read the 0 from, we would specify immediate mode, and give it the number 0.

 - loc 21 - In the register addressing mode, the instruction contains a register to access, rather than a memory location

 - loc 21 - In the direct addressing mode, the instruction contains the memory address to access. For example, I could say, please load this register with the data at address 2002. The computer would go directly to byte number 2002 and copy the contents into our register

 - loc 21 - In the indexed addressing mode, the instruction contains a memory address to access, and also speciﬁes an index register to offset that address. For example, we could specify address 2002 and an index register. If the index register contains the number 4, the actual address the data is loaded from would be 2006

 - loc 21 - if you wanted to access the fourth word from location 2002, you would load your index register with 3 and set the multiplier to 4. This would load from location 2014 - the fourth word

 - loc 21 - In the indirect addressing mode, the instruction contains a register that contains a pointer to where the data should be accessed

 - loc 22 - pointer addressing mode. This is similar to indirect addressing, but you also include a number called the offset to add to the register’s value before using it for lookup

 - loc 22 - base pointer addressing mode. This is similar to indirect addressing, but you also include a number called the offset to add to the register’s value before using it for lookup

 - loc 27 - The linker is the program that is responsible for putting the object ﬁles together and adding information to it so that the kernel knows how to load and run it

 - loc 27 - as is the command which runs the assembler, exit.s is the source ﬁle, and -o exit.o tells the assemble to put it’s output in the ﬁle exit.o. exit.o is an object ﬁle. An object ﬁle is code that is in the machine’s language, but has not been completely put together

 - loc 27 - You must always re-assemble and re-link programs after you modify the source ﬁle for the changes to occur in the program

 - loc 29 - Anything starting with a period isn’t directly translated into a machine instruction. Instead, it’s an instruction to the assembler itself. These are called assembler directives or pseudo-operations

 - loc 30 - globl means that the assembler shouldn’t discard this symbol after assembly, because the linker will need it. _start is a special symbol that always needs to be marked with .globl because it marks the location of the start of the program. Without marking this location in this way, when the computer loads your program it won’t know where to begin running your program

 - loc 30 - A label is a symbol followed by a colon. Labels deﬁne a symbol’s value

 - loc 30 - On most instructions which have two operands, the ﬁrst one is the source operand and the second one is the destination

 - loc 32 - The dollar-sign in front of the one indicates that we want to use immediate mode addressing

 - loc 32 - Without the dollar-sign it would do direct addressing, loading whatever number is at address 1. We want the actual number 1 loaded in, so we have to use immediate mode

 - loc 34 - Operating System features are accessed through system calls. These are invoked by setting up the registers in a special way and issuing the instruction int $0x80. Linux knows which system call we want to access by what we stored in the %eax register. Each system call has other requirements as to what needs to be stored in the other registers. System call number 1 is the exit system call, which requires the status code to be placed in %ebx

 - loc 43 - movl BEGINNINGADDRESS(,%INDEXREGISTER,WORDSIZE)

 - loc 43 - This is how you write indexed addressing mode instructions in assembly language. The instruction in a general form is this: movl BEGINNINGADDRESS(,%INDEXREGISTER,WORDSIZE)

 - loc 45 - The cmpl instruction compares the two values. Here, we are comparing the number 0 to the number stored in %eax This compare instruction also affects a register not mentioned here, the %eflags register

 - loc 45 - The cmpl instruction compares the two values. Here, we are comparing the number 0 to the number stored in %eax This compare instruction also affects a register not mentioned here, the %eflags register. This is also known as the status register, and has many uses which we will discuss later. Just be aware that the result of the comparison is stored in the status register

 - loc 45 - je Jump if the values were equal jg Jump if the second value was greater than the ﬁrst value 12 jge Jump if the second value was greater than or equal to the ﬁrst value jl Jump if the second value was less than the ﬁrst value jle Jump if the second value was less than or equal to the ﬁrst value jmp Jump no matter what. This does not need to be preceeded by a comparison

 - loc 47 - The general form of memory address references is this: ADDRESS_OR_OFFSET(%BASE_OR_OFFSET,%INDEX,MULTIPLIER) All of the ﬁelds are optional

 - loc 48 - FINAL ADDRESS = ADDRESS_OR_OFFSET + %BASE_OR_OFFSET + MULTIPLIER * % ADDRESS_OR_OFFSET and MULTIPLIER must both be constants, while the other two must be registers. If any of the pieces is left out, it is just substituted with zero in the equation

 - loc 48 - direct addressing mode This is done by only using the ADDRESS_OR_OFFSET portion. Example:

 - loc 48 - direct addressing mode This is done by only using the ADDRESS_OR_OFFSET portion. Example: movl ADDRESS, %eax

 - loc 48 - indexed addressing mode This is done by using the ADDRESS_OR_OFFSET and the %INDEX portion. You can use any general-purpose register as the index register

 - loc 48 - movl string_start(,%ecx,1), %eax This starts at string_start, and adds 1 * %ecx to that address, and loads the value into %eax

 - loc 48 - indirect addressing mode Indirect addressing mode loads a value from the address indicated by a register

 - loc 49 - movl (%eax), %ebx

 - loc 49 - base pointer addressing mode Base-pointer addressing is similar to indirect addressing, except that it adds a constant value to the address in the register. For example, if you have a record where the age value is 4 bytes into the record, and you have the address of the record in %eax, you can retrieve the age into %ebx by issuing the following instruction: movl 4(%eax), %ebx

 - loc 50 - . %ax is the least-signiﬁcant half (i.e. - the last part of the number) of the %eax register, and is useful when dealing with two-byte quantities. %ax is further divided up into %al and %ah

 - loc 62 - the function reserves space on the stack for any local variables it needs. This is done by simply moving the stack pointer out of the way. Let’s say that we are going to need two words of memory to run a function. We can simply move the stack pointer down two words to reserve the space. This is done like this: subl $8, %esp

 - loc 63 - The only difference between the global and static variables is that static variables are only used by one function, while global variables are used by many functions. Assembly language treats them exactly the same, although most other languages distinguish them

 - loc 68 - The difference between call and jmp is that call also pushes the return address onto the stack so that the function can return, while the jmp does not. 62

 - loc 68 - The difference between call and jmp is that call also pushes the return address onto the stack so that the function can return, while the jmp does not

 - loc 73 - When programming functions, you are supposed to put the parameters of the function on the top of the stack right before you call it

 - loc 74 - The addl instruction moves the stack pointer back to where it was before we pushed the $4 onto the stack. You should always clean up your stack parameters after a function call returns

 - loc 81 - When you access a ﬁle, you start by opening it by name. The operating system then gives you a number, called a ﬁle descriptor, which you use to refer to the ﬁle until you are through with it. You can then read and write to the ﬁle using its ﬁle descriptor. When you are done reading and writing, you then close the ﬁle, which then makes the ﬁle descriptor useless

 - loc 84 - I placed a dollar sign in front of my_buffer. Remember that the reason for this is that without the dollar sign, my_buffer is treated as a memory location, and is accessed in direct addressing mode. The dollar sign switches it to immediate mode addressing, which actually loads the number represented by my_buffer

 - loc 84 - lcomm my_buffer, 500 This directive, .lcomm, will create a symbol, my_buffer, that refers to a 500-byte storage location that we can use as a buffer

 - loc 97 - Fortunately, command-line parameters are already stored by Linux in an easy-to-access location, and are already null-terminated. When a Linux program begins, all pointers to command-line arguments are stored on the stack. The number of arguments is stored at 8(%esp), the name of the program is stored at 12(%esp), and the arguments are stored from 16(%esp) on

 - loc 98 - In normal programs, every system call should normally be checked for success or failure. In failure cases, %eax will hold an error code instead of a return value. Error codes are negative, so they can be detected by comparing %eax to zero and jumping if it is less than zero

 - loc 102 - there are several constants that we have been deﬁning over and over in our programs, and it is useful to put them in a ﬁle, so that we don’t have to keep entering them. Put the following constants in a ﬁle called linux.s

 - loc 106 - rept tells #the assembler to repeat the section between #.rept and .endr the number of times specified

 - loc 106 - #.rept is used to pad each item. .rept tells #the assembler to repeat the section between #.rept and .endr the number of times specified

 - loc 110 - include "linux.s" .include "record-def.s" These statements cause the given ﬁles to basically be pasted right there in the code. You don’t need to do this with functions, because the linker can take care of combining functions exported with .globl. However, constants deﬁned in another ﬁle do need to be imported in this way

 - loc 110 - You may have noticed the lines: .include "linux.s" .include "record-def.s" These statements cause the given ﬁles to basically be pasted right there in the code. You don’t need to do this with functions, because the linker can take care of combining functions exported with .globl. However, constants deﬁned in another ﬁle do need to be imported in this way

 - loc 138 - as helloworld-lib.s -o helloworld-lib.o ld -dynamic-linker /lib/ld-linux.so.2 \ -o helloworld-lib helloworld-lib.o -lc Remember, the backslash in the ﬁrst line simply means that the command continues on the next line. The option -dynamic-linker /lib/ld-linux.so.2 allows our program to be linked to libraries. This builds the executable so that before executing, the operating system will load the program /lib/ld-linux.so.2 to load in external libraries and link them with the program. This program is known as a dynamic linker

 - loc 139 - When using dynamic linking, the name itself resides within the executable, and is resolved by the dynamic linker when it is run. When the program is run by the user, the dynamic linker loads the shared libraries listed in our link statement, and then ﬁnds all of the function and variable names that were named by our program but not found at link time, and matches them up with corresponding entries in the shared libraries it loads.

 - loc 139 - we combined all of the code together using the linker at link-time, so it was still statically-linked. However, in the helloworld-lib program, we started using shared libraries. When you use shared libraries, your program is then dynamically-linked, which means that not all of the code needed to run the program is actually contained within the program ﬁle itself, but in external libraries

 - loc 140 - It will report back something like libc.so.6 => /lib/libc.so.6 (0x4001d000) /lib/ld-linux.so.2 => /lib/ld-linux.so.2 (0x400000000) The numbers in parenthesis may be different on your system. This means that the program helloworld is linked to libc.so.6 (the .6 is the version number), which is found at /lib/libc.so.6, and /lib/ld-linux.so.2 is found at /lib/ld-linux.so.2. These libraries have to be loaded before the program can be run. If you are interested, run the ldd program on various programs that are on your Linux distribution, and see what libraries they rely on.

 - loc 145 - . If the prototype said to pass an int, you would use direct addressing mode and do pushl my_location. However, if the prototype said to pass an int *, you would do pushl $my_location - an immediate mode push of the address that the value resides in

 - loc 146 - Most of your system libraries are in /usr/lib or /lib. If you want to just see what symbols they deﬁne, just run objdump -R FILENAME where FILENAME is the full path to the library

 - loc 148 - ld -shared write-record.o read-record.o -o librecord.so This links both of these ﬁles together into a shared library called librecord.so. This ﬁle can now be used for multiple programs

 - loc 148 - as write-records.s -o write-records ld -L . -dynamic-linker /lib/ld-linux.so.2 \ -o write-records -lrecord write-records.o In this command, -L . told the linker to look for libraries in the current directory (it usually only searches /lib directory, /usr/lib directory, and a few others). As we’ve seen, the option -dynamic-linker /lib/ld-linux.so.2 speciﬁed the dynamic linker. The option -lrecord tells the linker to search for functions in the ﬁle named librecord.so

 - loc 149 - by default, the dynamic linker only searches /lib, /usr/lib, and whatever directories are listed in /etc/ld.so.conf for libraries. In order to run the program, you either need to move the library to one of these directories, or execute the following command: LD_LIBRARY_PATH=. export LD_LIBRARY_PATH

 - loc 149 - The man page for ld.so contains a lot of information about how the Linux dynamic linker works

 - loc 154 - Word This is the size of a normal register. On x86 processors, a word is four bytes long. Most computer operations handle a word at a time

 - loc 155 - The initial layout of the stack is as follows: At the bottom of the stack (the bottom of the stack is the top address of memory - see Chapter 4), there is a word of memory that is zero. After that comes the null-terminated name of the program using ASCII characters. After the program name comes the program’s environment variables (these are not important to us in this book). Then come the program’s command-line arguments. These are the values that the user typed in on the command line to run this program. When we run as, for example, we give it several arguments - as, sourcefile.s, -o, and objectfile.o. After these, we have the number of arguments that were used. When the program begins, this is where the stack pointer, %esp, is pointing

 - loc 155 - pushl %eax is equivalent to movl %eax, (%esp) 149

 - loc 156 - popl %eax is the same as movl (%esp), %eax addl $4, %esp

 - loc 156 - subl $4, %esp

 - loc 156 - This middle part between the stack and your program’s data sections is inaccessible memory - you are not allowed to access it until you tell the kernel that you need it. 2 If you try, you will get an error (the error message is usually "segmentation fault").

 - loc 158 - Each program gets its own sandbox to play in. Every program running on your computer thinks that it was loaded at memory address 0x0804800, and that it’s stack starts at 0xbffffff. When Linux loads a program, it ﬁnds a section of unused memory, and then tells the processor to use that section of memory as the address 0x0804800 for this program. The address that a program believes it uses is called the virtual address, while the actual address on the chips that it refers to is called the physical address. The process of assigning virtual addresses to physical addresses is called mapping

 - loc 159 - Here is an overview of the way memory accesses are handled under Linux: • The program tries to load memory from a virtual address. • The processor, using tables supplied by Linux, transforms the virtual memory address into a physical memory address on the ﬂy

 - loc 160 - If the processor does not have a physical address listed for the memory address, it sends a request to Linux to load it. • Linux looks at the address. If it is mapped to a disk location, it continues on to the next step. Otherwise, it terminates the program with a segmentation fault error. • If there is not enough room to load the memory from disk, Linux will move another part of the program or another program onto disk to make room. • Linux then moves the data into a free physical memory address. • Linux updates the processor’s virtual-to-physical memory mapping tables to reﬂect the changes. • Linux restores control to the program, causing it to re-issue the instruction which caused this process to happen. • The processor can now handle the instruction using the newly-loaded memory and translation tables

 - loc 160 - When running Linux on x86 processors, a page is 4096 bytes of memory. All of the memory mappings are done a page at a time

 - loc 161 - Resident Set Size: The amount of memory that your program currently has in physical memory is called it’s resident set size, and can be viewed by using the program top. The resident set size is listed under the column labelled "RSS

 - loc 161 - If you try to access a piece of virtual memory that hasn’t been mapped yet, it triggers an error known as a segmentation fault, which will terminate your program

 - loc 161 - If you need more memory, you can just tell Linux where you want the new break point to be, and Linux will map all the memory you need between the current and new break point, and then move the break point to the spot you specify. That memory is now available for your program to use. The way we tell Linux to move the break point is through the brk system call

 - loc 162 - Whenever you need a certain amount of memory, you can simply tell allocate how much you need, and it will give you back an address to the memory. When you’re done with it, you tell deallocate that you are through with it. allocate will then be able to reuse the memory. This pattern of memory management is called dynamic memory allocation. This minimizes the number of "holes" in your memory, making sure that you are making the best use of it you can. The pool of memory used by memory managers is commonly referred to as the heap

 - loc 162 - The way memory managers work is that they keep track of where the system break is, and where the memory that you have allocated is. They mark each block of memory in the heap as being used or unused. When you request memory, the memory manager checks to see if there are any unused blocks of the appropriate size. If not, it calls the brk system call to request more memory

 - loc 196 - XOR operation is faster than the loading operation, so many programmers use it to load a register with zero. For example, the code movl $0, %eax is often replaced by xorl %eax, %eax

 - loc 198 - AND, OR, NOT, and XOR are called boolean operators because they were ﬁrst studied by George Boole

 - loc 204 - To get the negative representation of a number in two’s complement form, you must perform the following steps: 1. Perform a NOT operation on the number 2. Add one to the resulting number So, to get the negative of 00000000000000000000000000000001, you would ﬁrst do a NOT operation, which gives 11111111111111111111111111111110, and then add one, giving 11111111111111111111111111111111

 - loc 205 - When you increase the size of a signed quantity in two’s complement representation, you have to perform sign extension. Sign extension means that you have to pad the left-hand side of the quantity with whatever digit is in the sign digit when you add bits. So, if we extend a negative number by 4 digits, we should ﬁll the new digits with a 1. If we extend a positive number by 4 digits, we should ﬁll the new digits with a 0

 - loc 206 - For example 010 means 10 in octal, which is 8 in decimal. If you just write 10 that means 10 in decimal. The beginning zero is what differentiates the two. So, be careful not to put any leading zeroes in front of decimal numbers, or they will be interepreted as octal numbers

 - loc 210 - For more in-depth look at byte order issues, you should read DAV’s Endian FAQ at http://www.rdrop.com/~cary/html/endian_faq.html, especially the article "On Holy Wars and a Plea for Peace" by Daniel Cohen

 - loc 219 - Languages are simply tools, and learning to use a new tool should not be something a programmer ﬂinches at

 - loc 221 - many choose Perl because it has a vast library of functions for handling just about every protocol or type of data on the planet. Python, however, has a cleaner syntax and often lends itself to more straightforward solutions. It’s cross-platform GUI tools are also excellent. PHP makes writing web applications simple. Common LISP has more power and features than any other environment for those willing to learn it. Scheme is the model of simplicity and power combined together. C is easy to interface with other languages

 - loc 223 - The angle brackets around the ﬁlename tell the compiler to look in it’s standard paths for the ﬁle (/usr/include and /usr/local/include, usually). If it was in quotes, like #include "stdio.h" it would look in the current directory for the ﬁle

 - loc 225 - The ﬁrst, optional line is used for UNIX machines to tell which interpreter to use to run the program. The #! tells the computer that this is an interpreted program, and the /usr/bin/perl tells the computer to use the program /usr/bin/perl to interpret the program

 - loc 229 - Even experienced programmers have trouble predicting which parts of the program will be the bottlenecks which need optimization, so you will probably end up wasting your time optimizing the wrong parts

 - loc 229 - It is better to not optimize at all than to optimize too soon. When you optimize, your code generally becomes less clear, because it becomes more complex. Readers of your code will have more trouble discovering why you did what you did which will increase the cost of maintenance of your project

 - loc 229 - While you develop your program, you need to have the following priorities: • Everything is documented • Everything works as documented • The code is written in an modular, easily modiﬁable form

 - loc 230 - Many new projects often have a ﬁrst code base which is completely rewritten as developers learn more about the problem they are trying to solve. Any optimization done on the ﬁrst codebase is completely wasted

 - loc 230 - A proﬁler is a program that will let you run your program, and it will tell you how much time is spent in each function, and how many times they are run

 - loc 231 - gprof is the standard GNU/Linux proﬁling tool

 - loc 231 - if you were trying to ﬁnd the best way for three people in different cities to meet in St. Louis, a local optimization would be ﬁnding a better road to get there, while a global optimization would be to decide to teleconference instead of meeting in person

