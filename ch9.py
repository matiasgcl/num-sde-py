# Chapter 9:   Illustrate weak convergence of Euler-Maruyama
#              on a linear SDE. 

# Different paths are used for each timestep.
# Code is vectorized over paths.

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

#np.random.seed(666);
mu = 2; sigma = 0.1; Xzero = 1; T = 1;   # problem parameters
M = 5*10**4;                             # 50,000 sample paths

Xem = zeros(5,1);                        # preallocate arrays
for p in range(5):                       # loop over timesteps
       Dt = 2^(p-10); N = round(T/Dt);   # N steps of size Dt 
       Xtemp = Xzero*ones(M,1);            
       for j in range(N):
           Winc = sqrt(Dt)*randn(M,1);   # Brown. inc. for each path
           Xtemp = Xtemp + Dt*mu*Xtemp + sigma*Xtemp.*Winc; # EM 
       
       Xem(p) = mean(Xtemp);             # EM sample mean at T
       Cwidth(p) = 2*1.96*sqrt(var(Xtemp)/M); # C. I. width

Xerr = abs(Xem - exp(mu*N*Dt));      # true expected value is exp(mu*T)

Dtvals = 2.^([1:5]-10);          
loglog(Dtvals,Xerr,'b*-')
loglog(Dtvals,2*Dtvals,'r--') # reference slope of 1
axis([1e-3 1e-1 1e-3 1])
xlabel('\Delta t'), ylabel('| E(X(T)) - Sample average of X_N |')

# Least squares fit of error = C * Dt^q %%%%
A = [ones(p,1), log(Dtvals).T]; 
b = log(Xerr);
x = A\b; 
q = x(2);
resid = norm(A*x - b)

maxCIwidth = max(Cwidth)  # max 95 percent conf. interval width
