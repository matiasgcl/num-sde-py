# Chapter 3

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
import seaborn as sns
import time

# brute-classical for
L = 101;
T = 1;
dt = T/L;
xvals = np.linspace(0,T,L);
W = np.zeros(L);
xi = np.random.normal(0,1,L-1);
start_time = time.time();
for i in range(L-1):
    W[i+1] = W[i] + np.sqrt(dt)*xi[i];
elapsed = time.time()-start_time;
print(elapsed);
plt.plot(xvals,W);
plt.title('MB W(t)');
plt.xlabel('t');
plt.ylabel('W(t)');
plt.grid(True);
plt.show();

# vectorized(ish)
dB = np.zeros(L-1);
B = np.zeros(L);
start_time = time.time();
dB = np.sqrt(dt)*xi;
B = np.append([0],np.cumsum(dB));
elapsed2 = time.time()-start_time;
print(elapsed2);
ratio = elapsed2/elapsed*100;
print('vectorized method runs in '+str(ratio)+'% of time elapsed using a for loop');
plt.plot(xvals,B);
plt.title('MB B(t)');
plt.xlabel('t');
plt.ylabel('B(t)');
plt.grid(True);
plt.show();

def buildMB(L,T):
    # vectorized(ish)
    dB = np.sqrt(dt)*np.random.normal(0,1,L-1);
    B = np.append([0],np.cumsum(dB));
    return(B);

# exercise 1: Refining the BM (vectorized).

xvalsref = np.linspace(0,T,2*L-1);
aux = 0.5*(W+np.roll(W,-1))+np.sqrt(dt)*np.random.normal(0,1,L);
Bref = np.zeros(2*L-1);
Bref[::2] = B;
Bref[1::2] = aux[0:L-1];
plt.plot(xvalsref,Bref, color='red',linestyle='dashed', marker='x');
plt.plot(xvals,B, color='green', marker='o');
plt.title('B_refined(t) (red, dashed, x) and B(t) (green, o)');
plt.xlabel('t');
plt.ylabel('B(t) and B_ref(t)');
plt.grid(True);
plt.show();

# exercise 2: Exploring the scaling.
c = 1/10;
Tc = T*(c*c);
dtc = Tc/L;
dBc = np.sqrt(dtc)*np.random.normal(0,1,L-1);
Bc = 1/c*np.append([0],np.cumsum(dBc));
xcvals = np.linspace(0,Tc,L);
plt.plot(xcvals,Bc);
plt.title('V(t)=1/c*W(c^2*t)');
plt.xlabel('t');
plt.ylabel('V(t)');
plt.grid(True);
plt.show();

# example: u(t,W(t)) = exp(t+1/4*W(t))
# plot 5 different trajectories (t,u(t,W(t))
# compute M different trajectories to get a sample mean (MonteCarlo!) - dashed blue
# and compares with theoretical mean (exp(33/32*t)) - dashed black
# for M ~ 100 it is already quite good approximation.

u = np.zeros([5,L])
samp_mean = np.zeros(L);
M=100
for i in range(M):
    if(i<5):
        u[:][i] = np.exp(xvals + 1/4*buildMB(L,T));
        plt.plot(xvals,u[:][i]);
        aux = u[:][i];
    else:
        aux = np.exp(xvals + 1/4*buildMB(L,T));
    samp_mean += aux
samp_mean *= 1/M;
exact_mean = np.exp(33/32*xvals);
plt.plot(xvals,samp_mean,linestyle='dashed',color='blue');
plt.plot(xvals,exact_mean,linestyle='dashed',color='black');
plt.title('u(t,W(t)) = exp(t+1/4*W(t))');
plt.xlabel('t');
plt.ylabel('u(t,W(t))');
plt.grid(True);
plt.show();

