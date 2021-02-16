% Constants
T =input('Input the bodys orbital period around the Earth (in hours):  ');
G = 6.67*10^(-11);
M = 5.98*10^(24);
R = 6.371*10^(6);
grain = 100;
% Calculations
t = 3600*T;
h=(G*M*t^2/(4*pi^2))^(1/3) - R;
v = sqrt(G*M/(R+h));
ang = linspace(0,2*pi,grain);
% Polar plot of earth surface and orbit
pax = polarplot(ang,ones(grain,1)*(h+R),'r--');
hold on
polarplot(ang,ones(grain,1)*R,'k-')
text(pi,h+R,"orbit")
hold off
% Output
sprintf("The satellite orbits at a altitude of %0.1f km at a velocity of %.1f km/s",h/1000,v/1000)