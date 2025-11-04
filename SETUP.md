# Quick Setup Guide

## Installation

### Via Claude Code (Recommended)

```bash
# Install the plugin from marketplace
/plugin install obsidian-note-taker
```

### Manual Installation

```bash
# Clone to Claude Code plugins directory
git clone https://github.com/RandomStateLabs/obsidian-note-taker ~/.claude/plugins/obsidian-note-taker

# Or download and extract
cd ~/.claude/plugins/
wget https://github.com/RandomStateLabs/obsidian-note-taker/archive/main.zip
unzip main.zip
mv obsidian-note-taker-main obsidian-note-taker
```

### Project-Specific Installation

```bash
# In your project directory
mkdir -p .claude/plugins
git clone https://github.com/RandomStateLabs/obsidian-note-taker .claude/plugins/obsidian-note-taker
```

## Verification

Check that the plugin is properly installed:

```bash
# List installed plugins
/plugin list

# Check plugin directory
ls -la ~/.claude/plugins/obsidian-note-taker/

# You should see:
# agents/
# commands/
# skills/
# .claude-plugin/
```

## Usage

### Slash Commands

```bash
/create-note           # Interactive note creation wizard
/organize-vault        # Analyze and organize your vault
/validate-notes file.md  # Validate note formatting
```

### Agent Invocation

**note-organizer Agent**
```
"Help me organize my Obsidian vault"
"Fix all broken wikilinks"
"Clean up my note frontmatter"
```

**vault-analyzer Agent**
```
"Analyze my Obsidian vault"
"Show me my vault health score"
"Find knowledge gaps"
```

### Skill (Automatic)

Just ask naturally:
```
"Create a technical note about our API"
"Document this business idea"
"Help me create meeting notes"
```

## Testing the Validation Script

```bash
# Install dependencies
pip3 install pyyaml

# Validate a note
python plugins/obsidian-note-taker/skills/obsidian-note-taker/scripts/validate_frontmatter.py "note.md"

# Or pipe content
cat note.md | python plugins/obsidian-note-taker/skills/obsidian-note-taker/scripts/validate_frontmatter.py -
```

## Plugin Structure

```
obsidian-note-taker/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace configuration
├── plugins/
│   └── obsidian-note-taker/
│       ├── .claude-plugin/
│       │   └── plugin.json       # Plugin metadata
│       ├── agents/               # Specialized agents
│       │   ├── note-organizer.md
│       │   └── vault-analyzer.md
│       ├── commands/             # Slash commands
│       │   ├── create-note.md
│       │   ├── organize-vault.md
│       │   └── validate-notes.md
│       └── skills/               # Agent Skills
│           └── obsidian-note-taker/
│               ├── SKILL.md
│               ├── references/
│               └── scripts/
├── README.md
├── EXAMPLES.md
├── SETUP.md
└── LICENSE
```

## Next Steps

1. **Try it out**: Run `/create-note` to create your first note
2. **Customize**: Edit templates in `plugins/obsidian-note-taker/skills/obsidian-note-taker/references/`
3. **Organize**: Run `/organize-vault` to analyze your vault
4. **Validate**: Use `/validate-notes` to check note quality
5. **Share**: If useful, star the repo and share with others!

## Troubleshooting

### Plugin Not Found

```bash
# Check installation
ls ~/.claude/plugins/obsidian-note-taker/

# Reinstall if missing
git clone https://github.com/RandomStateLabs/obsidian-note-taker ~/.claude/plugins/obsidian-note-taker
```

### Commands Not Working

```bash
# List available commands
/help

# Check command files
ls ~/.claude/plugins/obsidian-note-taker/commands/
```

### Validation Script Errors

```bash
# Ensure Python 3 is installed
python3 --version

# Install PyYAML
pip3 install pyyaml

# Test installation
python3 -c "import yaml; print('PyYAML OK')"
```

## Resources

- [README.md](./README.md) - Full documentation
- [EXAMPLES.md](./EXAMPLES.md) - Usage examples
- [plugins/obsidian-note-taker/skills/obsidian-note-taker/references/templates.md](./plugins/obsidian-note-taker/skills/obsidian-note-taker/references/templates.md) - All templates
- [plugins/obsidian-note-taker/skills/obsidian-note-taker/references/folder-structure.md](./plugins/obsidian-note-taker/skills/obsidian-note-taker/references/folder-structure.md) - Organization guide

## Support

For issues or questions:
- Review EXAMPLES.md for usage patterns
- Check the references/ folder for templates
- Consult README.md for detailed documentation
- Open an issue on GitHub

---

**Ready to take better notes!** 📝
