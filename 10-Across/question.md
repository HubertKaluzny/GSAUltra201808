## 10 Across: "Horse-chestnutting around"

>Alice and Bob like playing games together. One day they collect N chestnuts on a pile <i>(5 <= N <= 20000)</i> and come up with the following game:
- Alice and Bob randomly pick integers A, B, X, Y <i>(2 <= A, B, X, Y <= 1000, not necessarily distinct)</i>
- Alice and Bob take turns to play the game, and Alice plays first
- The player loses if the pile is empty at the start of their turn or if they are unable to make a valid move
- In each turn, the player must take 1, 2 or 3 chestnuts from the pile as follows:
 - They can take 1,2 or 3 chestnuts if it would leave the pile empty
 - If they are to leave a non-empty pile of chestnuts after their turn, they can only make a move that obeys the following restrictions
   - If it is Alice's turn, the number of chestnuts she leaves on the pile must not be divisible by A or B
   - If it is Bob's turn, the number of chestnuts he leaves on the pile must not be divisible by X or Y
>
>Your function should return W + 123 where W is the number of rounds that Alice won. Assume that rounds are independent and that both players play optimally.

I feel like there's something easier that we can do than what I did. Seems like a variety of https://en.wikipedia.org/wiki/Nim.
