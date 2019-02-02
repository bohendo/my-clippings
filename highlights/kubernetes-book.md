
---
#  Kubernetes Book
## by Nigel Poulton
---

 - loc 213 - A Kubernetes master is a collection of small services that make up the control plane of the cluster.

 - loc 213 - A Kubernetes master is a collection of small services that make up the control plane of the cluster. The simplest (and most common) setups run all the master services on a single host. However, multi-master HA is becoming more and more popular, and is a must have for production environments.

 - loc 218 - It’s also considered a good practice not to run application workloads on the master.

 - loc 220 - The API Server (apiserver) is the frontend into the Kubernetes control plane. It exposes a RESTful API that preferentially consumes JSON. We POST manifest files to it, these get validated, and the work they define gets deployed to the cluster.

 - loc 223 - If the API Server is the brains of the cluster, the cluster store is its memory. The config and state of the cluster gets persistently stored in the cluster store, which is the only stateful component of the cluster and is vital to its operation - no cluster store, no cluster!

 - loc 306 - The Pod itself doesn’t actually run anything, it’s just a sandbox to run containers in.

 - loc 319 - Pods are also the minimum unit of scaling in Kubernetes. If you need to scale your app, you do so by adding or removing Pods.

 - loc 320 - You do not scale by adding more of the same containers to an existing Pod!

 - loc 346 - Services provide a reliable networking endpoint for a set of Pods.

 - loc 393 - Play with Kubernetes (PWK) is a web-based Kubernetes playground that you can use for free. All you need is a web browser and an internet connection. It is the fastest and easiest way to get your hands on Kubernetes. Let’s see what it looks like. Point your browser at http://play-with-k8s.com

 - loc 395 - Point your browser at http://play-with-k8s.com

 - loc 469 - Minikube is great if you’re a developer and need a local Kubernetes development environment on your laptop. What it’s not great for is production. You’ve been warned!

 - loc 825 - Virtualization does VM’s, Docker does containers, and Kubernetes does Pods!

 - loc 827 - and a VM. They’re bigger, and arguably more high level than a container, but they’re a lot smaller than a VM.

 - loc 828 - a Pod is just a shared execution environment for one or more containers.

 - loc 845 - a manifest file and then POST that manifest file to the Kubernetes API server.

 - loc 845 - To deploy a Pod to a Kubernetes cluster we define it in a manifest file and then POST that manifest file to the Kubernetes API server.

 - loc 865 - All containers in a Pod have access to the same volumes, the same memory, the same IPC sockets and more. Technically speaking, the Pod (pause container) holds all the namespaces, any containers in the Pod inherit and share these Pod namespaces.

 - loc 872 - Intra-pod communication - where two containers in the same Pod need to communicate - can happen via the Pod’s localhost interface.

 - loc 873 - same Pod need to communicate - can happen via the Pod’s localhost interface.

 - loc 879 - At a high level, Control Groups (cgroups) are what stop individual containers from consuming all of the available CPU, RAM and IOPS on a node.

 - loc 886 - you can never have a situation where you have a multi-container Pod with one of its containers up and accessible but the other container in a failed state!

 - loc 889 - you can’t have part of a Pod on one node and another part of it on another node.

 - loc 896 - If a Pod fails, it is not rescheduled! For this reason, we rarely deploy them directly. It is far more common to deploy them via higher-level constructs such as ReplicaSets, DaemonSets, and Deployments, which reschedule them when they fail.

 - loc 897 - deploy them directly. It is far more common to deploy them via higher-level constructs such as ReplicaSets, DaemonSets, and Deployments, which reschedule them when they fail.

 - loc 987 - The -o yaml and -o json flags take things to the next level! Both return full copies of the Pod manifest from the cluster store.

 - loc 1020 - Another great Kubernetes introspection command is kubectl describe. This provides a nicely formatted, multi-line overview of the Pod. It even includes some important Pod lifecycle related events.

 - loc 1103 - You can see the ordering and names of containers in a Pod with the kubectl describe pods command.

 - loc 1104 - One other command for introspecting Pods is the kubectl logs command. Like other Pod-related commands, if you don’t specify a container by name, it will execute against the first container in the Pod. The format of the command is kubectl logs <pod>.

 - loc 1121 - More often than not, you’re going to deploy your applications via Deployments rather than ReplicaSets. However, Deployments build on top of ReplicaSets,

 - loc 1131 - single ReplicaSet cannot manage more than one type of Pod.

 - loc 1131 - To manage these three Pods, you’ll need three ReplicaSets. That’s because a single ReplicaSet cannot manage more than one type of Pod.

 - loc 1235 - When a new ReplicaSet starts managing an existing Pod, we say the ReplicaSet has adopted the Pods. Another example of the power of loose coupling is the ability to delete a ReplicaSet without deleting the Pods it’s managing.

 - loc 1316 - You need to be very careful when creating label selectors. Kubernetes does not check for clashes with label selectors in use by other objects (existing ReplicaSets, Deployments etc.). This means it is possible to have more than one ReplicaSet with the same label selector. In this scenario, the two ReplicaSets will fight over managing the Pods. You do not want to go there!

 - loc 1518 - Pods and Services are loosely coupled via labels and label selectors. This is the same technology and principle that links Pods with ReplicaSets.

 - loc 1522 - For a Service to match a set of Pods, and therefore provide stable networking and load-balancing, it only needs to match some of the Pods labels. However, for a Pod to match a Service, the Pod must match all of the values in the Service’s label selector.

 - loc 1571 - Each Service that is created automatically gets an associated Endpoint object. This Endpoint object is a dynamic list of all of the Pods that match the Service’s label selector.

 - loc 1584 - The Service object has a reliable port mapped to every node in the cluster – the port that the Service uses is the same on every node. This means that traffic from outside of the cluster can hit any node on that port and get through to the application (Pods).

 - loc 1704 - ClusterIP. This is the default option, and gives the Service a stable IP address internally within the cluster. It will not make the Service available outside of the cluster.

 - loc 1706 - NodePort. This builds on top of ClusterIP and adds a cluster-wide TCP or UDP port. It makes the Service available outside of the cluster on this port.

 - loc 1707 - LoadBalancer. This builds on top of NodePort and integrates with cloud-native load-balancers.

 - loc 1813 - Deployments manage ReplicaSets, and ReplicaSets manage Pods.

 - loc 1826 - When we need to push an update, we commit the changes to the same Deployment manifest file and rePOST it to the API server. In the background, Kubernetes creates a new ReplicaSet (now we have two) and winds the old one down at the same time that it winds the new one up.

 - loc 2003 - A moment ago, we used kubectl apply to perform the rolling update on a Deployment. We used the --record flag so that Kubernetes would maintain a revision history of the Deployment. The following kubectl rollout history command shows the Deployment with two revisions.

