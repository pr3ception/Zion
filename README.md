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

Forms with underscores are invalid.

## Simulation examples

Run `python3 Sim.py` to run the coil-bead and dual-turbine demos and compute a vibergy value using the ``vibergy`` function.
For a toy model of the buoyant launch idea, run `python3 launch.py`.
`FFF.py` shows the airflow pattern from three fans facing the center.
The ``EnergyLog.md`` file also notes a spheron test where beads spin inside glass pockets between two fans.

More notes on these mechanisms can be found in ``EnergyLog.md``.

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
