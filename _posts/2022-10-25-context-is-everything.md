---
title: "Context is everything"
header:
  overlay_image: "/assets/images/context-fire.png"
  og_image: "/assets/images/context-fire.png"
  caption: "Photo credit: [**IT Crowd**](https://www.youtube.com/watch?v=1EBfxjSFAxQ)"
tagline: "Why your team does not take good decisions?"
img: "/assets/images/context-fire.png"
last_modified_at: 2022-10-05 10:05:20 +0200
related: false
published: true
---

It's always frustrating when your team does not take good decisions, right? Certainly when it looks like an _easy_ one to take, one that should not require your input. Most of the time, the reason why team fails to take good decisions is that they don't have the right context and understanding of the problem. This post will explain some of the root causes through XXX stories and how to prevent them.

## The Chinese whispers game

Customer's feedbacks are a the only thing that matter in product development. The feedbacks are the source for vision, improvements and fixes. When an organisation is growing teams are getting more and more specialized and the feedback needs to be _processed_. Fig. 1 shows a classic (simplified) customer's feedback loop within a company.

<img src="/assets/images/context-customer-feedback.png" alt="Customer's feedbacks" width="40%" />
Fig. 1: Customer's feedback loop

Most of the time, the customer contacts support team to express a problem or a need. Support team qualifies the request and states that it's an improvement that should go to the product (feedback) backlog. Feedbacks are then researched and solutions (a.k.a. features) are validated by the product team (n.b.: it's intentionally oversimplified as we could have a specific post around feedback and product management). Then the product team goes to the tech team for estimates or in more mature teams, product during the validation precess discuss with the tech lead in order to validate the feasibility of the solution. Then the tech team develops the solution to the customer. Finally the customer receives the new feature, solving his inital problem, and everyone is happy! 

On paper, everyone has clear responsibilities and the result should solve the problem of the customer. The reality can be a bit more complicated than expected. At every step of the process, information are passed from one person to another.

- **Customer to support:** the customer express a need but did the support understand correctly? Support team's goal is to support people not to do product research. Their goal is to know if they need to take further action or is it qualified as an improvement meaning passed to the product team.

- **Support team to product team:** support team has qualified the ticket and transmit a summary of the user feedback to the product team.

- **Product team digests the feedback:** the product team analyse and bundle feedbacks into a new epic. The solution _should_ confront the solution to the set of users for validation and aligned with development teams. Is this validation always done? not necessary.

- **Product team to tech team:** Tech team mostly receive the solution to implement and they need to provide estimates. Most of the time, they are no challenge about the necessity of this feature and accept to build it. It even occurs that tech team members don't even know what customer's problems they are trying to solve. To give an analogy, it's like you ask a buidler to build a wall but he does not know for what part of the house it belongs. 

<div class="banner">
You can perceive that:
<ul>
<li> Customers might not express their needs properly.</li>
<li> Parties interprete and communicate information to another, dissolving the essence of customer's feedback.</li>
<li> Tech team might not be confronted to the initial feedback when they are developing and when they felt on a pitfall they might take decisions, in good faith, that will just prevent solving the initial problem.</li>
</ul>
</div>


For instance, when a tech team is getting a hard time to finish a feature, they will reduce the scope in order to keep the deadline. They will take _product_ decisions and if they don't have their north star, you can have a new feature that is doing everyuthing but solving initial feedback. Even worse, it can lead to more frustrations from the customer as they were hoping from the feature to have their problem resolved.

This is what happened when the business context is not correctly passed to the tech team and the tech team does not understand the bigger plan behind the feature. It can also happen when the product vision behind the feature is not fully understood by the tech team.


context:

- Business context
- Technical context
- Team context
