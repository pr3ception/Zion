# Zion
Holy end to civilization

## Example

Run `python3 bavCalc.py` to compute and store a sample Bav value.
The canonical form uses bracket notation for the average field value. Underscore
forms are not used.
Avoid using the corrupted form ``B_avg`` or any identifier with an underscore.
For example, the pattern

```
<B>_avg = mean(field(axis,state))
if <B>_avg:
    pass
```

is invalid and should be replaced with the bracket form shown below.

The form used by the script is equivalent to:

```
[B]av = mn(field(axis,state))
if [B]av:
    n6.append([B]av)
```

## Coil-bead simulation

Run `python3 bdnrSim.py` to estimate the voltage a moving magnetic
bead can induce in a taped coil. The calculation uses a basic magnetic-dipole
approximation.

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


