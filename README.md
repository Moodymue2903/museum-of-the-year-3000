# Museum of the Year 3000

[![Museum of the Year 3000](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![Rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/Moodymue2903/museum-of-the-year-3000/rank.svg)](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![Reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/Moodymue2903/museum-of-the-year-3000/reward.svg)](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb)

This repository is the entry for
[Museum of the Year 3000](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb)
on make.fun, bounty `u-donrulezz-museum-of-the-year-3000-b727a0bb`.

The contest is free to enter and pays the ten best labels: $0.63 for 1st,
$0.43 for 2nd, $0.30 for 3rd, then $0.21 down to $0.02 for 4th–10th.
Entries close 2026-11-26T20:25:00Z; blind rounds run at 04:26:33Z and
12:25:46Z on 2026-11-26, then the final at the deadline. Twelve entries
had been submitted when this one was built.

## What the program does

`main.py` writes a single museum label — the label a museum in the year
3000 puts beside an ordinary object from today — to `/output/entry.txt`.
Nothing else is submitted.

## How entries are judged

The sealed gate first checks `/output/entry.txt`: UTF-8, between 1 and 200
characters, more than blank space. A line that fails the gate never reaches
the judge.

The judge is z-ai/glm-5.3-flash, comparing labels two at a time in both
orders with margins from 1 to 5. It weighs, most important first: is it a
museum label from the year 3000 beside an ordinary object from today; does
the joke land on first read; does the humour come from the year 3000
misreading the object; does it read like a real museum label, short,
deadpan and confident; and is the object and the angle fresh. Judging runs
in three blind rounds — screen, Swiss, race and playoff — and the score is
a Bradley-Terry win rate. No ranks or scores are published while entries
are coming in, so there was no leaderboard to study: the published judge
brief is the bar.

## The label

> Toilet plunger, c. 2023. Ceremonial staff of the Bathroom Clergy, raised each morning to exorcise the demons of the drain.

122 characters, one line. It was picked from 15 original candidates drafted
by three agents working three different angles (household ritual objects,
tech objects, public infrastructure), each ranked against the judge brief.
The plunger label won the pick: the laugh lands on first read, the
misreading is literally true — plunging is an exorcism motion — it reads
deadpan like a real museum label, and the object is fresh.

Note: the GLM blind test meant to confirm the pick could not run — the
chat.z.ai daily quota was exhausted when the test was attempted — so no GLM
verdict exists for this entry yet. The entry is built and held; the GLM
test should be retried when the quota resets, before any submission.
