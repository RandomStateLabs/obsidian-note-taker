# Obsidian Note-Taker Skill for Claude Code

A Claude Code skill that helps you create well-formatted Obsidian notes with proper frontmatter, templates, and organization.

## What This Skill Does

This skill provides:
- **Structured note templates** for different types of content (technical docs, business ideas, meeting notes, etc.)
- **Automatic frontmatter generation** with proper YAML formatting
- **Folder organization guidance** based on note type
- **Wikilink formatting** for internal references
- **Validation tooling** to ensure note quality
- **Consistent naming conventions** for your Obsidian vault

## When to Use This Skill

The skill automatically activates when you:
- Ask to "create a note" or "document" something for Obsidian
- Mention your vault, knowledge base, or Zettelkasten
- Want to capture ideas, meeting notes, or technical documentation
- Need help structuring information in Obsidian-compatible markdown

You can also manually invoke it using: `/skill obsidian-note-taker`

## Installation

### Option 1: Personal Skill (Recommended)

Install globally across all your projects:

```bash
# Create skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Clone or copy this repository
git clone https://github.com/YOUR_USERNAME/obsidian-note-taker ~/.claude/skills/obsidian-note-taker

# Or manually copy
cp -r obsidian-note-taker ~/.claude/skills/
```

### Option 2: Project Skill

Install for a specific project only:

```bash
# In your project directory
mkdir -p .claude/skills

# Clone or copy
git clone https://github.com/YOUR_USERNAME/obsidian-note-taker .claude/skills/obsidian-note-taker
```

### Option 3: Manual Installation

1. Download this repository
2. Copy the entire folder to `~/.claude/skills/obsidian-note-taker/`
3. Restart Claude Code if it's running

## Verify Installation

After installation, you can verify the skill is available:

```bash
# List available skills
ls ~/.claude/skills/

# Check if obsidian-note-taker is listed
ls ~/.claude/skills/obsidian-note-taker/
```

You should see:
```
SKILL.md
references/
scripts/
```

## Usage

### Automatic Activation

Simply ask Claude Code to create a note:

```
"Create a technical note documenting our new authentication system"
"I need to capture this business idea for a SaaS product"
"Help me create meeting notes for today's standup"
```

### Manual Invocation

If you want to explicitly use this skill:

```
/skill obsidian-note-taker
```

Then provide your note requirements.

## Examples

### Example 1: Technical Documentation

**You:** "Create a technical note about our new Redis caching layer"

**Claude Code will:**
1. Identify it as technical documentation
2. Suggest folder: `1 - Main Notes/Architecture/`
3. Generate proper frontmatter with relevant tags
4. Apply the Architecture Document template
5. Format with wikilinks for related concepts

### Example 2: Business Idea

**You:** "Document my idea for an AI-powered code review tool"

**Claude Code will:**
1. Recognize it as a business idea
2. Suggest folder: `Personal/Thoughts & Ideas/`
3. Use the Business Idea template
4. Include sections for problem statement, solution, market analysis
5. Add action items and next steps

### Example 3: Meeting Notes

**You:** "Create notes for the Q4 planning meeting"

**Claude Code will:**
1. Use the Meeting Notes template
2. Suggest folder: `Personal/Meetings/`
3. Include sections for attendees, agenda, decisions, action items
4. Format date in YYYY-MM-DD format

## What's Included

### Templates
- **Technical**: Architecture docs, how-to guides, documentation
- **Business**: Business ideas, project brainstorms
- **Personal**: Meeting notes, daily notes
- **Research**: Literature notes, learning notes

### Reference Materials
- `references/folder-structure.md` - Complete vault organization guide
- `references/templates.md` - Detailed templates for all note types

### Validation Tool
- `scripts/validate_frontmatter.py` - Python script to validate note structure

Run validation:
```bash
python ~/.claude/skills/obsidian-note-taker/scripts/validate_frontmatter.py "My Note.md"
```

## Frontmatter Format

All notes include YAML frontmatter:

```yaml
---
date: 2025-11-04          # YYYY-MM-DD format
status: capture            # capture, develop, refine, complete
type: note                 # note, guide, architecture, workflow, idea
tags:
  - technical             # lowercase with hyphens
  - redis
  - architecture
---
```

## File Naming Conventions

- **Format**: Title Case with spaces
- **Example**: `Redis Caching Architecture.md`
- **Length**: Under 60 characters
- **Avoid**: `: / \ | * ? " < >`

## Customization

You can customize templates by editing:
- `references/templates.md` - Modify existing templates
- `references/folder-structure.md` - Adjust folder organization
- `SKILL.md` - Change skill behavior and instructions

## Troubleshooting

### Skill Not Activating

1. **Check installation location:**
   ```bash
   ls ~/.claude/skills/obsidian-note-taker/SKILL.md
   ```

2. **Verify SKILL.md frontmatter** has proper YAML format

3. **Try manual invocation:**
   ```
   /skill obsidian-note-taker
   ```

### Validation Script Not Working

Ensure Python 3 and PyYAML are installed:
```bash
pip install pyyaml
```

## Contributing

Contributions welcome! Areas for improvement:
- Additional note templates
- More validation rules
- Integration with Obsidian plugins
- Enhanced folder organization strategies

## License

MIT License - Feel free to use and modify for your needs

## Resources

- [Obsidian Official Site](https://obsidian.md/)
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Claude Code Skills](https://github.com/anthropics/skills)

## Support

For issues or questions:
1. Check the templates in `references/`
2. Review the SKILL.md for detailed instructions
3. Open an issue on GitHub
4. Consult Claude Code documentation

---

**Made with Claude Code** 🚀
