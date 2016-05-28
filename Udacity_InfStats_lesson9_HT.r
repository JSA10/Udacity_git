#Hypothesis Testing

#How do you determine whether something is unlikely to happen or not??
#what probability is unlikely? 0.05? 0.10?

#Statisticians have set and agreed on three thresholds for unlikely - called alpha levels
alpha =c(0.05, 0.01, 0.01)
# = 5%, 1% and .1%
#The alpha level represents the area above the z score in a normal distribution curve

SREng_PM <- 7.5
SREng_Psigma <- 0.64

SREng_SM <- 7.13
#What is the z-score of this sample mean?
#1 calc standard error (sampling distribution standard deviation)
SREng_SStdErr <- SREng_Psigma/sqrt(20)
#2 Calc z-score
SREng_SZ <- (SREng_SM - SREng_PM) / SREng_SStdErr

# One-tailed tests
# alpha = 0.5, z = 1.65
# alpha = 0.01, z = 2.32
# alpha = 0.001, z = 3.08

# Two-tailed tests
# alpha = 0.5, z = +-1.96
# alpha = 0.01, z = +-2.57
# alpha = 0.001, z = +-3.27

# EXAMPLE: Using Self-reported scores for engagement and learning
SRscores <- read.csv("/Users/jeromeahye/Downloads/Copy of Engagement and Learning Results - Lesson 9 - Sheet1.csv")
head(SRscores)
names(SRscores) <- c("Timestamp", "Engagement", "Learning")
str(SRscores)
summary(SRscores)
fivenum(SRscores)

install.packages("Pysch")
library(Psych)
#Psych package not available for R version 3.2.1... Need to update R on mac?

install.packages("rafalib")
library(rafalib)
popsd(SRscores$Engagement)
sapply(SRscores, popsd)

#One vs. Two-tailed tests:
#Two-tailed tests are more conservative, with less of a chance of missing an impact that
#disproves our null hypothesis. With a One-tailed test, we are only predicting whether an
#action is better or worse than something. SO generally it carries the risk that our prediction is wrong
#and we may miss the evidence. An exception is in the case of comparing a new to an existing treatment
# - we only care whether the new one is better than the old, if it doesn't have an effect or makes it worse
#it doesn't really matter - we would only accept it if it improved on the old one.

zscore <- function(mu, sig, xbar, n) {
    SE <- sig/sqrt(n)
    zs <- (xbar - mu) / SE
    return(zs)
}

SRengZ30 <- zscore(7.47, 2.41, 8.3, 30)
probSRengZ30 <- 1 - 0.9706

#What if we had the same sample mean from a larger sample size?
SRengZ50 <- zscore(7.47, 2.41, 8.3, 50)
probSRengZ50 <- 1 - 0.9927

SRengZactual <- zscore(7.47, 2.41, 7.8, 8702)

#in the examples we ran through, we reached different conclusions on whether to reject
#or accept the null depending on how large the samples were.
# NOTE: Statistics can be prone to misinterpretationa and the Data only gets us so far...
# What's important?
    # How we collected our data
    # How big our sample sizes are
    # Is our sample random?
    # etc...



