"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        o2n = {}
        
        queue = deque([node])
        o2n[node] = Node(node.val)
        
        while queue:
            curr = queue.popleft()
            
            for neighbor in curr.neighbors:
                if neighbor not in o2n:
                    o2n[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                o2n[curr].neighbors.append(o2n[neighbor])
        
        return o2n[node]