# Reflection

## Lines of Symmetry

* Connect two vertices; or connect midpoints of two edges; or connect one vertex
to midpoint of one edge
* Have equal number of vertices on either side of line

##

Count # points.

Order points.

Pick starting point.

Derive set of points A, B, C and midpoints AB, BC, AC

Radiate lines 


## Requirements

Create and implement an algorithm that, when given a set of points on an
infinite plane, will return the complete set of lines of symmetry for those
points.

A line of symmetry is defined to be a line such that every point in the input
set, when reflected across the line, finds another point in the input set. We
would like the code to find for us the guaranteed-complete set of these lines.
 
An image that demonstrates the concept of lines of symmetry, where each point in
the input set can be thought of as a vertex of an input shape:

![Lines of Symmetry Example](https://www.onlinemathlearning.com/image-files/xlines-symmetry.png.pagespeed.ic.jD1kSL8EFu.png)

Unlike the image, for this problem statement the inputs are only the vertex
points, not the complete shapes, and they can form any arbitrary pattern, not
just the shapes shown in the image. Also because we both know that users are
very creative in terms of probing the limits of any software that we write,
your algorithm should be ready for the points in the input set to be rotated or
translated by any arbitrary amount.
