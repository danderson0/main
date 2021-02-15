# Problem 3 "Writing Function Files in MATLAB"
## Outcomes
- Use the function syntax in MATLAB
- Clearly delineate input and output
 
## Problem 

Now it's time to learn to write and call functions in MATLAB. Functions should take specified input and pass specified output. Functions accomplish specific tasks that can be generalized and used in several programs. 

In this problem, we will write a program called `projectile.m`. It will model projectile motion as it occurs on Earth. The program `projectile.m` should take launch velocity, launch angle, and initial height (do not accept negative values here), and return range, time of flight, and maximum height during its motion. For purposes of this program, the projectile is "in flight" whenever its vertical position is above "ground", which we set at `h=0`. In addition, create a graph of the trajectory of the projectile, that is `y` vs `x`.

Please remember to check that your function works for multiple situations with varying initial heights (**oooo, come up with some good test cases and check with an online calculator**). 