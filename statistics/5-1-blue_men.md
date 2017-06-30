[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```python
import scipy.stats

# Create normal distribution with mean 178 cm and standard deviation 7.7 cm
distribution = scipy.stats.norm(loc=178, scale=7.7)

#Find probability that a man is in between 5'10" and 6'1"
prob = distribution.cdf((6*12+1)*2.54) - distribution.cdf((5*12+10)*2.54)

print("Probability a man can meet the blue man group requirements: {0:.3f}".format(prob))
```

>> Probability a man can meet the blue man group requirements is 0.342.
