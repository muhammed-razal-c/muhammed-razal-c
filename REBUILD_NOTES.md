# Rebuild notes

## Baseline
The original main branch contained only README.md, featuring HTML/Markdown, external badges, statistics and project links.

## Changes
- Simplified the profile for readability and accessibility.
- Replaced misleading featured project summaries with descriptions aligned to linked repositories.
- Removed arbitrary learning-progress percentages and most external image dependencies.
- Added an offline README validator and a GitHub Actions check with read-only permissions.
- Documented security scope.

## Authentication
No authentication is implemented or required. GitHub provides account authentication and repository permissions. This profile has no passwords, JWTs, OAuth callbacks, sessions, or refresh tokens.

## Validate
Run `python3 scripts/validate_profile.py` from any directory.

## Limits
The validator is not a comprehensive secret scanner and does not verify remote links. Review the profile rendering before merging.
