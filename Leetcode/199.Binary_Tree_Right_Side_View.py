class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        search_depth = 0    

        def search(node, height):
            
            #search_depth
            if node == None:
                
                return
            
            if height == search_depth:
                search_depth += 1
                answer.append(node.val)
            search(node.right, height + 1)
            search(node.left, height + 1)
            
        search(root, 0)
        
        return answer
