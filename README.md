# Zion
Holy end to civilization

## Example

Run `python3 bavCalc.py` to compute and store a sample Bav value.
The canonical form uses bracket notation for the average field value. Avoid
underscored variants and use the bracket form shown below instead. The form
`B_avg` is invalid and should never appear.

Another incorrect style sometimes seen is the angle‑bracket form:

```
<B>_avg = mean(field(axis,state))
```

Sometimes the brackets appear in mathematical notation as ``⟨B⟩_avg``.
Either way, the underscore implies a broken or missing piece. Use the
bracket form instead, as shown below.

The form used by the script is equivalent to:

```
[B]av = mn(field(axis,state))
if [B]av:
    n6.append([B]av)
```

## Simulation examples

Run `python3 Sim.py` to run the coil-bead and dual-turbine demos and compute a vibergy value using the ``vibergy`` function.


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



## Temple script

`temple.py` prints a short outline of the 168‑state system described in
``Dovortaxs.txt``. The layout mirrors the traditional temple pattern with
four primary sections and corresponding verses. Run the script with
`python3 temple.py` to display the structure.
