# Chapter 4: Computing Ito integrals

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

#np.random.seed(666);
L = 5001;
T = 1;
dt = T/L;
xvals = np.linspace(0,T,L);

def buildMB(L,T):
    # vectorized(ish)
    dB = np.sqrt(dt)*np.random.normal(0,1,L-1);
    B = np.append([0],np.cumsum(dB));
    return(dB,B);

(dW,W) = buildMB(L,T);
plt.plot(xvals,W);
plt.title('MB W(t)');
plt.xlabel('t');
plt.ylabel('W(t)');
plt.grid(True);
plt.show();
ito = np.sum(W[0:-1]*dW)
itoerr = abs(ito - 0.5*(W[-1]**2-T))/abs(0.5*(W[-1]**2-T))*100
print('Ito integral W dW from 0 to 1: '+str(ito))
print('With L: '+str(L))
print('relative error computed Ito versus exact value, in pct: ' +str(itoerr)+'%') # relative error, in pct

# Exercises: DIY (not particularly appealing tbh)