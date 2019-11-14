null=0
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val=int(t1.val)+int(t2.val)
        t1.left = self.mergeTrees(t1=t1.left,t2=t2.left)
        t1.right = self.mergeTrees(t1=t1.right,t2=t2.right)
        return t1

'列表创建二叉树'
from collections import deque
 
class Tree(object):
    def __init__(self):
        self.root = None

    def construct_tree(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1

    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret

    def pre_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            ret.append(head.val)
            traversal(head.left)
            traversal(head.right)
        traversal(self.root)
        return ret

    def in_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)

        traversal(self.root)
        return ret

    def post_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            traversal(head.right)
            ret.append(head.val)

        traversal(self.root)
        return ret

tree1=[1,3,null,4,5,null,7,5,4,3,6,7,8,9,8,9]

tree2=[2,1,null,4,7,6,6,7,null,8,9,7,7,5,4,3]
# tree1=[1,0,0,1]
# tree2=[1,0,0,1]
t1 = Tree()
t1.construct_tree(tree1)
T1 = t1.root
t2 = Tree()
t2.construct_tree(tree2)
T2 = t2.root
Solution().mergeTrees(T1,T2)
print(tree1)
print(tree2)
print(t1.bfs())
# print(t1.pre_traversal())
# print(t1.in_traversal())
# print(t1.post_traversal())


