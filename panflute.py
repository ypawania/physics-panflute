from openpyscad import *

air_column_lengths = []
u = Union()

# note frequencies
freq_list = [1046.5, 1174.66, 1318.51, 1396.91, 1567.98, 1760.0, 1975.53, 2093.01]

# calculate air column heights
for f in freq_list:
    air_column_lengths.append(round((346.4 / f) * 100 * 0.5, 4))


radius = 10
thickness = 4

for i in range(len(air_column_lengths)):
    h = 10 * air_column_lengths[i]
    u.append(Cylinder(h, r=radius).translate([2 * radius * 0.85 * i, 0, 0]))

base = Cube([145, 25, 30]).translate([-15, -12.5, 0])
u.append(base)

d = Union()
for i in range(len(air_column_lengths)):
    d.append(
        Cylinder(200, r=radius - thickness).translate(
            [2 * radius * 0.85 * i, 0, -0.001]
        )
    )
(u - d).write("panflute.scad")


def make_column(height, radius, thickness=4):
    c = Difference()
    c.append(Cylinder(h=height, r=radius))
    c.append(Cylinder(h=height + 0.002, r=radius - thickness).translate([0, 0, -0.001]))
    return c
