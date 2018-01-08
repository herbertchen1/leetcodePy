#-*-coding:UTF8-*-
#  class Solution(object):
# 	def lengthOfLongestSubstring(self, s):
# 		maxx = -1
# 		for i in range(len(s)):
# 			for j in range(len(s), i, -1):
# 				if len(set(s[i:j+1])) == len(s[i:j+1]):
# 					maxx = len(s[i:j+1]) if len(s[i:j+1]) > maxx else maxx
# 		if maxx==-1:
# 			maxx=0
# 		return maxx

class Solution:
	# @return an integer
	def lengthOfLongestSubstring(self, s):
		#
		start = maxLength = 0
		usedChar = {}

		for i in range(len(s)):
			#用字典记录每个出现的字母上次出现的位置,start记录序列的开始
			#从头开始遍历,如果当前字母是第二次出现,开始位置就要从他第一次出现开始后移
			#如果是第一次出现,或者开始位置大于最近一次出现就更新最大序列长度
			if s[i] in usedChar and start <= usedChar[s[i]]:
				start = usedChar[s[i]] + 1
			else:
				maxLength = max(maxLength, i - start + 1)
			#每读一个位置maintain该字母最大位置
			usedChar[s[i]] = i

		return maxLength

p = Solution()
print(p.lengthOfLongestSubstring("cfukwksugbsukqpeftkzwhwwbszvyhicmfnkpfewjzsvphbucmwyvsxwkyukhcnwhcizjpxu"))
