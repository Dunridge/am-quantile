import pandas as pd

df = pd.DataFrame({"A": [1, 5, 3, 4, 2],
                   "B": [3, 2, 4, 3, 4],
                   "C": [2, 2, 7, 3, 4],
                   "D": [4, 3, 6, 12, 7]})

print(df)

# find the product over the index axis
print(df.quantile(.2, axis=0))

# Use quantile() function to find the (.1, .25, .5, .75) qunatiles along the index axis.
print(df.quantile([.1, .25, .5, .75], axis=0))

'''
Quantiles are cut points dividing the range of a probability distribution into continuous
intervals with equal probabilities, or dividing the observations in a sample in the same
way. There is one fewer quantile than the number of groups created. Common quantiles have
special names, such as quartiles (four groups), deciles (ten groups), and percentiles (100 
groups). The groups created are termed halves, thirds, quarters, etc., though sometimes the
terms for the quantile are used for the groups created, rather than for the cut points.
'''