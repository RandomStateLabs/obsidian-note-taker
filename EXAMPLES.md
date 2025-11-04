# Usage Examples

This document provides practical examples of using the Obsidian Note-Taker skill in Claude Code.

## Example 1: Creating a Technical Architecture Note

### User Request
```
Create a note documenting our new microservices authentication system
```

### Skill Output

**File**: `1 - Main Notes/Architecture/Microservices Authentication System.md`

```markdown
---
date: 2025-11-04
status: capture
type: architecture
tags:
  - architecture
  - authentication
  - microservices
  - security
---

# Microservices Authentication System

## Overview
[High-level description of the authentication system and its purpose]

## System Context
[How this system fits within the broader microservices ecosystem]

## Key Components

### API Gateway
- **Purpose**: Central entry point for authentication
- **Technology**: Kong/Nginx
- **Interfaces**: REST API, OAuth endpoints

### Auth Service
- **Purpose**: Token validation and user management
- **Technology**: Node.js, JWT
- **Interfaces**: gRPC, Redis cache

## Data Flow
[Describe authentication flow through the system]

## Technical Decisions
- **JWT vs Session**: JWT chosen for stateless scalability
- **OAuth 2.0**: Industry standard for authorization

## Security Considerations
[Authentication, authorization, token expiration, rate limiting]

## Scalability Strategy
[Horizontal scaling, caching strategy, load balancing]

## Monitoring & Observability
[Auth metrics, failed login tracking, latency monitoring]

## Related Notes
- [[API Gateway Configuration]]
- [[Security Best Practices]]
- [[OAuth Implementation Guide]]
```

### Why This Template?
- Identified as **technical/architecture** content
- Placed in `1 - Main Notes/Architecture/`
- Uses architecture-specific template with components, decisions, security
- Adds relevant technical tags

---

## Example 2: Capturing a Business Idea

### User Request
```
I have an idea for a SaaS tool that helps developers automatically generate API documentation from code comments
```

### Skill Output

**File**: `Personal/Thoughts & Ideas/API Documentation Generator.md`

```markdown
---
date: 2025-11-04
status: capture
type: idea
tags:
  - business
  - saas
  - developer-tools
  - api
---

# API Documentation Generator

## Executive Summary
A SaaS platform that automatically generates beautiful, interactive API documentation from inline code comments and type definitions.

## Problem Statement
- **Who**: Software development teams building APIs
- **What**: Manual API documentation is time-consuming and often outdated
- **Why**: Developers hate writing docs; stale docs frustrate API consumers
- **Current Solutions**: Swagger/OpenAPI (manual), JSDoc (basic), Postman (not integrated)

## Proposed Solution
AI-powered tool that:
1. Scans codebase for API endpoints
2. Extracts comments, types, and examples
3. Generates interactive documentation
4. Auto-updates on code changes
5. Provides try-it-now playground

## Value Proposition
- Save 10+ hours per week on documentation
- Always up-to-date docs synced with code
- Better developer experience for API consumers
- Supports multiple languages and frameworks

## Business Model
- **Revenue Streams**:
  - Freemium SaaS ($0 for public projects, $29-99/month for teams)
  - Enterprise on-premise deployment
  - API access for integration
- **Cost Structure**:
  - Cloud hosting and processing
  - AI inference costs
  - Customer support
- **Pricing Strategy**:
  - Free tier for open source
  - Team tier at $49/month
  - Enterprise custom pricing

## Market Analysis
- **Market Size**:
  - TAM: All software companies building APIs (millions)
  - SAM: Dev teams of 5+ people (hundreds of thousands)
  - SOM: Early adopters in tech hubs (thousands)
- **Competition**:
  - Swagger/OpenAPI (manual, established)
  - ReadMe.io (documentation hosting)
  - GitBook (general docs, not API-focused)
- **Target Customer**:
  - Startups and scale-ups with API products
  - Engineering managers tired of doc maintenance
  - Developer experience teams

## Implementation Roadmap

### Phase 1: MVP (0-3 months)
- [ ] Build code parser for top 3 languages (Python, JavaScript, Go)
- [ ] Create basic documentation UI
- [ ] Implement GitHub integration
- [ ] Launch beta with 10 pilot customers

### Phase 2: Growth (3-6 months)
- [ ] Add interactive API playground
- [ ] Support 5 more languages
- [ ] Build CI/CD integration
- [ ] Implement team collaboration features

## Success Metrics
- 100 beta signups in first month
- 10 paying customers by month 3
- 90% customer satisfaction score
- <2% monthly churn

## Risks & Mitigation
- **Risk 1**: Parsing complex codebases - Start with well-structured projects, expand gradually
- **Risk 2**: Competition from established tools - Focus on AI-powered auto-generation as differentiator
- **Risk 3**: Developer adoption - Heavy focus on DX, make integration effortless

## Next Actions
- [ ] Research existing solutions more deeply
- [ ] Interview 20 potential customers
- [ ] Build proof-of-concept parser
- [ ] Create landing page and gauge interest

## Resources & References
- [API documentation best practices]
- [OpenAPI specification]
- [Developer tools market analysis]

## Related Ideas
- [[Developer Tools Market]]
- [[Code Analysis Tools]]
- [[Documentation as Code]]
```

### Why This Template?
- Identified as **business idea**
- Placed in `Personal/Thoughts & Ideas/`
- Uses comprehensive business idea template
- Includes problem-solution fit, business model, roadmap
- Actionable next steps

---

## Example 3: Meeting Notes

### User Request
```
Create notes for our Q4 planning meeting with the product team
```

### Skill Output

**File**: `Personal/Meetings/Q4 Planning Meeting - 2025-11-04.md`

```markdown
---
date: 2025-11-04
status: complete
type: note
tags:
  - meeting
  - q4-planning
  - product-team
---

# Q4 Planning Meeting - 2025-11-04

## Attendees
- Sarah (Product Manager)
- Mike (Engineering Lead)
- Jessica (Design Lead)
- You (Engineer)

## Agenda
1. Q3 retrospective
2. Q4 goals and priorities
3. Resource allocation
4. Timeline and milestones

## Discussion Points

### Topic 1: Q3 Retrospective
- Shipped 3 major features on time
- Performance improvements exceeded targets
- Customer feedback was very positive
- Technical debt increased, need to address in Q4

### Topic 2: Q4 Goals
- Focus on platform stability
- Launch mobile app MVP
- Implement advanced analytics
- Refactor authentication system

### Topic 3: Resource Allocation
- 2 engineers on mobile
- 1 engineer on auth refactor
- 1 engineer on analytics
- Rotating on-call schedule

## Decisions Made
- **Decision 1**: Delay feature X to prioritize platform stability (unanimous agreement)
- **Decision 2**: Hire 2 additional engineers for mobile team (approved by leadership)
- **Decision 3**: Implement weekly progress check-ins (starting next week)

## Action Items
- [ ] @Sarah: Create detailed Q4 roadmap - Due: 2025-11-11
- [ ] @Mike: Draft technical architecture for mobile app - Due: 2025-11-08
- [ ] @Jessica: Complete mobile app designs - Due: 2025-11-15
- [ ] @You: Research auth refactor approaches - Due: 2025-11-10

## Next Meeting
- **Date**: 2025-11-18
- **Topics**: Review Q4 progress, mobile app architecture approval

## Attachments/Resources
- [Q3 Metrics Dashboard](https://example.com/dashboard)
- [Q4 Planning Doc](https://example.com/q4-plan)

## Related Meetings
- [[Q3 Planning Meeting]]
- [[Product Roadmap 2025]]
```

### Why This Template?
- Identified as **meeting notes**
- Placed in `Personal/Meetings/`
- Date in filename for chronological sorting
- Includes attendees, decisions, action items with owners
- Links to related content

---

## Example 4: Daily Note

### User Request
```
Create my daily note for today
```

### Skill Output

**File**: `Personal/Daily Notes/2025-11-04.md`

```markdown
---
date: 2025-11-04
status: complete
type: note
tags:
  - daily-note
  - journal
---

# Daily Note - 2025-11-04

## Morning Intentions
- Main focus: Complete authentication refactor research
- Secondary: Review PR for analytics feature
- Energy level: 7/10

## Tasks
- [ ] High Priority: Research JWT vs OAuth implementation
- [ ] High Priority: Review Mike's PR #234
- [ ] Medium Priority: Write tests for API endpoint
- [ ] Low Priority: Update documentation

## Meetings & Events
- 10:00 - Daily standup
- 14:00 - 1:1 with Sarah
- 16:00 - Code review session

## Notes & Thoughts
[Capture ideas, observations, learnings throughout the day]

## Accomplishments
-
-
-

## Challenges
-
-

## Gratitude
-

## Tomorrow's Priorities
- [ ]
- [ ]

## Related Notes
- [[Weekly Review]]
- [[Q4 Goals]]
```

### Why This Template?
- Identified as **daily planning/journal**
- Placed in `Personal/Daily Notes/`
- Uses YYYY-MM-DD filename for easy sorting
- Includes intentions, tasks, reflections
- Provides structure for daily organization

---

## Example 5: Learning/Research Note

### User Request
```
I just read about the new React Server Components. Help me create a note about it.
```

### Skill Output

**File**: `Personal/Learning/React Server Components.md`

```markdown
---
date: 2025-11-04
status: develop
type: note
tags:
  - learning
  - react
  - server-components
  - web-development
---

# Learning React Server Components

## Learning Objectives
- Understand what React Server Components are
- Know when to use server vs client components
- Be able to implement server components in Next.js
- Understand the performance benefits

## Resources
- **Primary**: [React Server Components RFC](https://github.com/reactjs/rfcs/blob/main/text/0188-server-components.md)
- **Supplementary**: Next.js documentation, React blog
- **Practice**: Build demo app with server components

## Key Concepts

### Foundation Concepts
1. **Server Components**: Components that render on the server only
   - No JavaScript sent to client
   - Can access backend resources directly
   - Cannot use useState, useEffect, or browser APIs

2. **Client Components**: Traditional React components
   - Use 'use client' directive
   - Can use hooks and interactivity
   - JavaScript bundled to client

### Advanced Concepts
1. **Composition**: Server components can import client components
2. **Streaming**: Progressive rendering with Suspense
3. **Data Fetching**: Async server components

## Practice Exercises
- [ ] Create a basic server component
- [ ] Mix server and client components in one page
- [ ] Implement streaming with Suspense
- [ ] Project: Build a blog with server components

## Progress Tracking
- [x] Read RFC and documentation
- [ ] In progress: Building demo app
- [ ] Next: Deploy to production environment

## Questions & Gaps
- How do server components work with state management libraries?
- What about SEO implications?
- Performance comparison with SSR?

## Application Ideas
- Apply to current blog project
- Use for dashboard with real-time data
- Consider for next company project

## Review Schedule
- First review: 2025-11-11
- Second review: 2025-11-18
- Practice session: 2025-11-25

## Related Learning
- [[Next.js App Router]]
- [[React Performance Optimization]]
- [[Server-Side Rendering]]
```

### Why This Template?
- Identified as **learning/educational content**
- Placed in `Personal/Learning/`
- Structured for progressive learning
- Includes objectives, practice, and review schedule
- Links to related concepts

---

## Tips for Best Results

1. **Be specific about note type**: "Create a technical architecture note" vs just "create a note"
2. **Provide context**: Include key information you want in the note
3. **Mention folder preferences**: "Save in my Projects folder" if you have a preference
4. **Review and adjust**: The skill generates starting templates you can customize
5. **Use wikilinks**: Ask to "link to related notes" for better vault navigation

## Common Patterns

| Request Pattern | Note Type | Folder |
|----------------|-----------|---------|
| "document our..." | Technical | `1 - Main Notes/` |
| "I have an idea for..." | Business Idea | `Personal/Thoughts & Ideas/` |
| "meeting notes for..." | Meeting | `Personal/Meetings/` |
| "daily note" or "journal" | Daily | `Personal/Daily Notes/` |
| "I learned about..." | Learning | `Personal/Learning/` |
| "how to..." or "guide for..." | How-To Guide | `1 - Main Notes/Guides/` |

---

## Validation Example

After creating a note, validate it:

```bash
python ~/.claude/skills/obsidian-note-taker/scripts/validate_frontmatter.py "My Note.md"
```

**Output:**
```
📄 Validating: My Note.md
==================================================
✅ Frontmatter: Valid
✅ Content Structure: Good
==================================================
✨ Perfect! Note is well-formatted.
```
