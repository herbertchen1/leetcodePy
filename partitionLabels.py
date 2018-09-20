
class Solution(object):
	def partitionLabels(self, S):
		"""
		:type S: str
		:rtype: List[int]
		"""
		last = {}
		l = len(S)
		for i in range(l):
			last[S[i]] = i
		p = 0
		be = 0
		lens = []
		for i in range(l):
			p = max(p, last[S[i]])
			if p == i:
				lens.append( i - be +1)
				be = i+ 1
		return lens