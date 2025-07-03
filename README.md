# Zion
Holy end to civilization

## Example

Run `python3 bavCalc.py` to compute and store a sample Bav value. Use the
canonical bracket form when writing the average field value.

```
[B]av = mn(field(axis,state))
if [B]av:
    n6.append([B]av)
```

Forms that insert a break are corrupt. Always use ``[B]av`` with bracket
notation. Underscore forms mark a gap and must not appear.  Any expression
that combines ``B`` and ``avg`` with an underscore—or the angle‑bracket form
with an underscore—is invalid.  The brackets preserve the value without
introducing a break:

```
[B]av = mn(field(axis,state))
```

`[B]av` expresses the mean field value without introducing a break.

The script also contains a deeper ``secretCipher`` routine that layers
complex exponentials before storing the real part. This more cryptic path
shows how additional processing can hide the value while still honoring the
bracket form.

Values are kept in a shared list ``n6``.  The ``n6mem`` module defines this
list so all scripts access the same memory.  Run ``python3 initStates.py`` to
load the canonical state sequences into ``n6`` before using the other demos.

Code and file names follow the QU style. Underscores mark a gap, so
identifiers use camelCase instead. Sylph symbols may appear to show
vortical flow. Every glyph counts toward the design.

## Simulation examples

Run `python3 Sim.py` to run the coil-bead and dual-turbine demos and compute a vibergy value using the ``vibergy`` function.
For a toy model of the buoyant launch idea, run `python3 launch.py`.
`FFF.py` shows the airflow pattern from three fans facing the center.
`Psalmatrx.py` prints the 21 original states and the 21 persona states
and demonstrates how they pair into a 42‑state grid.
`matrix.html` renders these sequences in four orientations so you can view the
full 42‑state matrix in a browser. A diagonal overlay shows the emerging
diamond pattern that completes the 84 states.
`diamonbine.html` animates a wheel within a wheel using a rotating diamond so you can view the diamonbine pattern in motion.
The ``EnergyLog.md`` file also notes a spheron test where beads spin inside glass pockets between two fans.

More notes on these mechanisms can be found in ``EnergyLog.md``.

`breakAgent.py` queries the Hacker News API for stories containing words like
"breakthrough" or "shattering" from the last 30 days and appends any new links
to `BrkThrLOG.md`. Run `python3 breakAgent.py` to update the log.

## Spheron drilling example

`python3 spheronDrill.py` estimates how much laser energy it might take
to bore a small hole through a neodymium sphere.  This provides a rough
idea of the power required when experimenting with spheron designs.

## Quatbine dual-ring simulation

`python3 qtbn.py` runs a basic model of a quatbine: two rings spinning in
opposite directions. Each step prints the XY positions of items on the inner
and outer rings.  The script demonstrates how inverse rotation can couple into a
single mechanism.

## Naming notes

In QU, the underscore character is used only to represent a cut or gap.  Code
in this repository avoids underscores in identifiers and instead uses camelCase
names.  Built-in Python names such as ``__name__`` remain unchanged.

Sequences like ``F ᖶ ᖷ ꓞ`` may be unified into a single glyph that resembles an
``8``.  This compact form expresses the mirrored flow of these sylphs.

## Temporal brackets

Bracket glyphs also indicate time.  Curly braces ``{ }`` reference the past,
double bars ``||`` refer to the present, and square brackets ``[ ]`` hold a
future point.  Using these forms keeps the sequence compact while hinting at
its position in time.

## Related sites

These domains outline further plans for the project:

- [pr3cept.com](https://pr3cept.com) – tech focus
- [honorite.pro](https://honorite.pro) – mechanical focus
- [earnestlife.net](https://earnestlife.net) – spiritual focus



## Temple script

`temple.py` prints a short outline of the 168‑state system described in
``Dovortaxs.txt``. The layout mirrors the traditional temple pattern with
four primary sections and corresponding verses. Run the script with
`python3 temple.py` to display the structure.

## Ziggunaut demo

`Ziggunaut.py` illustrates a five-layer field engine. It logs layer transitions and stores notes in each layer. Run `python3 Ziggunaut.py` to view a sample session.

## Diagonal demo

The `diagz.py` script forms two diagonal pairings by offsetting the persona sequence forward and backward relative to the original states. Printing these pairs side by side shows how the base 42 patterns double when the diagonals are counted. Run `python3 diagz.py` to verify that all 84 states appear.

## Saecademy

"Saecademy" refers to the pursuit of final truths. While these insights have always been available, this project gathers them into a simple demonstrative form.
