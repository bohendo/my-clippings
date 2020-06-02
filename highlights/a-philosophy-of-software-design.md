
#  A Philosophy of Software Design

## by John Ousterhout

 - loc 352 - The overall complexity of a system (C) is determined by the complexity of each part p (cp) weighted by the fraction of time developers spend working on that part (tp). Isolating complexity in a place where it will never be seen is almost as good as eliminating the complexity entirely.

 - loc 361 - Change amplification: The first symptom of complexity is that a seemingly simple change requires code modifications in many different places.

 - loc 369 - Cognitive load: The second symptom of complexity is cognitive load, which refers to how much a developer needs to know in order to complete a task.

 - loc 379 - Sometimes an approach that requires more lines of code is actually simpler, because it reduces cognitive load.

 - loc 384 - Unknown unknowns: The third symptom of complexity is that it is not obvious which pieces of code must be modified to complete a task, or what information a developer must have to carry out the task successfully.

 - loc 398 - One of the most important goals of good design is for a system to be obvious.

 - loc 404 - Complexity is caused by two things: dependencies and obscurity.

 - loc 475 - Almost every software development organization has at least one developer who takes tactical programming to the extreme: a tactical tornado. The tactical tornado is a prolific programmer who pumps out code far faster than others but works in a totally tactical fashion.

 - loc 500 - I suggest spending about 10–20% of your total development time on investments. This amount is small enough that it won’t impact your schedules significantly, but large enough to produce significant benefits over time.

 - loc 573 - For the purposes of this book, a module is any unit of code that has an interface and an implementation.

 - loc 577 - The best modules are those whose interfaces are much simpler than their implementations. Such modules have two advantages. First, a simple interface minimizes the complexity that a module imposes on the rest of the system. Second, if a module is modified in a way that does not change its interface,

 - loc 577 - The best modules are those whose interfaces are much simpler than their implementations. Such modules have two advantages. First, a simple interface minimizes the complexity that a module imposes on the rest of the system. Second, if a module is modified in a way that does not change its interface, then no other module will be affected by the modification.

 - loc 603 - An abstraction can go wrong in two ways. First, it can include details that are not really important; when this happens, it makes the abstraction more complicated than necessary, which increases the cognitive load on developers using the abstraction. The second error is when an abstraction omits details that really are important. This results in obscurity: developers looking only at the abstraction will not have all the information they need to use the abstraction correctly. An abstraction that omits important details is a false abstraction: it might appear simple, but in reality it isn’t.

 - loc 676 - A shallow module is one whose interface is complicated relative to the functionality it provides. Shallow modules don’t help much in the battle against complexity, because the benefit they provide (not having to learn about how they work internally) is negated by the cost of learning and using their interfaces.

 - loc 676 - A shallow module is one whose interface is complicated relative to the functionality it provides. Shallow modules don’t help much in the battle against complexity, because the benefit they provide (not having to learn about how they work internally) is negated by the cost of learning and using their interfaces. Small modules tend to be shallow.

 - loc 771 - Information leakage occurs when the same knowledge is used in multiple places, such as two different classes that both understand the format of a particular type of file.

 - loc 881 - If the API for a commonly used feature forces users to learn about other features that are rarely used, this increases the cognitive load on users who don’t need the rarely used features.

 - loc 919 - In my experience, the sweet spot is to implement new modules in a somewhat general-purpose fashion. The phrase “somewhat general-purpose” means that the module’s functionality should reflect your current needs, but its interface should not. Instead, the

 - loc 1065 - Red Flag: Pass-Through Method  A pass-through method is one that does nothing except pass its arguments to another method, usually with the same API as the pass-through method. This typically indicates that there is not a clean division of responsibility between the classes.

 - loc 1167 - The solution I use most often is to introduce a context object as in Figure 7.2(d). A context stores all of the application’s global state (anything that would otherwise be a pass-through variable or global variable). Most applications have multiple variables in their global state, representing things such as configuration options, shared subsystems, and performance counters. There is one context object per instance of the system. The context allows multiple instances of the system to coexist in a single process, each with its own context.

 - loc 1192 - Without discipline, a context can turn into a huge grab-bag of data that creates nonobvious dependencies throughout the system. Contexts may also create thread-safety issues; the best way to avoid problems is for variables in a context to be immutable. Unfortunately, I haven’t found a better solution than contexts.

 - loc 1208 - As a module developer, you should strive to make life as easy as possible for the users of your module, even if that means extra work for you. Another way of expressing this idea is that it is more important for a module to have a simple interface than a simple implementation.

 - loc 1364 - Red Flag: Special-General Mixture  This red flag occurs when a general-purpose mechanism also contains code specialized for a particular use of that mechanism. This makes the mechanism more complicated and creates information leakage between the mechanism and the particular use case: future modifications to the use case are likely to require changes to the underlying mechanism as well.

 - loc 1500 - Each method should do one thing and do it completely. The method should have a clean and simple interface, so that users don’t need to have much information in their heads in order to use it correctly. The method should be deep: its interface should be much simpler than its implementation. If a method has all of these properties, then it probably doesn’t matter whether it is long or not.

 - loc 1507 - This form of subdivision makes sense if there is a subtask that is cleanly separable from the rest of the original method, which means (a) someone reading the child method doesn’t need to know anything about the parent method and (b) someone reading the parent method doesn’t need to understand the implementation of the child method. Typically this means that the child method is relatively general-purpose: it could conceivably be used by other methods besides the parent. If you make a split of this form and then find yourself flipping back and forth between the parent and child to understand how they work together, that is a red flag (“Conjoined Methods”) indicating that the split was probably a bad idea.

 - loc 1529 - Flag: Conjoined Methods  It should be possible

 - loc 1529 - Red Flag: Conjoined Methods  It should be possible to understand each method independently. If you can’t understand the implementation of one method without also understanding the implementation of another, that’s a red flag. This red flag can occur in other contexts as well: if two pieces of code are physically separated, but each can only be understood by looking at the other, that is a red flag.

 - loc 1626 - The exceptions thrown by a class are part of its interface; classes with lots of exceptions have complex interfaces, and they are shallower than classes with fewer exceptions.

 - loc 1637 - I should have changed the definition of unset slightly: rather than deleting a variable, unset should ensure that a variable no longer exists. With the first definition, unset can’t do its job if the variable doesn’t exist, so generating an exception makes sense. With the second definition, it is perfectly natural for unset to be invoked with the name of a variable that doesn’t exist.

 - loc 1827 - This chapter focused on exceptions, which are one of the most significant sources of special-case code, and discussed how to reduce the number of places where exceptions must be handled. The best way to do this is by redefining semantics to eliminate error conditions. For exceptions that can’t be defined away, you should look for opportunities to mask them at a low level, so their impact is limited, or aggregate several special-case handlers into a single more generic handler.

 - loc 1921 - If users must read the code of a method in order to use it, then there is no abstraction: all of the complexity of the method is exposed. Without comments, the only abstraction of a method is its declaration, which specifies its name and the names and types of its arguments and results. The declaration is missing too much

 - loc 1921 - If users must read the code of a method in order to use it, then there is no abstraction: all of the complexity of the method is exposed. Without comments, the only abstraction of a method is its declaration, which specifies its name and the names and types of its arguments and results. The declaration is missing too much essential information to provide a useful abstraction by itself.

 - loc 1990 - Developers should be able to understand the abstraction provided by a module without reading any code other than its externally visible declarations.

 - loc 2172 - Higher-level comments are more difficult to write than lower-level comments because you must think about the code in a different way. Ask yourself: What is this code trying to do? What is the simplest thing you can say that explains everything in the code? What is the most important thing about this code?

 - loc 2213 - Comments of the form “how we get here” are very useful for helping people to understand code. For example, when documenting a method, it can be very helpful to describe the conditions under which the method is most likely to be invoked (especially if the method is only invoked in unusual situations).

 - loc 2219 - abstraction. The only way to describe an abstraction is with comments. If you want code that presents good abstractions, you must document those abstractions with comments. The first step in documenting abstractions is

 - loc 2220 - If you want code that presents good abstractions, you must document those abstractions with comments. The first step in documenting abstractions

 - loc 2220 - If you want code that presents good abstractions, you must document those abstractions with comments. The first step in documenting abstractions is to separate interface comments from implementation comments.

 - loc 2224 - If interface comments must also describe the implementation, then the class or method is shallow.

 - loc 2496 - I have recently been experimenting with an approach where cross-module issues are documented in a central file called designNotes. The file is divided up into clearly labeled sections, one for each major topic.

 - loc 2512 - Then, in any piece of code that relates to one of these issues there is a short comment referring to the designNotes file:

 - loc 2648 - If it’s hard to find a simple name for a variable or method that creates a clear image of the underlying object, that’s a hint that the underlying object may not have a clean design.

 - loc 2654 - Consistent naming reduces cognitive load in much the same way as reusing a common class: once the reader has seen the name in one context, they can reuse their knowledge and instantly make assumptions when they see the name in a different context.

 - loc 2654 - Consistent naming reduces cognitive load in much the same way as reusing a common class: once the reader has seen the name in one context, they can reuse their knowledge and instantly make assumptions when they see the name in a different context. Consistency has three requirements: first, always use the common name for the given purpose; second, never use the common name for anything other than the given purpose; third, make sure that the purpose is narrow enough

 - loc 2654 - Consistent naming reduces cognitive load in much the same way as reusing a common class: once the reader has seen the name in one context, they can reuse their knowledge and instantly make assumptions when they see the name in a different context. Consistency has three requirements: first, always use the common name for the given purpose; second, never use the common name for anything other than the given purpose; third, make sure that the purpose is narrow enough that all variables with the name have the same behavior.

 - loc 2660 - Sometimes you will need multiple variables that refer to the same general sort of thing. For example, a method that copies file data will need two block numbers, one for the source and one for the destination. When this happens, use the common name for each variable but add a distinguishing prefix, such as srcFileBlock and dstFileBlock.

 - loc 2717 - Gerrand makes one comment that I agree with: “The greater the distance between a name’s declaration and its uses, the longer the name should be.” The earlier discussion about using loop variables named i and j is an example of this rule.

 - loc 2744 - Even if you do have the self-discipline to go back and write the comments (and don’t fool yourself: you probably don’t), the comments won’t be very good. By this time in the process, you have checked out mentally.

 - loc 2766 - you write comments describing the abstractions at the beginning, you can review and tune them before writing implementation code. To write a good comment, you must identify the essence of a variable or piece of code: what are the most important aspects of this thing? It’s important to do this early in the design process; otherwise you are just hacking code.

 - loc 2766 - If you write comments describing the abstractions at the beginning, you can review and tune them before writing implementation code. To write a good comment, you must identify the essence of a variable or piece of code: what are the most important aspects of this thing? It’s important to do this early

 - loc 2766 - If you write comments describing the abstractions at the beginning, you can review and tune them before writing implementation code. To write a good comment, you must identify the essence of a variable or piece of code: what are the most important aspects of this thing? It’s important to do this early in the design process; otherwise you are just hacking code.

 - loc 2780 - The comment that describes a method or variable should be simple and yet complete. If you find it difficult to write such a comment, that’s an indicator that there may be a problem with the design of the thing you are describing.

 - loc 2797 - Writing the comments first will mean that the abstractions will be more stable before you start writing code. This will probably save time during coding. In contrast, if you write the code first, the abstractions will probably evolve as you code, which will require more code revisions than the comments-first approach.

 - loc 2822 - Ideally, when you have finished with each change, the system will have the structure it would have had if you had designed it from the start with that change in mind. To achieve this goal, you must resist the temptation to make a quick fix. Instead, think about whether the current system design is still the best one, in light of the desired change. If not, refactor the system so that you end up with the best possible design. With this approach, the system design improves with every modification.

 - loc 2829 - Whenever you modify any code, try to find a way to improve the system design at least a little bit in the process. If you’re not making the design better, you are probably making it worse.

 - loc 2844 - The best way to ensure that comments get updated is to position them close to the code they describe, so developers will see them when they change the code. The farther a comment is from its associated

 - loc 2844 - The best way to ensure that comments get updated is to position them close to the code they describe, so developers will see them when they change the code. The farther a comment is from its associated code, the less likely it is that it will be updated properly.

 - loc 2865 - In general, the farther a comment is from the code it describes, the more abstract it should be (this reduces the likelihood that the comment will be invalidated by code changes).

 - loc 2894 - If information is already documented someplace outside your program, don’t repeat the documentation inside the program; just reference the external documentation.

 - loc 2916 - Consistency creates cognitive leverage: once you have learned how something is done in one place, you can use that knowledge to immediately understand other places that use the same approach.

 - loc 2966 - Resist the urge to “improve” on existing conventions. Having a “better idea” is not a sufficient excuse to introduce inconsistencies. Your new idea may indeed be better, but the value of consistency over inconsistency is almost always greater than the value of one approach over another.

 - loc 2991 - “Obvious” is in the mind of the reader: it’s easier to notice that someone else’s code is nonobvious than to see problems with your own code. Thus, the best way to determine the obviousness of code is through code reviews. If someone reading your code says it’s not obvious, then it’s not obvious, no matter how clear it may seem to you.

 - loc 3080 - There are many things that can make code nonobvious; this section provides a few examples. Some of these, such as event-driven programming, are useful in some situations, so you may end up using them anyway. When this happens, extra documentation can help to minimize reader confusion.

 - loc 3085 - Event-driven programming makes it hard to follow the flow of control. The event handler functions are never invoked directly; they are invoked indirectly by the event module, typically using a function pointer or interface. Even if you find the point of invocation in the event module, it still isn’t possible to tell which specific function will be invoked: this will depend on which handlers were registered at runtime. Because of this, it’s hard to reason about event-driven code or convince yourself that it works. To compensate for this obscurity, use the interface comment for each handler function to indicate when it is invoked,

 - loc 3112 - This example illustrates a general rule: software should be designed for ease of reading, not ease of writing. Generic containers are expedient for the person writing

 - loc 3112 - This example illustrates a general rule: software should be designed for ease of reading, not ease of writing. Generic containers are expedient for the person writing the code, but they create confusion for all the readers that follow.

 - loc 3137 - If code is nonobvious, that usually means there is important

 - loc 3141 - To make code obvious, you must ensure that readers always have the information they need to understand it. You can do this in three ways. The best way is to reduce the amount of information that is needed, using design techniques such as abstraction and eliminating special cases. Second, you can take advantage of information that readers have already acquired in other contexts (for example, by following conventions and conforming to expectations) so readers don’t have to learn new information for your code. Third, you can present the important information to them in the code, using techniques such as good names and strategic comments.

 - loc 3201 - Developing incrementally is generally a good idea, but the increments of development should be abstractions, not features. It’s fine to put off all thoughts about a particular abstraction until it’s needed by a feature. Once you need the abstraction, invest the time to design it cleanly; follow the advice of Chapter 6 and make it somewhat general-purpose.

 - loc 3229 - The problem with test-driven development is that it focuses attention on getting specific features working, rather than finding the best design. This is tactical programming pure and simple, with all of its disadvantages.

 - loc 3236 - One place where it makes sense to write the tests first is when fixing bugs. Before fixing a bug, write a unit test that fails because of the bug.

 - loc 3257 - Although it may make sense to use getters and setters if you must expose instance variables, it’s better not to expose instance variables in the first place. Exposed instance variables mean that part of the class’s implementation is visible externally, which violates the idea of information hiding and increases the complexity of the class’s interface.

 - loc 3349 - When redesigning for performance, try to minimize the number of special cases you must check. Ideally, there will be a single if statement at the beginning, which detects all special cases with one test.

