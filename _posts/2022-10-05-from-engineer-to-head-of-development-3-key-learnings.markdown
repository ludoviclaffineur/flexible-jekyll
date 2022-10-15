---
layout: post
title: From engineer to head of development&#58; 3 key learnings 
date: 2022-10-05 10:05:20 +0200
img: from_soft_en_hod.jpg # Add image post (optional)
description: "Sharing 3 key learning from my 5 year experience as an engineer in a growing company"
tags: [career]
---

When I started my journey as a software engineer in my last company, I had no idea that I would end up in a team leading/engineer manager role. This happens frequently with fast-growing companies, where founding engineers evolve to a leader role quickly without being really prepared (that's where the fun is, right?). It's challenging to be promoted from a building role (where you are in charge to discuss and deliver a scope) to a role where your team needs to commit on a deadline where the scope, feasibility and timing are keys and are most of the time not _totally_ under your control. This post will introduce struggles I faced with 3 key learnings I would have like to know when starting this journey.

<div class="banner">
This post relates to my experience and what I faced during the past 5 years. This is probably not what other founding engineers might have faced in other companies.
</div>

## Founding software engineer

When joining an early stage company, everyone is taking extra responsibilities (even if they are not the best to do it) to run the business and it goes the same way for the software engineer role that requires much more than coding skills. Your main asset at that time is probably <mark>communication</mark> because this is the time when everything _looks_ possible and being able to communicate internally and externally about what you are able to do will definitely help the company to achieve their objectives.

Also, it's a green field with very little technical debt so you can build everything (disclaimer: you certainly should not). The most tricky part is to iterate fast and <mark>validate business hypothesis with as less developments as possible</mark>, nobody wants to invest your time in something that might be discarded next month because nobody is using it. 

Also, your time will be spread into other topics than pure development. To make it more tangible, this is a list of tasks I did on a regular basis the first year at the company:

### Tech:
- Architecture decision
- Developing
- Testing
- Shipping
- DevOps
- Analyse external solutions to accelerate the development
- Documentation

### Product Management:
- Providing feedback from bugs and limitations of the solution
- Defining user stories
- Data analysis
- Project management

### External communication:
- Reassure partners that you are a trustworthy tech department
- Going to events to sell/explain the solution
- Users' feedback management (support, bug)

Concretely, some mornings you will have to isolate yourself to ship that feature at the end of the sprint and the next day, you are going to explain and sell the solution to external parties in order to get access to their API.

<mark>The asset for a company is to have a communicative engineer able to solve problems.</mark> As the company has at best some traction, no product and of course no product market fit (PMF), the usual mindset is to be fast in the delivery with a scope that is quite important. At that time, you are ready to build anything that must be rebuilt when the PMF has been found. Say hello to technical debt, no code solutions and manual work!


<div class="banner">
This stage has the incredible power that alignment across people is easy as you work all together in the same place. The tech team (very small) is also very confident about what they are able to deliver.
</div>

## From building to leading
The company is getting more funds to accelerate the development so, good news, the tech team is growing! As you are the one who participated to most of the development you start to onboard new team members on the different codebases, make sure they understand product requirements and you review the code/features because you know the dark places of the code. You naturally receive a title according to these new responsibilities as you are less and less developing new features.

<mark>Your role start to shift from solving problems to creating stability, process, common understanding and standards.</mark> You are not in a very small team and having team members with different experiences can lead to frustrations and inconsistencies in the way of delivering features as a whole. The team needs to set standard ways of working to avoid arguing on an architecture decision in every pull request to provide clear rules of the games for new players/joiners.

At this stage you start to understand that your biggest strength for the team is probably not producing code itself as you hired experienced software engineers for the technology you used but the knowledge you have on the business, software and past implementations, you have a global vision. You start to ask yourself more and more: <mark>What did we forget to think about this feature at this stage and might fire back in a later stage of development?</mark>

On a regular basis, you find gaps in the way a feature is being implemented and you communicate your findings proactively to the team and product managers and ask them how we should deal with this new information. Side story: the team starts to know that if you unexpectedly join a meeting , it's probably to bring _bad_ news meaning that something popped out that we did not think about earlier. It means most of the time _gap in the story_, AKA part of experience is not covered. It can be purely on the development part (adding some missing security,...) or the experience outside of the development: we send emails, are the templates ready, translated ? Most of the time, as part of the experience is not covered, there are 3 options: drop that part and manage user's expectations, find a workaround outside the development team to keep the deadline or the team needs to develop it, creating delays.


The logical reaction of the team is following: next time, they will involve you in all scope and implementation discussions which is not scalable and is quite schizophrenic for you. The biggest challenge is to transfer your knowledge and make stakeholders aware that the team needs to learn, thus, needs to fail and your support throughout this process is key — <mark>don't be the safety net for your team but help them to recover from failures.</mark> At the beginning the team velocity will probably be slower than at the previous stage.

That is also the moment you most of the time have to focus as the CTO plays the cross team alignment role and set the vision, your role becomes more and more precise and that's the moment you and the team start to tackle the big part of the technical debt. You focus on an area and delegate parts of the codebase to other technical lead, so they can move their own pace. You start to loose the control on implementations but most of the time you keep the global picture

## Key learnings

### Setting standards and governance rules early ease onboarding of new teammates
Loads of frustration of team members from bad or not defined code practices or worse, multiple code practices in one codebase. Early on, make it clear on what are the values of the team, how we operate things and what are the standard rules of coding.

### At early stage an easy solution that needs to be rebuilt is better that a complex one
Don't built a solution for scaling at the first stage of your company. When the company grows there are a lot of time wasted in processes in general (can be in the IT solution or anywhere else) you can sometimes predict them before actually facing them but if your sales is not growing fast, you don't need to care too much. The first metrics should be how fast you can add and remove features from the codebase. Onboarding time should be less than a few days to be able to add a small feature and a few weeks to really find your way in the codebase. Also don't be too creative for your first architectures and use (a standard) one and stick to it. New joiners will thank you and will reduce the amount the questions.

<div class="banner">
Make it work, make it right and then make it fast. 
</div>


### Having a high performing team requires time

This is one of the most complex learning to apply. Having a high performing team require time. You can't really control how quick the company evolves but hiring good team members is a given and they need time to work well and fast together. Team members need to be happy and thrilled by the challenge. This requires soft skills skill such as patience, empathy and people management. On the otherwise, the team must have a clear vision and objectives so everybody feels the boat is going in the right direction. 

