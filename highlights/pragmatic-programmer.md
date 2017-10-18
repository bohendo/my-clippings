
---
#  Pragmatic Programmer
## by Andrew Hunt & David Thomas
---

 - loc 237 - "Kaizen" is a Japanese term that captures the concept of continuously making many small improvements

 - loc 313 - The greatest of all weaknesses is the fear of appearing weak. • J. B. Bossuet,

 - loc 364 - One broken window, left unrepaired for any substantial length of time, instills in the inhabitants of the building a sense of abandonment—a sense that the powers that be don't care about the building. So another window gets broken. People start littering. Graffiti appears.

 - loc 371 - Don't leave "broken windows" (bad designs, wrong decisions, or poor code) unrepaired. Fix each one as soon as it is discovered. If there is insufficient time to fix it properly, then board it up.

 - loc 389 - if you find yourself on a team and a project where the code is pristinely beautiful—cleanly written, well designed, and elegant—you will likely take extra special care not to mess it up,

 - loc 415 - But ask permission to tackle the whole thing and you'll be met with delays and blank stares. People will form committees, budgets will need approval, and things will get complicated. Everyone will guard their own resources. Sometimes this is called "start-up fatigue."

 - loc 420 - People find it easier to join an ongoing success. Show them a glimpse of the future and you'll get them to rally around.[1]

 - loc 473 - Great software today is often preferable to perfect software tomorrow. If you give your users something to play with early, their feedback will often lead you to a better eventual solution (see Tracer Bullets, page 48).

 - loc 481 - Don't spoil a perfectly good program by overembellishment and over-refinement. Move on, and let your code stand in its own right for a while. It may not be perfect. Don't worry: it could never be perfect

 - loc 493 - An investment in knowledge always pays the best interest. • Benjamin Franklin

 - loc 497 - Your knowledge and experience are your most important professional assets. Unfortunately, they're expiring assets.

 - loc 511 - Just as in financial investing, you must invest in your knowledge portfolio regularly. Even if it's just a small amount, the habit itself is as important as the sums.

 - loc 515 - The more technologies you are comfortable with, the better you will be able to adjust to change.

 - loc 529 - Learn at least one new language every year. Different languages solve the same problems in different ways. By learning several different approaches, you can help broaden your thinking and avoid getting stuck in a rut.

 - loc 537 - Isolation can be deadly to your career; find out what people are working on outside of your company

 - loc 537 - Participate in local user groups. Don't just go and listen, but actively participate. Isolation can be deadly to your career; find out what people are working on outside of your company

 - loc 544 - Once you feel comfortable with some new language or bit of technology, move on. Learn another one.

 - loc 547 - The cross-pollination of ideas is important; try to apply the lessons you've learned to your current project. Even if your project doesn't use that technology, perhaps you can borrow some ideas.

 - loc 556 - If you can't find the answer yourself, find out who can. Don't let it rest. Talking to other people will help build your personal network, and you may surprise yourself by finding solutions to other, unrelated problems along the way.

 - loc 564 - Never underestimate the power of commercialism. Just because a Web search engine lists a hit first doesn't mean that it's the best match; the content provider can pay to get top billing. Just because a bookstore features a book prominently doesn't mean it's a good book,

 - loc 625 - Make what you're saying relevant in time, as well as in content. Sometimes all it takes is the simple question "Is this a good time to talk about...?"

 - loc 634 - Too many developers (and their managers) concentrate solely on content when producing written documents. We think this is a mistake. Any chef will tell you that you can slave in the kitchen for hours only to ruin your efforts with poor presentation.

 - loc 636 - There is no excuse today for producing poor-looking printed documents.

 - loc 642 - If possible, involve your readers with early drafts of your document. Get their feedback, and pick their brains.

 - loc 645 - There's one technique that you must use if you want people to listen to you: listen to them. Even if this is a situation where you have all the information

 - loc 715 - DRY principle: EVERY PIECE OF KNOWLEDGE MUST HAVE A SINGLE, UNAMBIGUOUS, AUTHORITATIVE REPRESENTATION WITHIN A SYSTEM.

 - loc 741 - answer is to write a simple filter or code generator. Structures in multiple languages can be built from a common metadata representation using a simple code generator each time the software is built

 - loc 741 - Structures in multiple languages can be built from a common metadata representation using a simple code generator each time the software is built

 - loc 748 - The DRY principle tells us to keep the low-level knowledge in the code, where it belongs, and reserve the comments for other, high-level explanations. Otherwise, we're duplicating knowledge, and every change means changing both the code and the comments.

 - loc 752 - The documentation and code both contain representations of the same knowledge.

 - loc 767 - There is absolutely no point in duplicating a function or class header comment between the two files. Use the header files to document interface issues, and the implementation files to document the nitty-gritty details that users of your code don't need to know.

 - loc 770 - Sometimes, duplication comes about as the result of mistakes in the design.

 - loc 777 - There is a slightly less obvious kind of unnormalized data that occurs when we have multiple data elements that are mutually dependent.

 - loc 779 - A line clearly has a start and end, and will always have a length (even if it's zero). But we have duplication. The length is defined by the start and end points: change one of the points and the length changes. It's better to make the length a calculated field:

 - loc 782 - Later on in the development process, you may choose to violate the DRY principle for performance reasons. Frequently this occurs when you need to cache data to avoid repeating expensive operations. The trick is to localize the impact. The violation is not exposed to the outside world:

 - loc 795 - remember the hackneyed aphorism "shortcuts make for long delays." You may well save some seconds now, but at the potential loss of hours later.

 - loc 812 - make a point of reading other people's source code and documentation, either informally or during code reviews. You're not snooping—you're learning from them. And remember, the access is reciprocal—don't get twisted about other people poring (pawing?) through your code, either.

 - loc 814 - Tip 12 Make It Easy to Reuse What you're trying to do is foster an environment where it's easier to find and reuse existing stuff than to write it yourself. If it isn't easy, people won't do it. And if you fail to reuse, you risk duplicating knowledge.

 - loc 815 - What you're trying to do is foster an environment where it's easier to find and reuse existing stuff than to write it yourself. If it isn't easy, people won't do it. And if you fail to reuse, you risk duplicating knowledge.

 - loc 831 - In computing, the term has come to signify a kind of independence or decoupling. Two or more things are orthogonal if changes in one do not affect any of the others.

 - loc 850 - Tip 13 Eliminate Effects Between Unrelated Things We want to design components that are self-contained: independent, and with a single, well-defined purpose (what Yourdon and Constantine call cohesion [YC86]).

 - loc 855 - You get two major benefits if you write orthogonal systems: increased productivity and reduced risk.

 - loc 858 - Simple components can be designed, coded, unit tested, and then forgotten—

 - loc 859 - If components have specific, well-defined responsibilities, they can be combined with new components in ways that were not envisioned by their original implementors.

 - loc 866 - Diseased sections of code are isolated.

 - loc 868 - Make small changes and fixes to a particular area, and any problems you generate will be restricted to that area.

 - loc 893 - ask yourself: If I dramatically change the requirements behind a particular function, how many modules are affected? In an orthogonal system, the answer should be "one."

 - loc 908 - We once worked on a project that required that a certain body of Java code run both locally on a server machine and remotely on a client machine. The alternatives for distributing classes this way were RMI and CORBA.

 - loc 934 - Avoid global data. Every time your code references global data, it ties itself into the other components that share that data. Even globals that you intend only to read can lead to trouble (for example, if you suddenly need to change your code to be multithreaded). In general, your code is easier to understand and maintain if you explicitly pass any required context into your modules. In object-oriented applications, context is often passed as parameters to objects' constructors. In other code, you can create structures containing the context and pass around references to them.

 - loc 941 - Avoid similar functions. Often you'll come across a set of functions that all look similar—maybe they share common code at the start and end, but each has a different central algorithm. Duplicate code is a symptom of structural problems.

 - loc 950 - we suggest that every module have its own unit test built into its code, and that these tests be performed automatically as part of the regular build process

 - loc 952 - Building unit tests is itself an interesting test of orthogonality. What does it take to build and link a unit test?

 - loc 1023 - Most of the time, calls to third-party products are entangled throughout the code. But if you really abstracted the idea of a database out—to the point where it simply provides persistence as a service—then you have the flexibility to change horses in midstream.

 - loc 1044 - Normally, you can simply hide a third-party product behind a well-defined, abstract interface.

 - loc 1048 - Whatever mechanism you use, make it reversible. If something is added automatically, it can be taken out automatically as well.

 - loc 1059 - But think of code evolution along the same lines as a box full of Schrödinger's cats: every decision results in a different version of the future. How many possible futures can your code support? Which ones are more likely? How hard will it be to support them when the time comes?

 - loc 1084 - we're looking for something that gets us from a requirement to some aspect of the final system quickly, visibly, and repeatably. Tip 15 Use Tracer Bullets to Find the Target

 - loc 1097 - Tracer code is not disposable: you write it for keeps. It contains all the error checking, structuring, documentation, and self-checking that any piece of production code has.

 - loc 1098 - once you have achieved an end-to-end connection among the components of your system, you can check how close to the target you are, adjusting if necessary. Once you're on target, adding functionality is easy.

 - loc 1100 - Tracer development is consistent with the idea that a project is never finished: there will always be changes required and functions to add. It is an incremental approach.

 - loc 1111 - As the system is connected end-to-end, you have an environment to which you can add new pieces of code once they have been unit-tested.

 - loc 1121 - You use the technique in situations where you're not 100% certain of where you're going. You shouldn't be surprised if your first couple of attempts miss: the user says "that's not what I meant," or data you need isn't available when you need it, or performance problems seem likely. Work out how to change what you've got to bring it nearer the target, and be thankful that you've used a lean development methodology.

 - loc 1144 - Prototyping generates disposable code. Tracer code is lean but complete, and forms part of the skeleton of the final system. Think of prototyping as the reconnaissance and intelligence gathering that takes place before a single tracer bullet is fired.

 - loc 1158 - We tend to think of prototypes as code-based, but they don't always have to be.

 - loc 1161 - Prototypes are designed to answer just a few questions, so they are much cheaper and faster to develop than applications that go into production. The code can ignore unimportant details—

 - loc 1165 - But if you find yourself in an environment where you cannot give up the details, then you need to ask yourself if you are really building a prototype at all.

 - loc 1172 - Prototyping is a learning experience. Its value lies not in the code produced, but in the lessons learned.

 - loc 1203 - Prototypes can be deceptively attractive to people who don't know that they are just prototypes. You must make it very clear that this code is disposable, incomplete, and unable to be completed.

 - loc 1227 - We always try to write code using the vocabulary of the application domain (see The Requirements Pit, page 210, where we suggest using a project glossary).

 - loc 1236 - This language need not be executable. Initially, it could be simply a way of capturing the user's requirements—a specification. However, you may want to consider taking this a step further and actually implementing the language. Your specification has become executable code.

 - loc 1243 - Tip 17 Program Close to the Problem Domain Whether it's a simple language to configure and control an application program, or a more complex language to specify rules or procedures, we think you should consider ways of moving your project closer to the problem domain. By coding at a higher level of abstraction, you are free to concentrate on solving domain problems, and can ignore petty implementation details.

 - loc 1256 - If this happened in a standard, general-purpose programming language, you might receive a standard, general-purpose error message: Syntax error: undeclared identifier But with a mini-language, you would instead be able to issue an error message using the vocabulary of the domain:

 - loc 1284 - Data languages produce some form of data structure used by an application. These languages are often used to represent configuration information

 - loc 1298 - Imperative languages take this a step further. Here the language is actually executed, and so can contain statements, control constructs, and the like

 - loc 1312 - A mini-language doesn't have to be used directly by the application to be useful. Many times we may use a specification language to create artifacts (including metadata) that are compiled, read-in, or otherwise used by the program itself (see Metaprogramming, page 144).

 - loc 1350 - By learning to estimate, and by developing this skill to the point where you have an intuitive feel for the magnitudes of things, you will be able to show an apparent magical ability to determine their feasibility.

 - loc 1366 - One of the interesting things about estimating is that the units you use make a difference in the interpretation of the result.

 - loc 1375 - before we get too deeply into the techniques of building models, we have to mention a basic estimating trick that always gives good answers: ask someone who's already done it.

 - loc 1380 - you need to have a grasp of the scope of the domain. Often this is implicit in the question, but you need to make it a habit to think about the scope before starting to guess.

 - loc 1391 - You are trading off model simplicity for accuracy. Doubling the effort on the model may give you only a slight increase in accuracy. Your experience will tell you when to stop refining.

 - loc 1405 - you'll often find yourself basing an estimate on other subestimates. This is where your largest errors will creep in.

 - loc 1411 - (Notice how "three quarters of a second" conveys a different feeling of accuracy than 750 ms.)

 - loc 1417 - When an estimate turns out wrong, don't just shrug and walk away. Find out why it differed from your guess.

 - loc 1422 - practice incremental development, repeating the following steps. Check requirements Analyze risk Design, implement, integrate Validate with the users Initially, you may have only a vague idea of how many iterations will be required, or how long they may be.

 - loc 1427 - Based on that experience, you can refine your initial guess on the number of iterations and what can be included in each.

 - loc 1428 - The refinement gets better and better each time, and confidence in the schedule grows along with it.

 - loc 1434 - What to Say When Asked for an Estimate You say "I'll get back to you." You almost always get better results if you slow the process down and spend some time going through the steps we describe in this section.

 - loc 1459 - If you come across a situation where you feel your current tools can't cut it, make a note to look for something different or more powerful that would have helped. Let need drive your acquisitions.

 - loc 1485 - Plain text doesn't mean that the text is unstructured; XML, SGML, and HTML are great examples of plain text that has a well-defined structure.

 - loc 1494 - Tip 20 Keep Knowledge in Plain Text

 - loc 1531 - Virtually every tool in the computing universe, from source code management systems to compiler environments to editors and stand-alone filters, can operate on plain text.

 - loc 1596 - Tip 21 Use the Power of Command Shells Gain familiarity with the shell, and you'll find your productivity soaring.

 - loc 1648 - Tip 22 Use a Single Editor Well Choose an editor, know it thoroughly, and use it for all editing tasks.

 - loc 1710 - Source code control systems, or the more widely scoped configuration management systems, keep track of every change you make in your source code and documentation.

 - loc 1714 - A good SCCS will let you track changes, answering questions such as: Who made changes in this line of code? What's the difference between the current version and last week's? How many lines of code did we change in this release? Which files get changed most often?

 - loc 1729 - Tip 23 Always Use Source Code Control Always. Even if you are a single-person team on a one-week project. Even if it's a "throw-away" prototype

 - loc 1746 - Although this may seem to be duplication of effort, we can pretty much guarantee it will save you grief (and save your project money) the first time you need to answer questions such as "What did you do to the xyz module?" and "What broke the build?"

 - loc 1774 - Debugging itself is a sensitive, emotional subject for many developers. Instead of attacking it as a puzzle to be solved, you may encounter denial, finger pointing, lame excuses, or just plain apathy.

 - loc 1780 - Tip 24 Fix the Problem, Not the Blame It doesn't really matter whether the bug is your fault or someone else's. It is still your problem.

 - loc 1809 - You may need to interview the user who reported the bug in order to gather more data than you were initially given.

 - loc 1809 - You may need to interview the user who reported the bug in order to gather more data than you were initially given. Artificial tests (such as the programmer's single brush stroke from bottom to top) don't exercise enough of an application. You must brutally test both boundary conditions and realistic end-user usage patterns. You need to do this systematically (see Ruthless Testing, page 237).

 - loc 1810 - Artificial tests (such as the programmer's single brush stroke from bottom to top) don't exercise enough of an application. You must brutally test both boundary conditions and realistic end-user usage patterns. You need to do this systematically (see Ruthless Testing, page 237).

 - loc 1820 - we want a bug that can be reproduced with a single command. It's a lot harder to fix a bug if you have to go through 15 steps to get to the point where the bug shows up.

 - loc 1825 - Often, the easiest way to discern what a program is doing—or what it is going to do—is to get a good look at the data it is operating on.

 - loc 1841 - Tracing statements are those little diagnostic messages you print to the screen or to a file that say things such as "got here" and "value of x = 2." It's a primitive technique compared with IDE-style debuggers, but it is peculiarly effective at diagnosing several classes of errors that debuggers can't.

 - loc 1861 - the simple act of explaining, step by step, what the code is supposed to do often causes the problem to leap off the screen and announce itself.[

 - loc 1874 - Even if the problem does lie with a third party, you'll still have to eliminate your code before submitting the bug report.

 - loc 1889 - See if the symptoms are present at either of two far away spots in the code. Then look in the middle. If the problem is present, then the bug lies between the start and the middle point; otherwise, it is between the middle point and the end.

 - loc 1896 - The amount of surprise you feel when something goes wrong is directly proportional to the amount of trust and faith you have in the code being run. That's why, when faced with a "surprising" failure, you must realize that one or more of your assumptions is wrong. Don't gloss over a routine or piece of code involved in the bug because you "know" it works. Prove it.

 - loc 1907 - If it took a long time to fix this bug, ask yourself why. Is there anything you can do to make fixing this bug easier the next time around?

 - loc 1911 - Debugging Checklist Is the problem being reported a direct result of the underlying bug, or merely a symptom? Is the bug really in the compiler? Is it in the OS? Or is it in your code? If you explained this problem in detail to a coworker, what would you say? If the suspect code passes its unit tests, are the tests complete enough? What happens if you run the unit test with this data? Do the conditions that caused this bug exist anywhere else in the system?

 - loc 1924 - Text manipulation languages are to programming what routers[8] are to woodworking. They are noisy, messy, and somewhat brute force. Make mistakes with them, and entire pieces can be ruined. Some people swear they have no place in the toolbox. But in the right hands, both routers and text manipulation languages can be incredibly powerful and versatile.

 - loc 2002 - Passive code generators are run once to produce a result. From that point forward, the result becomes freestanding—it is divorced from the code generator. The wizards discussed in Evil Wizards, page 198, along with some CASE tools, are examples of passive code generators.

 - loc 2004 - Active code generators are used each time their results are required. The result is a throw-away—it can always be reproduced by the code generator. Often, active code generators read some form of script or control file to produce their results.

 - loc 2020 - While passive code generators are simply a convenience, their active cousins are a necessity if you want to follow the DRY principle.

 - loc 2028 - If a column is removed from a table, but the code base is not changed, you might not even get a compilation error. The first you'll know about it is when your tests start failing (or when the user calls). An alternative is to use an active code generator—take the schema and use it to generate the source code for the structures,

 - loc 2043 - Sometimes you can parse the information out of the source files of one language and use it to generate code in a second language. Often, though, it is simpler to express it in a simpler, language-neutral representation and generate the code for both languages,

 - loc 2065 - Tip 30 You Can't Write Perfect Software Did that hurt? It shouldn't. Accept it as an axiom of life. Embrace it. Celebrate it. Because perfect software doesn't exist. No one in the brief history of computing has ever written a piece of perfect software.

 - loc 2078 - Knowing that no one writes perfect code, including themselves, Pragmatic Programmers code in defenses against their own mistakes.

 - loc 2103 - What is a correct program? One that does no more and no less than it claims to do. Documenting and verifying that claim is the heart of Design by Contract (DBC, for short).

 - loc 2110 - What must be true in order for the routine to be called; the routine's requirements. A routine should never get called when its preconditions would be violated.

 - loc 2110 - Preconditions. What must be true in order for the routine to be called; the routine's requirements. A routine should never get called when its preconditions would be violated.

 - loc 2112 - Postconditions. What the routine is guaranteed to do; the state of the world when the routine is done.

 - loc 2113 - Class invariants. A class ensures that this condition is always true from the perspective of a caller. During internal processing of a routine, the invariant may not hold, but by the time the routine exits and control returns to the caller, the invariant must be true.

 - loc 2131 - The contract between a routine and any potential caller can thus be read as If all the routine's preconditions are met by the caller, the routine shall guarantee that all postconditions and invariants will be true when it completes.

 - loc 2133 - If either party fails to live up to the terms of the contract, then a remedy (which was previously agreed to) is invoked—an exception is raised, or the program terminates, for instance. Whatever happens, make no mistake that failure to live up to the contract is a bug.

 - loc 2143 - Liskov Substitution Principle [Lis88]: Subclasses must be usable through the base class interface without the need for the user to know the difference.

 - loc 2163 - Simply enumerating at design time what the input domain range is, what the boundary conditions are, and what the routine promises to deliver—or, more importantly, what it doesn't promise to deliver—is a huge leap forward in writing better software.

 - loc 2168 - DBC is, after all, a design technique. Even without automatic checking, you can put the contract in the code as comments and still get a very real benefit.

 - loc 2212 - By expressing the domain of the square root function in the precondition of the sqrt routine, you shift the burden of correctness to the caller—where it belongs. You can then design the sqrt routine secure in the knowledge that its input will be in range.

 - loc 2224 - Loops are subject to the banana problem (I know how to spell "banana," but I don't know when to stop), fencepost errors (not knowing whether to count the fenceposts or the spaces between them), and the ubiquitous "off by one" error

 - loc 2227 - a loop invariant is a statement of the eventual goal of a loop, but is generalized so that it is also valid before the loop executes and on each iteration through the loop.

 - loc 2286 - 22. Dead Programs Tell No Lies

 - loc 2291 - one reason why each and every case/switch statement needs to have a default clause—we want to know when the "impossible" has happened).

 - loc 2298 - Tip 32 Crash Early Crash, Don't Trash One of the benefits of detecting problems as soon as you can is that you can crash earlier. And many times, crashing your program is the best thing you can do.

 - loc 2315 - when your code discovers that something that was supposed to be impossible just happened, your program is no longer viable. Anything it does from this point forward becomes suspect, so terminate it as soon as possible. A dead program normally does a lot less damage than a crippled one.

 - loc 2320 - 23. Assertive Programming

 - loc 2328 - Tip 33 If It Can't Happen, Use Assertions to Ensure That It Won't Whenever you find yourself thinking "but of course that could never happen," add code to check it.

 - loc 2340 - the condition passed to an assertion should not have a side effect (see the box on page 124). Also remember that assertions may be turned off at compile time—never put code that must be executed into an assert. Don't use assertions in place of real error handling.

 - loc 2348 - make sure the code you execute in those dying milliseconds doesn't rely on the information that triggered the assertion failure in the first place.

 - loc 2355 - for any complex program you are unlikely to test even a miniscule percentage of the permutations your code will be put through

 - loc 2359 - Your first line of defense is checking for any possible error, and your second is using assertions to try to detect those you've missed. Turning off assertions when you deliver a program to production is like crossing a high wire without a net because you once made it across in practice.

 - loc 2401 - Assume that an uncaught exception will terminate your program and ask yourself, "Will this code still run if I remove all the exception handlers?" If the answer is "no," then maybe exceptions are being used in nonexceptional circumstances.

 - loc 2414 - Tip 34 Use Exceptions for Exceptional Problems Why do we suggest this approach to exceptions? Well, an exception represents an immediate, nonlocal transfer of control—it's a kind of cascading goto. Programs that use exceptions as part of their normal processing suffer from all the readability and maintainability problems of classic spaghetti code.

 - loc 2447 - Tip 35 Finish What You Start This tip is easy to apply in most circumstances. It simply means that the routine or object that allocates a resource should be responsible for deallocating it.

 - loc 2475 - Deallocate resources in the opposite order to that in which you allocate them. That way you won't orphan resources if one resource contains references to another.

 - loc 2476 - When allocating the same set of resources in different places in your code, always allocate them in the same order. This will reduce the possibility of deadlock.

 - loc 2484 - If you are programming in an object-oriented language, you may find it useful to encapsulate resources in classes.

 - loc 2532 - Because Pragmatic Programmers trust no one, including ourselves, we feel that it is always a good idea to build code that actually checks that resources are indeed freed appropriately. For most applications, this normally means producing wrappers for each type of resource, and using these wrappers to keep track of all allocations and deallocations.

 - loc 2552 - Chapter 5

 - loc 2568 - 26. Decoupling and the Law of Demeter

 - loc 2576 - Organize your code into cells (modules) and limit the interaction between them. If one module then gets compromised and has to be replaced, the other modules should be able to carry on.

 - loc 2599 - Traversing relationships between objects directly can quickly lead to a combinatorial explosion[1] of dependency relationships.

 - loc 2605 - Systems with many unnecessary dependencies are very hard (and expensive) to maintain, and tend to be highly unstable.

 - loc 2621 - Using The Law of Demeter will make your code more adaptable and robust, but at a cost: as a "general contractor," your module must delegate and manage any and all subcontractors directly, without involving clients of your module. In practice, this means that you will be writing a large number of wrapper methods that simply forward the request on to a delegate.

 - loc 2625 - As with any technique, you must balance the pros and cons for your particular application.

 - loc 2658 - 27. Metaprogramming

 - loc 2659 - No amount of genius can overcome a preoccupation with detail • Levy's Eighth Law

 - loc 2668 - Tip 37 Configure, Don't Integrate Use metadata to describe configuration options for an application: tuning parameters, user preferences, the installation directory, and so on.

 - loc 2689 - general rule: program for the general case, and put the specifics somewhere else—outside the compiled code base. Tip 38 Put Abstractions in Code, Details in Metadata

 - loc 2715 - Many programs will scan such things only at startup, which is unfortunate. If you need to change the configuration, this forces you to restart the application. A more flexible approach is to write programs that can reload their configuration while they're running.

 - loc 2715 - Many programs will scan such things only at startup, which is unfortunate. If you need to change the configuration, this forces you to restart the application. A more flexible approach is to write programs that can reload their configuration while they're running. This flexibility comes at a cost: it is more complex to implement.

 - loc 2759 - 28. Temporal Coupling

 - loc 2775 - We'd like to find out what can happen at the same time, and what must happen in a strict order.

 - loc 2822 - programming with threads imposes some design constraints—and that's a good thing. Those constraints are actually so helpful that we want to abide by them whenever we program. It will help us decouple our code and fight programming by coincidence

 - loc 2867 - 29. It's Just a View

 - loc 2883 - Why is it bad to push all the events through a single routine? It violates object encapsulation—that one routine now has to have intimate knowledge of the interactions among many objects. It also increases the coupling—and we're trying to decrease coupling.

 - loc 2888 - Objects should be able to register to receive only the events they need, and should never be sent events they don't need.

 - loc 2916 - CORBA facilitates communication among objects written in different programming languages running on geographically dispersed machines with different architectures.

 - loc 2923 - the key concept behind the Model-View-Controller (MVC) idiom: separating the model from both the GUI that represents it and the controls that manage the view.[

 - loc 2929 - 42 Separate Views from Models By loosening the coupling between the model and the view/controller, you buy yourself a lot of flexibility at low cost.

 - loc 2929 - Tip 42 Separate Views from Models By loosening the coupling between the model and the view/controller, you buy yourself a lot of flexibility at low cost.

 - loc 2948 - The view is an interpretation of the model (perhaps a subset)—it doesn't need to be graphical. The controller is more of a coordination mechanism, and doesn't have to be related to any sort of input device.

 - loc 2992 - 30. Blackboards

 - loc 3071 - While You Are Coding

 - loc 3091 - 31. Programming by Coincidence

 - loc 3091 - Programming by Coincidence

 - loc 3103 - No matter what he does, it just doesn't ever seem to work right. Fred doesn't know why the code is failing because he didn't know why it worked in the first place.

 - loc 3121 - "It works now, better leave well enough alone...." It's easy to be fooled by this line of thought. Why should you take the risk of messing with something that's working? Well, we can think of several reasons: It may not really be working—it might just look like it is. The boundary condition you rely on may be just an accident. In different circumstances (a different screen resolution, perhaps), it might behave differently. Undocumented behavior may change with the next release of the library. Additional and unnecessary calls make your code slower. Additional calls also increase the risk of introducing new bugs of their own.

 - loc 3265 - Also be wary of premature optimization. It's always a good idea to make sure an algorithm really is a bottleneck before investing your precious time trying to improve it.

 - loc 3287 - Refactoring

 - loc 3289 - As a program evolves, it will become necessary to rethink earlier decisions and rework portions of the code. This process is perfectly natural. Code needs to evolve; it's not a static thing.

 - loc 3306 - When you come across a stumbling block because the code doesn't quite fit anymore, or you notice two things that should really be merged, or anything else at all strikes you as being "wrong," don't hesitate to change it.

 - loc 3322 - think of the code that needs refactoring as a "growth." Removing it requires invasive surgery. You can go in now, and take it out while it is still small. Or, you could wait while it grows and spreads—but removing it then will be both more expensive and more dangerous.

 - loc 3325 - Tip 47 Refactor Early, Refactor Often Keep track of the things that need to be refactored. If you can't refactor something immediately, make sure that it gets placed on the schedule.

 - loc 3337 - Don't try to refactor and add functionality at the same time.

 - loc 3337 - Make sure you have good tests before you begin refactoring. Run the tests as often as possible. That way you will know quickly if your changes have broken anything.

 - loc 3349 - Take short, deliberate steps: move a field from one class to another, fuse two similar methods into a superclass. Refactoring often involves making many localized changes that result in a larger-scale change. If you keep your steps small, and test after each step, you will avoid prolonged debugging.

 - loc 3420 - Tip 48 Design to Test When you design a module, or even a single routine, you should design both its contract and the code to test that contract.

 - loc 3424 - by building the tests before you implement the code, you get to try out the interface before you commit to it.

 - loc 3463 - At the end of the debugging session, you need to formalize the ad hoc test. If the code broke once, it is likely to break again.

 - loc 3474 - Log messages should be in a regular, consistent format; you may want to parse them automatically to deduce processing time or logic paths that the program took.

 - loc 3484 - All software you write will be tested—if not by you and your team, then by the eventual users—so you might as well plan on testing it thoroughly.

 - loc 3490 - Testing is more cultural than technical; we can instill this testing culture in a project regardless of the language being used. Tip 49 Test Your Software, or Your Users Will

 - loc 3522 - if you do use a wizard, and you don't understand all the code that it produces, you won't be in control of your own application. You won't be able to maintain it, and you'll be struggling when it comes time to debug. Tip 50 Don't Use Wizard Code You Don't Understand

 - loc 3540 - Before the Project

 - loc 3554 - The Requirements Pit

 - loc 3554 - Perfection is achieved, not when there is nothing left to add, but when there is nothing left to take away.... • Antoine de St. Exupery, Wind, Sand, and Stars, 1939

 - loc 3572 - Our recommendation is to document these policies separately from the requirement, and hyperlink the two.

 - loc 3572 - Policies change regularly, so we probably don't want to hardwire them into our requirements. Our recommendation is to document these policies separately from the requirement, and hyperlink the two. Make the requirement the general statement, and give the developers the policy information as an example of the type of thing they'll need to support in the implementation. Eventually, policy may end up as metadata in the application.

 - loc 3584 - It's important to discover the underlying reason why users do a particular thing, rather than just the way they currently do it. At the end of the day, your development has to solve their business problem, not just meet their stated requirements.

 - loc 3587 - There's a simple technique for getting inside your users' requirements that isn't used often enough: become a user.

 - loc 3595 - Tip 52 Work with a User to Think Like a User The requirements mining process is also the time to start to build a rapport with your user base, learning their expectations and hopes for the system you are building.

 - loc 3645 - Good requirements documents remain abstract. Where requirements are concerned, the simplest statement that accurately reflects the business need is best.

 - loc 3673 - It's easy to get sucked into the "just one more feature" maelstrom, but by tracking requirements you can get a clearer picture that "just one more feature" is really the fifteenth new feature added this month.

 - loc 3678 - Create and maintain a project glossary—one place that defines all the specific terms and vocabulary used in a project. All participants in the project, from end users to support staff, should use the glossary to ensure consistency.

 - loc 3706 - Solving Impossible Puzzles

 - loc 3725 - The key to solving puzzles is both to recognize the constraints placed on you and to recognize the degrees of freedom you do have, for in those you'll find your solution.

 - loc 3732 - Tip 55 Don't Think Outside the Box—Find the Box When faced with an intractable problem, enumerate all the possible avenues you have before you. Don't dismiss anything, no matter how unusable or stupid it sounds. Now go through the list and explain why a certain path cannot be taken. Are you sure? Can you prove it?

 - loc 3755 - Not Until You're Ready

 - loc 3761 - Tip 56 Listen to Nagging Doubts—Start When You're Ready

 - loc 3772 - So how can you tell when you're simply procrastinating, rather than responsibly waiting for all the pieces to fall into place? A technique that has worked for us in these circumstances is to start prototyping. Choose an area that you feel will be difficult and begin producing some kind of proof of concept.

 - loc 3787 - The Specification Trap

 - loc 3799 - First, it's naive to assume that a specification will ever capture every detail and nuance of a system or its requirement.

 - loc 3805 - Second, there is a problem with the expressive power of language itself.

 - loc 3810 - Write a short description that tells someone how to tie bows in their shoelaces.

 - loc 3810 - Here's a challenge for you. Write a short description that tells someone how to tie bows in their shoelaces.

 - loc 3813 - Tip 57 Some Things Are Better Done than Described

 - loc 3815 - Finally, there is the straightjacket effect. A design that leaves the coder no room for interpretation robs the programming effort of any skill and art.

 - loc 3828 - be aware that you reach a point of diminishing, or even negative, returns as the specifications get more and more detailed.

 - loc 3842 - Circles and Arrows

 - loc 3854 - Tip 58 Don't Be a Slave to Formal Methods

 - loc 3872 - Although there is an indication that some methods have benefits, these benefits start to manifest themselves only after a significant productivity and quality drop while the technique is adopted and its users train themselves. Never underestimate the cost of adopting new tools and methods.

 - loc 3882 - Tip 59 Expensive Tools Do Not Produce Better Designs

 - loc 3895 - Pragmatic Projects

 - loc 3909 - Pragmatic Teams

 - loc 3968 - It is a mistake to think that the activities of a project—analysis, design, coding, and testing—can happen in isolation. They can't. These are different views of the same problem, and artificially separating them can cause a boatload of trouble.

 - loc 3971 - Tip 60 Organize Around Functionality, Not Job Functions

 - loc 3973 - Divide your people into small teams, each responsible for a particular functional aspect of the final system. Let the teams organize themselves internally, building on individual strengths as they can.

 - loc 4037 - Tip 61 Don't Use Manual Procedures People just aren't as repeatable as computers are. Nor should we expect them to be. A shell script or batch file will execute the same instructions, in the same order, time after time. It can be put under source control, so you can examine changes to the procedure over time as well ("but it used to work...").

 - loc 4048 - There are several advantages in using makefiles. It is a scripted, automatic procedure. We can add in hooks to generate code for us, and run regression tests automatically. IDEs have their advantages, but with IDEs alone it can be hard to achieve the level of automation that we're looking for.

 - loc 4144 - Ruthless Testing

 - loc 4149 - Tip 62 Test Early. Test Often. Test Automatically. We want to start testing as soon as we have code.

 - loc 4155 - "Code a little, test a little" is a popular saying in the Smalltalk world,[6] and we can adopt that mantra as our own by writing test code at the same time (or even before) we write the production code.

 - loc 4162 - Tip 63 Coding Ain't Done 'Til All the Tests Run Just because you have finished hacking out a piece of code doesn't mean you can go tell your boss or your client that it's done. It's not. First of all, code is never really done. More importantly, you can't claim that it is usable by anyone until it passes all of the available tests.

 - loc 4168 - There are several major types of software testing that you need to perform: Unit testing Integration testing Validation and verification Resource exhaustion, errors, and recovery Performance testing Usability testing

 - loc 4179 - With good contracts in place and well tested, any integration issues can be detected easily. Otherwise, integration becomes a fertile breeding ground for bugs. In fact, it is often the single largest source of bugs in the system.

 - loc 4261 - Think of our set of test suites as an elaborate security system, designed to sound the alarm when a bug shows up. How better to test a security system than to try to break in?

 - loc 4264 - Tip 64 Use Saboteurs to Test Your Testing If you are really serious about testing, you might want to appoint a project saboteur.

 - loc 4264 - Tip 64 Use Saboteurs to Test Your Testing If you are really serious about testing, you might want to appoint a project saboteur. The saboteur's role is to take a separate copy of the source tree, introduce bugs on purpose, and verify that the tests will catch them.

 - loc 4301 - Tip 66 Find Bugs Once Once a human tester finds a bug, it should be the last time a human tester finds that bug. The automated tests should be modified to check for that particular bug from then on, every time, with no exceptions,

 - loc 4316 - It's All Writing

 - loc 4337 - In general, comments should discuss why something is done, its purpose and its goal. The code already shows how it is done, so commenting on this is redundant—and is a violation of the DRY principle.

 - loc 4345 - Remember that you (and others after you) will be reading the code many hundreds of times, but only writing it a few times. Take the time to spell out connectionPool instead of cp.

 - loc 4356 - Here's a list of things that should not appear in source comments. A list of the functions exported by code in the file. There are programs that analyze source for you. Use them, and the list is guaranteed to be up to date.

 - loc 4397 - We can generate API-level documentation from source code using tools such as JavaDoc and DOC++ in a similar fashion. The model is the source code: one view of the model can be compiled; other views are meant to be printed out or viewed on the Web. Our goal is always to work on the model—whether the model is the code itself or some other document—and have all views updated automatically

 - loc 4449 - Great Expectations

 - loc 4456 - A project that falls below their expectations is deemed a failure, no matter how good the deliverable is in absolute terms. However, like the parent of the child expecting the cheap doll, go too far and you'll be a failure, too.

 - loc 4456 - A project that falls below their expectations is deemed a failure, no matter how good the deliverable is in absolute terms. However, like the parent of the child expecting the cheap doll, go too far and you'll be a failure, too. Tip 69 Gently Exceed Your Users' Expectations

 - loc 4495 - Pride and Prejudice

 - loc 4498 - If we are responsible for a design, or a piece of code, we do a job we can be proud of. Tip 70 Sign Your Work

 - loc 4507 - Anonymity, especially on large projects, can provide a breeding ground for sloppiness, mistakes, sloth, and bad code

