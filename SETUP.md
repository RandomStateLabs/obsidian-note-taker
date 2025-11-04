# Quick Setup Guide

## Installation

### For All Projects (Recommended)

```bash
# Copy this skill to your personal skills directory
cp -r /home/user/obsidian-note-taker ~/.claude/skills/obsidian-note-taker
```

### For This Project Only

The skill is already in the repository and will work automatically when you use Claude Code in this project.

## Verification

Check that the skill is properly installed:

```bash
# Check personal installation
ls -la ~/.claude/skills/obsidian-note-taker/SKILL.md

# Check project installation
ls -la .claude/skills/obsidian-note-taker/SKILL.md
```

## Usage

### Automatic Activation

Just ask Claude Code naturally:

```
"Create a technical note about our Redis caching strategy"
"I need to document this business idea"
"Help me create meeting notes for today's standup"
```

The skill will automatically activate based on your request.

### Manual Activation

Explicitly invoke the skill:

```
/skill obsidian-note-taker
```

## Testing the Validation Script

The Python validation script helps ensure your notes are properly formatted:

```bash
# Install dependencies (if needed)
pip install pyyaml

# Validate a note
python scripts/validate_frontmatter.py "path/to/your/note.md"

# Or pipe content
cat note.md | python scripts/validate_frontmatter.py -
```

## File Structure

```
obsidian-note-taker/
├── SKILL.md                          # Main skill definition (required)
├── README.md                         # Installation and usage guide
├── EXAMPLES.md                       # Practical usage examples
├── SETUP.md                          # Quick setup guide (this file)
├── LICENSE                           # MIT License
├── .gitignore                        # Git ignore patterns
├── references/
│   ├── folder-structure.md          # Vault organization guide
│   └── templates.md                 # Detailed note templates
└── scripts/
    └── validate_frontmatter.py      # Note validation tool
```

## Next Steps

1. **Try it out**: Create a test note by asking Claude Code
2. **Customize**: Edit templates in `references/templates.md` to match your workflow
3. **Organize**: Adjust folder structure in `references/folder-structure.md`
4. **Validate**: Test the validation script on your notes
5. **Share**: If useful, share with your team or contribute improvements

## Troubleshooting

### Skill doesn't activate automatically

1. Check the SKILL.md file has proper frontmatter
2. Try manual invocation: `/skill obsidian-note-taker`
3. Restart Claude Code
4. Verify installation path

### Validation script errors

```bash
# Ensure Python 3 is installed
python3 --version

# Install PyYAML
pip3 install pyyaml
```

### Custom templates not being used

1. The skill reads from `references/templates.md`
2. Modify templates there
3. Changes take effect immediately (no restart needed)

## Resources

- [README.md](./README.md) - Full documentation
- [EXAMPLES.md](./EXAMPLES.md) - Usage examples
- [references/templates.md](./references/templates.md) - All templates
- [references/folder-structure.md](./references/folder-structure.md) - Organization guide

## Support

For issues or questions:
- Review the detailed EXAMPLES.md
- Check the references/ folder for templates
- Consult Claude Code documentation
- Open an issue on GitHub

---

**Ready to take better notes!** 📝
