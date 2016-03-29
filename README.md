# get_missing_letters
python library with tools for determining if a string is an pangram

The sentence "A quick brown fox jumps over the lazy dog" contains every single letter in the 
alphabet. Such sentences are called pangrams. Contains a method called get_missing_letters as will as other variations and returns
a string with all the letters it is missing (which prevent it from being an anagram).

The case of the letters is ignored
The return is all the lower case letters it is missing, in alphabetical order 

Examples:

1) "A quick brown fox jumps over the lazy dog"

Returns: ""

(This sentence contains every letter)

2) "A slow yellow fox crawls under the proactive dog"

Returns: "bjkmqz"

3) "Lions, and tigers, and bears, oh my!"

Returns: "cfjkpquvwxz"

4) ""

Returns: "abcdefghijklmnopqrstuvwxyz"

#particle_chamber

A collection of particles is contained in a linear chamber. They all have the same speed, but some are

headed toward the right and others are headed toward the left. These particles can pass through each 

other without disturbing the motion of the particles, so all the particles will leave the chamber 

relatively quickly.

You will be given the initial conditions by a string, init, containing at each position an 'L' for a 

leftward moving particle, an 'R' for a rightward moving particle, or a '.' for an empty location. init

shows all the positions in the chamber. Initially, no location in the chamber contains two particles 

passing through each other.

We would like an animation of the process. At each unit of time, we want a string showing occupied 

locations with an 'X' and unoccupied locations with a '.'. Create a class Animation that contains 

an instance method animate that is given an int, speed, and a string, init, giving the initial 

conditions. speed is the number of positions each particle moves in one time unit.

The method will return a list of strings in which each successive element shows the occupied 

locations at the next time unit. The first element of the return should show the occupied locations at 

the initial instant (at time = 0) in the 'X', '.' format. The last element in the return should show the 

empty chamber at the first time that it becomes empty.

Examples: (Note: the double quotes should not be considered part of the input or output strings.)

1) 2, "..R...."

The single particle starts at the 

3rd position, moves to the 5th, 

then 7th, and then out of the 

chamber.

Returns:

[ "..X....",

"....X..",

"......X",

"......." ]

2) 3, "RR..LRL"

At time 1, there are actually 4 

particles in the chamber, but two 

are passing through each other at 

the 4th position

Returns:

[ "XX..XXX",

".X.XX..",

"X.....X",

"......." ]

3) 2, "LRLR.LRLR"

At time 0 there are 8 particles. At 

time 1, there are still 6 

particles,

but only 4 positions are occupied 

since particles are passing through

each other. These particles are 

moving so fast that they all exit 

the chamber by time 1.

Returns:

[ "XXXX.XXXX",

"X..X.X..X",

".X.X.X.X.",

".X.....X.",

"........." [

4) 1, "..."

Returns:

[ "..." ]
