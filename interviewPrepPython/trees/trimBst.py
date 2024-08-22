from binarytreeoops import BinaryTree

def trimBst(tree, minVal, maxVal):
    if not tree:
        return
    tree.leftChild = trimBst(tree.leftChild, minVal, maxVal)
    tree.rightChild = trimBst(tree.rightChild, minVal, maxVal)

    if minVal <= tree.key <= maxVal:
        return tree
    
    if tree.key < minVal:
        return tree.rightChild
    
    if tree.key > maxVal:
        return tree.leftChild
    

r = BinaryTree(8)
r.insertLeft(3)
r.insertLeft(1)
r.insertRight(10)
r.insertRight(14)
r.getLeftChild().insertRight(6)
r.getLeftChild().getRightChild().insertLeft(4)
r.getLeftChild().getRightChild().insertRight(7)
r.getRightChild().getRightChild().insertLeft(13)

trimtree = trimBst(r, 5, 13)
print(r)