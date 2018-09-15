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