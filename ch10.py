# Chapter 10:  Strong endpoint convergence test for Euler-Maruyama
#
# Discretized Brownian path over [0,1] has dt = 2^(-9).
# EM uses 5 different stepsizes: 16dt, 8dt, 4dt, 2dt, dt.

rng(500)
mu = 2; sigma = 1; Xzero = 1;     # problem parameters
T = 1; N = 2^9; dt = T/N;         #
M = 1e3;                          # number of sample paths

Xerr = zeros(M,5);                # preallocate array
for s = 1:M,                      # loop over disc. Brownian paths
    dW = sqrt(dt)*randn(1,N);     # Brownian increments
    W = cumsum(dW);               # discrete Brownian path 
    Xtrue = Xzero*exp((mu-0.5*sigma^2)+sigma*W(end));
    for p = 1:5                            
        R = 2^(p-1); Dt = R*dt; L = N/R;     # EM steps, Dt = R*dt
        Xtemp = Xzero;
        for j = 1:L
             Winc = sum(dW(R*(j-1)+1:R*j));
             Xtemp = Xtemp + Dt*mu*Xtemp + sigma*Xtemp*Winc;
        end
        Xerr(s,p) = abs(Xtemp - Xtrue);      # store endpoint error
    end
end

Dtvals = dt*(2.^([0:4]));               
loglog(Dtvals,mean(Xerr),'b*-'), hold on
loglog(Dtvals,(Dtvals.^(.5)),'r--'), hold off % reference slope  
axis([1e-3 1e-1 1e-2 1])
xlabel('\Delta t'), ylabel('Sample average of | X(T) - X_L |')
