# Chapter 2: Frequency with which conf interval contains exact mean.
#            Exact mean is known to equal 1.

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
import seaborn as sns

random.seed(100);             # set random number generator seed
se = np.sqrt(np.exp(1));
 
M=10**4;
Ms = [10**2, 10**3, 10**4, 10**5, 10**6, 10**7];
repeats = [10**2, 10**3, 10**4];
length = len(repeats);
m = np.zeros(length);
s_mean = np.zeros(length);
s_std = np.zeros(length);
hitfreq = np.zeros(length);

for i in range(length):
  reps = repeats[i];
  hits = 0;
  for k in range(reps):
      x = np.exp(random.normal(0,1,M))/se;   # samples
      s_mean = np.mean(x);         # sample mean
      s_std = np.std(x,ddof=1);           # sample standard deviation
      ebar = 1.96*s_std/np.sqrt(M); 
      clower = s_mean-ebar;     # left endpoint of C.I.
      cupper = s_mean+ebar;     # right endpoint of C.I.
      if ((s_mean-ebar<1) and (s_mean+ebar>1)):
        hits = hits+1;          # increment if successful
  hitfreq[i] = hits/reps;  # required frequency 

print('frequencies = '+str(hitfreq))

# Exercise 1 - Intervals and sample means, varying M.
plt.figure(figsize = (10, 10))
for j in range(len(Ms)):
    x = np.exp(random.normal(0,1,Ms[j]))/se;   # samples
    s_mean = np.mean(x);         # sample mean
    s_std = np.std(x,ddof=1);           # sample standard deviation
    ebar = 1.96*s_std/np.sqrt(Ms[j]); 
    clower = s_mean-ebar;     # left endpoint of C.I.
    cupper = s_mean+ebar;     # right endpoint of C.I.
    plt.vlines(x = Ms[j], ymin = clower, ymax = cupper,
           colors = 'blue',
           label = 'vline_multiple - full height')
    plt.plot(Ms[j], s_mean, marker="x")           
    plt.xlabel('M: Number of samples')
    plt.xscale('log')
    plt.ylabel('Sample mean & Confidence intervals')
    plt.axhline(y=1, color='r', linestyle='dotted', linewidth=0.5)

plt.show()

# Exercise 2 - CLT illustration with Z_i = sin(2pi Y_i), Y_i ~ Unif(0,1).
x = np.zeros(10**4);
for j in range(10**4):
    u = np.sin(2*np.pi*random.uniform(0,1,10**4));   # samples
    x[j] = u.sum();

v = x/(np.sqrt(10**4)*1/4) # CLT affirms (Sum Z_i - ME(Z))/(sqrt(M)V(Z)) approaches a rv N ~ N(0,1) 
sns.displot(v,kde=True); # Lets verify it!
plt.show();
