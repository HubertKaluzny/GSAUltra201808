## 2 Down: "Flower power"

>Anna is visiting a botanical garden and notices a row of N beautiful flowers <i>(3 <= N <= 2000)</i>. The colour of each of the flowers is yellow, red or blue. Anna says that a subsequence of contiguous flowers is "super-colourful" if both of the following conditions are satisfied:
- Each of the possible colours appears at least once in the subsequence
- No two colours appear the same number of times in the subsequence
>
>For instance, the subsequence (red, red, blue) is not super-colourful as yellow does not appear. Nor is (red, red, blue, yellow, yellow) as red and yellow appear the same number of times. However, (red, blue, red, red, yellow, yellow, red) is super-colourful.
>
>Even if two flowers have the same colour, a careful observer will know that they are still two different flowers. Two sub-sequences of contiguous flowers. Two sub-sequences of contigous flowers are said to be "different" if they start or end at different flowers.

The above paragraph had me the most stumped.

>Write a function that takes as input a string S of length N. Each character S is 'Y', 'R', or 'B'. The <i>i</i>th character of S describes the colour of the <i>i</i>th flower in the row: the characters 'Y', 'R', and 'B' denote yellow, red or blue respectively. Your function should compute the number, C, of different super-colourful sub-sequences of contigous flowers there are in the entire row of flowers, and return 10000 + C.

I wasn't sure whether to maximise the length of each sub-sequence or to find out all the different sub-sequences possible. I think the solution was to find the one set of sub-sequences that would ensure all the sub-sequences added up to the full string.
