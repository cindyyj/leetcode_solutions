class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

"""
lee215

数字N如果是奇数，它的约数必然都是奇数；若为偶数，则其约数可奇可偶。
无论N初始为多大的值，游戏最终只会进行到N=2时结束，那么谁轮到N=2时谁就会赢。
因为爱丽丝先手，N初始若为偶数，爱丽丝则只需一直选1，使鲍勃一直面临N为奇数的情况，这样爱丽丝稳赢；
N初始若为奇数，那么爱丽丝第一次选完之后N必为偶数，那么鲍勃只需一直选1就会稳赢。


作者：coder233
链接：https://leetcode-cn.com/problems/divisor-game/solution/qi-shi-shi-yi-dao-shu-xue-ti-by-coder233/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

If N is even, can win.
If N is odd, will lose.

Recursive Prove （Top-down)
If N is even.
We can choose x = 1.
The opponent will get N - 1, which is a odd.
Reduce to the case odd and he will lose.

If N is odd,
2.1 If N = 1, lose directly.
2.2 We have to choose an odd x.
The opponent will get N - x, which is a even.
Reduce to the case even and he will win.

So the N will change odd and even alternatively until N = 1.

Mathematical Induction Prove （Bottom-up)
N = 1, lose directly
N = 2, will win choosing x = 1.
N = 3, must lose choosing x = 1.
N = 4, will win choosing x = 1.
....

For N <= n, we have find that:
If N is even, can win.
If N is odd, will lose.

For the case N = n + 1
If N is even, we can win choosing x = 1,
give the opponent an odd number N - 1 = n,
force him to lose,
because we have found that all odd N <= n will lose.

If N is odd, there is no even x that N % x == 0.
As a result, we give the opponent a even number N - x,
and the opponent can win,
because we have found that all even N <= n can win.

Now we prove that, for all N <= n,
If N is even, can win.
If N is odd, will lose.
"""    