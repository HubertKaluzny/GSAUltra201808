## 9 Down: "Truly a mazing mouse"

>You have made a maze for your beloved pet mouse. The maze is divided into N imes N×N squares of unit size, arranged into N rows and N columns. One of the squares contains your mouse's goal: a piece of cheese. Each of the squares is of one of the following types:
- S - start
- . - pathway
- W - wall
- R - red key
- G - green key
- B - blue key
- C - cheese
>
>The mouse starts at S, needs all the keys before picking up the cheese.  
>
>The mouse starts without any keys. Let the tuple (i,j) denote the square at row i and column j. The mouse can move from one square to another only if those two squares share a side, and if all the conditions specific to the destination square (as listed above) are satisfied. The mouse completes the maze when it picks up the cheese.
>
>Given this representation of the maze, your function should return the minimum time in milliseconds the mouse needs to complete the maze.
