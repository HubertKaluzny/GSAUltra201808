## 1 Down: "Having a ball"

> You are given N labelled boxes and 1 <= N <= 10 balls labeled 1 to N where each box contains exactly one ball. The <i>i</i>th box contains ball <i>i</i>.
>
> You want to generate as many different configurations as possible by swapping the balls present in the boxes. A swap consists of choosing two boxes, say <i>x</i> and <i>y</i>, and putting the ball present in box <i>x</i> in box <i>y</i> and vice versa. One configuration is considered different from another if at least one ball is in a different box.
>
> The list of possible swaps you can perform is represented by <i>M</i> pairs of integers <i>(xi, yi)</i> where 1 <= M <= 10^5 and 1 <= <i>xi, yi</i> <= <i>N</i>, denoting that you can make a swap between boxes <i>x</i> and <i>y</i> if <i>(x, y)</i> or <i>(y, x)</i> is present in these <i>M</i> pairs. You can apply a permitted swap as many times as you like.
>
>Write a function that takes the following inputs:
- An integer <i>N</i>, denoting the number of boxes and balls
- A tuple of length <i>M</i>, consisting of tuples of length 2, listing the allowed swaps
and outputs the number of different configurations achievable. Since the answer could be huge, output the answer modulo (10^9 + 7).
>
>For example, the output of <i>solution(3, ((1,2),))</i> would be 2, since the two possible configurations are <i>[1, 2, 3]</i> and <i>[2, 1, 3]</i> (which can be formed by swapping the balls in first two boxes in the initial configuration).

I'm pretty confident I got the solution correct, I calculated all the permutations that were possible by evaluating all the possible swap-cycles.
