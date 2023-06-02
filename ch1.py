# Chapter 1

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import poisson

def plotNorm(xvals,mu,sigma):
    denom = np.sqrt(2*np.pi)*sigma;
    func = np.exp(-0.5*(xvals-mu)**2/(sigma**2));
    yvals = (1/denom)*func;
    plt.plot(xvals,yvals);
    plt.title('\mu =' +str(mu)+' \sigma ='+str(sigma));
    plt.xlabel('x');
    plt.ylabel('p(x)');
    plt.grid(True);
    plt.show();

xvals = np.linspace(-10,10,101);
mu = 0;
sigma = 1;
plotNorm(xvals,mu,sigma);
xvals = np.linspace(0,20,101);
mu = 10;
sigma = 2;
plotNorm(xvals,mu,sigma);

# requested exercise
lamb = 4;
r = poisson.rvs(lamb, size=100);
sns.displot(r) # muchas opciones, plt.hist(r,bins=[0,1,2,3,4,5,6,7,8,9]) va mejor!
plt.show()