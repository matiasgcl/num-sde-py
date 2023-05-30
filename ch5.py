%CH05.M   lognormal density for two different volatilities

clf
x = linspace(.01,4,1000);
T = 1; Xzero = 1; mu = 0.05; 

sigma = 0.3;
upper = ((log(x/Xzero) - (mu-0.5*sigma^2)*T).^2)/(2*T*sigma^2);
lower = x*sigma*sqrt(2*pi*T);
y1 = exp(-upper)./lower;
plot(x,y1,'r-','LineWidth',2)
ylim([0 1.5]) 
hold on

sigma = 0.5;
upper = ((log(x/Xzero) - (mu-0.5*sigma^2)*T).^2)/(2*T*sigma^2);
lower = x*sigma*sqrt(2*pi*T);
y2 = exp(-upper)./lower;
plot(x,y2,'b--','LineWidth',2)

legend('\sigma = 0.3','\sigma = 0.5',1)
title('Lognormal density, T = 1, X(0) = 1, \mu = 0.05','FontWeight','Bold')
xlabel('x','FontWeight','Bold'), ylabel('p(x)','FontWeight','Bold')
grid on
