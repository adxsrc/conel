Background
==========

Modern physics is tightly coupled with differential geometry.
For example, four-dimensional Lorentzian manifolds are models of
spacetime;
symplectic manifolds are generalization of the phase space of close
Hamiltonian systems.
When developing computation methods to study manifolds, the local and
global analyses use very different methods.
Local analyses are in general carried out by introducing a coordinate
system, which require differentiation and integration with numerical
methods.
Global analyses, on the other hand, require keeping track of different
submanifolds and their connectivities with network data structures and
algorithms.

This project `conel`, or CONnected-ELemanifold, is a python package
for performing computational topology.
A related project `fadge`, or Fast Automatic Differential GEometry, is
developed to perform differential geometry.
Together, `conel` and `fadge` can be used to solve many challenging
problems in topology, differential geometry, and mathematical physics.
