# UDACTIY: Inferential
# T-tests


#Note: remember to use degrees of freedom and not n when calculating p-values.
# Use T-statistic for small sample sizes and when population mean unknown (pretty much all the time)
# It has a similar but more spread out distribution to the normal one, due to higher error rates as inputs less certain
# Degrees of freedom; df = n-1
# Find P-value in t stat tables or online calculators http://www.graphpad.com/quickcalcs/ (OR R?)
# Don't forget to take into account whether one or two tailed test (referenced at top of t tables)
# To double check above point, the confidence level at bottom of table

# Then find the t-statistic

t_statistic <- function(sm, pm, s, n) {
    meandiff <- sm - pm
    stan_error <- s/sqrt(n)
    t <- meandiff/stan_error
    return(t)
  }

#rent example
rent_t <- t_statistic(1700, 1830, 200, 25)

cohens_d <- function(sm, pm, s){
      d <- (sm-pm)/s
      return(d)
}

rent_d <- cohens_d(1700, 1830, 200)

#Recap confidence intervals
#to capture 95% of the population, we multiply the standard error by 2

std_error <- function(s, n) {
  se <- s/(sqrt(n))
  return(se)
}

rent_se <- std_error(200, 25)

rent_lower_CI <- 1700 - (2.064*rent_se)
rent_upper_CI <- 1700 + (2.064*rent_se)

#margin of error if n changes to 100
# remember that with t dist, the t statistic will also change when n changes
# z however stays the same

rent_se_n100 <- std_error(200, 100)

rent_me_n100 <- margin_error(1.984, rent_se_n100)

# NOTE: significant drop in margin of error when n rises
# Remember the t distribution is relatively flat compared to the normal.
# As we are able to increase accuracy, the t distribution will condense, to approach reality

# All above (t & z) designed to ensure we now how to statistically decide if a sample is different from it's population'


### Now we look at dependent t-test for paired samples
# a sample is dependent when same subject takes the test twice
#
## Within subject design examples:
# two conditions (control and then treatment, or two treatments to test)
# pre-test and post-test
# growth over time (longitudinal study)

#measurements correspond to two events or tests or points in time
#and we are concerned with the difference between the two.

?sd

#see 'keyboards' sheet on google drive for workings of point estimate and std_error

kt <- -2.72 / (3.69/sqrt(25))

# is this difference significant? - need t-critical value for desired confidence level
# to check the distribution

# NOTE: just coincidence that the keyboard t-test statistic is same as s

## In this test we find the t-statistic is bigger than the t-critical values for alphs = 0.05
## Therefore we can reject the null and given the experiment design enablse causal conclusions
## we can state that the QWERTY keyboard is directly responsbile for fewer errors


key_cohensd <- -2.72 / 3.69

k_se <- std_error(3.69, 25)

k_lower_ci <- lower_ci(-2.72, 2.064, k_se)
k_upper_ci <- upper_ci(-2.72, 2.064, k_se)

# klci_l <- -2.72 - (-3.69 * k_se)
# klci_u <- -2.72 + (-3.69 * k_se)

## NOTE:remember t-critical value is != t-statistic, rather the threshold for chosen alpha level
## so of the above two examples the # ones are wrong

### Conclusion: We can conclude that on average, users will make around 4 to 1 less
### errors on QWERTY than alphabetical

