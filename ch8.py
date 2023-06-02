# Chapter 8:   Plot a path of linear SDE and EM approximation

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

#np.random.seed(666);

mu = 2; sigma = 1; Xzero = 1;     # problem parameters
T = 1;                            # final time 

N = 100; dt = T/N;                # grid spacing for Brownian path
                                  # and for EM approximation 

Xpath = np.zeros(N+1);             # initialize storage for true path
Xem = np.zeros(N+1);               # initialize storage for EM path

Xpath[0] = Xzero;                 # initial value
Xem[0] = Xzero;                   # initial value

# Reminder: 
# SDE: dX(t) = mu*X(t)dt + sigma*X(t)dW(t)
# analytic sol: X(t) = X(0)exp((mu−2*sigma)t+sigma*W(t))
# EM generic iteration: X[n+1] = X[n] + dt*f(X[n]) + dW[n]g(X[n])
# In our case: f(X[n]) = mu*X[n], g(X[n])= sigma*X[n]
for j in range(N):
    Winc = np.sqrt(dt)*np.random.normal(0,1);        # Brownian path increment 
    Xpath[j+1] = Xpath[j]*np.exp((mu-0.5*sigma**2)*dt+sigma*Winc); # exact
    Xem[j+1] = Xem[j] + dt*mu*Xem[j] + sigma*Xem[j]*Winc;      # EM

tvals = np.linspace(0,T,N+1);
plt.plot(tvals,Xpath,marker='o',color='orange');
plt.plot(tvals,Xem,marker='x',linestyle='dotted',color='blue');
plt.xlabel('t');
plt.ylabel('X(t),X_em(t)');
plt.legend(['True Path','Euler-Maruyama']);
plt.title('dX(t) = mu*X(t)dt + sigma*X(t)dW(t): Analytic and Euler-Maruyama');
plt.grid(True);
plt.show()
emerr = abs(Xem[-1]-Xpath[-1]);
print(emerr);

# To-do: Vectorized.

# Ex1: 