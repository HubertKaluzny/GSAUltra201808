## 4 Down: "Fibonarcos"

> Jimmy's dangerous "just one more episode" mentality when binge-watching his favourite TV shows has led him to investigate the Fibonacci sequence, a series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers and first two numbers are 1 i.e the series 1, 1, 2, 3, 5, 8,...
>
>Now, he's curious which natural numbers can be expressed as the product of powers of Fibonacci numbers only. For example, 5, 9, and 12 can all be expressed as the product of powers of Fibonacci numbers whereas 11 can't be. Formally, whether a number is expressible as <i>f1^P1 x f2^P2 x ... x fi^Pi</i> where <i>fi</i> is a Fibonacci number and <i>Pi > 0</i>, for all <i>i</i>.
>
>Write a function that takes two positive integers L and R (<i>1 <= L <= R <= 10^18, 1 <= R - L + 1 <= 10^6</i>) as inputs, and outputs the number of integers in this range (both L and R inclusive) which cannot be expressed as the product of powers of Fibonacci numbers.
>
>For example, the output of <i>solution(3, 9)</i> is 1, as 7 is the only integer in the range which cannot be expressed as the product of powers of Fibonacci numbers.

Turns out calculating a list of primes and then checking if each prime belongs to the Fibonacci sequence is expensive, so I pre-baked a list of Fibonacci primes. 
