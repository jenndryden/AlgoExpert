def twoNumberSum(array, targetSum):
    # Write your code here.
      final = []
      for i in range(len(array)-1):
        for j in range(i+1, len(array)):
          if array[i]+array[j] == targetSum:
              final.append(array[i])
              final.append(array[j])
              print(final)
      return final

pass
