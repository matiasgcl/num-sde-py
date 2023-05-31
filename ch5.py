# Chapter 5: lognormal density for two different volatilities

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

x = np.linspace(.01,4,1000);
T = 1; Xzero = 1; mu = 0.05; 

sigma = 0.3;
upper = ((np.log(x/Xzero) - (mu-0.5*sigma**2)*T)**2)/(2*T*sigma**2);
lower = x*sigma*np.sqrt(2*np.pi*T);
y1 = np.exp(-upper)/lower;
plt.plot(x,y1,label='\sigma=0.3')#,'r-','LineWidth',2)
#ylim([0 1.5]) 
#hold on

sigma = 0.5;
upper = ((np.log(x/Xzero) - (mu-0.5*sigma**2)*T)**2)/(2*T*sigma**2);
lower = x*sigma*np.sqrt(2*np.pi*T);
y2 = np.exp(-upper)/lower;
plt.plot(x,y2,label='\sigma=0.5')#,'b--','LineWidth',2)
plt.legend(['\sigma=0.3','\sigma=0.5'])
plt.title('Lognormal density, T = 1, X(0) = 1, \mu = 0.05')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.show()
