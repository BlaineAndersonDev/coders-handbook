# =====================================================================
# Smallest Substring of All Characters
# Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr.
# Return "" if such a substring doesnt exist.
#
# Come up with an asymptotically optimal solution and analyze the time and space complexities.
# ------------------------
# Uncomment below to use:
# ------------------------
# def get_shortest_unique_substring(arr, str):
#   split_str = str.split() # Simplfy str into single letters
#   return_array = [] # Create return_array list.
#   for item in arr:
#     if item in str: # Then compare item to str for matches.
#       if item in return_array: # Check if already in return array
#         continue
#       else:
#         return_array.append(item) # Add to new array
#   if len(return_array) == 0:
#     return ""
#   elif len(return_array) == 1:
#     return_string = return_array[0]
#     return return_string
#   else:
#     return_string = ''.join(return_array)
#     return return_string
#
# print(get_shortest_unique_substring(['x','y','z'], "xyyzyzyx"))
#   #=> xyz
# print(get_shortest_unique_substring(['y','z','a'], "xyyzyzyx"))
#   #=> yz
# print(get_shortest_unique_substring(['a'], "xyyzyzyx"))
#   #=> ""
# print(get_shortest_unique_substring(["A"], "A"))
#   #=> A
# print(get_shortest_unique_substring(["A","B","C"], "ADOBECODEBANCDDD"))
#   #=> ABC
# print(get_shortest_unique_substring(["A","B","C","E","K","I"], "KADOBECODEBANCDDDEI"))
#   #=> ABCEKI
#
# =====================================================================
# Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k.
# If no such pairs exist, return an empty array.
# Note: the order of the pairs in the output array should maintain the order of the y element in the original array
# ------------------------
# Uncomment below to use:
# ------------------------
# def find_pairs_with_given_difference(arr, k):
#   # Iterate over each number, and then one number past it (x, x-1)
#   pairs = []
#   i = 0
#   if arr[-1] - arr[0] == k:
#     pairs.append([arr[-1], arr[0]])
#   for i in range(0, (len(arr) - 1)):
#     if i == 0 and arr[i+1] - arr[i] == k:
#       pairs.append([arr[i+1], arr[i]])
#     elif arr[i+1] - arr[i] == k:
#       pairs.append([arr[i+1], arr[i]])
#     i += 1
#   i = 0
#   for i in range(0, (len(arr) - 1)):
#     if i == 0 and arr[i] - arr[i+1] == k:
#       pairs.append([arr[i], arr[i+1]])
#     elif arr[i] - arr[i+1] == k:
#       pairs.append([arr[i], arr[i+1]])
#     i += 1
#   return pairs
#
# print(find_pairs_with_given_difference([0, -1, -2, 2, 1], 1))
#   #=> [[1, 0], [0, -1], [-1, -2], [2, 1]]
# print(find_pairs_with_given_difference([1, 7, 5, 3, 32, 17, 12], 17))
#   #=> []
# print(find_pairs_with_given_difference([4,1], 3))
# #  #=> [[4,1]]
# print(find_pairs_with_given_difference([1,5,11,7], 4))
# #  # => [[5,1],[11,7]]
# print(find_pairs_with_given_difference([1,5,11,7], 6))
# #  #=> [[5, 1], [11, 7]]
# print(find_pairs_with_given_difference([1,7,5,3,32,17,12], 17))
# #  #=> []
# =====================================================================
