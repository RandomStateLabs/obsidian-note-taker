#!/usr/bin/env python3
"""
Validate Obsidian note frontmatter format.
This script checks if a note has valid YAML frontmatter with required fields.
"""

import sys
import re
import yaml
from datetime import datetime
from pathlib import Path
from typing import Tuple, List

def validate_frontmatter(content: str) -> Tuple[bool, List[str]]:
    """
    Validate YAML frontmatter in an Obsidian note.
    
    Args:
        content: The full content of the markdown file
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    # Check for frontmatter presence
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*$'
    match = re.match(frontmatter_pattern, content, re.MULTILINE | re.DOTALL)
    
    if not match:
        return False, ["No frontmatter found. Notes must start with --- frontmatter ---"]
    
    # Extract and parse YAML
    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        return False, [f"Invalid YAML syntax: {e}"]
    
    if not frontmatter:
        return False, ["Empty frontmatter"]
    
    # Check required fields
    required_fields = ['date', 'status', 'type', 'tags']
    for field in required_fields:
        if field not in frontmatter:
            errors.append(f"Missing required field: {field}")
    
    # Validate date format
    if 'date' in frontmatter:
        try:
            date_str = str(frontmatter['date'])
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            errors.append(f"Invalid date format: '{frontmatter['date']}'. Use YYYY-MM-DD format")
    
    # Validate status
    valid_statuses = ['capture', 'develop', 'refine', 'complete']
    if 'status' in frontmatter:
        if frontmatter['status'] not in valid_statuses:
            errors.append(f"Invalid status: '{frontmatter['status']}'. Must be one of: {', '.join(valid_statuses)}")
    
    # Validate type
    valid_types = ['note', 'guide', 'architecture', 'workflow', 'idea']
    if 'type' in frontmatter:
        if frontmatter['type'] not in valid_types:
            errors.append(f"Invalid type: '{frontmatter['type']}'. Must be one of: {', '.join(valid_types)}")
    
    # Validate tags
    if 'tags' in frontmatter:
        if not isinstance(frontmatter['tags'], list):
            errors.append("Tags must be a list")
        elif len(frontmatter['tags']) < 1:
            errors.append("At least one tag is required")
        else:
            # Check tag format
            for tag in frontmatter['tags']:
                if not isinstance(tag, str):
                    errors.append(f"Tag must be a string: {tag}")
                elif not re.match(r'^[a-z0-9-]+$', tag):
                    errors.append(f"Tag '{tag}' must be lowercase with only letters, numbers, and hyphens")
    
    return len(errors) == 0, errors

def validate_content_structure(content: str) -> List[str]:
    """
    Validate the content structure of the note.
    
    Args:
        content: The full content of the markdown file
        
    Returns:
        List of warnings (not errors)
    """
    warnings = []
    lines = content.split('\n')
    
    # Find where frontmatter ends
    frontmatter_end = 0
    for i, line in enumerate(lines):
        if i > 0 and line.strip() == '---':
            frontmatter_end = i + 1
            break
    
    # Check for main heading
    has_h1 = False
    for line in lines[frontmatter_end:]:
        if line.startswith('# '):
            has_h1 = True
            break
    
    if not has_h1:
        warnings.append("No main heading (# Title) found after frontmatter")
    
    # Check for wikilinks
    content_body = '\n'.join(lines[frontmatter_end:])
    if '[[' in content_body and ']]' in content_body:
        # Validate wikilink format
        wikilink_pattern = r'\[\[([^\]]+)\]\]'
        wikilinks = re.findall(wikilink_pattern, content_body)
        for link in wikilinks:
            if '|' in link:  # Aliased link
                parts = link.split('|')
                if len(parts) != 2:
                    warnings.append(f"Invalid wikilink format: [[{link}]]")
    
    # Check filename length in title
    for line in lines[frontmatter_end:]:
        if line.startswith('# '):
            title = line[2:].strip()
            if len(title) > 60:
                warnings.append(f"Title too long ({len(title)} chars): Consider shortening for filename")
            # Check for invalid filename characters
            invalid_chars = [':', '/', '\\', '|', '*', '?', '"', '<', '>']
            for char in invalid_chars:
                if char in title:
                    warnings.append(f"Title contains invalid filename character: '{char}'")
    
    return warnings

def validate_file(filepath: Path) -> bool:
    """
    Validate a markdown file.
    
    Args:
        filepath: Path to the markdown file
        
    Returns:
        True if valid, False otherwise
    """
    if not filepath.exists():
        print(f"❌ File not found: {filepath}")
        return False
    
    if not filepath.suffix == '.md':
        print(f"⚠️  Not a markdown file: {filepath}")
        return False
    
    content = filepath.read_text(encoding='utf-8')
    
    # Validate frontmatter
    is_valid, errors = validate_frontmatter(content)
    
    # Get content warnings
    warnings = validate_content_structure(content)
    
    # Display results
    print(f"\n📄 Validating: {filepath.name}")
    print("=" * 50)
    
    if is_valid:
        print("✅ Frontmatter: Valid")
    else:
        print("❌ Frontmatter: Invalid")
        for error in errors:
            print(f"   • {error}")
    
    if warnings:
        print("\n⚠️  Content Warnings:")
        for warning in warnings:
            print(f"   • {warning}")
    elif is_valid:
        print("✅ Content Structure: Good")
    
    print("=" * 50)
    
    if is_valid and not warnings:
        print("✨ Perfect! Note is well-formatted.")
    elif is_valid:
        print("✓ Valid with minor suggestions")
    
    return is_valid

def validate_content_string(content: str) -> bool:
    """
    Validate markdown content provided as a string.
    
    Args:
        content: Markdown content as string
        
    Returns:
        True if valid, False otherwise
    """
    # Validate frontmatter
    is_valid, errors = validate_frontmatter(content)
    
    # Get content warnings
    warnings = validate_content_structure(content)
    
    # Display results
    print("\n📄 Validating provided content")
    print("=" * 50)
    
    if is_valid:
        print("✅ Frontmatter: Valid")
    else:
        print("❌ Frontmatter: Invalid")
        for error in errors:
            print(f"   • {error}")
    
    if warnings:
        print("\n⚠️  Content Warnings:")
        for warning in warnings:
            print(f"   • {warning}")
    elif is_valid:
        print("✅ Content Structure: Good")
    
    print("=" * 50)
    
    if is_valid and not warnings:
        print("✨ Perfect! Note is well-formatted.")
    elif is_valid:
        print("✓ Valid with minor suggestions")
    
    return is_valid

def main():
    """Main function for CLI usage."""
    if len(sys.argv) < 2:
        print("Obsidian Note Validator")
        print("=" * 50)
        print("\nUsage:")
        print("  python validate_frontmatter.py <note.md>")
        print("  python validate_frontmatter.py -")
        print("\nOptions:")
        print("  <note.md>  Path to markdown file to validate")
        print("  -          Read content from stdin")
        print("\nExample:")
        print("  python validate_frontmatter.py 'My Note.md'")
        print("  cat note.md | python validate_frontmatter.py -")
        sys.exit(1)
    
    if sys.argv[1] == '-':
        # Read from stdin
        content = sys.stdin.read()
        is_valid = validate_content_string(content)
    else:
        # Read from file
        filepath = Path(sys.argv[1])
        is_valid = validate_file(filepath)
    
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()
