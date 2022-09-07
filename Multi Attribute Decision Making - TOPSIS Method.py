
import numpy as np
from scikitmcda.topsis import TOPSIS
topsis = TOPSIS()

# [250 128 24 5]
# [200 128 16 3]
# [300 256 32 4]
# [275 256 16 4]
# [225 128 32 2]

# [-1 1 1 1]

# [0.6 0.24 0.12 0.04]

# [1 4 5 7]
# [0.25 1 3 5]
# [0.2 0.33 1 3]
# [0.14 0.2 0.33 1]

print("Hello Nice to meet you")

nalt = int(input("Enter the number of alternatives: "))

ncrit = int(input("Enter the number of criterias: "))

print("Enter the elements of decision matrix in a single line separated by space:")

val = list(map(float, input().split()))

matrix = np.array(val).reshape(nalt,ncrit)

topsis.dataframe(matrix)

print("Enter 1 if maximum of criteria is preffered and -1 if minimum is preferred: ")

signal = list(map(int, input().split()))

topsis.set_signals(signal)

kind = input("Would you enter weights mannually(M), use AHP(A) or Entropy(E)? ")

if kind == ("M"):
    print("Enter the weights of  criterias in a single line separated by space: ")
    weight = list(map(float, input().split()))
    topsis.set_weights_manually(weight)
elif kind ==("A"):
    print("Enter the Comparison of  criterias in a single line separated by space: ")
    weight = list(map(float, input().split()))
    weights = np.array(weight).reshape(ncrit,ncrit)
    topsis.set_weights_by_AHP(weights)
elif kind == ("E"):
    topsis.set_weights_by_entropy()
topsis.decide()
print("RANKING TOPSIS with", topsis.normalization_method , ":\n", topsis.pretty_decision())