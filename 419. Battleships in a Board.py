"""最直观的做法就是dfs 数团块，但是dfs要排坑，不能转弯，最多两次遍历，
这样的话数船头是最好的"""
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]:return 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':continue
                if i > 0 and board[i-1][j] == 'X':continue
                if j > 0 and board[i][j-1] == 'X':continue
                count += 1
        return count