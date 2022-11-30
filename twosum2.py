def twoNumberSum(array, targetSum):
    # Write your code here.
    seen = {}
    for i, n in enumerate(array):
        if (targetSum-n) in seen:
            return((targetSum-n), n)
        else:
            seen[n]=True
    return []
    pass
