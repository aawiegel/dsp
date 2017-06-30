[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python

# Import libraries
import numpy as np

import nsfg
import thinkstats2
import thinkplot

# Load data into PMF for number of kids and find its mean
resp = nsfg.ReadFemResp()
child_dist = thinkstats2.Pmf(resp.numkdhh)
child_dist.Mean()


# Plot a histogram of the data
thinkplot.Hist(child_dist)
thinkplot.Config(xlabel="Number of children", ylabel="PMF")


# Copy the data to create a biased distribution
biased_child_dist = child_dist.Copy()

# Bias the sample by the number of children 
for value, prob in child_dist.Items():
    biased_child_dist.Mult(value, value)

# Renormalize and calculate a mean
biased_child_dist.Normalize()
biased_child_dist.Mean()


# Plot new histogram
thinkplot.Hist(biased_child_dist)
thinkplot.Config(xlabel="Number of children", ylabel="biased PMF")
```

>> The original distribution had a mean of 1.02, while the child-biased distribution had a mean of 2.89. Slightly less than half of families had 0 children so finding the distribution based on the observations of the child would skew the mean high.
