#CH07.M     Approximate Stratonovich integral of W dW
import numpy as np
import numpy.random as random

T = 1; 
L = 500; 
dt = T/L;

# Brownian increments
dW = np.sqrt(dt)*np.random.normal(0,1,L-1);
# cumulative sum
W = np.append([0],np.cumsum(dW));                        
# midpoints
Wroll = np.roll(W,1);
Wroll[0] = 0;
mid = 0.5*(Wroll[0:-1] + W[1:]);   
# new path midpoints
Wmid = mid + 0.5*np.sqrt(dt)*np.random.normal(0,1,L-1);    

strat = np.sum(Wmid*dW)    
straterr = abs(strat - 0.5*(W[-1]**2))
print(straterr)
