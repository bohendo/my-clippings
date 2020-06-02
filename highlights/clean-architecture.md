
---
#  Clean Architecture
## by Uncle Bob
---

 - loc 555 - Structured programming imposes discipline on direct transfer of control.

 - loc 557 - Ole Johan Dahl and Kristen Nygaard. These two programmers noticed that the function call stack frame in the ALGOL language could be moved to a heap, thereby allowing local variables declared by a function to exist long after the function returned. The function became a constructor for a class, the local variables became instance variables, and the nested functions became methods. This led inevitably to the discovery of polymorphism through the disciplined use of function pointers.

 - loc 562 - Object-oriented programming imposes discipline on indirect transfer of control.

 - loc 571 - Functional programming imposes discipline upon assignment

 - loc 610 - Dijkstra discovered that certain uses of goto statements prevent modules from being decomposed recursively into smaller and smaller units, thereby preventing use of the divide-and-conquer approach necessary for reasonable proofs. Other uses of goto, however, did not have this problem. Dijkstra realized that these “good” uses of goto corresponded to simple selection and iteration control structures such as if/then/else and do/while.

 - loc 628 - In 1968, Dijkstra wrote a letter to the editor of CACM, which was published in the March issue. The title of this letter was “Go To Statement Considered Harmful.”

 - loc 669 - Dijkstra once said, “Testing shows the presence, not the absence, of bugs.”

 - loc 672 - Software development is not a mathematical endeavor, even though it seems to manipulate mathematical constructs. Rather, software is like a science. We show correctness by failing to prove incorrectness, despite our best efforts.

 - loc 688 - object-oriented design (OO).

 - loc 696 - Some folks fall back on three magic words to explain the nature of OO: encapsulation, inheritance, and polymorphism.

 - loc 875 - OO is the ability, through the use of polymorphism, to gain absolute control over every source code dependency in the system. It allows the architect to create a plugin architecture, in which modules that contain high-level policies are independent of modules that contain low-level details. The low-level details are relegated to plugin modules that can be deployed and developed independently from the modules that contain high-level policies.

 - loc 923 - Variables in functional languages do not vary.

 - loc 935 - One of the most common compromises in regard to immutability is to segregate the application, or the services within the application, into mutable and immutable components. The immutable components perform their tasks in a purely functional way, without using any mutable variables.

 - loc 941 - Since mutating state exposes those components to all the problems of concurrency, it is common practice to use some kind of transactional memory to protect the mutable variables from concurrent updates and race conditions. Transactional memory simply treats variables in memory the same way a database treats records on disk. It protects those variables with a transaction- or retry-based scheme.

 - loc 961 - Architects would be wise to push as much processing as possible into the immutable components, and to drive as much code as possible out of those components that must allow mutation.

 - loc 974 - Event sourcing is a strategy wherein we store the transactions, but not the state. When state is required, we simply apply all the transactions from the beginning of time. Of course, we can take shortcuts. For example, we can compute and save the state every midnight. Then, when the state information is required, we need compute only the transactions since midnight.

 - loc 1020 - SRP (The Single Responsibility Principle): An active corollary to Conway’s law: The best structure for a software system is heavily influenced by the social structure of the organization that uses it so that each software module has one, and only one, reason to change.

 - loc 1023 - OCP (The Open-Closed Principle): Bertrand Meyer made this principle famous in the 1980s. The gist is that for software systems to be easy to change, they must be designed to allow the behavior of those systems to be changed by adding new code, rather than changing existing code.

 - loc 1026 - LSP (The Liskov Substitution Principle): Barbara Liskov’s famous definition of subtypes, from 1988. In short, this principle says that to build software systems from interchangeable parts, those parts must adhere to a contract that allows those parts to be substituted one for another.

 - loc 1029 - ISP (The Interface Segregation Principle): This principle advises software designers to avoid depending on things that they don’t use.

 - loc 1031 - DIP (The Dependency Inversion Principle): The code that implements high-level policy should not depend on the code that implements low-level details. Rather, details should depend on policies.

 - loc 1167 - Let me say that again: If component A should be protected from changes in component B, then component B should depend on component A.

 - loc 1172 - Why should the Interactor hold such a privileged position? Because it contains the business rules. The Interactor contains the highest-level policies of the application. All the other components are dealing with peripheral concerns. The Interactor deals with the central concern.

 - loc 1313 - The lesson here is that depending on something that carries baggage that you don’t need can cause you troubles that you didn’t expect.

 - loc 1319 - The Dependency Inversion Principle (DIP) tells us that the most flexible systems are those in which source code dependencies refer only to abstractions, not to concretions. In a statically typed language, like Java, this means that the use, import, and include statements should refer only to source modules containing interfaces, abstract classes, or some other kind of abstract declaration. Nothing concrete should be depended on.

 - loc 1366 - The source code dependencies are inverted against the flow of control—which is why we refer to this principle as Dependency Inversion.

 - loc 1505 - The Reuse/Release Equivalence Principle (REP) is a principle that seems obvious, at least in hindsight. People who want to reuse software components cannot, and will not, do so unless those components are tracked through a release process and are given release numbers.

 - loc 1524 - The Common Closure Principle: Gather into components those classes that change for the same reasons and at the same times. Separate into different components those classes that change at different times and for different reasons. This is the Single Responsibility Principle restated for components. Just as the SRP says that a class should not contain multiples reasons to change, so the Common Closure Principle (CCP) says that a component should not have multiple reasons to change.

 - loc 1546 - The Common Reuse Principle (CRP): Don’t force users of a component to depend on things they don’t need.

 - loc 1546 - THE COMMON REUSE PRINCIPLE Don’t force users of a component to depend on things they don’t need.

 - loc 1551 - Classes are seldom reused in isolation. More typically, reusable classes collaborate with other classes that are part of the reusable abstraction. The CRP states that these classes belong together in the same component. In such a component we would expect to see classes that have lots of dependencies on each other.

 - loc 1565 - The CRP says that classes that are not tightly bound to each other should not be in the same component.

 - loc 1572 - The REP and CCP are inclusive principles: Both tend to make components larger. The CRP is an exclusive principle, driving components to be smaller. It is the tension between these principles that good architects seek to resolve.

 - loc 1641 - Regardless of which component you begin at, it is impossible to follow the dependency relationships and wind up back at that component. This structure has no cycles. It is a directed acyclic graph (DAG).

 - loc 1661 - A cycle creates some immediate problems. For example, the developers working on the Database component know that to release it, the component must be compatible with Entities. However, with the cycle in place, the Database component must now also be compatible with Authorizer. But Authorizer depends on Interactors. This makes Database much more difficult to release. Entities, Authorizer, and Interactors have, in effect, become one large component—which means that all of the developers working on any of those components will experience the dreaded “morning after syndrome.” They will be stepping all over one another because they must all use exactly the same release of one another’s components

 - loc 1678 - It is always possible to break a cycle of components and reinstate the dependency graph as a DAG. There are two primary mechanisms for doing so: 1. Apply the Dependency Inversion Principle (DIP). In the case in Figure 14.3, we could create an interface that has the methods that User needs. We could then put that interface into Entities and inherit it into Authorizer. This inverts the dependency between Entities and Authorizer, thereby breaking the cycle.

 - loc 1685 - 2. Create a new component that both Entities and Authorizer depend on. Move the class(es) that they both depend on into that new component

 - loc 1694 - The issues we have discussed so far lead to an inescapable conclusion: The component structure cannot be designed from the top down. It is not one of the first things about the system that is designed, but rather evolves as the system grows and changes.

 - loc 1699 - Component dependency diagrams have very little do to with describing the function of the application. Instead, they are a map to the buildability and maintainability of the application. This is why they aren’t designed at the beginning of the project. There is no software to build or maintain, so there is no need for a build and maintenance map.

 - loc 1723 - By conforming to the Stable Dependencies Principle (SDP), we ensure that modules that are intended to be easy to change are not depended on by modules that are harder to change.

 - loc 1731 - Many factors may make a software component hard to change—for example, its size, complexity, and clarity, among other characteristics. We will ignore all those factors and focus on something different here. One sure way to make a software component difficult to change, is to make lots of other software components depend on it.

 - loc 1815 - The Stable Abstractions Principle (SAP) sets up a relationship between stability and abstractness. On the one hand, it says that a stable component should also be abstract so that its stability does not prevent it from being extended. On the other hand, it says that an unstable component should be concrete since it its instability allows the concrete code within it to be easily changed.

 - loc 1820 - The Stable Dependencies Principle (SDP) says that dependencies should run in the direction of stability, and the Stable Abstractions Principle (SAP) says that stability implies abstraction. Thus dependencies run in the direction of abstraction.

 - loc 1848 - On a graph of increasing stability vs increasing abstraction, The area around (0, 0) is a zone of exclusion called the Zone of Pain. Some software entities do, in fact, fall within the Zone of Pain. An example would be a database schema. Database schemas are notoriously volatile, extremely concrete, and highly depended on.

 - loc 1858 - Consider a component near (1, 1). This location is undesirable because it is maximally abstract, yet has no dependents. Such components are useless. Thus this area is called the Zone of Uselessness.

 - loc 1865 - The locus of points that are maximally distant from each zone is the line that connects (1, 0) and (0, 1). I call this line the Main Sequence.

 - loc 1918 - The purpose of that shape is to facilitate the development, deployment, operation, and maintenance of the software system contained within it. The strategy behind that facilitation is to leave as many options open as possible, for as long as possible.

 - loc 1978 - All software systems can be decomposed into two major elements: policy and details. The policy element embodies all the business rules and procedures.

 - loc 1982 - The goal of the architect is to create a shape for the system that recognizes policy as the most essential element of the system while making the details irrelevant to that policy. This allows decisions about those details to be delayed and deferred.

 - loc 1996 - If you can develop the high-level policy without committing to the details that surround it, you can delay and defer decisions about those details for a long time. And the longer you wait to make those decisions, the more information you have with which to make them properly.

 - loc 2003 - What if the decisions have already been made by someone else? What if your company has made a commitment to a certain database, or a certain web server, or a certain framework? A good architect pretends that the decision has not been made, and shapes the system such that those decisions can still be deferred or changed for as long as possible. A good architect maximizes the number of decisions not made.

 - loc 2095 - The most important thing a good architecture can do to support behavior is to clarify and expose that behavior so that the intent of the system is visible at the architectural level.

 - loc 2114 - Conway’s law says: Any organization that designs a system will produce a design whose structure is a copy of the organization’s communication structure.

 - loc 2191 - There is true duplication, in which every change to one instance necessitates the same change to every duplicate of that instance. Then there is false or accidental duplication. If two apparently duplicated sections of code evolve along different paths—if they change at different rates, and for different reasons—then they are not true duplicates.

 - loc 2200 - Resist the temptation to commit the sin of knee-jerk elimination of duplication. Make sure the duplication is real.

 - loc 2228 - Dealing with service boundaries where none are needed is a waste of effort, memory, and cycles. And, yes, I know that the last two are cheap—but the first is not. My preference is to push the decoupling to the point where a service could be formed.

 - loc 2371 - The direction of this line is important. It shows that the Database does not matter to the BusinessRules, but the Database cannot exist without the BusinessRules. If that seems strange to you, just remember this point: The Database component contains the code that translates the calls made by the BusinessRules into the query language of the database. It is that translation code that knows about the BusinessRules.

 - loc 2424 - Boundaries are drawn where there is an axis of change. The components on one side of the boundary change at different rates, and for different reasons, than the components on the other side of the boundary.

 - loc 2540 - A strict definition of “level” is “the distance from the inputs and outputs.” The farther a policy is from both the inputs and the outputs of the system, the higher its level.

 - loc 2587 - Strictly speaking, business rules are rules or procedures that make or save the business money. Very strictly speaking, these rules would make or save the business money, irrespective of whether they were implemented on a computer. They would make or save money even if they were executed manually.

 - loc 2593 - Critical Business Rules usually require some data to work with. For example, our loan requires a loan balance, an interest rate, and a payment schedule. We shall call this data Critical Business Data.

 - loc 2595 - The critical rules and critical data are inextricably bound, so they are a good candidate for an object. We’ll call this kind of object an Entity.

 - loc 2618 - A use case is a description of the way that an automated system is used. It specifies the input to be provided by the user, the output to be returned to the user, and the processing steps involved in producing that output. A use case describes application-specific business rules as opposed to the Critical Business Rules within the Entities.

 - loc 2626 - Use cases control the dance of the Entities.

 - loc 2635 - High-level concepts, such as Entities, know nothing of lower-level concepts, such as use cases.

 - loc 2739 - In general, the further in you go, the higher level the software becomes. The outer circles are mechanisms. The inner circles are policies. The overriding rule that makes this architecture work is the Dependency Rule: Source code dependencies must point only inward, toward higher-level policies. Nothing in an inner circle can know anything at all about something in an outer circle.

 - loc 2761 - The software in the interface adapters layer is a set of adapters that convert data from the format most convenient for the use cases and entities, to the format most convenient for some external agency such as the database or the web.

 - loc 2786 - For example, suppose the use case needs to call the presenter. This call must not be direct because that would violate the Dependency Rule: No name in an outer circle can be mentioned by an inner circle. So we have the use case call an interface (shown in Figure 22.1 as “use case output port”) in the inner circle, and have the presenter in the outer circle implement it.

 - loc 2798 - We don’t want to pass that row structure inward across a boundary. Doing so would violate the Dependency Rule because it would force an inner circle to know something about an outer circle. Thus, when we pass data across a boundary, it is always in the form that is most convenient for the inner circle.

 - loc 2829 - The Humble Object pattern is a design pattern that was originally identified as a way to help unit testers to separate behaviors that are hard to test from behaviors that are easy to test.

 - loc 2834 - Using the Humble Object pattern, we can separate these two kinds of behaviors into two different classes called the Presenter and the View.

 - loc 2834 - most of the behavior of a GUI is, in fact, easy to test. Using the Humble Object pattern, we can separate these two kinds of behaviors into two different classes called the Presenter and the View.

 - loc 2836 - The View is the humble object that is hard to test. The code in this object is kept as simple as possible.

 - loc 2838 - The Presenter is the testable object. Its job is to accept data from the application and format it for presentation so that the View can simply move it to the screen.

 - loc 2860 - Recall that we do not allow SQL in the use cases layer; instead, we use gateway interfaces that have appropriate methods. Those gateways are implemented by classes in the database layer. That implementation is the humble object.

 - loc 2871 - Where should such ORM systems reside? In the database layer of course. Indeed, ORMs form another kind of Humble Object boundary between the gateway interfaces and the database.

 - loc 2879 - At each architectural boundary, we are likely to find the Humble Object pattern lurking somewhere nearby.

 - loc 3031 - You note where boundaries may be required, and then carefully watch for the first inkling of friction because those boundaries don’t exist. At that point, you weigh the costs of implementing those boundaries versus the cost of ignoring them—and you review that decision frequently. Your goal is to implement the boundaries right at the inflection point where the cost of implementing becomes less than the cost of ignoring.

 - loc 3113 - The point is that Main is a dirty low-level module in the outermost circle of the clean architecture. It loads everything up for the high level system, and then hands control over to it.

 - loc 3189 - Functional decompositions, of the kind depicted in the service diagram in Figure 27.1, are very vulnerable to new features that cut across all those functional behaviors.

 - loc 3219 - Architectural boundaries do not fall between services. Rather, those boundaries run through the services, dividing them into components. To deal with the cross-cutting concerns that all significant systems face, services must be designed with internal component architectures that follow the Dependency Rule,

 - loc 3245 - You can think of the tests as the outermost circle in the architecture. Nothing within the system depends on the tests, and the tests always depend inward on the components of the system.

 - loc 3264 - The first rule of software design—whether for testability or for any other reason—is always the same: Don’t depend on volatile things.

 - loc 3268 - Create a specific API that the tests can use to verify all the business rules. This API should have superpowers that allow the tests to avoid security constraints, bypass expensive resources (such as databases), and force the system into particular testable states. This API will be a superset of the suite of interactors and interface adapters that are used by the user interface. The purpose of the testing API is to decouple the tests from the application.

 - loc 3278 - The role of the testing API is to hide the structure of the application from the tests. This allows the production code to be refactored and evolved in ways that don’t affect the tests.

 - loc 3301 - Although software does not wear out, it can be destroyed from within by unmanaged dependencies on firmware and hardware.

 - loc 3318 - You non-embedded developers essentially write firmware whenever you bury SQL in your code or when you spread platform dependencies throughout your code.

 - loc 3426 - The name of the boundary between the software and the firmware is the hardware abstraction layer (HAL) (Figure 29.4). This is not a new idea: It has been in PCs since the days before Windows.

 - loc 3759 - Don’t let frameworks into your core code. Instead, integrate them into components that plug in to your core code, following the Dependency Rule.

