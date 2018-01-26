
---
#  Docker Deep Dive
## by Nigel Poulton
---

 - loc 108 - brand new oversized server every time the business asked for a

 - loc 112 - The fact that every VM requires its own dedicated OS is a major flaw. Every OS consumes CPU, RAM and storage that could otherwise be used to power more applications.

 - loc 138 - The core Windows technologies required to implement containers are collectively referred to as Windows Containers. The user-space tooling to work with these Windows Containers is Docker. This makes the Docker experience on Windows almost exactly the same as Docker on Linux.

 - loc 145 - At the time of writing this revision of the book, it is possible to run Linux containers on Windows machines... This is an area that is developing fast and you should consult the Docker documentation for the latest.

 - loc 145 - At the time of writing this revision of the book, it is possible to run Linux containers on Windows machines. For example, Docker for Windows (a product offering from Docker, Inc. designed for Windows 10) can switch modes between Windows containers and Linux containers. This is an area that is developing fast and you should consult the Docker documentation for the latest.

 - loc 149 - There is currently no such thing as Mac containers. However, you can run Linux containers on your Mac using the Docker for Mac product. This works by seamlessly running your containers inside of a lightweight Linux VM running on your Mac.

 - loc 154 - Following the success of VMware and hypervisors came a newer more efficient and lightweight virtualization technology called containers. But containers were initially hard to implement and were only found in the data centers of web giants that had Linux kernel engineers on staff. Then along came Docker Inc. and suddenly container virtualization technologies were available to the masses.

 - loc 154 - But as good as VMware and the VM model is, it’s not perfect. Following the success of VMware and hypervisors came a newer more efficient and lightweight virtualization technology called containers. But containers were initially hard to implement and were only found in the data centers of web giants that had Linux kernel engineers on staff. Then along came Docker Inc. and suddenly container virtualization technologies were available to the masses.

 - loc 186 - In the same way that ESXi is the core hypervisor technology that runs virtual machines, the Docker Engine is the core container runtime that runs containers.

 - loc 219 - One of the core philosophies at Docker, Inc. is often referred to as Batteries included but removable. This is a way of saying you can swap out a lot of the native Docker stuff and replace it with stuff from 3rd parties. A good example of this is the networking stack.

 - loc 219 - One of the core philosophies at Docker, Inc. is often referred to as Batteries included but removable. This is a way of saying you can swap out a lot of the native Docker stuff and replace it with stuff from 3rd parties. A good example of this is the networking stack. The core Docker product ships with built-in networking. But the networking stack is pluggable meaning you can rip out the native Docker networking and replace it with something else from a 3rd party. Plenty of people do that.

 - loc 219 - One of the core philosophies at Docker, Inc. is often referred to as Batteries included but removable. This is a way of saying you can swap out a lot of the native Docker stuff and replace it with stuff from 3rd parties.

 - loc 226 - To cut a long story short, the native Docker batteries are still removable, there’s just less and less reason to need to remove them.

 - loc 228 - You’ll often hear people use terms like co-opetition (a balance of co-operation and competition) and frenemy (a mix of a friend and an enemy) when talking about the container ecosystem. This is great! Healthy competition is the mother of innovation!

 - loc 230 - The Open Container Initiative (OCI) is a relatively new governance council responsible for standardizing the most fundamental components of container infrastructure such as image format and container runtime

 - loc 230 - The Open Container Initiative (OCI)

 - loc 233 - The OCI is a relatively new governance council responsible for standardizing the most fundamental components of container infrastructure such as image format and container runtime

 - loc 238 - The TLDR of this history according to Nigel is that a company called CoreOS didn’t like the way Docker did certain things. So they did something about it! They created a new open standard called appc that defined things like image format and container runtime.

 - loc 243 - While competition is usually a good thing, competing standards is usually not. They cause confusion and slowdown user adoption. Not good for anybody. With this in mind, everybody did their best to act like adults and came together to form the OCI - a lightweight agile council to govern container standards.

 - loc 243 - though, this threatened to fracture the ecosystem

 - loc 243 - ecosystem and present users and customers with a dilemma. While competition is usually a good thing, competing standards is usually not. They cause confusion and slowdown user adoption.

 - loc 243 - While competition is usually a good thing, competing standards is usually not. They cause confusion and slowdown user adoption. Not good for anybody.

 - loc 422 - It is best practice to only use non-root users when working with Docker. To do this you need to add your non-root users to the local docker Unix group on your Linux machine.

 - loc 501 - In a default Linux installation, the client talks to the daemon via a local IPC/Unix socket at /var/run/docker.sock.

 - loc 501 - In a default Linux installation, the client talks to the daemon via a local IPC/Unix socket at /var/run/docker.sock. On

 - loc 503 - You can test that the client and daemon are running and can talk to each other with the docker version command... If you get a response back from the Client and Server components you should be good to go.

 - loc 503 - You can test that the client and daemon are running and can talk to each other with the docker version command.

 - loc 514 - If you get a response back from the Client and Server components you should be good to go.

 - loc 517 - A good way to think of a Docker image is as an object that contains an OS filesystem and an application. If you work in operations, it’s like a virtual machine template. A virtual machine template is essentially a stopped virtual machine. In the Docker world, an image is effectively a stopped container. If you’re a developer, you can think of an image as a class.

 - loc 517 - A good way to think of a Docker image is as an object that contains an OS filesystem and an application.

 - loc 539 - If you pull an application container such as nginx or microsoft/iis, you will get an image that contains some OS as well as the code to run either nginx or IIS.

 - loc 654 - In a previous step you pressed Ctrl-PQ to exit from the container. Doing this from inside of a container will exit you from the container without killing it.

 - loc 775 - The Docker engine is modular in design with many swappable components. Where possible, these are based on open-standards outlined by the Open Container Initiative (OCI).

 - loc 792 - their own tool called libcontainer as a replacement for LXC. The goal of libcontainer was to be a platform-agnostic tool that provided Docker with access to the fundamental container building-blocks that exist inside the OS. Libcontainer replaced LXC as the default execution driver in Docker 0.9.

 - loc 793 - The goal of libcontainer was to be a platform-agnostic tool that provided Docker with access to the fundamental container building-blocks that exist inside the OS. Libcontainer replaced LXC as the default execution driver in Docker 0.9.

 - loc 801 - This work of breaking apart and re-factoring the Docker engine is an ongoing process. However, it has already seen all of the container execution and container runtime code entirely removed from the daemon and refactored into small, specialized tools.

 - loc 813 - the containerd component of the Docker Engine makes sure Docker images are presented to runc as valid OCI bundles.

 - loc 817 - runc is the reference implementation of the OCI container-runtime-spec.

 - loc 818 - runc is small. It’s effectively a lightweight CLI that wraps around libcontainer. It has a single purpose in life - to create containers. And it’s damn good at it. And fast!

 - loc 818 - runc is small. It’s effectively a lightweight CLI that wraps around libcontainer. It has a single purpose in life - to create containers. And it’s damn good at it. And fast! We often refer to runc as a container runtime.

 - loc 824 - It’s helpful to think of containerd as a container supervisor - the component that is responsible for container lifecycle operations such as; starting and stopping containers, pausing and un-pausing them, and destroying them. Like runc, containerd is small, lightweight, and designed for a single task in life - containerd is only interested container lifecycle operations.

 - loc 833 - When you type commands like this into the Docker CLI, the Docker client converts them into the appropriate API payload and POSTs them to the correct API endpoint. The API is implemented in the daemon. It is the same rich, versioned, REST API that has become a hallmark of Docker and is accepted in the industry as the de facto container API.

 - loc 851 - The shim is integral to the implementation of daemonless containers (the thing we just mentioned about decoupling running containers from the daemon for things like upgrading the daemon without killing containers). We mentioned earlier that containerd uses runc to create new containers. In fact, it forks a new instance of runc for every container it creates. However, once each container is created, its parent runc process exits. This means we can run hundreds of containers without having to run hundreds of runc instances. Once a container’s parent runc process exits, the associated containerd-shim process becomes the container’s parent process.

 - loc 887 - Images are made up of multiple layers that get stacked on top of each other and represented as a single object. Inside of the image is a cut-down operating system (OS) and all of the files and dependencies required to run an application.

 - loc 887 - Images are made up of multiple layers that get stacked on top of each other and represented as a single object. Inside of the image is a cut-down operating system (OS) and all of the files and dependencies required to run an application. Because containers are intended to be fast and lightweight, images tend to be small.

 - loc 893 - images are considered build-time constructs whereas containers are run-time constructs.

 - loc 906 - Docker images do not ship with 6 different shells for you to choose from - they usually ship with a single minimalist shell, or no shell at all. They also don’t contain a kernel - all containers running on a Docker host share access to the host’s kernel. For these reasons, we sometimes say images contain just enough operating system (usually just OS-related files and filesystem objects).

 - loc 911 - The official Alpine Linux Docker image is about 4MB in size and is an extreme example of how small Docker images can be.

 - loc 922 - The process of getting images onto a Docker host is called pulling.

 - loc 951 - Docker images are stored in image registries. The most common registry is Docker Hub (https://hub.docker.com)

 - loc 951 - Docker images are stored in image registries. The most common registry is Docker Hub (https://hub.docker.com

 - loc 954 - Image registries contain multiple image repositories. In turn, image repositories can contain multiple images.

 - loc 964 - Most of the popular operating systems and applications have their own official repositories on Docker Hub. They’re easy to spot because they live at the top level of the Docker Hub namespace.

 - loc 992 - If you do not specify an image tag after the repository name, Docker will assume you are referring to the image tagged as latest.

 - loc 992 - you do not specify an image tag after the repository name, Docker will assume you are referring to the image tagged as latest.

 - loc 993 - Just because an image is tagged as latest does not guarantee it is the most recent image in a repository! For example, the most recent image in the alpine repository is usually tagged as edge.

 - loc 1006 - If you want to pull images from 3rd party registries (not Docker Hub), you need to prepend the repository name with the DNS name of the registry. For example, if the image in the example above was in the Google Container Registry (GCR) you’d need to add gcr.io before the repository name as follows - docker pull gcr.io/nigelpoulton/tu-demo:v2

 - loc 1037 - A Docker image is just a bunch of loosely-connected read-only layers.

 - loc 1046 - Each line in the output above that ends with “Pull complete” represents a layer in the image that was pulled.

 - loc 1048 - Another way to see the layers of an image is to inspect the image with the docker image inspect command.

 - loc 1116 - You push the fixed image back to its repository with the same tag as the vulnerable image! How are you going to know which of your production systems are running the vulnerable image and which are running the patched image? Both images have the same tag! This is where image digests come to the rescue.

 - loc 1116 - you push the fixed image back to its repository with the same tag as the vulnerable image! How are you going to know which of your production systems are running the vulnerable image and which are running the patched image? Both images have the same tag! This is where image digests come to the rescue.

 - loc 1144 - The image itself is really just a configuration object that lists the layers and as well as some metadata. The layers that make up an image are fully independent and have no concept of being part of a collective image. Each image is identified by a crypto ID that is a hash of the config object. Each layer is identified by a crypto ID that is a hash of the content it contains. This means that changing the contents of the image, or any of its layers, will cause the associated crypto hashes to change. As a result, images and layers are immutable.

 - loc 1155 - Each layer also gets something called a distribution hash. This is a hash of the compressed version of the layer. When a layer is pushed and pulled from the registry, its distribution hash is included, and this is what is used to verify that the layer arrived without being tampered with.

 - loc 1155 - each layer also gets something called a distribution hash. This is a hash of the compressed version of the layer. When a layer is pushed and pulled from the registry, its distribution hash is included, and this is what is used to verify that the layer arrived without being tampered with.

 - loc 1161 - The Registry API supports a fat manifest as well as an image manifest. Fat manifests list the architectures supported by a particular image, whereas image manifests list the layers that make up a particular image. Let’s look at a quick example. Assume you are running Docker on Linux x64. When you pull an image from Docker hub, your Docker client makes the relevant API requests to the Docker Registry API running on Docker Hub. If a fat manifest exists for that image, it will be parsed to see if an entry exists for Linux on x64. If it exists, the image manifest for that image is retrieved and parsed for the actual layers that make up the image.

 - loc 1161 - the Registry API supports a fat manifest as well as an image manifest. Fat manifests list the architectures supported by a particular image, whereas image manifests list the layers that make up a particular image. Let’s look at a quick example. Assume you are running Docker on Linux x64. When you pull an image from Docker hub, your Docker client makes the relevant API requests to the Docker Registry API running on Docker Hub. If a fat manifest exists for that image, it will be parsed to see if an entry exists for Linux on x64. If it exists, the image manifest for that image is retrieved and parsed for the actual layers that make up the image.

 - loc 1203 - docker image inspect is a thing of beauty! It gives you all of the glorious details of image - layer data and metadata.

 - loc 1227 - Containers run until the program they are executing exits.

 - loc 1262 - At a high level we can say that hypervisors perform hardware virtualization - they carve up physical hardware resources into virtual versions. On the other hand, containers perform OS virtualization - they carve up OS resources into virtual versions.

 - loc 1426 - When we started the Ubuntu container in the previous section we told it to run the Bash shell (/bin/bash). This makes the Bash shell the one and only process running inside of the container. You can see this by running ps -elf from inside the container.

 - loc 1452 - A container cannot exist without a running process - killing the Bash shell would kill the container’s only process, resulting in the container also being killed.

 - loc 1452 - a container cannot exist without a running process - killing the Bash shell would kill the container’s only process, resulting in the container also being killed.

 - loc 1452 - if you type exit to exit the Bash shell, the container will also exit (terminate). The reason for this is that a container cannot exist without a running process - killing the Bash shell would kill the container’s only process, resulting in the container also being killed.

 - loc 1533 - Stopping a container is like stopping a virtual machine. Although it’s not currently running, its entire configuration and contents still exist on the filesystem of the Docker host and it can be restarted at any time.

 - loc 1561 - I should point out that volumes are the preferred way to store persistent data in containers.

 - loc 1587 - Docker container stop sends a SIGTERM signal to the process with PID 1 inside of the container. As we just said, this gives the process a chance to clean things up and gracefully shut itself down. If it doesn’t exit within 10 seconds it will receive a SIGKILL. This is effectively the bullet to the head. But hey, it got 10 seconds to sort itself out first! docker container rm <container> -f doesn’t bother asking nicely with a SIGTERM, it just goes straight to the SIGKILL.

 - loc 1587 - docker container stop sends a SIGTERM signal to the process with PID 1 inside of the container. As we just said, this gives the process a chance to clean things up and gracefully shut itself down. If it doesn’t exit within 10 seconds it will receive a SIGKILL. This is effectively the bullet to the head. But hey, it got 10 seconds to sort itself out first! docker container rm <container> -f doesn’t bother asking nicely with a SIGTERM, it just goes straight to the SIGKILL.

 - loc 1618 - port mappings are expressed as host-port:container-port.

 - loc 1689 - The process of taking an application and configuring it to run as a container is called “containerizing”. Sometimes we call it “Dockerizing”.

 - loc 1735 - The directory that contains your application code is referred to as the build context. It’s a common practice to keep your Dockerfile in the root directory of the build context.

 - loc 1744 - Do not underestimate the impact of the Dockerfile from a documentation perspective. It has the ability to bridge the gap between dev and ops! It also has the power to speed up on-boarding of new developers etc. This is because the file accurately describes the application and its dependencies in an easy-to-read format.

 - loc 1755 - Labels are simple key-value pairs and are an excellent way of adding custom metadata to an image.

 - loc 1767 - Then the RUN npm install instruction uses npm to install application dependencies listed in package.json. It runs within the context of the WORKDIR set in the previous instruction, and installs the dependencies as a new layer in the image.

 - loc 1770 - The application exposes a web service on TCP port 8080, so the Dockerfile documents this with the EXPOSE 8080 instruction. This is added as image metadata and not an image layer.

 - loc 1775 - The period (.) at the end of the command tells Docker to use the shell’s current working directory as the build context.

 - loc 1814 - Comment lines in a Dockerfile start with the # character. All non-comment lines are Instructions. Instructions take the format INSTRUCTION argument. Instruction names are not case sensitive, but it is normal practice to write them in UPPERCASE.

 - loc 1817 - The `docker image build` command parses the Dockerfile one-line-at-a-time starting from the top. Some Instructions create new layers, whereas others just add metadata to the image. Examples of instructions that create new layers are FROM, RUN, and COPY. Examples of instructions that create metadata include EXPSOE, WORKDIR, ENV, and ENTRYPOINT. The basic premise is this - if an instruction is adding content such as files and programs to the image, it will create a new layer. If it is adding instructions on how to build the image and run the application, it will create metadata.

 - loc 1817 - The docker image build command parses the Dockerfile one-line-at-a-time starting from the top. Some Instructions create new layers, whereas others just add metadata to the image. Examples of instructions that create new layers are FROM, RUN, and COPY. Examples of instructions that create metadata include EXPSOE, WORKDIR, ENV, and ENTRYPOINT. The basic premise is this - if an instruction is adding content such as files and programs to the image, it will create a new layer. If it is adding instructions on how to build the image and run the application, it will create metadata.

 - loc 1822 - You can view the instructions that were used to build the image with the docker image history command.

 - loc 1898 - The important things to note are that the COPY --from instructions only copy production-related application code from the images built by the previous stages. They do not copy across build artefacts that are not needed for production.

 - loc 1900 - production.

 - loc 1950 - Multi-stage builds were new with Docker 17.05 and are an excellent feature for building small production-worthy images.

 - loc 2008 - A swarm consists of one or more nodes. These can be physical servers, VMs, or cloud instances. The only requirement is that all nodes in a swarm can communicate with each other over reliable networks. Nodes are then configured as managers or workers. Managers look after the state of the cluster and are in charge of dispatching tasks to workers. Workers accept tasks from managers and execute them.

 - loc 2008 - A swarm consists of one or more nodes. These can be physical servers, VMs, or cloud instances. The only requirement is that all nodes in a swarm can communicate with each other over reliable networks.

 - loc 2009 - Nodes are then configured as managers or workers. Managers look after the state of the cluster and are in charge of dispatching tasks to workers. Workers accept tasks from managers and execute them.

 - loc 2011 - When talking about tasks in the context of a swarm, we mean containers. So, when we say “managers dispatch tasks to workers”, we’re saying they dispatch container workloads. You might also hear them referred to as replicas. This might be confusing at this point, so try and remember that tasks and replicas are words that mean containers.

 - loc 2015 - At the highest level, services are the way to run tasks on a Swarm. To run a task (container) on Swarm we wrap it in a service and deploy the service. Beneath the hood, services are a declarative way of setting the desired state on the cluster.

 - loc 2018 - The configuration and state of the swarm is held in a distributed etcd database located on all managers in the swarm. It’s kept extremely up-to-date

 - loc 2021 - Something else that’s game changing about swarm mode is its approach to security. TLS is so tightly integrated that it’s not possible to build a swarm without it.

 - loc 2046 - --advertise-addr is the IP and port that other nodes should use to connect to this manager. The flag is optional, but it gives you control over which IP gets used on nodes with multiple IPs. It also gives you the chance to specify an IP address that does not exist on the node, such as a load balancer IP address. --listen-addr lets you specify which IP and port you want to listen on for swarm traffic. This will usually match the --advertise-addr, but is useful in situations where you want to restrict swarm to a particular IP on a system with multiple IPs. It’s also required in situations where the --advertise-addr refers to a remote IP address like a load balancer. I recommend you be specific and always use both flags.

 - loc 2052 - The default port that swarm mode operates on is 2377. This is entirely customizable, but Docker, Inc. are looking to register this with IANA as the official Docker Swarm port.

 - loc 2098 - It’s a pain to specify the --advertise-addr and --listen-addr flags every time you join a node to the swarm. However, it can be even more of a pain if you get the network configuration of your swarm wrong. Manually adding nodes to a swarm is unlikely to be a daily task so I think it’s worth the extra up-front effort to use the flags.

 - loc 2105 - Swarm managers have native support for high availability (H/A). This means that one or more can fail and the survivors will keep the swarm running.

 - loc 2113 - Swarm uses an implementation of the Raft consensus algorithm to power manager HA, and the following two best practices apply: Deploy an odd number of managers. Don’t deploy too many managers (3 or 5 is recommended)

 - loc 2126 - at the time of writing, the nirvana of hosting your active production applications and infrastructure across multiple cloud providers such as AWS and Azure is a bit of a daydream. Take time to make sure your managers are connected via high speed reliable networks!

 - loc 2152 - All services are constantly monitored by the swarm - the swarm runs a reconciliation loop that constantly compares the actual state of the service to the desired state. If the two states match, the world is a happy place and no further action is needed. If they don’t match, the swarm takes actions so that they do. Put another way, the swarm is constantly making sure that actual state matches desired state.

 - loc 2177 - service, use the docker service inspect command. $ docker service inspect --pretty web-fe

 - loc 2178 - docker service inspect --pretty web-fe

 - loc 2238 - An overlay network essentially creates a new layer 2 network that we can place containers on, and all containers on it will be able to communicate with each other. This works even if the Docker hosts they’re running on are on different underlying networks.

 - loc 2323 - If you run a `docker inspect --pretty` command against the service you’ll see the update parallelism and update delay settings you just used are now part of the service definition. This means future updates that you push will automatically use these settings unless you override them as part of the docker service update command.

 - loc 2323 - If you run a docker inspect --pretty command against the service you’ll see the update parallelism and update delay settings you just used are now part of the service definition. This means future updates that you push will automatically use these settings unless you override them as part of the docker service update command.

 - loc 2365 - `docker swarm join-token` reveals the commands and tokens required to join workers and managers to existing swarms.

 - loc 2365 - docker swarm join-token reveals the commands and tokens required to join workers and managers to existing swarms.

 - loc 2371 - `docker service inspect` gives very detailed information on a service. It accepts the `--pretty` flag to limit the information returned to the most important information.

 - loc 2371 - docker service inspect gives very detailed information on a service. It accepts the --pretty flag to limit the information returned to the most important information.

 - loc 2387 - Docker overlay networking - The TLDR In the real world it’s vital that containers can communicate with each other reliably and securely,

 - loc 2388 - In the real world it’s vital that containers can communicate with each other reliably and securely, even when they’re on different hosts on different networks. This is where overlay networking comes in to play. It allows you to create a flat secure layer 2 network spanning multiple hosts that containers can connect to. Containers on this network can then communicate directly.

 - loc 2474 - Run a docker network inspect to see the Subnet assigned to the overlay.

 - loc 2583 - Docker overlay networking uses VXLAN tunnels to create virtual Layer 2 overlay networks... VXLANs let you create a virtual Layer 2 network on top of an existing Layer 3 infrastructure.

 - loc 2583 - Docker overlay networking uses VXLAN tunnels to create virtual Layer 2 overlay networks.

 - loc 2585 - VXLANs let you create a virtual Layer 2 network on top of an existing Layer 3 infrastructure.

 - loc 2589 - To create the virtual Layer 2 overlay network, a VXLAN tunnel is created through the underlying Layer 3 IP infrastructure. You might hear the term underlay network used to refer to the underlying Layer 3 infrastructure. Each end of the VXLAN tunnel is terminated by a VXLAN Tunnel Endpoint (VTEP). It’s this VTEP that performs the encapsulation/de-encapsulation

 - loc 2589 - To create the virtual Layer 2 overlay network a VXLAN tunnel is created through the underlying Layer 3 IP infrastructure. You might hear the term underlay network used to refer to the underlying Layer 3 infrastructure. Each end of the VXLAN tunnel is terminated by a VXLAN Tunnel Endpoint (VTEP). It’s this VTEP that performs the encapsulation/de-encapsulation

 - loc 2591 - Each end of the VXLAN tunnel is terminated by a VXLAN Tunnel Endpoint (VTEP). It’s this VTEP that performs the encapsulation/de-encapsulation

 - loc 2596 - A network namespace is like a container, but instead of running an application it runs an isolated network stack - one that’s sandboxed from the network stack on the host itself.

 - loc 2596 - network namespace is like a container, but instead of running an application it runs an isolated network stack - one that’s sandboxed from the network stack on the host itself.

 - loc 2597 - A virtual switch (a.k.a. virtual bridge) called Br0 is created inside the network namespace. A VTEP is also created with one end plumbed into the Br0 virtual switch, and the other end plumbed into the host network stack. The end in the host network stack gets an IP address on the underlay network the host is connected to and is bound to a UDP socket on port 4789.

 - loc 2602 - Each container then gets its own virtual Ethernet (veth) adapter that is also plumbed into the local Br0 virtual switch.

 - loc 2610 - Container C1 creates the ping requests and sets the destination IP address to be the 10.0.0.4 address of C2. It sends the traffic over its veth interface which is connected to the Br0 virtual switch. The virtual switch doesn’t know where to send the packet as it doesn’t have an entry in its MAC address table (ARP table) that corresponds to the destination IP address. As a result, it floods the packet to all ports. The VTEP interface connected to Br0 knows how to forward the frame so responds with its own MAC address. This is a proxy ARP reply and results in the Br0 switch learning how to forward the packet and it updates its ARP table mapping 10.0.0.4 to the MAC address of the VTEP. Now that the Br0 switch has learned how to forward traffic to C2 all future packets for C2 will be transmitted directly to the VTEP interface. The VTEP interface knows about C2 because all newly started containers have their network details propagated to other nodes in the swarm using the network’s built-in gossip protocol.

 - loc 2610 - Container C1 creates the ping requests and sets the destination IP address to be the 10.0.0.4 address of C2. It sends the traffic over its veth interface which is connected to the Br0 virtual switch. The virtual switch doesn’t know where to send the packet as it doesn’t have an entry in its MAC address table (ARP table) that corresponds to the destination IP address. As a result, it floods the packet to all ports. The VTEP interface connected to Br0 knows how to forward the frame so responds with its own MAC address. This is a proxy ARP reply and results in the Br0 switch learning how to forward the packet and it updates its ARP table mapping 10.0.0.4 to the MAC address of the VTEP. Now that the Br0 switch has learned how to forward traffic to C2 all future packets for C2 will be transmitted directly to the VTEP interface.

 - loc 2615 - the VTEP. Now that the Br0 switch has learned how to forward traffic to C2 all future packets for C2 will be transmitted directly to the VTEP interface. The VTEP interface knows about C2 because all newly started containers have their network details propagated to other nodes in the swarm using the network’s built-in gossip protocol.

 - loc 2619 - At a fairly high level this encapsulation includes adding a VXLAN header to the Ethernet frame. The VXLAN header contains the VXLAN network ID (VNID) which is used to map frames from VLANs to VXLANs and vice versa. Each VLAN gets mapped to VNID so that on the receiving end the packet can be de-encapsulated and forwarded on to the correct VLAN. This obviously maintains network isolation. The encapsulation also wraps the frame in a IP/UDP packet with the IP address of the VTEP on node2 in the destination IP field and the UDP port 4789 socket information. This encapsulation allows the data to be sent across the underlying networks without the underlying networks having to know anything about VXLAN.

 - loc 2660 - Docker Swarm Mode is secure by default. You get all of the following with zero configuration required; cryptographic node IDs, mutual authentication, automatic CA configuration, automatic certificate rotation, encrypted cluster store, encrypted networks, and more.

 - loc 2660 - following with zero configuration required; cryptographic node IDs, mutual authentication, automatic CA configuration, automatic certificate rotation, encrypted cluster store, encrypted networks, and more.

 - loc 2694 - Docker containers are an organized collection of namespaces. Let me repeat that… A Docker container is an organized collection of namespaces. For example, every container is made up of its own pid, net, mnt, ipc, uts, and potentially user namespace.

 - loc 2694 - moment. But the most important thing to understand is that Docker containers are an organized collection of namespaces. Let me repeat that… A Docker container is an organized collection of namespaces.

 - loc 2694 - Docker containers are an organized collection of namespaces. Let me repeat that… A Docker container is an organized collection of namespaces.

 - loc 2699 - Process ID namespace: Docker uses the pid namespace to provide isolated process trees for each container. Every container gets its own process tree meaning that every container can have its own PID 1. PID namespaces also mean that a container cannot see or access to the process tree of other containers or host it’s running on.

 - loc 2699 - Process ID namespace: Docker uses the pid namespace to provide isolated process trees for each container. Every container gets its own process tree meaning that every container can have its own PID 1. PID namespaces also mean that a container cannot see or access to

 - loc 2717 - In the real world containers are isolated from each other but all share a common set of OS resources - things like CPU, RAM and disk I/O. Cgroups let us set limits on each of these so that a single container cannot use all of the CPU, RAM, or storage I/O of the Linux host.

 - loc 2717 - In the real world (not the silly hotel analogy) containers are isolated from each other but all share a common set of OS resources - things like CPU, RAM and disk I/O. Cgroups let us set limits on each of these so that a single container cannot use all of the CPU, RAM, or storage I/O of the Linux host.

 - loc 2721 - What we need is a technology that lets us pick and choose which root powers our containers need in order to run. Enter capabilities! Under the hood, the Linux root account is made up of a long list of capabilities. Some of these include: CAP_CHOWN lets you change file ownership CAP_NET_BIND_SERVICE lets you bind a socket to low numbered network ports

 - loc 2725 - Docker works with capabilities so that you can run containers as root, but strip out the root capabilities that you don’t need. For example, if the only root privilege your container needs is the ability to bind to low numbered network ports, you should start a container and drop all root capabilities, then add back the CAP_NET_BIND_SERVICE capability.

 - loc 2729 - Docker works with major Linux MAC technologies such as AppArmor and SELinux.

 - loc 2744 - Swarm Mode is the future of Docker.

 - loc 2811 - The only thing that is needed to join managers and workers to an existing Swarm is the relevant join token. For this reason, it is vital that you keep your join-tokens safe!

 - loc 2811 - Swarm join tokens The only thing that is needed to join managers and workers to an existing Swarm is the relevant join token. For this reason, it is vital that you keep your join-tokens safe! No posting them on public GitHub pages!

 - loc 2814 - Every join token is comprised of 4 distinct fields separated by dashes (-): PREFIX - VERSION - SWARM ID - TOKEN The prefix is always “SWMTKN”. The version field indicates the version of the Swarm. The Swarm ID field is a hash of the Swarm’s certificate. The token portion is the part that determines if the token can be used to join the node as a manager or worker.

 - loc 2814 - It’s worth understanding the format of the Swarm join token. Every join token is comprised of 4 distinct fields separated by dashes (-): PREFIX - VERSION - SWARM ID - TOKEN

 - loc 2820 - The following example revokes the existing manager join token and issues a new one: `docker swarm join-token --rotate manager`

 - loc 2820 - The following example revokes the existing manager join token and issues a new one. $ docker swarm join-token --rotate manager

 - loc 2826 - Join tokens are stored in the cluster config database which is encrypted by default.

 - loc 2846 - The organization O field stores the Swarm ID, the organizational unit OU field stores the nodes role in the Swarm, the canonical name CN field stores the nodes crypto ID.

 - loc 2846 - The organization O field stores the Swarm ID The organizational unit OU field stores the nodes role in the Swarm The canonical name CN field stores the nodes crypto ID.

 - loc 2861 - The new docker swarm ca sub-command can be used to manage CA related configuration. Run the command with the --help flag to see a list of things it can do.

 - loc 2934 - Docker 1.13 introduced Docker Secrets, effectively making secrets first-class citizens in the Docker ecosystem.

 - loc 2934 - Docker 1.13 introduced Docker Secrets, effectively making secrets first-class citizens in the Docker ecosystem. For example, there is a whole new docker secret sub-command dedicated to managing secrets.

 - loc 2936 - Behind the scenes secrets are encrypted at rest, encrypted in-flight, mounted in in-memory filesystems, and only available to services/containers that have been explicitly granted access to them. It’s quite a comprehensive end-to-end solution.

