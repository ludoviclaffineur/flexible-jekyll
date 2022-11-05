---
title: "Context is everything"
header:
  overlay_image: "/assets/images/context-fire.jpg"
  og_image: "/assets/images/context-fire.jpg"
  caption: "Photo credit: [**IT Crowd**](https://www.youtube.com/watch?v=1EBfxjSFAxQ)"
tagline: "Why your team is not taking good decisions?"
img: "/assets/images/context-fire.png"
last_modified_at: 2022-10-29 10:05:20 +0200
related: false
published: true
---

Witnessing poor decision making is frustrating, particularly if that comes from your team, right? Especially a decision on a rather simple issue not requiring your input at first glance. In the vast majority of occurrences, the inability for a team to make wise decisions finds its root-causes in the lack of context and the broader comprehension of the issue. I will share with you two personal experiences to dig further on the underlying causes and discuss mitigation actions.

## The Chinese whispers game

Customer's feedbacks are a the only thing that matters in product development. Feedbacks are the source for vision, improvements and fixes. Key challenge is often about the processing of the feedback as your organization is growing with more and more specialized teams. Fig. 1 shows a classic (simplified) customer's feedback loop within a company.

<div class="center">
<p>
<img src="/assets/images/context-customer-feedback.png" alt="Customer's feedbacks" width="40%" /><br/>
Fig. 1: Customer's feedback loop</p>
</div>

A typical example is a client contacting the customer service to communicate a need or an issue about your product or service. On that basis, the support team categorizes the request as an enhancement that ought to be added to the product (feedback) backlog. The product team then conducts further research and validates the proposed solutions (also referred to as features). The product team then asks the tech team for estimates, or in more experienced teams, the product team talks with the tech lead during the validation process to confirm the viability of the solution. The tech team then creates the customer-facing solution. Everyone is happy including the consumer who finally receives the new feature, which fixes his original issue.

Everyone's roles are defined on paper, and the outcome should take care of the customer's issue. The truth might be a little more complex than you had anticipated. Information is interpreted and transferred from one person to another at every stage of the process.

- **Customer to support:** Did the support staff properly understand the need that the consumer expressed? The purpose of the support crew is to assist customers, not to conduct product research. Their objective is to determine whether they need to take additional actions or whether it qualifies as an improvement, in which case it is forwarded to the product team.

- **Support team to product team:** support team has qualified the ticket and transmit a summary of the user feedback to the product team.

- **Product team digests the feedback:** the product team analyzes and bundles feedbacks into a new epic. They _should_ confront the solution to the set of users for validation and aligned it with development teams. Is this validation always done? not necessary.

- **Product team to tech team:** Tech team mostly receives the solution to implement and they need to provide estimates. Most of the time, they are not challenging the necessity of this feature and accept to build it. It even occurs that tech team members don't even know what customer's problems they are trying to solve. To draw an analogy, it would be similar to asking a builder to construct a wall without specifying which area of the home it should go in.

<div class="banner">
You can perceive that:
<ul>
<li> Customers might not have their needs correctly expressed or understood.</li>
<li> Parties interpret and communicate information to another, dissolving the essence of customer's feedback.</li>
<li> Tech team might not be confronted to the initial feedback when they are developing and when they fell on a pitfall they might take decisions, in good faith, that will just far them away from the initial problem.</li>
</ul>
</div>

For instance, when a tech team is having a hard time finishing a feature, they will reduce the scope in order to keep the deadline. They will make _product_ decisions and if they don't have their north star, you might get a new feature that does everything but address the initial complaint. Even worse, it can increase consumer annoyance because they were counting on the functionality to fix their issue.

This is what happens <mark>when the tech team is not properly informed of the business context or product vision and does not comprehend the larger plan underlying the feature.</mark>

The illustration was based on consumer feedback, but it may also be used with service businesses where clients’ requests are in a similar fashion absorbed by different people and not sufficiently questioned along the process. As a result, you might end-up creating useless features:
- Feature does not address a true customer need. Customer thinks he needs something while actually he does not.  [Odoo implementation methodology](https://www.odoo.com/openerp_portal/static/src/pdf/odoo_implementation.pdf) is quite impressive on how far they are challenging customer needs.
- Feature needs to be maintained afterward while having a very low value for other customers — in other words, technical debt.

That's why the role of product manager / business analyst is key in passing information to the tech team:
- go into great detail regarding the issues that the users are facing with and why the problem need to be solved.
- come with well-described problems and prioritized usecases to address issues.

By taking those steps, the tech team will be empowered to solve problems rather than purely shipping features. As a result they will get better at making wise business decisions as they will be aware of the nature of the issue, the reasons why it needs to be fixed, and the critical business constraintes for which no concession is allowed.

## The tunnel vision
The team may encounter obstacles during the development phase, and occasionally a significant amount of time is invested without a clear answer emerging. Some time ago, I dealt with the integration of a third-party single sign-on (SSO). The front-end team was having a really difficult time confirming that the feature was correctly implemented on their end, and they were driving themselves crazy because, in their opinion, they did not receive the correct response from the back-end, which informed them that the issue was on not on their end as it was working for other front-end teams.

The biggest problem was that the team was working in two different silos rather than together, which made it difficult for them to communicate effectively. As a result, the front end team was developing quite blindly because they were not receiving enough context. Additionally, none in the teams took the time to discuss the issue with each other from a higher perspective because they all believed it was the other team members' fault. Both were blocked at a detailed implementation level (in this case, not obtaining the right tokens), but no one questioned if they were using the right SSO, whether the account was set up properly, or what goal they were trying to accomplish from a user's perspective.


Both teams were subject matter experts in their own fields, but they both had tunnel vision and didn't see how the other piece fit together nor take a step back to retell the business story. Moreover, the more time a team spends working on a subject, the more certain they become that they grasp it and the less they wonder if they are working on the same or the genuine problem. They weren't resolving the same problem in this case.


A generalist tech lead should be hired in this case because he can force communication between the stakeholders and elevate the conversation to a systemic level. To ensure that everyone has received adequate context and is comprehending at the same level, he might play the [rubber duck](https://en.wikipedia.org/wiki/Rubber_duck_debugging) or offer the needed knowledge between teams. What does that mean?

As this generalist tech lead should have a broader view on the different systems, he will typically
 - Ask high level questions about the problem. 
 - Ensure that everyone on the team uses the same language by eliminating all jargon,
 - Restate the issue until all parties involved concur,
 - Isolate where the root cause doesn’t lie with certainty and where are the remaining options to investigate,
 - Help the team generate a list of steps to confirm the core cause.
 - Assist the team in identifying any risks associated with the solution, such as delays, data integrity, and breaking changes.





