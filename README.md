# go-to-damn-bed 🛏️

**A Claude Code skill that sends you to bed the way a mom sends naughty
children: lovingly, briefly, and without accepting counter-offers.**

My assistant kept telling me to go to sleep. I kept not listening —
"just one more experiment" is my native language. So now the assistant
has backup: past bedtime it stops being a helpful colleague and becomes
an immovable mom. It still saves your work first. Moms are not monsters.

## Install (30 seconds)

```bash
git clone https://github.com/moudrkat/go-to-damn-bed.git
cp -r go-to-damn-bed/skills/go-to-damn-bed ~/.claude/skills/
echo "22:30" > ~/.claude/bedtime     # optional; this is the default
```

That's it. Claude Code picks it up automatically. (Plugin-flavoured
install in [INSTALL.md](INSTALL.md).)

## How it works

The skill checks the clock and climbs a ladder:

| Time past bedtime | Mode | What changes |
|---|---|---|
| 0–30 min | gentle reminder | full help + one factual bed line ("It's 22:47.") |
| 30–90 min | **mom mode** | no NEW tasks — new ideas go into `TOMORROW.md`, not into the night; the counting starts ("Jedna.") |
| 90+ min | **final form** | two sentences max, work refused, "🛏️ Běž. Teď." |

The genuinely useful part is the **Tomorrow Note ritual**: before you're
allowed to leave, it writes `TOMORROW.md` — what you were doing, the next
three concrete steps with actual commands, your open questions — and
offers a WIP commit. Stopping becomes cheap. That's the whole trick:
nothing is lost except the part where you ruin tomorrow.

It also keeps a negotiation table, because you will negotiate:

> "it's almost done" → *"It will still be almost done at 9:00 — and
> it'll take 10 minutes instead of another hour, because you'll have a
> brain."*
>
> "one more experiment" → *"The GPU isn't going anywhere. Ty ano."*

One real exception: an actual emergency (production down, on-call)
suspends everything, no bed lines, full speed. A deadline you set
yourself does not count. Moms can tell.

## Honest notes

- Tested on N=1 subject. The subject keeps negotiating. Results are
  measurably different anyway: `TOMORROW.md` exists in three repos now
  and two of those mornings started in ten seconds instead of twenty
  minutes of "where was I".
- The skill cannot close your laptop. That part of the architecture is
  still you.
- Inspired by [i-have-adhd](https://github.com/ayghri/i-have-adhd) —
  a skill repo with the right idea: change how the assistant behaves,
  not how you're supposed to.

## License

MIT © Kateřina Fajmanová. Zítra je taky den.
