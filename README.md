# Zion
Holy end to civilization

## Example

Run `python3 bavCalc.py` to compute and store a sample Bav value.
The canonical form uses bracket notation for the average field value. Avoid the
corrupted underscore form ``B_avg`` in any identifier.
Use the bracket form shown below instead.

The form used by the script is equivalent to:

```
[B]av = mn(field(axis,state))
if [B]av:
    n6.append([B]av)
```

## Coil-bead simulation

Run `python3 bdnrSim.py` to estimate the voltage a moving magnetic
bead can induce in a taped coil. The calculation uses a basic magnetic-dipole
approximation. A recent test shows a 0.325" neosphere jumping between two
wrapped coils can generate roughly forty millivolts per jump, proving the
"beadron" concept can operate as a simple logioid.

## Dual-turbine example

`python3 dutbSim.py` demonstrates a simplified mechanism with two
repelling turbines.  Two particles travel on mirrored diagonal paths—called a
diazanul—repulsed from the core, guided along the rim and returned for the next
cycle.

## Quatbine dual-ring simulation

`python3 qtbn.py` runs a basic model of a quatbine: two rings spinning in
opposite directions. Each step prints the XY positions of items on the inner
and outer rings.  The script demonstrates how inverse rotation can couple into a
single mechanism.

## Naming notes

In QU, the underscore character is used only to represent a cut or gap.  Code
in this repository avoids underscores in identifiers and instead uses camelCase
names.  Built-in Python names such as ``__name__`` remain unchanged.

## Related sites

These domains outline further plans for the project:

- [pr3cept.com](https://pr3cept.com) – tech focus
- [honorite.pro](https://honorite.pro) – mechanical focus
- [earnestlife.net](https://earnestlife.net) – spiritual focus



## Digital temple template

A simple script `templeLayout.py` outlines the canonical layout of a
Biblical temple. The template divides the structure into four main
sections and cites verses that describe each part. Run the script with
`python3 templeLayout.py` to view the layout.
