# Obsidian Note-Taker Plugin for Claude Code

A comprehensive Claude Code plugin for creating, organizing, and maintaining well-formatted Obsidian notes with proper frontmatter, templates, and vault organization.

## 🎯 What This Plugin Provides

### **Agent Skills**
- **obsidian-note-taker** - Automatically activated skill for creating formatted notes

### **Specialized Agents**
- **note-organizer** - Analyze and organize existing notes, fix frontmatter, repair broken links
- **vault-analyzer** - Generate insights, visualize connections, detect knowledge gaps

### **Slash Commands**
- `/create-note` - Interactive note creation wizard
- `/organize-vault` - Trigger vault organization and cleanup
- `/validate-notes` - Run validation checks on note formatting

### **Validation Tools**
- Python script for automated frontmatter and structure validation
- Pre-commit hook support
- CI/CD integration ready

## 📦 Components

```
plugins/obsidian-note-taker/
├── agents/              # Specialized AI agents
│   ├── note-organizer.md
│   └── vault-analyzer.md
├── commands/            # Slash commands
│   ├── create-note.md
│   ├── organize-vault.md
│   └── validate-notes.md
└── skills/              # Agent Skills
    └── obsidian-note-taker/
        ├── SKILL.md
        ├── references/
        └── scripts/
```

## 🚀 Installation

### Option 1: Via Claude Code (Recommended)

```bash
# Add the marketplace
claude code plugin add https://github.com/RandomStateLabs/obsidian-note-taker

# Install the plugin
/plugin install obsidian-note-taker
```

### Option 2: Manual Installation

```bash
# Clone to Claude Code plugins directory
git clone https://github.com/RandomStateLabs/obsidian-note-taker ~/.claude/plugins/obsidian-note-taker

# Or download and extract
cd ~/.claude/plugins/
wget https://github.com/RandomStateLabs/obsidian-note-taker/archive/main.zip
unzip main.zip
mv obsidian-note-taker-main obsidian-note-taker
```

### Option 3: Project-Specific Installation

```bash
# In your project directory
mkdir -p .claude/plugins
git clone https://github.com/RandomStateLabs/obsidian-note-taker .claude/plugins/obsidian-note-taker
```

## ✅ Verify Installation

```bash
# List installed plugins
/plugin list

# Check plugin directory
ls ~/.claude/plugins/obsidian-note-taker/
```

You should see:
```
agents/
commands/
skills/
.claude-plugin/
```

## 💻 Usage

### Creating Notes

**Via Skill (Automatic)**
Simply ask Claude Code naturally:
```
"Create a technical note about our new Redis caching layer"
"Document this business idea for a SaaS product"
"Help me create meeting notes for the standup"
```

**Via Command (Interactive)**
```
/create-note
```
→ Guides you through an interactive wizard

### Organizing Your Vault

**Quick Organization**
```
/organize-vault
```
→ Analyzes vault structure, fixes frontmatter, repairs broken links

**Manual Invocation of note-organizer Agent**
```
"Help me organize my Obsidian vault"
"Fix all broken wikilinks"
"Clean up my note frontmatter"
```

### Analyzing Your Vault

**Invoke vault-analyzer Agent**
```
"Analyze my Obsidian vault"
"Show me my most important notes"
"Find knowledge gaps in my vault"
"What's my vault health score?"
```

### Validating Notes

**Single File**
```
/validate-notes path/to/note.md
```

**Entire Vault**
```
/validate-notes .
```

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

## 📚 What's Included

### Agents
- **note-organizer** - Vault cleanup and organization specialist
- **vault-analyzer** - Strategic insights and health monitoring

### Commands
- `/create-note` - Interactive note creation
- `/organize-vault` - Automated vault organization
- `/validate-notes` - Note validation and quality checks

### Skills
- **obsidian-note-taker** - Core note creation with templates

### Templates
- **Technical**: Architecture docs, how-to guides, documentation
- **Business**: Business ideas, project brainstorms
- **Personal**: Meeting notes, daily notes
- **Research**: Literature notes, learning notes

### Reference Materials
- `plugins/obsidian-note-taker/skills/obsidian-note-taker/references/folder-structure.md` - Vault organization guide
- `plugins/obsidian-note-taker/skills/obsidian-note-taker/references/templates.md` - Detailed templates

### Validation Tool
- `plugins/obsidian-note-taker/skills/obsidian-note-taker/scripts/validate_frontmatter.py` - Python validation script

Run validation:
```bash
python plugins/obsidian-note-taker/skills/obsidian-note-taker/scripts/validate_frontmatter.py "My Note.md"
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

## ⚙️ Customization

You can customize the plugin by editing:
- `plugins/obsidian-note-taker/skills/obsidian-note-taker/references/templates.md` - Modify note templates
- `plugins/obsidian-note-taker/skills/obsidian-note-taker/references/folder-structure.md` - Adjust vault organization
- `plugins/obsidian-note-taker/skills/obsidian-note-taker/SKILL.md` - Change skill behavior
- `plugins/obsidian-note-taker/agents/*.md` - Customize agent instructions
- `plugins/obsidian-note-taker/commands/*.md` - Modify command workflows

## 🔧 Troubleshooting

### Plugin Not Found

1. **Check installation location:**
   ```bash
   ls ~/.claude/plugins/obsidian-note-taker/
   ```

2. **Verify plugin.json exists:**
   ```bash
   cat ~/.claude/plugins/obsidian-note-taker/.claude-plugin/plugin.json
   ```

3. **Reinstall the plugin:**
   ```bash
   /plugin install obsidian-note-taker
   ```

### Commands Not Working

1. **List available commands:**
   ```bash
   /help
   ```

2. **Check command files exist:**
   ```bash
   ls ~/.claude/plugins/obsidian-note-taker/commands/
   ```

### Agents Not Responding

1. **Invoke explicitly:**
   ```
   "Use the note-organizer agent to help me"
   ```

2. **Check agent files:**
   ```bash
   ls ~/.claude/plugins/obsidian-note-taker/agents/
   ```

### Validation Script Not Working

Ensure Python 3 and PyYAML are installed:
```bash
pip3 install pyyaml

# Verify installation
python3 -c "import yaml; print('PyYAML installed successfully')"
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
