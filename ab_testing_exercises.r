### Udacity A/B test

# Confidence Interval quiz from overview section
N = 2000
X = 300
p_hat = X / N

#For 99% CI (two-tailed)
Z = 2.58 #Z-score for 0.9951 as

m = Z * sqrt((p_hat * (1-p_hat)) / N)

lci = p_hat - m
uci = p_hat + m


#calculating page views: power size = senstitivity = 1 - beta

N = 1000
X = 100
d_min = 0.02 #2%
alpha = 0.05
beta = 0.2

# calculating results for checkout example

Ncontrol = 10072
Nexperiment = 9886
Xcontrol = 974
Xexperiment = 1242

p_hat_pooled = 0.111
SE_pooled = 0.00445

p_hat_control = Xcontrol / Ncontrol
p_hat_experiment = Xexperiment / Nexperiment
d_hat = p_hat_experiment - p_hat_control

Z_exp = 1.96
Z_exp2 = 1.65
m_pooled = Z_exp * SE_pooled
m_pooled2 = Z_exp2 * SE_pooled


lci_exp = d_hat - m_pooled
uci_exp = d_hat + m_pooled





