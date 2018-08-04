## 12 Across: "Mission: Demolition"

>You are tasked with demolishing a building and decide to model the distribution of your explosives one-dimensionally as points on a line. The N explosives <i>(1 <= N <= 200)</i> are described by two tuples X and R. For each explosive <i>i</i>, integer Xi <i>0 <= Xi <= 10000</i> is the x-coordinate of the explosive and integer Ri <i>(1 <= Ri <= 10000)</i> is it's explosive strength.
>
>Once an explosive is detonated it explodes. Explosive i can be detonated in one of two ways:
- By using a detonator on explosive i
- By the explosion of explosive j such that (Xj - Rj) <= Xi <= (Xj + Rj)
>
>You will only successfully demolish the building if you detonate all the explosives that have been laid. For the sake of efficiency, you want to find out the minimum number of detonators that must be used in order to detonate all the explosives.
>
>Write a function that takes as input the integer N, the tuple X and the tuple R. Your function should calculate the minimum number, D, of detonators that must be used in order to detonate all the explosives and return D * 10000.
