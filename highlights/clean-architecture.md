
---
#  Clean Architecture
## by Uncle Bob
---

 - loc 552 - Dijkstra showed that the use of unrestrained jumps (goto statements) is harmful to program structure. As we’ll see in the chapters that follow, he replaced those jumps with the more familiar if/then/else and do/while/until constructs.

 - loc 555 - Structured programming imposes discipline on direct transfer of control.

 - loc 557 - Ole Johan Dahl and Kristen Nygaard. These two programmers noticed that the function call stack frame in the ALGOL language could be moved to a heap, thereby allowing local variables declared by a function to exist long after the function returned. The function became a constructor for a class, the local variables became instance variables, and the nested functions became methods. This led inevitably to the discovery of polymorphism through the disciplined use of function pointers.

 - loc 558 - two programmers noticed that the function call stack frame in the ALGOL language could be moved to a heap, thereby allowing local variables declared by a function to exist long after the function returned. The function became a constructor for a class, the local variables became instance variables, and the nested functions became methods. This led inevitably to the discovery of polymorphism through the disciplined use of function pointers.

 - loc 562 - Object-oriented programming imposes discipline on indirect transfer of control.

 - loc 571 - Functional programming imposes discipline upon assignment

 - loc 610 - Dijkstra discovered that certain uses of goto statements prevent modules from being decomposed recursively into smaller and smaller units, thereby preventing use of the divide-and-conquer approach necessary for reasonable proofs. Other uses of goto, however, did not have this problem. Dijkstra realized that these “good” uses of goto corresponded to simple selection and iteration control structures such as if/then/else and do/while.

 - loc 628 - In 1968, Dijkstra wrote a letter to the editor of CACM, which was published in the March issue. The title of this letter was “Go To Statement Considered Harmful.”

 - loc 665 - purposes. Of course, not all statements are provable. The statement “This is a lie” is neither true nor false. It is one of the simplest examples of a statement that is not provable. Ultimately, we can say that mathematics is the discipline of proving provable statements true. Science, in contrast, is the discipline of proving provable

 - loc 669 - Dijkstra once said, “Testing shows the presence, not the absence, of bugs.”

 - loc 672 - Software development is not a mathematical endeavor, even though it seems to manipulate mathematical constructs. Rather, software is like a science. We show correctness by failing to prove incorrectness, despite our best efforts.

 - loc 688 - object-oriented design (OO).

 - loc 696 - Some folks fall back on three magic words to explain the nature of OO: encapsulation, inheritance, and polymorphism.

 - loc 875 - OO is the ability, through the use of polymorphism, to gain absolute control over every source code dependency in the system. It allows the architect to create a plugin architecture, in which modules that contain high-level policies are independent of modules that contain low-level details. The low-level details are relegated to plugin modules that can be deployed and developed independently from the modules that contain high-level policies.

 - loc 923 - Variables in functional languages do not vary.

 - loc 935 - One of the most common compromises in regard to immutability is to segregate the application, or the services within the application, into mutable and immutable components. The immutable components perform their tasks in a purely functional way, without using any mutable variables.

 - loc 941 - Since mutating state exposes those components to all the problems of concurrency, it is common practice to use some kind of transactional memory to protect the mutable variables from concurrent updates and race conditions. Transactional memory simply treats variables in memory the same way a database treats records on disk.1 It protects those variables with a transaction- or retry-based scheme.

 - loc 961 - Architects would be wise to push as much processing as possible into the immutable components, and to drive as much code as possible out of those components that must allow mutation.

 - loc 974 - Event sourcing is a strategy wherein we store the transactions, but not the state. When state is required, we simply apply all the transactions from the beginning of time.

 - loc 974 - Event sourcing is a strategy wherein we store the transactions, but not the state. When state is required, we simply apply all the transactions from the beginning of time. Of course, we can take shortcuts. For example, we can compute and save the state every midnight. Then, when the state information is required,

 - loc 974 - Event sourcing is a strategy wherein we store the transactions, but not the state. When state is required, we simply apply all the transactions from the beginning of time. Of course, we can take shortcuts. For example, we can compute and save the state every midnight. Then, when the state information is required, we need compute only the transactions since midnight.

 - loc 1000 - architecture of the building doesn’t matter much. On the other hand, you

 - loc 1020 - SRP: The Single Responsibility Principle An active corollary to Conway’s law: The best structure for a software system is heavily influenced by the social structure of the organization that uses it so that each software module has one, and only one, reason to change.

 - loc 1021 - Conway’s law: The best structure for a software system is heavily influenced by the social structure of the organization that uses it so that each software module has one, and only one, reason to change.

 - loc 1023 - OCP: The Open-Closed Principle Bertrand Meyer made this principle famous in the 1980s. The gist is that for software systems to be easy to change, they must be designed to allow the behavior of those systems to be changed by adding new code, rather than changing existing code.

 - loc 1026 - LSP: The Liskov Substitution Principle Barbara Liskov’s famous definition of subtypes, from 1988. In short, this principle says that to build software systems from interchangeable parts, those parts must adhere to a contract that allows those parts to be substituted one for another.

 - loc 1029 - ISP: The Interface Segregation Principle This principle advises software designers to avoid depending on things that they don’t use.

 - loc 1031 - DIP: The Dependency Inversion Principle The code that implements high-level policy should not depend on the code that implements low-level details. Rather, details should depend on policies.

 - loc 1167 - Let me say that again: If component A should be protected from changes in component B, then component B should depend on component A.

 - loc 1172 - Why should the Interactor hold such a privileged position? Because it contains the business rules. The Interactor contains the highest-level policies of the application. All the other components are dealing with peripheral concerns. The Interactor deals with the central concern.

 - loc 1313 - The lesson here is that depending on something that carries baggage that you don’t need can cause you troubles that you didn’t expect.

 - loc 1314 - carries baggage that you don’t need can cause you troubles that you didn’t expect.

 - loc 1319 - The Dependency Inversion Principle (DIP) tells us that the most flexible systems are those in which source code dependencies refer only to abstractions, not to concretions. In a statically typed language, like Java, this means that the use, import, and include statements should refer only to source modules containing interfaces, abstract classes, or some other kind of abstract declaration. Nothing concrete should be depended on.

 - loc 1350 - Never mention the name of anything concrete and volatile. This is really just a restatement of the principle itself.

 - loc 1366 - Note that the flow of control crosses the curved line in the opposite direction of the source code dependencies. The source code dependencies are inverted against the flow of control—which is why we refer to this principle as Dependency Inversion.

 - loc 1505 - The Reuse/Release Equivalence Principle (REP) is a principle that seems obvious, at least in hindsight. People who want to reuse software components cannot, and will not, do so unless those components are tracked through a release process and are given release numbers.

 - loc 1524 - THE COMMON CLOSURE PRINCIPLE Gather into components those classes that change for the same reasons and at the same times. Separate into different components those classes that change at different times and for different reasons. This is the Single Responsibility Principle restated for components. Just as the SRP says that a class should not contain multiples reasons to change, so the Common Closure Principle (CCP) says that a component should not have multiple reasons to change.

 - loc 1525 - Gather into components those classes that change for the same reasons and at the same times. Separate into different components those classes that change at different times and for different reasons. This is the Single Responsibility Principle restated for components. Just as the SRP says that a class should not contain multiples reasons to change, so the Common Closure Principle (CCP) says that a component should not have multiple reasons to change.

 - loc 1545 - Gather together those things that change at the same times and for the same reasons. Separate those

 - loc 1545 - Gather together those things that change at the same times and for the same reasons. Separate those things that change at different times or for different reasons.

 - loc 1572 - The REP and CCP are inclusive principles: Both tend to make components larger. The CRP is an exclusive principle, driving components to be smaller. It is the tension between these principles that good architects seek to resolve.

 - loc 1641 - Regardless of which component you begin at, it is impossible to follow the dependency relationships and wind up back at that component. This structure has no cycles. It is a directed acyclic graph (DAG).

 - loc 1661 - This cycle creates some immediate problems. For example, the developers working on the Database component know that to release it, the component must be compatible with Entities. However, with the cycle in place, the Database component must now also be compatible with Authorizer. But Authorizer depends on Interactors. This makes Database much more difficult to release. Entities, Authorizer, and Interactors have, in effect, become one large component—which means that all of the developers working on any of those components will experience the dreaded “morning after syndrome.” They will be stepping all over one another because they must all use exactly the same release of one another’s components

 - loc 1678 - It is always possible to break a cycle of components and reinstate the dependency graph as a DAG. There are two primary mechanisms for doing so: 1. Apply the Dependency Inversion Principle (DIP). In the case in Figure 14.3, we could create an interface that has the methods that User needs. We could then put that interface into Entities and inherit it into Authorizer. This inverts the dependency between Entities and Authorizer, thereby breaking the cycle.

 - loc 1685 - 2. Create a new component that both Entities and Authorizer depend on. Move the class(es) that they both depend on into that new component

 - loc 1694 - The issues we have discussed so far lead to an inescapable conclusion: The component structure cannot be designed from the top down. It is not one of the first things about the system that is designed, but rather evolves as the system grows and changes.

 - loc 1699 - component dependency diagrams have very little do to with describing the function of the application. Instead, they are a map to the buildability and maintainability of the application. This is why they aren’t designed at the beginning of the project. There is no software to build or maintain, so there is no need for a build and maintenance map.

 - loc 1723 - By conforming to the Stable Dependencies Principle (SDP), we ensure that modules that are intended to be easy to change are not depended on by modules that are harder to change.

 - loc 1731 - Many factors may make a software component hard to change—for example, its size, complexity, and clarity, among other characteristics. We will ignore all those factors and focus on something different here. One sure way to make a software component difficult to change, is to make lots of other software components depend on it.

 - loc 1815 - The Stable Abstractions Principle (SAP) sets up a relationship between stability and abstractness. On the one hand, it says that a stable component should also be abstract so that its stability does not prevent it from being extended. On the other hand, it says that an unstable component should be concrete since it its instability allows the concrete code within it to be easily changed.

 - loc 1820 - the SDP says that dependencies should run in the direction of stability, and the SAP says that stability implies abstraction. Thus dependencies run in the direction of abstraction.

 - loc 1848 - The area around (0, 0) is a zone of exclusion called the Zone of Pain. Some software entities do, in fact, fall within the Zone of Pain. An example would be a database schema. Database schemas are notoriously volatile, extremely concrete, and highly depended on.

 - loc 1858 - Consider a component near (1, 1). This location is undesirable because it is maximally abstract, yet has no dependents. Such components are useless. Thus this area is called the Zone of Uselessness.

 - loc 1865 - The locus of points that are maximally distant from each zone is the line that connects (1, 0) and (0, 1). I call this line the Main Sequence.

 - loc 1918 - The purpose of that shape is to facilitate the development, deployment, operation, and maintenance of the software system contained within it. The strategy behind that facilitation is to leave as many options open as possible, for as long as possible.

 - loc 1978 - All software systems can be decomposed into two major elements: policy and details. The policy element embodies all the business rules and procedures.

 - loc 1982 - The goal of the architect is to create a shape for the system that recognizes policy as the most essential element of the system while making the details irrelevant to that policy. This allows decisions about those details to be delayed and deferred.

 - loc 1996 - If you can develop the high-level policy without committing to the details that surround it, you can delay and defer decisions about those details for a long time. And the longer you wait to make those decisions, the more information you have with which to make them properly.

 - loc 2003 - What if the decisions have already been made by someone else? What if your company has made a commitment to a certain database, or a certain web server, or a certain framework? A good architect pretends that the decision has not been made, and shapes the system such that those decisions can still be deferred or changed for as long as possible. A good architect maximizes the number of decisions not made.

