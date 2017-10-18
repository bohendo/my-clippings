
---
#  Threat Modeling
## by Adam Shostack
---

 - loc 594 - Adding boundaries to show who controls what is a simple way to improve the diagram. You can pretty easily see that the threats that cross those boundaries are likely important ones, and may be a good place to start identifying threats.

 - loc 594 - Adding boundaries to show who controls what is a simple way to improve the diagram. You can pretty easily see that the threats that cross those boundaries are likely important ones, and may be a good place to start identifying threats. These boundaries are called trust boundaries, and you should draw them wherever different people control different things. Good examples of this include the following: Accounts (UIDs on unix systems, or SIDS on Windows) Network interfaces Different physical computers Virtual machines Organizational boundaries Almost anywhere you can argue for different privileges

 - loc 605 - A system that exposes lots of interfaces presents a larger attack surface than one that presents few APIs or other interfaces. Network firewalls are useful boundaries because they reduce the attack surface relative to an external attacker. However, much like the Captain's safe, there are still trust boundaries inside the firewall. A trust boundary and an attack surface are very similar views of the same thing. An attack surface is a trust boundary and a direction from which an attacker could launch an attack.

 - loc 624 - You should think of threat model diagrams as part of the development process, so try to keep it in source control with everything else.

 - loc 670 - STRIDE is a mnemonic for things that go wrong in security. It stands for Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege:

 - loc 809 - if you're getting data from a shared memory segment, is it ACLed so only the other process can see it?

 - loc 841 - Addressing repudiation is generally a matter of ensuring that your system is designed to log and ensuring that those logs are preserved and protected.

 - loc 915 - Work to ensure attacker resource consumption is as high as or higher than yours.

 - loc 920 - Look for places where attackers can multiply CPU consumption on your end with minimal effort on their end: Do something to require work or enable distinguishing attackers, such as client does crypto first or login before large work factors (of course, that can't mean that logins are unencrypted).

 - loc 988 - Command injection attacks Be careful. Validate that your input is the size and form you expect. Don't sanitize. Log and then throw it away if it's weird.

 - loc 994 - Validate, Don't Sanitize Know what you expect to see, how much you expect to see, and validate that that's what you're receiving. If you get something else, throw it away and return an error message.

 - loc 996 - If you get something else, throw it away and return an error message. Unless your code is perfect, errors in sanitization will hurt a lot, because after you write that sanitize input function you're going to rely on it. There have been fascinating attacks that rely on a sanitize function to get their code into shape to execute.

 - loc 1055 - Don't have data sinks: You write the data for a reason. Show who uses it. Data can't move itself from one data store to another: Show the process that moves it.

 - loc 1067 - “All models are wrong. Some models are useful.” Therefore, when you're adding additional diagrams, don't ask, “Is this the right way to do it?” Instead, ask, “Does this help me think about what might go wrong?”

 - loc 1256 - As a precursor to brainstorming (or any other approach to finding threats), reviewing threats to systems similar to yours is a helpful starting point in threat modeling. You can do this using search engines, or by checking the academic literature and following citations. It can be incredibly helpful to search on competitors or related products. To start, search on a competitor, appending terms such as “security,” “security bug,” “penetration test,” “pwning,” or “Black Hat,” and use your creativity.

 - loc 1259 - To start, search on a competitor, appending terms such as “security,” “security bug,” “penetration test,” “pwning,” or “Black Hat,” and use your creativity.

 - loc 1284 - When it's hard to answer “What's your threat model?” people often use an approach centered on models of their assets, models of attackers, or models of their software. Centering on one of those is preferable to using approaches that attempt to combine them because these combinations tend to be confusing.

 - loc 1320 - It turns out that focusing on assets is less useful than you may hope,

 - loc 1331 - There are three ways the term asset is commonly used in threat modeling: Things attackers want Things you want to protect Stepping stones to either of these

 - loc 1388 - There's no direct line from assets to threats, and no prescriptive set of steps. Essentially, effort put into enumerating assets is effort you're not spending finding or fixing threats. Sometimes, that involves a discussion of what's an asset, or which type of asset you're discussing. That discussion, at best, results in a list of things to look for in your software or operational model, so why not start by creating such a model?

 - loc 1430 - attacker lists or even personas are not enough structure for most people to figure out what those people will do. Engineers may subconsciously project their own biases or approaches into what an attacker might do.

 - loc 1510 - DFDs consist of numbered elements (data stores and processes) connected by data flows, interacting with external entities (those outside the developer's or the organization's control).

 - loc 1621 - If you find a trust boundary crossing an element of a diagram other than a data flow, either break that element into two (in the model, in reality, or both), or draw a subdiagram to show them separated into multiple entities.

 - loc 1626 - The trust boundaries delineate the attack surface between principals. This leads some to expect that threats appear only between the principals on the boundary, or only matter on the trust boundaries. That expectation is sometimes incorrect.

 - loc 1640 - Therefore, it is more accurate to say that threats tend to cluster around trust boundaries and complex parsing, but may appear anywhere that information is under the control of an attacker.

 - loc 1671 - Data flows should almost never be labeled using verbs. Even though it can be hard, you should work to find more descriptive labels than “read” or “write,” which are implied by the direction of the arrows. In other words, data flows communicate their information (nouns) to processes, which are active: verbs, verb phrases, or verb/noun chains.

 - loc 1677 - Generally, using a single counter for everything is less confusing. You can say “number 1” rather than “data flow 1, not process 1.”

 - loc 1725 - Don't have data sinks: You write the data for a reason. Show who uses it. Data can't move itself from one data store to another: Show the process that moves it. All ways data can arrive should be shown. If there are mechanisms for controlling data flows (such as firewalls or permissions) they should be shown. All processes must have at least one entry data flow and one exit data flow.

 - loc 1957 - Links are often left out of integrity checks.

 - loc 1959 - cache poisoning attacks insert data into web caches

 - loc 2994 - There are many tools you can use to find privacy issues, including Solove's taxonomy of privacy harms.

 - loc 8984 - “those who don't understand Unix are condemned to reinvent it, poorly.”

 - loc 8984 - Henry Spencer said, “those who don't understand Unix are condemned to reinvent it, poorly.”

