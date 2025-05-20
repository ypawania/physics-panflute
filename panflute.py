from openpyscad import *

freq_list = [1046.5, 1174.66, 1318.51, 1396.91, 1567.98, 1760.0, 1975.53, 2093.01]
air_column_lengths = []

for f in freq_list:
    air_column_lengths.append(round((346.4 / f) * 100 * 0.5, 4))

print(air_column_lengths)

u = Union()


def make_column(height, radius, thickness=4):
    c = Difference()
    c.append(Cylinder(h=height, r=radius))
    c.append(Cylinder(h=height + 0.002, r=radius - thickness).translate([0, 0, -0.001]))
    return c


radius = 10
for i in range(len(air_column_lengths)):
    h = 10 * air_column_lengths[i]
    u.append(make_column(h, radius).translate([2 * radius * 0.85 * i, 0, 0]))

base = Cube([170, 25, 30]).translate([0, -12.5, 0])
(u).write("panflute.scad")
