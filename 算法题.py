"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""
def climbStairs(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	dq = [0] * (n + 1)
	dq[1] = 1
	dq[2] = 2
	for i in range(3, n + 1):
		#斐波那契数列
		dq[i] = dq[i - 1] + dq[i - 2]
	return dq[n]

n = 5
print(climbStairs(n))
