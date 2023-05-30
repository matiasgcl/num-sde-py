%CH04.M     Approximate Ito integral of W dW

rng(500)            
T = 1; L = 500; dt = T/L;

dW = sqrt(dt)*randn(1,L);          % Brownian increments
W = cumsum(dW);                    % cumulative sum

ito = sum([0,W(1:end-1)].*dW)    
itoerr = abs(ito - 0.5*(W(end)^2-T))
