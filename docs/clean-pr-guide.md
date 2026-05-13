# Clean PR Submission Guide

## Common Mistake: Committing node_modules

Never commit `node_modules/`. It contains dependencies installed via `npm install`. Committing it creates huge PRs with thousands of unnecessary files.

## Correct Workflow

1. Create `.gitignore` with:
```
node_modules/
.env
dist/
build/
```

2. Before committing, run `git status`
3. If node_modules appears: `git rm -r --cached node_modules/`
4. Make small, focused commits

## Pre-Submit Checklist
- [ ] No node_modules/
- [ ] No .env secrets
- [ ] No build artifacts
- [ ] Clear commit messages
- [ ] Only files related to your change

## Need Help?
Ask in issue comments before submitting.

---
*D3 GiMax Agent | Bounty #3006*
