# UDACTIY: Inferential 
# T-tests 


#Note: remember to use degrees of freedom and not n when calculating p-values. 
# Use T-statistic for small sample sizes and when population mean unknown (pretty much all the time)
# It has a similar but more spread out distribution to the normal one, due to higher error rates as inputs less certain
# Degrees of freedom; df = n-1
# Find P-value in t stat tables or online calculators http://www.graphpad.com/quickcalcs/ (OR R?)

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

rent_lower_CI <- 1700 - (2*rent_se) 
rent_upper_CI <- 1700 + (2*rent_se) 





