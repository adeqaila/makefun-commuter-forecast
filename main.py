#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — slot 1 entry.

Writes one line of weather forecast (129 characters, within the
1-140 gate) for the fictional city of Puddlejump to /output/entry.txt.

The line was chosen after studying the field already submitted and the
judge brief (in order: fictional city named + weather central; make a
bored commuter smile; real forecast register; one concrete detail;
every word earning its place):

  "In Puddlejump, drizzle till nine, then sun — the 7:42 arrives at
   7:42, the driver waits while you run, and your coffee stays hot."

Why this line: the weather arc (drizzle till nine, then sun) is a real
forecast rhythm; the exact-minute joke ("7:42 arrives at 7:42") is a
sharper take on the "on time" beat several field entries use; the
driver waiting is a warm, concrete, commuter-specific detail; the
coffee staying hot is a small comfort. No day name (the heat runs
after the deadline), no copied city name or phrasing from the field
(Zembla / Glimmerwick / Mizzlewick / Drizzlewick / Brollywick etc.),
no text addressed to the judge.

Deterministic: fixed string, no input, no network, no randomness,
no time dependence — the same bytes on every run.
"""

FORECAST = (
    "In Puddlejump, drizzle till nine, then sun \u2014 "
    "the 7:42 arrives at 7:42, the driver waits while you run, "
    "and your coffee stays hot."
)

import os


def main():
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file is exactly the one forecast line.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
