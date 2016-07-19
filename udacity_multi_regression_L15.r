### Udacity multiple regression bonus!
###

## Multiple regression follows same principle as linear, but includes more than one predictor
## variable in the equation. They are included in the same equation as able to statistically
## determine the independent relationship each factor has on outcome variable, in context of the
## others.
## Each variable has a regression coefficient (slope), which mathematically determines the
## contribution of each variable to a 1 unit change in y(outcome)

# Example: alcohol, religiosity and self-esteem
# n = 203
# a(y-intercept) = 2.73
# religiosity coeff = -0.149
# self-esteem coeff = 0.093
# y = number of days in the last month the student drank alcohol

## For relig = 5 and self-est = 7
rel <- 5
se <- 7
days_drunk = 2.763 + (-0.149*rel) + (0.093*se)



