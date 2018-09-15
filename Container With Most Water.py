class Solution:
	#O(n2) solution
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		maxArea=-1
		for i in range(len(height)-1):
			for j in range(i+1,len(height)):
				Area=self.calculateIJ(i,j,height)
				if Area>maxArea:
					maxArea=Area
		return maxArea

	def calculateIJ(self,i,j,height):
		return abs(i-j)*min(height[i],height[j])