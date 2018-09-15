class Solution:
	#O(n2) solution
	# def maxArea(self, height):
	# 	"""
	# 	:type height: List[int]
	# 	:rtype: int
	# 	"""
	# 	maxArea=-1
	# 	for i in range(len(height)-1):
	# 		for j in range(i+1,len(height)):
	# 			Area=self.calculateIJ(i,j,height)
	# 			if Area>maxArea:
	# 				maxArea=Area
	# 	return maxArea
	"""
	简单来说，面积由宽度b和较短边的长度（a，c） 中的c决定.
	A=bc
	在宽度减小的情况下，只有c增大，才可能使得A变大
	A=（b-1）c’
	改变长边，使得面积变小。
	问题在于这种搜索方法得到是不是局部最小。
	/*
     * 贪心算法：从两边开始向中间缩小;每一步比较左右边界高度,高度小的那个向里走一步
     *
     * 这个贪心算法,为什么最优解不会被错过？         反证法 假设会被错过。
     *         假设最优解是横坐标为x1,x2(x2在右边)的这两个点组成的
     *               只考虑扫描到x2时,x1被错过的情况(x2被错过同理)：
     *         被错过指的是 当右指针向左扫描经过x2之后,左指针还在x1的左边P处时,x1被错过。
     *
     *                     情况一   x2>p:  x2会被保留,然后左指针向右移动到x1,x1不会被错过
     *                     情况二   x2<p:  小情况一：height[p]>height[x1]    则最优解为 p,x2而不是 x1,x2。  假设不成立
     *                                   小情况二：p<=x1  最优解还是p,x2。 假设不成立
     *                             //因为x2比p和x1都小,所以容器高度取决于x2,而p比x1偏左,所以p,x2比x1,x2面积大
     *
     *
     */

	"""
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		i = 0
		j = len(height) - 1
		maxarea = 0
		while (i < j):
			if height[i] < height[j]:
				area = height[i] * (j - i)
				if area > maxarea: maxarea = area
				i += 1
			else:
				area = height[j] * (j - i)
				if area > maxarea: maxarea = area
				j -= 1
		return maxarea

	def calculateIJ(self,i,j,height):
		return abs(i-j)*min(height[i],height[j])