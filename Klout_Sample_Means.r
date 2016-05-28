ksm_goog_sheet <- "https://docs.google.com/spreadsheets/d/1VP6RgkrrJlBjMtHoSwgBmUSqmzFuVVJ-8x1Nrmw7PZw/edit#gid=0"

library(readr)
ksm <- read_csv(ksm_goog_sheet)

setwd("~/Documents/DataScience/Udacity/Descriptive_stats")
ksm <- read_csv("Sampling Distributions - Lesson 7 (Responses) - Form Responses.csv")
names(ksm)
names(ksm) <- c("Timestamp", "n=1", "n=5","n=10")
str(ksm)
ksm$`n=1` <- gsub("","",ksm$`n=1`)

gsub()

?gsub
ksm$`n=1` <- as.numeric("ksm$`n=1`")

hist(ksm$`n=1`)


#Bieber Tweeter example
# Using existing population parameters, we can estimate the confidence interval for a new
# distribution that is built upon an old one

#klout population parameters
NK <- 1048
MeanK <- 37.72
sdK <- 16.04

#klout sampling distribution for samples of size 35
NKS <- 35
MeanKS <- MeanK
StdErrorK <- sdK/sqrt(NKS)

# calculating confidence intervals for sampling means of new bieber tweeter distribution
# using one sample mean
XbarBT <- 40
# see lesson 8, 'interval estimate for Population Mean' video for derivation
# to capture 95% of the population, we multiply the standard error from Klout dist by 2
# this is the equivalent of 2 standard deviations either side of the mean for sample distribution
twoSE <- 2*StdErrorK
LowerCI_BT <- XbarBT - twoSE
UpperCI_BT <- XbarBT + twoSE
#This interval is called the 95% Confidence Interval for the mean
#Using exact z score for 95% confidence interval: -1.96 < > 1.96
exactSE <- 1.96*StdErrorK
ElowerCI_BT <- XbarBT - exactSE
EupperCI_BT <- XbarBT + exactSE

#CI for sample size of 250
NKS <- 250
E250lowerCI_BT <- XbarBT - exactSE
E250upperCI_BT <- XbarBT + exactSE
#DON'T FORGET TO REFRESH DEPENDENT OBJECTS
#Probably better to create a formula that takes the population parameters as inputs

#calculations for CI are actually pretty simple - but conceptually difficult
# bigger samples give us more precise estimates by giving us smaller confidence intervals,
# because they shrink the standard deviation (standard error rate), giving us smaller
# intervals for our estimates to lie in

#CI of 98%
SE.98 <- 2.33*StdErrorK
E250.98lowerCI_BT <- XbarBT - SE.98
E250.98upperCI_BT <- XbarBT + SE.98

#z-scores for these CIs are called the CRITICAL VALUES

# Engagement Ratio example
moocER <- read.csv("/Users/jeromeahye/Downloads/Copy of Engagement ratio - Lesson 8 - Sheet1.csv", header = FALSE)
head(moocER)
names(moocER) <- "ER"
ER_mean <- mean(moocER$ER)
ER_sd <- sd(moocER$ER)
#NOTE: R's built in sd formula uses the sample correction N-1, to use the full population version use popsd()
#sample size of 20
ER_pointestimate <- 0.13
ER_StdError <- ERsd/sqrt(20)
ER_SE.95 <- 1.96*ERStdError
ER_lowerCI <- ER_pointestimate - ER_SE.95
ER_upperCI <- ER_pointestimate + ER_SE.95

#bringing this back to the task at hand. We calculated the current population parameters
#for all students engagement with the udacity course via an engagement rate metric
#which = number of minutes watched / total number of minutes available
#we then hyptohesised that if instrucur introduced a song for a key concept this may improve
#engagment. We then showed a sample of 20 students the version with the song and took the mean
#ER metric as a point estimate for effect song had (0.13mins watched per minutes available). Using the standard error calculation with
#Z score for 95% confidence we got our standard deviation score for the sampling distribution of means
#this allowed us to estimate the lower and upper intervals that 95% of means for all hypothetical samples
#exposed to the song could fall between.
# lower = 0.083 or 5 mins for every 60 available
# upper = 0.177 or 10.62 mins for every 60 available
# the original mean of population pre song was 0.077 or 4.62mins
#CONCLUSION: Thus we can conclude that we'd expect the musical version to increase
#average engagement from 4.62 mins per 60 to at least 5 and possibly up to 10.62 mins.

#Generalising the CI:
# Y% Confidence Interval = (Xbar - z*sigma/sqrt(n), Xbar + z*sigma/sqrt(n))

#Margin of error = the distance we go from sample mean on either side,
#which = half the width of the confidence interval; Margin of Error = z*sigma/sqrt(n)

#self reported engagement and learning quiz

#Mean of sample means will equal the population mean
#Need standard error for 100% of the distribution
SREngStdError <- 0.64/sqrt(20)
SRLeaStdError <- 0.73/sqrt(20)

zSREngXbar_8.94 <- (8.94 - 7.5)/SREngStdError
zSRLeaXbar_8.35 <- (8.35 - 8.2)/SRLeaStdError

#z score for engagement is 10.06 which is off the charts and has a very small probability
# of being randomly selected from the EXISTING sample of self reported engagment scores
#The z score for learning however was 0.92, which has an 18% chance of a sample being selected
# with this score or higher.
## Therefore we can say that there is SOME EVIDENCE (not conclusive) that the song has had
# an effect on the self reported scores for engagement, but not learning.
## This is because the sample mean recorded is so large and so far outside of expected means as to imply the change has had an impact








