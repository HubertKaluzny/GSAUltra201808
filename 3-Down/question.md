## 3 Down: "Fearful symmetry"

>A string is a palindrome if it reads the same backwards as forwards. For instance, "cabac" and "beeb" are palindromes, but "abb" is not.
>
>Given a string T, we define the "score" of T as the length of the longest palindrome that can be constructed by using some of the characters of T. For instance, the score of T = "abc" is 1, corresponding to the possible palindromes "a", "b", or "c". The score of T = "aacggg" is 5, corresponding to the palindrome "gacag".
>
>Write a function that takes as input a string S consisting of N characters <i>(200 <= N <= 5000)</i>, each from the set <i>{'a', 'b', 'c', 'd', 'e', 'f', 'g'}</i>. Your function should split S into four non-overlappig pieces such that:
- Each piece has non-zero length
- Each piece consists of contiguous characters
- The sum of the scores of each piece is minimised
>
>Your function should return the minimum total score for S.

Couldn't think of anything smarter than brute-forcing through all the possible combinations of string groups, although I did think about starting by splitting exactly into 4 quarters to minimise computation time but didn't get time to implement).

Calculating the longest possible palindrome seemed easy enough, I think there may have been a particular smart solution due to the set reduction to just 7 characters (e.g by setting numerical weight to each and checking divisibility), although it could be a dead-end. 
