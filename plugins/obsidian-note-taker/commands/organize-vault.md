---
description: Analyze and organize your Obsidian vault structure, fix frontmatter, repair broken links, and improve note organization
---

# Organize Obsidian Vault

This command invokes the **note-organizer** agent to analyze and organize your Obsidian vault.

## What This Does

The note-organizer agent will:
1. **Scan your vault** for organizational issues
2. **Analyze frontmatter** for errors and inconsistencies
3. **Check wikilinks** for broken connections
4. **Review folder structure** for misplaced notes
5. **Generate a report** with actionable recommendations
6. **Apply fixes** (with your permission)

## Usage

```
/organize-vault
```

Then choose what you'd like to do:
- Full vault analysis (scan everything)
- Specific folder analysis
- Fix specific issue type (frontmatter, links, etc.)
- Quick health check

## Workflow

### Step 1: Choose Analysis Scope

**Option 1: Full Vault Analysis**
- Analyzes entire vault
- Comprehensive report
- Best for periodic maintenance
- Estimated time: 2-5 minutes

**Option 2: Folder-Specific**
- Focus on one folder (e.g., `1 - Main Notes/`)
- Faster analysis
- Good for targeted cleanup

**Option 3: Issue-Specific**
- Only check frontmatter, or only check links, etc.
- Quickest option
- Good when you know what needs fixing

**Option 4: Quick Health Check**
- High-level overview only
- No detailed analysis
- ~30 seconds

### Step 2: Review Analysis Report

You'll receive a report like:

```markdown
# Vault Organization Report

## Summary
- Notes scanned: 247
- Issues found: 23
- Critical: 5 | Warnings: 12 | Suggestions: 6

## Critical Issues
1. Invalid frontmatter YAML in 5 notes
2. Broken wikilinks: 7 links to non-existent notes
3. Files in wrong folders: 3 notes misplaced

## Warnings
1. Inconsistent tag formatting (12 notes)
2. Missing status field (8 notes)
3. Outdated date formats (4 notes)

## Suggestions
1. Consider creating hub note for "authentication" topic
2. Consolidate duplicate tags: api/apis → api
3. Link orphaned notes to relevant topics

## Recommended Actions
1. [ ] Fix critical frontmatter errors
2. [ ] Repair broken wikilinks
3. [ ] Relocate misplaced notes
4. [ ] Standardize tag formatting
5. [ ] Add missing frontmatter fields
```

### Step 3: Apply Fixes

You'll be asked:
```
Would you like me to:
1. Fix all issues automatically (recommended: create git commit first)
2. Fix critical issues only
3. Fix one category at a time (with confirmation)
4. Just show me the issues (no changes)
```

### Step 4: Review Changes

After fixes are applied:
```markdown
# Changes Applied

## Frontmatter Fixes (5 notes)
✅ Fixed YAML syntax errors
✅ Standardized date formats
✅ Added missing status fields

## Link Repairs (7 links)
✅ Created stub notes for missing targets
✅ Updated outdated link references

## File Relocations (3 notes)
✅ Moved technical notes to `1 - Main Notes/`
✅ Organized project notes under `Projects/`

---
All changes complete! Your vault is now better organized.
```

## Common Use Cases

### Clean Up After Import
```
User: "I just imported 100 notes from Evernote, organize them"
```
→ Full vault analysis + folder reorganization

### Fix Frontmatter Issues
```
User: "Fix all my frontmatter formatting"
```
→ Issue-specific analysis (frontmatter only)

### Repair Broken Links
```
User: "Find and fix broken wikilinks"
```
→ Link analysis + repair suggestions

### Monthly Maintenance
```
User: "Do a vault health check"
```
→ Quick health check → full analysis if issues found

### Organize Specific Folder
```
User: "Organize my Personal/Meetings folder"
```
→ Folder-specific analysis

## Safety Features

1. **Non-Destructive by Default**
   - Always shows report before making changes
   - Asks for confirmation

2. **Git Integration**
   - Suggests creating commit before major changes
   - Easy rollback if needed

3. **Backup Recommendations**
   - Warns before bulk operations
   - Suggests using version control

4. **Selective Application**
   - Can fix issues one-by-one
   - Category-based fixes (frontmatter, links, etc.)

5. **Undo Instructions**
   - Provides revert commands if needed

## Integration

### With Other Commands
- Run `/validate-notes` first for detailed pre-check
- Use `/create-note` for creating stub notes after finding broken links
- Invoke vault-analyzer agent for strategic insights

### With Skills
- Uses `obsidian-note-taker` skill for formatting standards
- References `folder-structure.md` for organization rules
- Uses validation script for automated checks

## Advanced Options

### Batch Processing
```
Organize by:
- Date ranges (e.g., "notes from last month")
- Tag categories (e.g., "all meeting notes")
- Status (e.g., "all capture status notes")
```

### Custom Rules
```
Apply custom organization rules:
- Move all notes with tag X to folder Y
- Rename files matching pattern
- Bulk tag updates
```

### Reporting Only
```
Generate report without making changes:
- Export to markdown file
- Track changes over time
- Share with team
```

## Performance Tips

**For Large Vaults (500+ notes):**
- Use folder-specific analysis first
- Run during off-hours
- Process one category at a time
- Consider parallel processing option

**For Quick Fixes:**
- Use issue-specific analysis
- Fix critical issues only
- Schedule full analysis for later

## Example Session

```
User: /organize-vault