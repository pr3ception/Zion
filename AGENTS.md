This repository follows the QU naming style:

- The underscore `_` represents a cut or gap. Identifiers avoid underscores and
  use camelCase instead. Built-in names like `__name__` remain unchanged.
- Symbol glyphs such as `/\` and `\/` are called *sylphs* and may appear in
  documentation to represent vortical flow or other concepts.

File names must also stay short and purposeful.  Underscores imply broken
segments, so avoid them when creating new modules or variables.  This project
aims to build interplanetary systems for the glory of the LORD, and keeping the
file base clean helps preserve that mission.

Contributors should maintain these conventions in code and documentation.

### Diagznul paths

Diagonal segments in the Ziggunaut are called *diagznuls*.  They appear as
crawling diagonals across the lattice and show how the 42 base patterns
expand to 84 when mirrored.  Missing points labeled 2, 6, 8 and 9 act as a
container so the pattern steps cleanly through the full mirror.

## Research agent notes

`breakAgent.py` queries the Hacker News API for articles with terms such as
"breakthrough" or "shattering". It filters results to the last 30 days and
avoids duplicates in `BrkThrLOG.md`.  Adjust the keywords in the script if
certain topics become irrelevant.
