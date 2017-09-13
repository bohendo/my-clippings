______________________________

  How Linux Works
  by Brian Ward
______________________________

 loc 129 - The kernel is software residing in memory that tells the CPU what to do. The kernel manages the hardware and acts primarily as an interface between the hardware and any running program.

 loc 136 - The kernel runs in kernel mode, and the user processes run in user mode. Code running in kernel mode has unrestricted access to the processor and main memory. This is a powerful but dangerous privilege that allows a kernel process to easily crash the entire system. The area that only the kernel can access is called kernel space. User mode, in comparison, restricts access to a (usually quite small) subset of memory and safe CPU operations. User space refers to the parts of main memory that the user processes can access.

 loc 151 - A CPU is just an operator on memory; it reads its instructions and data from the memory and writes data back out to the memory.

 loc 159 - Because it’s common to refer to the state in abstract terms rather than to the actual bits, the term image refers to a particular physical arrangement of bits.

 loc 164 - The kernel is in charge of managing tasks in four general system areas: Processes. The kernel is responsible for determining which processes are allowed to use the CPU. Memory. The kernel needs to keep track of all memory—what is currently allocated to a particular process, what might be shared between processes, and what is free. Device drivers. The kernel acts as an interface between hardware (such as a disk) and processes. It’s usually the kernel’s job to operate the hardware. System calls and support. Processes normally use system calls to communicate with the kernel.

 loc 236 - Other than init (see Chapter 6), all user processes on a Linux system start as a result of fork(), and most of the time, you also run exec() to start a new program instead of running a copy of an existing process.

 loc 254 - Pseudo-devices look like devices to user processes, but they’re implemented purely in software. As such, they don’t technically need to be in the kernel, but they are usually there for practical reasons. For example, the kernel random number generator device (/dev/random) would be difficult to implement securely with a user process.

 loc 287 - Users exist primarily to support permissions and boundaries.

 loc 300 - Groups are sets of users. The primary purpose of groups is to allow a user to share file access to other users in a group.

 loc 333 - Every Unix system needs the Bourne shell in order to function correctly,

 loc 511 - If you don’t want the shell to expand a glob in a command, enclose the glob in single quotes ('').

 loc 579 - If you see a file and are unsure of its format,

 loc 579 - If you see a file and are unsure of its format, try using the file command to see if the system can guess:

 loc 627 - You may wish to use a pattern such as .[^.]* or .??* to get all dot files except the current and parent directories.

 loc 641 - The main difference between environment and shell variables is that the operating system passes all of your shell’s environment variables to programs that the shell runs, whereas shell variables cannot be accessed in the commands that you run.

 loc 641 - The main difference between environment and shell variables is that the operating system passes all of your shell’s environment variables to programs that the shell runs, whereas shell variables cannot be accessed in the commands that you run. Assign an environment variable with the shell’s export command.

 loc 647 - Environment variables are useful because many programs read them for configuration and options.

 loc 647 - For example, you can put your favorite less command-line options in the LESS environment variable, and less will use those options when you run it.

 loc 780 - so that you can ask him or her. To search for a manual page by keyword, use the -k option: $ man -k keyword This is helpful if you don’t quite know the name of the command that you want.

 loc 780 - To search for a manual page by keyword, use the -k option: $ man -k keyword This is helpful if you don’t quite know the name of the command that you want.

 loc 815 - to read the /etc/passwd file description (as opposed to the passwd command), you can insert the section number before the page name: $ man 5 passwd

 loc 826 - Some packages dump their available documentation into /usr/share/doc

 loc 857 - $ ls /fffffffff > f 2> e The number 2 specifies the stream ID that the shell modifies. Stream ID 1 is standard output (the default), and 2 is standard error.

 loc 859 - You can also send the standard error to the same place as stdout with the >& notation. For example, to send both standard output and standard error to the file named f, try this command: $ ls /fffffffff > f 2>&1

 loc 966 - $ kill -STOP pid A stopped process is still in memory, ready to pick up where it left off. Use the CONT signal to continue running the process again: $ kill -CONT pid

 loc 991 - To see if you’ve accidentally suspended any processes on your current terminal, run the jobs command.

 loc 1092 - You can list the contents of a directory if it’s readable, but you can only access a file in a directory if the directory is executable.

 loc 1174 - Before unpacking, it’s usually a good idea to check the contents of a .tar file with the table-of-contents mode by using the t flag instead of the x flag.

 loc 1180 - When unpacking, consider using the p option to preserve permissions. Use this in extract mode to override your umask and get the exact permissions specified in the archive. The p option is the default when working as the superuser.

 loc 1206 - The zcat command is the same as gunzip -dc. The -d option decompresses and the -c option sends the result to standard output

 loc 1209 - You can use z as an option to automatically invoke gzip on the archive; this works both for extracting an archive (with the x or t modes in tar) and creating one (with c). For example, use the following to verify a compressed archive: $ tar ztvf file.tar.gz

 loc 1223 - The bzip2 compression/decompression option for tar is j.

 loc 1251 - The /lib directory should contain only shared libraries,

 loc 1270 - (The reason that the root directory does not contain the complete system is primarily historic—in the past, it was to keep space requirements low for the root.)

 loc 1367 - Example 3-1. Device files $ ls -l brw-rw---- 1 root disk 8, 1 Sep 6 08:37 sda1 crw-rw-rw- 1 root root 1, 3 Sep 6 08:37 null prw-r--r-- 1 root root 0 Mar 3 19:17 fdata srw-rw-rw- 1 root root 0 Dec 18 07:43 log Note the first character of each line (the first character of the file’s mode) in Example 3-1. If this character is b, c, p, or s, the file is a device. These letters stand for block, character, pipe, and socket, respectively, as described in more detail below.

 loc 1368 - $ ls -l brw-rw---- 1 root disk 8, 1 Sep 6 08:37 sda1 crw-rw-rw- 1 root root 1, 3 Sep 6 08:37 null prw-r--r-- 1 root root 0 Mar 3 19:17 fdata srw-rw-rw- 1 root root 0 Dec 18 07:43 log Note the first character of each line (the first character of the file’s mode) in Example 3-1. If this character is b, c, p, or s, the file is a device. These letters stand for block, character, pipe, and socket, respectively, as described in more detail below.

 loc 1371 - Note the first character of each line (the first character of the file’s mode) in Example 3-1. If this character is b, c, p, or s, the file is a device. These letters stand for block, character, pipe, and socket, respectively, as described in more detail below.

 loc 1376 - Programs access data from a block device in fixed chunks. The sda1 in the preceding example is a disk device, a type of block device.

 loc 1380 - Character devices work with data streams. You can only read characters from or write characters to character devices, as previously demonstrated with /dev/null.

 loc 1380 - Character devices work with data streams. You can only read characters from or write characters to character devices, as previously demonstrated with /dev/null. Character devices don’t have a size; when you read from or write to one, the kernel usually performs a read or write operation on the device.

 loc 1380 - Character devices work with data streams. You can only read characters from or write characters to character devices, as previously demonstrated with /dev/null. Character devices don’t have a size; when you read from or write to one, the kernel usually performs a read or write operation on the device. Printers directly attached to your computer are represented by character devices. It’s important to note that during character device interaction, the kernel cannot back up and reexamine the data stream after it has passed data to a device or process. Pipe device Named pipes are like character devices, with another process at the other end of the I/O stream instead of a kernel driver. Socket device Sockets are special-purpose interfaces that are frequently used for interprocess communication. They’re often found outside of the /dev directory. Socket files represent Unix domain sockets; you’ll learn more about those in Chapter 10. The numbers before the dates in the first two lines of Example 3-1 are the major and minor device numbers that help the kernel identify the device. Similar devices usually have the same major number, such as sda3 and sdb1 (both of which are hard disk partitions).

 loc 1386 - Named pipes are like character devices, with another process at the

 loc 1386 - Named pipes are like character devices, with another process at the other end of the I/O stream instead of a kernel driver.

 loc 1389 - Sockets are special-purpose interfaces that are frequently used for interprocess communication. They’re often found outside of the /dev directory.

 loc 1391 - The numbers before the dates in the first two lines of Example 3-1 are the major and minor device numbers that help the kernel identify the device. Similar devices usually have the same major number, such as sda3 and sdb1 (both of which are hard disk partitions).

 loc 1396 - Not all devices have device files because the block and character device I/O interfaces are not appropriate in all cases. For example, network interfaces don’t have device files.

 loc 1501 - Most hard disks attached to current Linux systems correspond to device names with an sd prefix, such as /dev/sda, /dev/sdb, and so on. These devices represent entire disks; the kernel makes separate device files, such as /dev/sda1 and /dev/sda2, for the partitions on a disk.

 loc 1509 - To list the SCSI devices on your system, use a utility that walks the device paths provided by sysfs. One of the most succinct tools is lsscsi.

 loc 1548 - The /dev/tty device is the controlling terminal of the current process. If a program is currently reading from and writing to a terminal, this device is a synonym for that terminal. A process does not need to be attached to a terminal.

 loc 1592 - Some rudimentary operations are possible with the OSS dsp and audio devices. For example, the computer plays any WAV file that you send to /dev/dsp. However, the hardware may not do what you expect due to frequency mismatches.

 loc 1596 - Linux sound is a messy subject due to the many layers involved.

 loc 4983 - computer transmits data over a network in small chunks called packets, which consist of two parts: a header and a payload. The header contains identifying information such as the origin/destination hosts and basic protocol. The payload, on the other hand, is the actual application data that the computer wants to send (for example, HTML or image data).

 loc 4983 - chunks called packets, which consist of two parts: a header and a payload. The header contains identifying information such as the origin/destination hosts and basic protocol. The payload, on the other hand, is the actual application data that the computer wants to send (for example, HTML or image data).

 loc 4983 - A computer transmits data over a network in small chunks called packets, which consist of two parts: a header and a payload. The header contains identifying information such as the origin/destination hosts and basic protocol. The payload, on the other hand, is the actual application data that the computer wants to send (for example, HTML or image data).

 loc 4996 - Common application layer protocols include Hypertext Transfer Protocol (HTTP, used for the Web), Secure Socket Layer (SSL), and File Transfer Protocol (FTP).

 loc 5000 - Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) are the most common transport layer protocols. The transport layer is also sometimes called the protocol layer.

 loc 5003 - Network or Internet layer. Defines how to move packets from a source host to a destination host. The particular packet transit rule set for the Internet is known as Internet Protocol (IP).

 loc 5079 - You define a subnet with two pieces: a network prefix and a subnet mask (such as the one in the output of ifconfig in the previous section). Let’s say you want to create a subnet containing the IP addresses between 10.23.2.1 and 10.23.2.254. The network prefix is the part that is common to all addresses in the subnet; in this example, it’s 10.23.2.0, and the subnet mask is 255.255.255.0.

 loc 5084 - The mask marks the bit locations in an IP address that are common to the subnet.

 loc 5098 - Classless Inter-Domain Routing (CIDR)

 loc 5101 - The CIDR notation identifies the subnet mask by the number of leading 1s in the subnet mask.

 loc 5125 - This host is connected to a local network of 10.23.2.0/24 and can directly reach hosts on that network. To reach hosts on the rest of the Internet, it must communicate through the router at 10.23.2.1. How does the Linux kernel distinguish between these two different kinds of destinations? It uses a destination configuration called a routing table to determine its routing behavior. To show the routing table, use the route -n command.

 loc 5144 - This is where CIDR network form comes in particularly handy: 10.23.2.0/24 matches, and its prefix is 24 bits long; 0.0.0.0/0 also matches, but its prefix is 0 bits long (that is, it has no prefix), so the rule for 10.23.2.0/24 takes priority.

 loc 5164 - ping (see http://ftp.arl.mil/~mike/ping.html) is one of the most basic network debugging tools. It sends ICMP echo request packets to a host that ask a recipient host to return the packet to the sender.

 loc 5189 - Use traceroute host to see the path your packets take to a remote host. (traceroute -n host will disable hostname lookups.)

 loc 5198 - The output from traceroute can be inconsistent. For example, the replies may time out at a certain step, only to “reappear” in later steps. The reason is usually that the router at that step refused to return the debugging output that traceroute wants but routers in later steps were happy to return the output.

 loc 5201 - priority to the debugging traffic than it does to normal traffic.

 loc 5205 - To find the IP address behind a domain name, use the host command:

 loc 5222 - All devices on an Ethernet network have a Media Access Control (MAC) address, sometimes called a hardware address. This address is independent of a host’s IP address, and it is unique to the host’s Ethernet network (but not necessarily a larger software network such as the Internet).

 loc 5224 - Devices on an Ethernet network send messages in frames, which are wrappers around the data sent. A frame contains the origin and destination MAC addresses.

 loc 5229 - By convention, each Ethernet network is also usually an Internet subnet.

 loc 5229 - By convention, each Ethernet network is also usually an Internet subnet. Even though a frame can’t leave one physical network, a router can take the data out of a frame, repackage it, and send it to a host on a different physical network, which is exactly what happens on the Internet.

 loc 5233 - The Linux kernel maintains its own division between the two layers and provides communication standards for linking them called a (kernel) network interface. When you configure a network interface, you link the IP address settings from the Internet side with the hardware identification on the physical device side. Network interfaces have names that usually indicate the kind of hardware underneath, such as eth0 (the first Ethernet card in the computer) and wlan0 (a wireless interface).

 loc 5250 - Although ifconfig shows some hardware information (in this case, even some low-level device settings such as the interrupt and memory used), it’s designed primarily for viewing and configuring the software layers attached to the interfaces. To dig deeper into the hardware and physical layer behind a network interface, use something like the ethtool command to display or change the settings on Ethernet cards.

 loc 5265 - To manually set the IP address and netmask for a kernel network interface, you’d do this: # ifconfig interface address netmask mask Here, interface is the name of the interface, such as eth0.

 loc 5270 - When the interface was up, you’d be ready to add routes, which was typically just a matter of setting the default gateway, like this: # route add default gw gw-address The gw-address parameter is the IP address of your default gateway; it must be an address in a locally connected subnet defined by the address and mask settings of one of your network interfaces.

 loc 5295 - There have been many attempts in Linux to standardize configuration files for boot-time networking. The tools ifup and ifdown do so—for example, a boot script can (in theory) run ifup eth0 to run the correct ifconfig and route commands for the eth0 interface. Unfortunately, different distributions have completely different implementations of ifup and ifdown, and as a result, their configuration files are also completely different.

 loc 5334 - NetworkManager maintains two basic levels of configuration. The first is a collection of information about available hardware devices, which it normally collects from the kernel and maintains by monitoring udev over the Desktop Bus (D-Bus). The second configuration level is a more specific list of connections: hardware devices and additional physical and network layer configuration parameters.

 loc 5341 - Upon startup, NetworkManager gathers all available network device information, searches its list of connections, and then decides to try to activate one. Here’s how it makes that decision for Ethernet interfaces: If a wired connection is available, try to connect using it. Otherwise, try the wireless connections. Scan the list of available wireless networks. If a network is available that you’ve previously connected to, NetworkManager will try it again. If more than one previously connected wireless networks are available, select the most recently connected.

 loc 5354 - For a very quick summary of your current connection status, use the nm-tool command with no arguments. You’ll get a list of interfaces and configuration parameters. In some ways, this is like ifconfig except that there’s more detail, especially when viewing wireless connections. To control NetworkManager from the command line, use the nmcli command. This is a somewhat extensive command. See the nmcli(1) manual page for more information. Finally, the utility nm-online will tell you whether the network is up or down. If the network is up, the command returns zero as its exit code; it’s nonzero otherwise.

 loc 5362 - The general configuration directory for NetworkManager is usually /etc/NetworkManager, and there are several different kinds of configuration. The general configuration file is NetworkManager.conf.

 loc 5371 - For the most part, you won’t need to change NetworkManager.conf because the more specific configuration options are found in other files.

 loc 5442 - many machines (and routers, if acting as name servers) run an intermediate daemon to intercept name server requests and return a cached answer to name service requests if possible; otherwise, requests go to a real name server. Two of the most

 loc 5442 - many machines (and routers, if acting as name servers) run an intermediate daemon to intercept name server requests and return a cached answer to name service requests if possible; otherwise, requests go to a real name server. Two of the most common such daemons for Linux are dnsmasq and nscd.

 loc 5454 - you set up a network appliance on your network, you’ll want to be able to call it by name immediately. This is part of the idea behind zero-configuration name service systems such as Multicast DNS (mDNS) and Simple Service Discovery Protocol (SSDP).

 loc 5454 - example, if you set up a network appliance on your network, you’ll want to be able to call it by name immediately. This is part of the idea behind zero-configuration name service systems such as Multicast DNS (mDNS) and Simple Service Discovery Protocol (SSDP).

 loc 5454 - if you set up a network appliance on your network, you’ll want to be able to call it by name immediately. This is part of the idea behind zero-configuration name service systems such as Multicast DNS (mDNS) and Simple Service Discovery Protocol (SSDP).

 loc 5469 - the general rule of thumb is that if a particular host has a DNS entry, it has no place in /etc/hosts.

 loc 5469 - the general rule of thumb is that if a particular host has a DNS entry, it has no place in /etc/hosts. (The

 loc 5497 - TCP provides for multiple network applications on one machine by means of network ports.

 loc 5499 - When using TCP, an application opens a connection (not to be confused with NetworkManager connections) between one port on its own machine and a port on a remote host. For example, an application such as a web browser could open a connection between port 36406 on its own machine and port 80 on a remote host.

 loc 5503 - by using the pair of IP addresses and port numbers. To view the connections currently open on your machine, use netstat.

 loc 5503 - You can identify a connection by using the pair of IP addresses and port numbers. To view the connections currently open on your machine, use netstat.

 loc 5544 - How do you know if a port is a well-known port? There’s no single way to tell, but one good place to start is to look in /etc/services, which translates well-known port numbers into names.

 loc 5744 - In Linux, you create firewall rules in a series known as a chain. A set of chains makes up a table. As a packet moves through the various parts of the Linux networking subsystem, the kernel applies the rules in certain chains to the packets.

 loc 5747 - All of these data structures are maintained by the kernel. The whole system is called iptables, with an iptables user-space command to create and manipulate the rules.

 loc 5752 - you’ll normally work primarily with a single table named filter that controls basic packet flow. There are three basic chains in the filter table: INPUT for incoming packets, OUTPUT for outgoing packets, and FORWARD for routed packets.

 loc 5907 - Although it’s possible to configure wireless networking to have hosts talk directly to each other, most wireless networks are managed by one or more access points that all traffic goes through.

 loc 6481 - On Unix systems, a process uses a socket to identify when and how it’s talking to the network. Sockets are the interface that processes use to access the network through the kernel; they represent the boundary between user space and kernel space. They’re often also used for interprocess communication (IPC).

 loc 6510 - It’s important to remember that a Unix domain socket is not a network socket, and there’s no network behind one.

 loc 6510 - It’s important to remember that a Unix domain socket is not a network socket, and there’s no network behind one. You don’t even need networking to be configured to use one.

 loc 6515 - Developers like Unix domain sockets for IPC for two reasons. First, they allow developers the option to use special socket files in the filesystem to control access, so any process that doesn’t have access to a socket file can’t use it. And because there’s no interaction with the network, it’s simpler and less prone to conventional network intrusion.

 loc 6523 - For example, the MySQL database server mysqld can accept client connections from remote hosts, but it usually also offers a Unix domain socket at /var/run/mysqld/mysqld.sock.

