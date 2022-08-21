from random import sample
from itertools import product


N=3
M=6
total_mines=5
mine_coords = sample([*product(range(N), range(M))], total_mines)
print(mine_coords)

# N=3
# M=6
# pole = [[1 for _ in range(M)] for _ in range(N)]
# print(pole)