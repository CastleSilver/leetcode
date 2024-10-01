class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        root = [i for i in range(n)]
        rank = [1]*n
        
        def find(self, x):
            if root[x] == x:
                return x
            root[x] = find(self, root[x])
            return root[x]
            
        def union(self, x, y):
            if rank[x] < rank[y]:
                root[x] = y
                for i in range(n):
                    if root[i] == x:
                        root[i] = y
            elif rank[y] < rank[x]:
                root[y] = x
                for i in range(n):
                    if root[i] == y:
                        root[i] = x
            else:
                root[y] = x
                rank[x] += 1
                for i in range(n):
                    if root[i] == y:
                        root[i] = x
        
        for edge in edges:
            x, y = edge
            rootX, rootY = find(self, x), find(self, y)
            # cycle이 존재하는지 확인
            if rootX == rootY:
                return False
            if rootX != rootY:
                union(self, rootX, rootY)
        
        return len(set(root)) == 1