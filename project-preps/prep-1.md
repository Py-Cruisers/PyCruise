# Team Agreement

## Cooperation Plan

> What are the key strengths of each person on the team?

- **Liesl**: Problem solving, adaptability, organized, prioritized
- **Dennis**: Jack of all trades, leadership, data science
- **Marco**: Back-end development, data, speaking, project mapping (trello)
- **Brentice**: Resourceful, organized  
- Dom: UX/UI

> How can you best utilize these strengths in the execution of your project?

- **Liesl**: Problem solve whenever we run into issues/bugs   - with the project. Hash it out and make a plan of action
- **Dennis**: As a jack of all trades I can adapt fairly well to different areas of a project and contribute the best I can
- **Marco**: getting a Trello board going for project workflow; database administration; working on behalf of back-end with anyone else that’s keen to join
- **Brentice**: Having someone that is resourceful allows for a problem to multiple solutions found.  
- **Dom**: Creating documentation and a deck that really delivers our MVP visually.

> In which professional competencies do you each want to develop greater strength?

- **Liesl**: Communication skills, resourcefulness, time management
- **Dennis**: I want to develop greater strength in the Craft and Communication
- **Marco**: I’m always working on improving time management, I also have a major “opportunity for growth” in front-end dev work
- **Brentice**: Problem solving skills and time management
- **Dom**: Time management is something that this course has shown me how important it is as well as problem solving skills.

> Knowing that every person in your team needs to understand all aspects of the project, how do you plan to approach the day-to-day work?

- Daily stand-ups, both before and after the work day. This will allow everyone to be able to put any concerns, questions, and/or suggestions on the table and we can discuss them through. Another way is through pair programming in which no one person is doing a portion of the project and at least two people have understanding and can expand upon it if need be.  

## Conflict Plan  

>What will be your group’s process to resolve conflict, when it arises?

When a problem arises, take the step back:

- Identify the problem/issue  
- Identify possible solutions
- With each solution, consider them in the context of MVP (time constraints, project restraints, efficiency/Big O)
- Agree on solution and move on
> What will your team do if one person is taking over the project and not letting the other members contribute?

- Address this issue as soon as possible whenever the team meets up and gets a chance. Express this concern and try to come to a middle ground (i.e. pair programming).  
- Create shared understanding and see if adjustments to the plan and division of responsibilities can be made.  

> How will you approach each other and the challenges of the project knowing that it is impossible for all members to be at the exact same place in understanding and skill level?

We strive to keep an open mindset and leave the channel open for communication and understanding. Other than mindset, we strive to keep our MVP as realistic as possible within the constraints of time and requirements. Also, there will be pair programming a majority of the time so not one person is doing part of the project.

> How will you raise concerns to members who are not adequately contributing?

Address this issue as soon as possible whenever the team meets up and gets a chance. Express this concern and try to come to a middle ground (i.e. pair programming). Create shared understanding and see if adjustments to the plan and division of responsibilities can be made.  

> How and when will you escalate the conflict if your resolution attempts are unsuccessful?

Reach out to some higher-ups (i.e. instructor, director) who have more hands on experience in conflict resolution and understand the constraints of the project week itself.  

## Communication Plan

> What hours will you be available to communicate?
- Class hours (9am-6pm)
    - *open to communication any time but not heavy workload 
> What platforms will you use to communicate (ie. Slack, phone …)?
- Slack
> How often will you take breaks?

10 minutes every hour, hour lunch at around noon

> What is your plan if you start to fall behind?

Readdress either our time management plan or see if the issue is the MVP. If the MVP is too grand for the time constraints, adjust as needed.  

> How will you communicate after hours and on the weekend?
- Slack (*open to communication any time but not heavy workload)

> What is your strategy for ensuring everyone’s voice is heard?

Stand-ups before starting the day and after the day. We will have mini-stand ups throughout the day when meeting to converse our code where we can also bring up issues/concerns. Stand-ups only end once everyone has spoken their mind.

> How will you ensure that you are creating a safe environment where everyone feels comfortable speaking up?

At daily stand-ups, give everyone the chance to speak up and express any concerns they need to, even if it’s not related to the immediate project. We will go into this project in the understanding that sometimes things may happen in daily life and work might be affected by that. In that case, we will address as need be.  

## Work Plan

> How you will identify tasks, assign tasks, know when they are complete, and manage work in general?

Create and follow an up-to-date trello (assign one person to trello to keep track).

> What project management tool will be used?

Trello

## Git Process  

> What components of your project will live on GitHub?

- Front end, back end, and all scripts/text files

> How will you share the repository with your teammates?

- Create an organization and allow access to the whole group.  

> What is your Git flow?

In doing our work on the code, we’ll checkout individual branches to work on and when we feel a feature is done, we’ll have one big merge party together to resolve any “git-uations”.  

*For example:*

1. `git pull origin <working-dev-branch>`
2. `git checkout -b <my-dev-branch>`
3. **ACP** => `git push origin <my-dev-branch>`
4. Git pull origin `<working-dev-branch>` to get the latest (to avoid merge conflicts)
5. Create a PR to `main` from `<my-dev-branch>`
6. Assign reviewers to the PR and call a meeting via agreed communications methods
7. Two members assist with code-review and bug squashing
8. Two members `Approve` the PR and merge it into `<working-dev-branch>`
9. Everyone performs: `git pull origin <working-dev-branch>` into their own `<my-dev-branch> `so they have the latest version to avoid conflict
10. When a merge conflict occurs, you need to notify the team, and the person whose code is in conflict (between the `>>>>` and `<<<<` areas) will help work through accepting changes so that previously accepted changes are not lost or otherwise altered without a PR review  


> Will you be using a PR review workflow? If so, consider:

- How many people must review a PR?
    - Two
- Who merges PRs?
    - The one built the feature/made the push  
- How often will you merge?
    - At least once per day; probably around lunch to handle any conflicts
    - Can make more merges throughout the day  
- How will you communicate that it’s time to merge?
    - Set a time and say it’s time to merge
