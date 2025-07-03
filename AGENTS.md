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

## Research agent notes

`breakAgent.py` queries the Hacker News API for articles with terms such as
"breakthrough" or "shattering". It filters results to the last 30 days and
avoids duplicates in `BrkThrLOG.md`.  Adjust the keywords in the script if
certain topics become irrelevant.
