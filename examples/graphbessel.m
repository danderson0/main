% an example of using a for loop to graph multiple plots without have to
% specify each one
hold on
x=0:0.1:10;
line = {'-k','-g','-r','-b','--k','--g','--r','--b',':k',':b',':r' };
for k=0:10
    plot(x,sphbesselj(k,x),line{k+1});
end
hold off