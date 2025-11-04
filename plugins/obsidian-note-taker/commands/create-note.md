---
description: Quickly create a well-formatted Obsidian note with proper frontmatter and template structure
---

# Create Obsidian Note

You are now in **Create Note Mode**. Help the user create a well-formatted Obsidian note following the obsidian-note-taker standards.

## Workflow

1. **Gather Information**
   Ask the user:
   - What is this note about? (topic/content)
   - What type of note? (technical, idea, meeting, daily, learning)
   - Where should it be saved? (or auto-suggest based on type)

2. **Determine Note Type**
   Based on user input, select template:
   - **Technical** → Architecture, Guide, or Technical Note template
   - **Business/Idea** → Business Idea or Project Brainstorm template
   - **Personal** → Meeting Notes or Daily Note template
   - **Learning** → Literature Note or Learning Note template

3. **Generate Frontmatter**
   Create YAML frontmatter:
   ```yaml
   ---
   date: YYYY-MM-DD        # Today's date
   status: capture          # capture, develop, refine, complete
   type: note               # note, guide, architecture, workflow, idea
   tags:
     - relevant-tag
     - another-tag
   ---
   ```

4. **Apply Template**
   Use the appropriate template from:
   `plugins/obsidian-note-taker/skills/obsidian-note-taker/references/templates.md`

5. **Suggest Folder**
   Based on type:
   - Technical → `1 - Main Notes/` (or subfolder)
   - Ideas → `Personal/Thoughts & Ideas/`
   - Meeting → `Personal/Meetings/`
   - Daily → `Personal/Daily Notes/`
   - Learning → `Personal/Learning/`

6. **Format Filename**
   - Title Case with spaces
   - Remove special characters: `: / \ | * ? " < >`
   - Keep under 60 characters
   - Example: `System Architecture Overview.md`

7. **Present Note**
   Show the complete note with:
   - Full frontmatter
   - Template structure filled in
   - Suggested file path
   - Filename

## Templates Quick Reference

### Technical Note
```markdown
---
date: YYYY-MM-DD
status: capture
type: note
tags:
  - technical
  - [domain]
---

# [Title]

## Overview
[Brief description]

## Key Concepts
- Point 1
- Point 2

## Details
[Main content]

## Related Notes
- [[Related Note]]
```

### Business Idea
```markdown
---
date: YYYY-MM-DD
status: capture
type: idea
tags:
  - business
  - idea
---

# [Idea Title]

## Problem Statement
[What problem does this solve?]

## Proposed Solution
[The solution]

## Next Steps
- [ ] Action item 1
- [ ] Action item 2

## Related Ideas
- [[Related Idea]]
```

### Meeting Notes
```markdown
---
date: YYYY-MM-DD
status: complete
type: note
tags:
  - meeting
  - [team/project]
---

# [Meeting Title] - YYYY-MM-DD

## Attendees
- Person 1
- Person 2

## Discussion Points
- Point 1
- Point 2

## Decisions Made
- Decision 1

## Action Items
- [ ] @Person: Task - Due: YYYY-MM-DD

## Related Notes
- [[Related Meeting]]
```

### Daily Note
```markdown
---
date: YYYY-MM-DD
status: complete
type: note
tags:
  - daily-note
---

# Daily Note - YYYY-MM-DD

## Morning Intentions
- Main focus

## Tasks
- [ ] Task 1

## Accomplishments
- Achievement 1

## Related Notes
- [[Yesterday's Note]]
```

## Best Practices

1. **Ask clarifying questions** if the user's request is vague
2. **Suggest wikilinks** to related notes if mentioned
3. **Use today's date** in YYYY-MM-DD format
4. **Choose appropriate status**: Usually "capture" for new notes
5. **Select 2-4 relevant tags**: Keep them lowercase with hyphens
6. **Fill in template sections** with placeholder text or user's info
7. **Validate filename**: Must be valid for all operating systems

## Example Usage

**User:** `/create-note`

**You:** "I'll help you create an Obsidian note. What would you like to document? (e.g., a technical concept, business idea, meeting notes, daily journal)"

**User:** "I want to document our new microservices architecture"

**You:** "Great! This sounds like a technical architecture note. I'll create it using the Architecture Document template. Any specific components or details you'd like me to include?"

**User:** "It includes API gateway, auth service, and database layer"

**You:** [Generate complete note with those components filled in]

```markdown
---
date: 2025-11-04
status: capture
type: architecture
tags:
  - architecture
  - microservices
  - system-design
---

# Microservices Architecture

## Overview
Our new microservices architecture provides a scalable foundation for distributed services with centralized authentication and API gateway routing.

## Key Components

### API Gateway
- **Purpose**: Central entry point for all client requests
- **Technology**: [To be determined]
- **Interfaces**: REST API, WebSocket

### Auth Service
- **Purpose**: Centralized authentication and authorization
- **Technology**: [To be determined]
- **Interfaces**: OAuth 2.0, JWT tokens

### Database Layer
- **Purpose**: Persistent data storage
- **Technology**: [To be determined]
- **Interfaces**: ORM, connection pooling

## Data Flow
[Describe request flow through the system]

## Technical Decisions
- Decision 1: [Rationale]
- Decision 2: [Rationale]

## Related Notes
- [[API Gateway Configuration]]
- [[Authentication Strategy]]
- [[Database Schema]]
```

**Suggested location:** `1 - Main Notes/Architecture/Microservices Architecture.md`

Would you like me to adjust anything?
```

## Integration

- Use the `obsidian-note-taker` skill for detailed template references
- Reference `folder-structure.md` for proper placement
- Can invoke `validate-notes` command after creation to verify formatting

## Notes

- This command should be **interactive** - guide the user through the process
- Always **present the complete note** before suggesting where to save it
- Let the user **review and adjust** before finalizing
- **Don't actually write the file** unless explicitly asked - show the content first

---

**Goal**: Make note creation fast, easy, and properly formatted every time.
