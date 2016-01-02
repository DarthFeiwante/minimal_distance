# minimal_distance
Program is intended for calculation of minimal interatomic distance in atomic configuration that set as 
file with cartesian atomic coordinates in choosen units

Requirements: python3

Program uses following moduli:
glob

Input files:
minimal_distance.in - each line in this file contains three cartesian atomic coordinates (see example)

Program contains function min_dist that is used for calculation of minimal interatomic distance 
in lattce that set as list of lists of atomic coordinates. Function takes three arguments:
1) r_atoms - list (with length that equals to number of atoms) of lists (x,y,z) of the cartesian atomic coordinates
2) units - name of units in string type (default = 'angstroms')
3) print_distance_dict - need for print of the interatomic distances dictionary (default = False)

Output (on screen): minimal interatomic distance in a given lattice 

Program can be used as importable or executive
