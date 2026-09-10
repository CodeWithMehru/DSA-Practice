class Solution(object):
    def averageOfSubtree(self, root):
        self.res = 0
        
        def dfs(node):
            if not node:
                return 0, 0
                
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            curr_sum = node.val + left_sum + right_sum
            curr_count = 1 + left_count + right_count
            
            if curr_sum // curr_count == node.val:
                self.res += 1
                
            return curr_sum, curr_count
            
        dfs(root)
        return self.res