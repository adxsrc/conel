Design
======

`conel`'s design is closely related to polygon mesh in computer
graphics and cubical homology in computational homology.
In the former case, two-dimensional surfaces are represented by
elements including vertices, edges, faces, and their connectivities.
In the later case, topological space are turned into (computable)
algebra using multi-dimensional hyper-cubes.
`conel` generalizes these standard geometric elements into the notion
of "elemanifolds" so that they are not required to be simplices or
hyper-cubes.
By constructions, all elemanifolds other than vertices are open and
only include their "interior" points.
The connectivities between elemanifolds, e.g., boundaries, neighbors,
are encoded as networks in `conel`.
