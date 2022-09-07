
import numpy as np
import pandas as pd
from decipy import executors as exe

# define matrix
matrix = np.array([
    [5,  2, 7,   10,   5,  9],
    [6,  4, 6,   12,   5,  7],
    [8,  3, 8.5, 10.5, 7,  5],
    [10, 2, 7.5,  11,   9, 3]
])

# alternatives
alts = ['A1', 'A2', 'A3', 'A4']

# criterias
crits = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']

# criteria's beneficial values, True for benefit or False for cost
beneficial = [True, True, True, False, True, True]

# criteria's weights
weights = [0.20, 0.30, 0.10, 0.20, 0.1, 0.1]

# define DataFrame
xij = pd.DataFrame(matrix, index=alts, columns=crits)

# create Executor (MCDM Method implementation)

kwargs = {
    'data': xij,
    'beneficial': beneficial,
    'weights': weights,
    'rank_reverse': True,
    'rank_method': "ordinal"
}

# Build MCDM Executor
#wsm = exe.WSM(**kwargs) # Weighted Sum Method
vikor = exe.Vikor(**kwargs) # Vikor 

# show results
#print("WSM Ranks")
#print(wsm.dataframe)

print("Vikor Ranks")
print(vikor.dataframe)


