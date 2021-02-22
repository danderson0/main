 Project \#1 *Periodic Table Recall* 
===================================


Outcomes 
--------

-   Construct a function with variable number of inputs

-   Incorporate nuclear physics knowledge into a program

-   Read, process, and output data

-   Apply data structures in MATLAB

The Semi-Empirical Mass Formula 
-------------------------------

The Semi-Empirical Mass Formula is used to approximate the mass of
nuclei given the atomic number and the total number of nucleons in the
nuclei. As the name suggests, this formula derives from theory and on some empirical measurements. The theory is based on the liquid drop model proposed by George Gamow, which can account for most of the terms
in the formula and gives rough estimates for the values of the
coefficients. The formula is given in terms of the atomic number $Z$,
the total number of nucleons $A$, the proton mass $m_p$, the neutron
mass $n_p$, and 5 coefficients (the volume term, the surface term, the
Coulomb term, the asymmetry term, and the pairing term),

<a href="https://www.codecogs.com/eqnedit.php?latex=M(A,Z)&space;=&space;Zm_p&space;&plus;&space;(A-Z)m_n&space;-\frac{E_{B}}{c^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?M(A,Z)&space;=&space;Zm_p&space;&plus;&space;(A-Z)m_n&space;-\frac{E_{B}}{c^2}" title="M(A,Z) = Zm_p + (A-Z)m_n -\frac{E_{B}}{c^2}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=E_{B}&space;=&space;a_{V}&space;A&space;-&space;a_{S}&space;A^{2/3}&space;-&space;a_{C}\frac{Z(Z-1)}{A^{1/3}}&space;-&space;a_{A}&space;\frac{(A-2Z)^{2}}{A}&space;&plus;&space;\frac{a_{P}}{A^{1/2}}\delta(A,Z)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_{B}&space;=&space;a_{V}&space;A&space;-&space;a_{S}&space;A^{2/3}&space;-&space;a_{C}\frac{Z(Z-1)}{A^{1/3}}&space;-&space;a_{A}&space;\frac{(A-2Z)^{2}}{A}&space;&plus;&space;\frac{a_{P}}{A^{1/2}}\delta(A,Z)" title="E_{B} = a_{V} A - a_{S} A^{2/3} - a_{C}\frac{Z(Z-1)}{A^{1/3}} - a_{A} \frac{(A-2Z)^{2}}{A} + \frac{a_{P}}{A^{1/2}}\delta(A,Z)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=a_{V}&space;&=&&space;15.8\,MeV" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{V}&space;&=&&space;15.8\,MeV" title="a_{V} &=& 15.8\,MeV" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=a_{S}&space;&=&&space;18.3\,MeV" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{S}&space;&=&&space;18.3\,MeV" title="a_{S} &=& 18.3\,MeV" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=a_{C}&space;&=&&space;0.714\,MeV" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{C}&space;&=&&space;0.714\,MeV" title="a_{C} &=& 0.714\,MeV" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=a_{A}&space;&=&&space;23.2\,MeV" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{A}&space;&=&&space;23.2\,MeV" title="a_{A} &=& 23.2\,MeV" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=a_{P}&space;&=&&space;12.0\,MeV" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{P}&space;&=&&space;12.0\,MeV" title="a_{P} &=& 12.0\,MeV" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\delta(A,Z)=\begin{cases}&space;1,&space;&&space;\text{if&space;Z&space;even,&space;A&space;even}.\\&space;0,&space;&&space;\text{if&space;A&space;odd}&space;\\&space;-1,&space;&&space;\text{if&space;Z&space;odd,&space;A&space;even&space;}&space;\end{cases}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\delta(A,Z)=\begin{cases}&space;1,&space;&&space;\text{if&space;Z&space;even,&space;A&space;even}.\\&space;0,&space;&&space;\text{if&space;A&space;odd}&space;\\&space;-1,&space;&&space;\text{if&space;Z&space;odd,&space;A&space;even&space;}&space;\end{cases}" title="\delta(A,Z)=\begin{cases} 1, & \text{if Z even, A even}.\\ 0, & \text{if A odd} \\ -1, & \text{if Z odd, A even } \end{cases}" /></a>
 
 *E_{B}* is the binding energy of the nucleus with *A* nucleons and *Z* protons. This
quantity of mass from the protons and neutrons have been converted to
energy to bind the nuclei together. It should be noted that when talking
about masses, *MeV* is short for *MeV/c^2*. **I strongly encourage you to
work in units of MeV, where $c=1$.** 

<a href="https://www.codecogs.com/eqnedit.php?latex=931.5\,&space;MeV&space;=&space;1\,atomic\,mass\,unit&space;=&space;1.66*10^{-27}\,kg" target="_blank"><img src="https://latex.codecogs.com/gif.latex?931.5\,&space;MeV&space;=&space;1\,atomic\,mass\,unit&space;=&space;1.66*10^{-27}\,kg" title="931.5\, MeV = 1\,atomic\,mass\,unit = 1.66*10^{-27}\,kg" /></a>

Problem 
-------

You are tasked with creating a kind of periodic table "database"
program. This program (which I will call `ptable`) takes a variable
number of inputs and outputs information about the elements on the
periodic table (look into using `varargin` and `varargout` in MATLAB). The file *periodictabledata.csv* in the project folder on Github
contains the relevant information about the elements. The information
your program displays will depend upon the exact input.

1.  When taking no arguments, the program should produce two
    outputs: (i) a graph with 2 lines - mass (calculated by the
    Semi-Empircial formula) versus atomic number AND mass (calculated
    from the atomic weight) vs atomic number AND (ii) a graph of binding
    energy per nucleon vs atomic number.

2.  When taking 1 numerical argument (the atomic number of an element,
    equal to or less than 112 (the last named element Copernicium)), the
    program should return two arguments: (i) the mass of the element
    (given by the Semi-Empirical Mass formula) and (ii) a structure/table containing all the information about that element.

3.  When taking 2 numeric arguments (the atomic number and total number
    of nucleons), the program should return two outputs: (i) the mass of
    the isotope (calculated by the
    Semi-Empircial formula) and (ii) whether it is stable **(what does being stable
    even mean?? ooooo, we'll talk about this in class!)**.

4.  When taking 1 numeric argument (the atomic number) and 1 char
    argument (the name of a field/column in the .csv file), the program should
    return two outputs: (i) the mass of the element (calculated by the
    Semi-Empircial formula) and (ii) the value
    within that field (which itself could be numeric, char, or string).

Once submitted, I will test each of the 4 input types. Other things that
I will be looking for

-   Testing to make sure that the input makes sense

-   Generally applicability - (If I were to input an update .csv file
    with 118 elements, would your program still work?)

-   Comments - (would you be able to come back in 6 months and know what
    this does?)

-   Few, if any, repeated processes. You should be writing functions to accomplish repeated tasks.
