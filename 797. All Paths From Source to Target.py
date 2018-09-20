import copy
''' 一个dfs记录路径就搞定了,主要curpath 要deepcooy保存序列
'''
class Solution:
	def allPathsSourceTarget(self, graph):
		"""
		:type graph: List[List[int]]
		:rtype: List[List[int]]
		"""
		self.st = 0
		self.graph = graph
		self.ed = len(graph) - 1
		self.allpath = []
		self.curpath = []
		self.dfs(self.st)

		return self.allpath

	def dfs(self, st):
		self.curpath.append(st)
		if st == self.ed:
			self.allpath.append(copy.deepcopy(self.curpath))
		for son in self.graph[st]:
			self.dfs(son)
		self.curpath.pop()

if __name__ == '__main__':
    s=Solution()
    print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))