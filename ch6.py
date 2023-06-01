import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

# CH06   Plot a path of linear SDE solution

#np.random.seed(666);
L = 5001;
T = 1;
dt = T/L;
tvals = np.linspace(0,T,L);
mu = 2; 
sigma = 1; 
Xzero = 1;    

def buildMB(L,T):
    # vectorized(ish)
    dB = np.sqrt(dt)*np.random.normal(0,1,L-1);
    B = np.append([0],np.cumsum(dB));
    return(dB,B);


(dW,W) = buildMB(L,T)

# solution is given by
# Y(t)=Y(0)*exp(mu-1/2*sigma^2*t + sigma*W(t))
X = np.append([Xzero],Xzero*np.exp((mu-0.5*sigma**2)*(tvals[1:])+sigma*W[1:]));
plt.plot(tvals,X);
plt.title('dY=Y*(mu*dt + sigma*dW) solution path');
plt.xlabel('t');
plt.ylabel('X(t)');
plt.show();


