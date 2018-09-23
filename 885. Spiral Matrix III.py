class Solution(object):
	def spiralMatrixIII(self, R, C, r0, c0):
		ans = [(r0, c0)]
		if R * C == 1: return ans
		# For walk length k = 1, 3, 5 ...
		for k in range(1, 2 * (R + C), 2):
			# For direction (dr, dc) = east, south, west, north;
			#  and walk length dk...
			for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k + 1), (-1, 0, k + 1)):
				# For each of dk units in the current direction ...
				#东南西北走，为一轮，最后两步走长点，在轨道内就push进去
				for _ in range(dk):
					# Step in that direction
					r0 += dr
					c0 += dc
					# If on the grid ...
					if 0 <= r0 < R and 0 <= c0 < C:
						ans.append((r0, c0))
						if len(ans) == R * C:
							return ans