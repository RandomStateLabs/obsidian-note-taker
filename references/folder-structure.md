# Obsidian Vault Folder Structure Guide

This guide helps determine the correct folder placement for different types of notes.

## Standard Folder Structure

```
ObsidianVault/
├── 1 - Main Notes/           # Technical & professional content
│   ├── Architecture/         # System designs
│   ├── Guides/              # How-to documents
│   ├── Documentation/       # Technical docs
│   └── Research/            # Technical research
├── Personal/                # Personal workspace
│   ├── Thoughts & Ideas/    # Business ideas, brainstorming
│   ├── Daily Notes/         # Daily journals
│   ├── Meetings/            # Meeting notes
│   └── Learning/            # Personal learning notes
├── Projects/                # Active project documentation
│   ├── [Project Name]/      # Individual project folders
│   └── Archive/             # Completed projects
├── Resources/               # Reference materials
│   ├── Templates/           # Note templates
│   ├── Attachments/         # Images, PDFs, files
│   └── External/            # External resources
└── Archive/                 # Old/deprecated notes
```

## Folder Selection Decision Tree

```mermaid
graph TD
    A[New Note] --> B{Is it technical?}
    B -->|Yes| C[1 - Main Notes/]
    B -->|No| D{Is it personal?}
    D -->|Yes| E{What type?}
    D -->|No| F{Is it project-specific?}
    E -->|Idea/Brainstorm| G[Personal/Thoughts & Ideas/]
    E -->|Daily/Journal| H[Personal/Daily Notes/]
    E -->|Meeting| I[Personal/Meetings/]
    E -->|Learning| J[Personal/Learning/]
    F -->|Yes| K[Projects/[Project Name]/]
    F -->|No| L[Resources/]
```

## Detailed Folder Purposes

### 1 - Main Notes/
**Purpose**: Central repository for technical and professional knowledge

**Place here**:
- System architecture documentation
- Technical guides and tutorials
- API documentation
- Development notes
- Technical research
- Best practices documentation
- Tool configurations
- Code documentation

**Subfolders**:
- `Architecture/` - System designs, diagrams
- `Guides/` - How-to documents, tutorials
- `Documentation/` - Technical specifications
- `Research/` - Technical investigations

### Personal/
**Purpose**: Personal workspace for ideas, thoughts, and daily activities

**Place here**:
- Personal reflections
- Daily journals
- Meeting notes
- Learning progress
- Personal goals
- Ideas and brainstorming

**Subfolders**:
- `Thoughts & Ideas/` - Business ideas, creative thoughts
- `Daily Notes/` - Daily planning and journals
- `Meetings/` - Meeting notes and agendas
- `Learning/` - Personal study notes

### Personal/Thoughts & Ideas/
**Purpose**: Creative ideation and business concepts

**Place here**:
- Business ideas
- Startup concepts
- Product ideas
- Feature brainstorming
- Creative projects
- Innovation concepts
- Side project ideas

### Projects/
**Purpose**: Active project documentation

**Place here**:
- Project-specific documentation
- Project meeting notes
- Project requirements
- Sprint notes
- Project research
- Timeline and milestones

**Organization**:
- Create subfolder per project
- Move to `Archive/` when complete

### Resources/
**Purpose**: Reference materials and assets

**Place here**:
- Note templates
- Reference documents
- External PDFs
- Images and diagrams
- Spreadsheets
- Presentation files

**Subfolders**:
- `Templates/` - Reusable note templates
- `Attachments/` - Supporting files
- `External/` - Third-party resources

## Naming Conventions

### Folder Names
- Use clear, descriptive names
- Capitalize first letter of each word
- Use forward slash for hierarchy
- Avoid special characters

### File Names
- Title Case with spaces: `System Architecture.md`
- Remove special characters: `: / \ | * ? " < >`
- Keep under 60 characters
- Date prefix for time-sensitive: `2025-10-20 Meeting Notes.md`

## Special Cases

### Cross-Cutting Content
Some notes may fit multiple categories. Use this priority:

1. **Project-specific** → Projects/[Project]/
2. **Technical/Professional** → 1 - Main Notes/
3. **Personal/Ideas** → Personal/Thoughts & Ideas/
4. **General Personal** → Personal/
5. **Reference** → Resources/

### Meeting Notes
- **Work meeting about project** → Projects/[Project]/Meetings/
- **General work meeting** → 1 - Main Notes/Meetings/
- **Personal meeting** → Personal/Meetings/
- **Learning session** → Personal/Learning/

### Research Notes
- **Technical research** → 1 - Main Notes/Research/
- **Project research** → Projects/[Project]/Research/
- **Personal research** → Personal/Learning/
- **Business research** → Personal/Thoughts & Ideas/

## Folder Creation Guidelines

### When to Create New Folders
Create a new folder when:
- Starting a new project
- A topic has 5+ related notes
- Need clear separation of concerns
- Different access/sharing requirements

### When NOT to Create Folders
Avoid creating folders for:
- Single notes
- Temporary content
- Overly specific categories
- Duplicate organizational schemes

## Migration Strategy

### Moving Notes Between Folders
When a note's purpose changes:
1. Update frontmatter status
2. Move to appropriate folder
3. Update wikilinks if needed
4. Update related notes

### Archiving Old Content
Move to Archive/ when:
- Project completed 6+ months ago
- Information outdated
- No longer referenced
- Superseded by new documentation

## Quick Reference Table

| Content Type | Primary Folder | Alternative |
|-------------|---------------|-------------|
| System architecture | 1 - Main Notes/Architecture/ | Projects/[Name]/ |
| How-to guide | 1 - Main Notes/Guides/ | - |
| Business idea | Personal/Thoughts & Ideas/ | - |
| Daily journal | Personal/Daily Notes/ | - |
| Project docs | Projects/[Project Name]/ | - |
| Meeting notes | Personal/Meetings/ | Projects/[Name]/Meetings/ |
| Learning notes | Personal/Learning/ | 1 - Main Notes/ (if professional) |
| Templates | Resources/Templates/ | - |
| External PDFs | Resources/Attachments/ | - |
| Old projects | Archive/ | - |

## Best Practices

1. **Be consistent**: Use the same structure throughout
2. **Keep it shallow**: Avoid more than 3 levels deep
3. **Review regularly**: Reorganize quarterly
4. **Document decisions**: Note why content is placed where
5. **Use tags too**: Folders for structure, tags for topics
6. **Start simple**: Add complexity only when needed
