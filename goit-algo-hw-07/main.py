import binary_tree

def max_search(root):
    if root.right:
        return max_search(root.right)
    else:
        return root.val
    
def min_search(root):
    if root.left:
        return max_search(root.left)
    else:
        return root.val

def sum_all(root):
    if root:
        summ = root.val
        summ += sum_all(root.left)
        summ += sum_all(root.right)
        return summ
    return 0
        
# умова, дерево повинно бути бінарне деерво пошуку.
print(max_search(binary_tree.root))
print(min_search(binary_tree.root))
print(sum_all(binary_tree.root))