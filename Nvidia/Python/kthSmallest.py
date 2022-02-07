import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        heap = []
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            heapq.heappush(heap,node.val)
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
                
        for i in range(k-1):
            heapq.heappop(heap)
            
        return heap[0]