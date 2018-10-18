# =====================================================================
# Recursive Understanding Practice:
  # The base idea of how recursion works in function form:
      #if ___ == 1:
        #Perform Action Completion: Print/Append/Etc...
      #else:
        #Perform Action Division: Length of list / 2: Assign variables for each half.
        #Recall Self Function using new variables
  # A practical example: (With print statements available)


characters = ["Eric", "Kenny", "Kyle", "Stan", "Butters", "Wendy", "Token", "Clyde", "Tweek", "Coon", "Randy", "Shelia"]
def characters_find_chinpokemon(characters):
  if len(characters) == 1:
    print(characters[0] + " found a chinpokemon!")
  else:
    center = len(characters) / 2
    # print("center index: " + str(center) + ". Center Char: " + characters[center])
    front_half = characters[:center]
    # print("front_half: " + str(front_half))
    back_half = characters[center:]
    # print("back_half: " + str(back_half))
    characters_find_chinpokemon(front_half)
    characters_find_chinpokemon(back_half)
# Uncomment line below to run code:
# characters_find_chinpokemon(characters)


# Function "characters_find_chinpokemon" breakdown:
  # The Characters list has 12 names in it:
  # The Print statement only runs if there is ONE character in the given list.
  # Until there is only ONE character it will take the list of characters and find the center point, divide it into two lists, and RERUN the function using those new lists:
    # Run 1:
      # center index: 6. Center Char: Token
      # front_half: ['Eric', 'Kenny', 'Kyle', 'Stan', 'Butters', 'Wendy']
      # back_half: ['Token', 'Clyde', 'Tweek', 'Coon', 'Randy', 'Shelia']
    # Run 2 (Run 1 Front Half):
      # center index: 3. Center Char: Stan
      # front_half: ['Eric', 'Kenny', 'Kyle']
      # back_half: ['Stan', 'Butters', 'Wendy']
    # Run 3 (Run 2 Front Half)
      # center index: 1. Center Char: Kenny
      # front_half: ['Eric']
      # back_half: ['Kenny', 'Kyle']
    # Run 4 (Run 3 Front Half) - ONE character run, it performs the print action.
      # Eric found a chinpokemon!
    # Run 5 (Run 3 Back End)
      # center index: 1. Center Char: Kyle
      # front_half: ['Kenny']
      # back_half: ['Kyle']
    # Run 6 (Run 5 Front Half) - ONE character run, it performs the print action.
      # Kenny found a chinpokemon!
    # Run 7 (Run 5 Back Half) - ONE character run, it performs the print action.
      # Kyle found a chinpokemon!
    # Run 8 (Run 2 Back End)
      # center index: 1. Center Char: Butters
      # front_half: ['Stan']
      # back_half: ['Butters', 'Wendy']
    # Run 9 (Run 8 Front Half) - ONE character run, it performs the print action.
      # Stan found a chinpokemon!
    # Run 9 (Run 8 Back Half)
      # center index: 1. Center Char: Wendy
      # front_half: ['Butters']
      # back_half: ['Wendy']
    # Run 10 (Run 9 Front Half) - ONE character run, it performs the print action.
      # Butters found a chinpokemon!
    # Run 11 (Run 9 Back Half) - ONE character run, it performs the print action.
      # Wendy found a chinpokemon!
    # Run 12 (Run 1 Back End)
      # center index: 3. Center Char: Coon
      # front_half: ['Token', 'Clyde', 'Tweek']
      # back_half: ['Coon', 'Randy', 'Shelia']
    # Run 13 (Run 12 Front End)
      # center index: 1. Center Char: Clyde
      # front_half: ['Token']
      # back_half: ['Clyde', 'Tweek']
    # Run 14 (Run 13 Front Half) - ONE character run, it performs the print action.
      # Token found a chinpokemon!
    # Run 15 (Run 13 Back End)
      # center index: 1. Center Char: Tweek
      # front_half: ['Clyde']
      # back_half: ['Tweek']
    # Run 16 (Run 15 Front Half) - ONE character run, it performs the print action.
      # Clyde found a chinpokemon!
    # Run 17 (Run 15 Back Half) - ONE character run, it performs the print action.
      # Tweek found a chinpokemon!
    # Run 18 (Run 12 Back End)
      # center index: 1. Center Char: Randy
      # front_half: ['Coon']
      # back_half: ['Randy', 'Shelia']
    # Run 19 (Run 18 Front Half) - ONE character run, it performs the print action.
      # Coon found a chinpokemon!
    # Run 20 (Run 18 Back Half)
      # center index: 1. Center Char: Shelia
      # front_half: ['Randy']
      # back_half: ['Shelia']
    # Run 21 (Run 20 Front Half) - ONE character run, it performs the print action.
      # Randy found a chinpokemon!
    # Run 22 (Run 20 Back Half) - ONE character run, it performs the print action.
      # Shelia found a chinpokemon!


# Fibonacci Recursion:
  # The Fibonacci Sequence is essentially
    # A + B = C
    # A = B
    # B = C
    # Repeat to the n'th time.

def fibonacci_sequence(num_times, a=0, b=1):
    print("Sequence a: " + str(a) + ", b: " + str(b))
    c = 0
    if b >= num_times:
      print("END SEQUENCE")
    else:
      c = a + b
      a = b
      b = c
      fibonacci_sequence(num_times, a, b)
# Uncomment line below to run code:
# fibonacci_sequence(14)


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
