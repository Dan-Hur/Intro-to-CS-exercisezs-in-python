I devided my code into four parts: 
The first part consiists of functions that create the different menus (mostly by printing).
I also added the wav reading function in this part, and an "exit program" function that returns None, (instead of using just a constant None).
This was meant for clarification.

The second part consists of functions that manipulate the sound.
I used a few helping functions: one that averages two lists, to be used in the slow down function and low pass filter func.
Another one that reduces the values higher than max, and hightens values lover than min, used in the volume up function.
Third, a function that averages thee lists - to be used in low pass filter function.

The third pars consists of functins that copose a melody.
There are two functions for calculating the correct audio sample.
There is a function that reads a composition file (notes) and returns a list of the notes and play duration (together)
A function that converts a note (str) to the frequency (felt better than just using the dictionary straight up)
A func that translates one note and duration to an audio list, and a function that runs the previous one multiple times, to compose the melody.
In the end i added a function that runs the whole composition process.

In the last part I wrote the functions that bring the whole program together:
A function that routes between the user choice in the main menu to the different options.
A function that routes between the user choice in the alteration menu, and the manipulation function.	
A fuction that runs the manipulation process (as a loop)
and the main function that runs the whole program as long as the user did not choose to quit.

