---
layout: page_event
hide_hero: true
title: "PinT 2025: 14th Workshop on Parallel-in-Time Integration"
date: 2024-04-13 12:00:00 +0000
event_location: Edinburgh, UK
event_start: 2025-07-07 00:00
event_end: 2025-07-11 24:00
event_url: https://icms.ac.uk/activities/workshop/parallel-in-time-algorithms-for-exascale-applications
navbar: Events
subnavbar: Upcoming
organizers:
  - name: Jemma Shipton
    homepage: https://mathematics.exeter.ac.uk/people/profile/index.php?web_id=js1075
  - name: David Acreman
    homepage:
  - name: Beth Wingate
    homepage: https://mathematics.exeter.ac.uk/people/profile/index.php?web_id=bw290
  - name: Hiroe Yamazaki
    homepage: https://www.imperial.ac.uk/people/h.yamazaki
invited:
  - name: Josh Hope-Collins
  - name: Juliane Rosemeier
  - name: Giancarlo Antonucci
  - name: Rob Falgout
  - name: Felix Kwok

permalink: /events/14th-pint-workshop/
page_type: event_page
no_lead: true
---

### Brief overview

PinT 2025: the 14th Workshop on Parallel-in-time Integration will be hosted at the ICMS in Edinburgh, UK.
Please visit the [conference website for more information.](https://icms.ac.uk/activities/workshop/parallel-in-time-algorithms-for-exascale-applications/)

### Closing Discussion

#### Main Actions

- Redundant computation discussion: [Hans](https://crd.lbl.gov/divisions/amcr/computational-science-dept/anag/about/staff-and-postdocs/hans-johansen/) agreed to summarize.
- Collation of introductory material and example code on website ([Thibaut](https://github.com/tlunet) and [Jemma](https://github.com/jshipton)?)
- [Daniel](https://github.com/danielru) to share admin permissions for email list - we need to check that the join-up procedure is working!
- [Thibaut](https://github.com/tlunet), [Thomas](https://github.com/brownbaerchen) and [Julius](https://www.linkedin.com/in/juliusosatoehigie) to discuss how to implement Julius’s time-parallel RK - start with mpi4py tutorials. Could a short answer to the question "I'd like to code my method in parallel, where should I start?" could go somewhere on the website? Basically just a pointer to mpi4py (and maybe some examples e.g. of the ensemble communicator in [Firedrake](https://www.firedrakeproject.org/)).

#### Full Summary

- Redundant computation ([Hans](https://crd.lbl.gov/divisions/amcr/computational-science-dept/anag/about/staff-and-postdocs/hans-johansen/) to summarize).
- [Martin](https://www.unige.ch/~gander) cautioned against the use of the word “optimal” without more specific information - this comes from the DD community where it really means “mesh independent scaling”.
- Does PinT work for hyperbolic problems? See [Martin’s Acta Numerica paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E580B25A44766E6729A65D7AF05B1198/S0962492924000072a.pdf/time_parallelization_for_hyperbolic_and_parabolic_problems.pdf) - there are many methods that are not multilevel that can work. Multilevel is a challenge.
- [Josh](https://github.com/JHopeCollins) pointed out a common subproblem shared by ParaDiag and REXI methods: solution of systems that look like backwards Euler steps with complex timestep (which [Colin](https://github.com/colinjcotter) clarified lead to an indefinite-Helmholtz-like problem on elimination to one variable).
- Test problems: these help us to connect with the applications and each other. e.g. equations with fast singular limits / slow attractors - can we find any new and common test problems?
- How do we get domain scientists to adopt time-parallel methods? Need to show speed up for problems they care about. Find people who are really experiencing the bottleneck preventing them from doing exciting science. This would help answer the question "What is the PinT killer-app??" ... I’m not sure we answered this!!
- Next meeting:
  - When and where: Linz w/c 29th June but [Martin](https://www.unige.ch/~gander) pointed out that it clashes with SciCADE so it might shift by a week. Not yet announced on the website.
  - “Lightning” talks to introduce people early on in the meeting. Suggestion from [Daniel](https://github.com/danielru) to do 30min sessions of 60s talks on the first/second days - just one slide to introduce who you are and what you do.
  - Could we run introductory / tutorial sessions to introduce the different methods? This requires considerable effort and additional funding but is a good idea. Instead we will collate material on the parallel-in-time website (see below).
  - T-Shirts?!
- PinT website:
  - [Daniel](https://github.com/danielru) encouraged people to keep the references section of the website up to date. I think it would help to have the link at the top of the references page point directly to: https://github.com/Parallel-in-Time/parallel-in-time.github.io/wiki/Adding-Publications#steps-for-adding-a-new-publication ✅
  - [Martin](https://www.unige.ch/~gander) pointed out that there are a lot of links to click through for the workshops and sometimes it is hard to find the link to the main workshop page. ✅
  - [Daniel](https://github.com/danielru) pointed out that the “Codes” section of the website is not up to date and this could be a good place to collate the introductory material. [Thibaut](https://github.com/tlunet) offered to help with this ([Jemma](https://github.com/jshipton) is also happy to help!).
