## 8 Down: "Barb the builder"

>Barb the builder has been presented with a request to build a house with rectangular rooms.
>
>Now, Barb's idea is to represent the house as a matrix consisting of N rows and M columns where each cell has unit area. The rows are numbered 1 to N from top to bottom; columns are numbered 1 to M from left to right.
>
>Her plan is to create vertical and horizontal intersecting walls in some rows and columns. For example, if we denote empty cells with the character <b>.</b> and a wall block with the character <b>\*</b>, the following depicts the case when n=m=5 and Barb decides to create walls in the 2nd and 4th rows and similarly for columns:

```
.*.*.
*****
.*.*.
*****
.*.*.
```
>This would create rooms of closed areas (consisting of at least one empty cell) and open areas which have at least one open boundary. In the above example, we can see that there is only one room of 11 area unit.
>
>Now, the client comes to Barb and gives her an integer K and asks Barb to calculate the area of the Kth smallest room in the building.
>
>Write a function which takes the following inputs:
- Two integers N and M <i>(1 <= N, M <= 10^6)</i>
- A tuple R consisting of P <i>(1 <= P <= 10^4)</i> integers R1, R2, ..., Rp (<i>1 <= Ri <= N</i>) in an increasing order
- A tuple C consisting of Q <i>(1 <= Q <= 10^4)</i> integers C1, C2, ..., Cp (<i>1 <= Ci <= N</i>) in an increasing order
- An integer K (K >= 1) denoting the rank of the area of the required room.
>
>and outputs the area of the required room. It is guaranteed that there exists at least one room and that K doesn't exceed the number of rooms.

This was a pain because the values they gave you were huge.
