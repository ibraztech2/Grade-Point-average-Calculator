from sys import path
import os

print(path)
path.append('C:\\Users\\ARC-ROBOT\\PycharmProjects')
print(path[-1])

import tic_tac_toe_cisco_project.integrator as int
int.play()

