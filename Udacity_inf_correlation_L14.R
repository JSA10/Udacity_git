### LESSON 14: CORRELATION

# previous lessons primarily concerned with analysing one variable
# as we move to two, our experiment design will change:
#       how we collect and visualise our data in particular
# however the analysis is similar

# terminology for variables that may have a relationship
## predictor --> outcome
## explanatory --> response
## independent --> dependent
## can be thought of as x --> y, x determines what y will be

# to assess relationships between numeric variables = SCATTERPLOT!
# sometimes the strength and direction of a relationship is visible and obvious

## the correlation coefficient is a ratio that assess the strength and direction of a relationship
## correlation coefficient = r (pearson's r in this case)
# NOTE: r is covered in t-tests, so worth a review of missed videos. Used there to understand relationship between results from different sample means or tests
## r = covariance of X and Y = COV(X,Y) / St dev of X * St dev of Y
# The numerator measures the amount the two variables move together and the denominator the amount they vary

## r itself is not used as a ratio to symbolise the relationship - for this we need r^2
## r squared (r^2) is known as the coefficient of determination
## r squared shows us the % of variation in variable Y, explained by varation in X
## r^2 = 1 --> perfect positive relationship
## r^2 = -1 --> perfect negative relationship
## r^2 = 0 --> no relationship

l14 <- read.csv("Udacity/Correlations_L14.csv")

plot(l14$age, l14$party)
plot(l14$age, l14$pets)

cor(l14$age, l14$party, method = "pearson")
cor(l14$age, l14$pets, method = "pearson")

## NOTE: Correlations observed in samples may not transfer to populations and vice versa
## generally as sample size increases and sampling error decreases, we can be more sure that relationships hold in real life

### Hypothesis testing
### r is correlation for sample or data to hand. p (known as rho) is the true correlation for population
### Therefore a hypothesis test would be:
# H0: p = 0
# HA: p > 0, < 0, != 0

## Hypothesis testing for correlations / relationships uses the t-distribution, so need to remember degrees of freedom
## See screenshots for the formula - however will not need to calculate by hand, as software can do this
# formula: t = (r * sqrt(n-2)) / (sqrt(1 - r^2))
## What is important is intuitively understanding it and interpreting results
###  e.g. if t > t_critical for chosen alpha level then you would reject the null
###  as there is a significant relationship between x and y
###  AND the observed relationship is not likely due to sampling error

### Can calculate confidence intervals for p (rho)
### if 0 is contained within the CI, then you do not have enough evidence to reject the null
# NOTE: They used R in this example to calculate the CI...


# Add an Outlier
l14_out <- read.csv("Udacity/Correlations_L14_outlier.csv")
tail(l14_out)
cor(l14_out$age, l14_out$pets, method = "pearson")
plot(l14_out$age, l14_out$pets)

## adding an outlier changed the value of r dramatically. r is senstive to outliers, just like the mean
## Therefore it is important to gauge your data

