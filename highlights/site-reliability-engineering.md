
---
#  Site Reliability Engineering
## by Google SRE
---

 - loc 126 - much like security, the earlier you care about reliability, the better.

 - loc 326 - At their core, the development teams want to launch new features and see them adopted by users. At their core, the ops teams want to make sure the service doesn’t break while they are holding the pager. Because most outages are caused by some kind of change — a new configuration, a new feature launch, or a new type of user traffic — the two teams’ goals are fundamentally in tension.

 - loc 400 - In general, an SRE team is responsible for the availability, latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning of their service(s).

 - loc 428 - The error budget stems from the observation that 100% is the wrong reliability target for basically everything (pacemakers and anti-lock brakes being notable exceptions).

 - loc 443 - SRE’s goal is no longer “zero outages”; rather, SREs and product developers aim to spend the error budget getting maximum feature velocity.

 - loc 463 - Reliability is a function of mean time to failure (MTTF) and mean time to repair (MTTR)

 - loc 466 - Humans add latency. Even if a given system experiences more actual failures, a system that can avoid emergencies that require human intervention will have higher availability than a system that requires hands-on intervention.

 - loc 771 - a user on a 99% reliable smartphone cannot tell the difference between 99.99% and 99.999% service reliability!

 - loc 813 - we define availability in terms of the request success rate.

 - loc 878 - If we were to build and operate these systems at one more nine of availability, what would our incremental increase in revenue be? Does this additional revenue offset the cost of reaching that level of reliability?

 - loc 1017 - We use intuition, experience, and an understanding of what users want to define service level indicators (SLIs), objectives (SLOs), and agreements (SLAs).

 - loc 1017 - We use intuition, experience, and an understanding of what users want to define service level indicators (SLIs), objectives (SLOs), and agreements (SLAs). These measurements describe basic properties of metrics that matter, what values we want those metrics to have, and how we’ll react if we can’t provide the expected service.

 - loc 1245 - Toil is the kind of work tied to running a production service that tends to be manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows.

