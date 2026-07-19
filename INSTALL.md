# Install

## Claude Code — personal skill (recommended)

```bash
git clone https://github.com/moudrkat/go-to-damn-bed.git
cp -r go-to-damn-bed/skills/go-to-damn-bed ~/.claude/skills/
```

Restart Claude Code (or start a new session). The skill activates by
itself once the clock passes bedtime — no slash command needed. To
invoke the mom on demand: `/go-to-damn-bed`.

## Per-project

Copy the same folder into a repo's `.claude/skills/` to give one project
a bedtime (for example, the repo you *always* lose track of time in).

## Configure bedtime

```bash
echo "23:00" > ~/.claude/bedtime
```

Default is 22:30. There is no way to configure "later on weekends".
Moms don't do weekends.

## As a plugin

The repo carries `.claude-plugin/plugin.json`, so it also works as a
Claude Code plugin — point your marketplace at this repo or install it
with the plugin tooling of your choice; the skill is auto-discovered
from `skills/`.

## Uninstall

```bash
rm -r ~/.claude/skills/go-to-damn-bed
```

She will not take it personally. She will simply know.
