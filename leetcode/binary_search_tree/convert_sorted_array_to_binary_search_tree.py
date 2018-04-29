from leetcode.binary_tree.tree_node import TreeNode


def sorted_array_to_bst(nums):
    nums_len = len(nums)

    if nums_len == 0:
        return None

    middle = nums_len // 2

    root = TreeNode(nums[middle])
    root.left = sorted_array_to_bst(nums[:middle])
    root.right = sorted_array_to_bst(nums[middle+1:])
    return root
