# cochlear-design-project
This is the code LEA Consulting used to perform data analysis and visualisation for the Cochlear Wind Noise Reduction Design Project.

Sample data taken from the testing period has been provided for the final optimal design and the adapted Kanso 2 reference design.

A consistent naming convention for each design should be followed so the code can read the text file.
Note the design, angle, velocity and trial number for each test.
For example, for the third trial at angle 1 and velocity 3 for design p1, the text file should be named "p1_a1_v3_3"
  - Designs names were typically a letter followed by a number.
  - The letter refers to the series of iteration (ie. 'p' was used for the parametric study).
  - The number refers to the particular design iteration in the series, with the first being 0. (ie. p7 for the eight design in the parametric study)
  
To compare different designs, the function 'compare' should be called. An example is provided to compare the final deisng and the Kanso 2 reference design at angle 1 and velocity 1:

"compare('p0', 'z1', ang=1, vel=1, des=['Reference', 'Final'])"

This will plot a line graph for the averaged FFT plot across the three trials taken for angle 1 and velocity 1 of designs p0 and z1.
This will also plot a bar chart where the relative decibel difference is taken, comparing all subsequent designs with the first design entered in the function (ie. in the above function, a single bar will be plotted comparing the decibel difference of z1 compared to p0)

Any number of designs can be compared by firstly entering the design names as separate strings in the compare function 
ie. to compare p0, p1 and p2 - call "compare('p0', 'p1', 'p2', ang=1, vel=1, des=['P0', 'P1', 'P2'])"
    
Without specifying a value for ang or vel, the defaults are set as 1. A value for ang can be chosen out of 1 and 3 (or however many angles are available if another dataset is used). A value for velocity can be selected out of 1, 2 or 3 (can also be different depending on dataset). 

A frequency domain of between 200 - 6000 Hz is default in the function, although this can be changed by setting values for 'lower' and 'higher' in the compare function.
ie. "compare('p0', 'z1', ang=1, vel=1, lower=100, upper=1000, des=['Reference', 'Final'])" will plot values between 100 and 1000 Hz.

The 'des' component of the function adds no functionality to the code and can be removed. 
This was simply added to the function so that the legends/design names outputted in the graphs for the final report matched up with the parametric tables. 
At present, des must be set. 
des expects a list with the number of strings equal to the number of designs entered. 
These strings can be anything, such as 'P0', 'Reference', or 'Liam is the fifth leg'. 
In the legend for the graphs, this name will appear in place of the design in the equivalent position 
ie. From the first example of the compare function, 'p0' is called first, and the first name in the list for des is 'Reference'. 
Therefore, in the legend, p0 will be referred to as 'Reference'.
