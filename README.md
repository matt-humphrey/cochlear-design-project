# cochlear-design-project
This is the code LEA Consulting used to perform data analysis and visualisation for the Cochlear Wind Noise Reduction Design Project

Sample data taken from the testing period has been provided for the final optimal design and the adapted Kanso 2 reference design

To operate the code, simply call the function compare as follows:
compare('p0','z1',vel=1,ang=1,des=['Kanso','Final'])

The function initially accepts any number of designs as a string input.
The Kanso reference design has been referred to as 'p0', and the final design selected is 'z1'.

For each trial at a specific velocity and angle, the naming convention was 'design reference_angle number_velocity number_trial number'
For example, trial 2 of the reference design at velocity 2 and angle 1 would be "p0_a1_v2_2"

Any number of designs can be entered to compare against each other, provided 

A velocity value of 1, 2 or 3 can be selected, with an angle value of 1 or 3 available.
