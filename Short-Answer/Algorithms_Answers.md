#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

    O(n^2)
    For the while loop on line 10 to break, the code on line 11 will have to run "n" number of times in order to break the while loop.
    Since mulitpication is the same as adding a certain number of times.

    3 * 5 is the same as 3+3+3+3+3

b)

    O(n log n)

    O(n) because the loop is directly related to the size of n
    O(log n) becuase the while loop runs only a sq rt # of times of the size of n

    The while loop on line 19 will run square root of n(rounded up), number of times for each iteration on the range of n.


c)

    O(n)

    The run time of this function is directly relevant to the size of n. It will run the same amount of times as the size of n.
    Line 29 shows the size of n decreasing by 1 each iteration or recursion call.


## Exercise II
Curret floors are all of them

runtime is O(log n)

Step 1 - Go to the middle of the current floors:
    Step 2 - drop the egg:
        if it breaks:
            and if this is the last floor to try:
                this floor is the first floor the egg will start breaking on
            Step 3a 
            Make all the floors below you, your current floors
            Go to step 1 with your new current floors

        if it does not break:
            and if this is the last floor to try:
                the floor you tried before is the first floor the egg will break on
            Step 3b - 
            make all the floors above you, your current floors
            go to step 1 with your new current floors