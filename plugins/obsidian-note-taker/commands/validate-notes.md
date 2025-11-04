---
description: Validate Obsidian note frontmatter and structure using automated validation tools
---

# Validate Obsidian Notes

This command runs validation checks on your Obsidian notes to ensure proper formatting, valid frontmatter, and content structure compliance.

## What This Does

Validates notes against obsidian-note-taker standards:
- ✅ YAML frontmatter syntax and structure
- ✅ Required fields (date, status, type, tags)
- ✅ Date format (YYYY-MM-DD)
- ✅ Valid status values (capture, develop, refine, complete)
- ✅ Valid type values (note, guide, architecture, workflow, idea)
- ✅ Tag formatting (lowercase, hyphens only)
- ✅ Content structure (headings, wikilinks)
- ✅ Filename compatibility

## Usage

### Single File Validation
```
/validate-notes path/to/note.md
```

### Multiple Files
```
/validate-notes path/to/folder/
```

### Current Directory
```
/validate-notes
```
(validates all .md files in current directory)

### Pipe Content
```
/validate-notes < note.md
```

## Validation Script

This command uses the Python validation tool:
```
plugins/obsidian-note-taker/skills/obsidian-note-taker/scripts/validate_frontmatter.py
```

## Output Examples

### ✅ Valid Note
```
📄 Validating: System Architecture.md
==================================================
✅ Frontmatter: Valid
✅ Content Structure: Good
==================================================
✨ Perfect! Note is well-formatted.
```

### ❌ Invalid Note with Errors
```
📄 Validating: Meeting Notes.md
==================================================
❌ Frontmatter: Invalid
   • Missing required field: status
   • Invalid date format: '2024-Nov-04'. Use YYYY-MM-DD format
   • Tag 'API' must be lowercase with only letters, numbers, and hyphens

⚠️  Content Warnings:
   • Title too long (68 chars): Consider shortening for filename
   • Title contains invalid filename character: ':'
==================================================
```

### ⚠️ Valid with Warnings
```
📄 Validating: Project Idea.md
==================================================
✅ Frontmatter: Valid

⚠️  Content Warnings:
   • No main heading (# Title) found after frontmatter
   • Title too long (62 chars): Consider shortening for filename
==================================================
✓ Valid with minor suggestions
```

## Validation Rules

### Required Frontmatter Fields
```yaml
---
date: YYYY-MM-DD       # Required, must be valid date format
status: capture        # Required, must be: capture|develop|refine|complete
type: note             # Required, must be: note|guide|architecture|workflow|idea
tags:                  # Required, must be array with at least 1 tag
  - valid-tag         # Lowercase, hyphens only, no spaces
---
```

### Date Format
- ✅ `2025-11-04` (YYYY-MM-DD)
- ❌ `11-04-2025` (wrong order)
- ❌ `2025/11/04` (slashes not allowed)
- ❌ `Nov 4, 2025` (text format not allowed)

### Status Values
- ✅ `capture` - Initial capture of information
- ✅ `develop` - Actively developing the note
- ✅ `refine` - Refining and improving
- ✅ `complete` - Complete and polished
- ❌ `draft`, `wip`, `done` (not standard values)

### Type Values
- ✅ `note` - General note
- ✅ `guide` - How-to guide
- ✅ `architecture` - System architecture
- ✅ `workflow` - Process/workflow documentation
- ✅ `idea` - Business/project idea
- ❌ `document`, `article`, `post` (not standard values)

### Tag Format
- ✅ `technical`, `api`, `meeting-notes`, `q4-2025`
- ❌ `Technical` (uppercase not allowed)
- ❌ `API` (all caps not allowed)
- ❌ `meeting notes` (spaces not allowed)
- ❌ `q4_2025` (underscores not allowed, use hyphens)

### Filename Rules
Invalid characters in title:
- `: / \ | * ? " < >`

Length recommendations:
- ✅ Under 60 characters
- ⚠️ 60-80 characters (warning)
- ❌ Over 80 characters (too long)

## Batch Validation

### Validate Entire Vault
```bash
cd ~/ObsidianVault
/validate-notes .
```

Generates summary report:
```
# Vault Validation Summary

Scanned: 247 notes
✅ Valid: 198 (80%)
⚠️  Valid with warnings: 36 (15%)
❌ Invalid: 13 (5%)

## Issues Breakdown
- Missing required fields: 8 notes
- Invalid date format: 5 notes
- Invalid status values: 3 notes
- Invalid tag formatting: 12 notes
- Content warnings: 36 notes

## Files with Errors
1. ❌ Meeting Notes 2024-10-15.md
   - Missing status field
   - Invalid tag: 'Meeting'

2. ❌ System Design v2.md
   - Invalid date format: '10/15/2024'
   - Invalid status: 'draft'

[... full list ...]

## Recommendations
1. Fix 8 notes missing required fields
2. Update 5 notes with incorrect date format
3. Standardize 12 notes with invalid tags
```

### Validate Specific Folder
```bash
/validate-notes Personal/Meetings/
```

### Validate by Pattern
```bash
/validate-notes **/*architecture*.md
```

## Integration with Other Commands

### With `/organize-vault`
```
/validate-notes        # Check what's broken
/organize-vault        # Fix the issues
/validate-notes        # Verify fixes worked
```

### With `/create-note`
```
/create-note           # Create new note
/validate-notes note.md    # Verify it's correct
```

### As Pre-commit Hook
Run validation before git commits:
```bash
# .git/hooks/pre-commit
python plugins/obsidian-note-taker/skills/obsidian-note-taker/scripts/validate_frontmatter.py $(git diff --cached --name-only | grep '\.md$')
```

## Automated Validation

### CI/CD Integration
```yaml
# .github/workflows/validate-notes.yml
name: Validate Notes
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
      - name: Install dependencies
        run: pip install pyyaml
      - name: Validate notes
        run: |
          python plugins/obsidian-note-taker/skills/obsidian-note-taker/scripts/validate_frontmatter.py *.md
```

### Watch Mode
Continuously validate on file changes:
```bash
watch -n 2 '/validate-notes .'
```

## Configuration

### Custom Validation Rules
Extend the validation script with:
- Custom required fields
- Additional valid status/type values
- Custom tag patterns
- Organization-specific rules

### Severity Levels
- **Error**: Fails validation, must fix
- **Warning**: Should fix, but note is usable
- **Info**: Suggestions for improvement

## Troubleshooting

### Script Not Found
```bash
# Verify script location
ls plugins/obsidian-note-taker/skills/obsidian-note-taker/scripts/validate_frontmatter.py

# Make executable
chmod +x plugins/obsidian-note-taker/skills/obsidian-note-taker/scripts/validate_frontmatter.py
```

### Python Dependencies Missing
```bash
pip install pyyaml
# or
pip3 install pyyaml
```

### Permission Errors
```bash
# Ensure read permissions
chmod +r path/to/notes/*.md
```

## Output Formats

### Terminal (Default)
Colored output with emoji indicators

### JSON (for automation)
```bash
/validate-notes --format json
```
```json
{
  "file": "note.md",
  "valid": false,
  "errors": [
    "Missing required field: status",
    "Invalid date format"
  ],
  "warnings": [
    "Title too long"
  ]
}
```

### Markdown Report
```bash
/validate-notes --format markdown > validation-report.md
```

## Best Practices

1. **Validate Before Sharing**
   - Run validation before sharing notes with team
   - Ensure consistency across team vaults

2. **Regular Audits**
   - Weekly: Validate new/modified notes
   - Monthly: Full vault validation
   - Quarterly: Review and update standards

3. **Automated Checks**
   - Pre-commit hooks for git
   - CI/CD validation on PR
   - Scheduled vault audits

4. **Fix Progressively**
   - Start with critical errors
   - Address warnings over time
   - Refine standards as needed

5. **Document Exceptions**
   - Some notes may need non-standard formats
   - Document why and where exceptions exist
   - Consider adding validation config for exceptions

---

**Remember**: Validation helps maintain consistency and quality across your Obsidian vault. Run it regularly to catch issues early!
