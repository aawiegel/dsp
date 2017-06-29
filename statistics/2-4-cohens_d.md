[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```python
import numpy as np
import nsfg

# Define function to calculate Cohen's d

def CohenEffectSize(group1, group2):
    """Calculate Cohen's d for two groups
    using the means and pooled standard deviations
    Inputs must have same columns
    
    group1 and group2 can be Series or DataFrames
    
    returns: pooled standard deviation difference between two groups
             as a float if arguments are Series
             as a Series (of differences) if arguments are DataFrames
    """
    # Find difference in means
    diff = group1.mean() - group2.mean()
    
    
    # Find variance and number of observations for each Series/DataFrame
    var1, var2 = group1.var(), group2.var()
    n1, n2 = len(group1), len(group2)
    
    # Calculate pooled variance
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    
    # Return Cohen's d
    return diff / np.sqrt(pooled_var)


# Load in pregnancy data and only select live births
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

# Create two new data frames containing both the first birth and all other
# births

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

# Show means for both

print("Average weight for first born: {0:.3f}".format(firsts.totalwgt_lb.mean()))
print("Average weight for all others: {0:.3f}".format(others.totalwgt_lb.mean()))

# Show Cohen's d

weight_d = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

print("Cohen's d for birth weight between groups: {0:.3f}".format(weight_d))
```
>> Outputs:
>> Average weight for first born: 7.201
>> Average weight for all others: 7.326
>> Cohen's d for birth weight between groups: -0.089
