# Python Refresher:
  > As of Oct 10th I began learning Python a little at a time.
  > I've compiled the basics as well as some more complex uses of Python here for future reference.

___
##### Authors Note:
  > This guide is one of many written by [Blaine Anderson](https://github.com/BlaineAndersonDev).
  > You can find this and the rest of his guides in a special Github repository called [The Coders Handbook](https://github.com/BlaineAndersonDev/coders-handbook).
___
### Basics:

##### Printing & Type Conversion:
  * Printing: requires it be encased in built in function.
  * Type Conversion: Requires Int to be converted into a string before it will print properly.
  ```
  print() # Print example
  str() # String Conversion example

  # Converting a number into a string and printing it example:
  number = 1000
  print(str(number))
  ```

##### Boolean Values
  * `True` & `False` boolean values are notated in Python by using a capital first letter. These will generally change color in editors to indicate they are a boolean.
  ```
  True
  False
  ```

##### Basic Function Setup:
  * Requires `def`, `:`, `()` & __consistant__ indentation. I.E.
  ```
  def function_name_with_underscores():
    # The next line down is required to be indented at least two spaces or a single tab.
  ```

##### Returns:
  * Returns must be explicit or nothing will be returned.
  ```
  def printing_strings():
    string = str("This is a string in Python!")
    return string
  ```

##### Multi-Variable Inputs and Returns:
  * Functions are able to return more than one value at a time, divided by commas. These can be saved __in order__ as you would normally save a functions results.
  ```
  def multiple_results():
    str = str("This is a string.")
    int = str("This is a integer")
    return str, int # This will return two values

  new_str, new_int = multiple_results() # This will save two values in order.
  ```

##### Parameters:
  * Python functions take parameters in their `()`.
  ```
  def parameter_exmaple(x, y, z):
    print(x)
    print(y)
    print(z)
  ```

##### Comparator Statements:
  * Using If statements for simple comparisons requires: `if`, `:`, and comparators such as:
    * `<`    :    Less Than
    * `<=`   :    Less Then or Equal To
    * `>`    :    Greater Than
    * `>=`   :    Greater Than or Equal To
    * `==`   :    Equal To
    * `!=`   :    Not Equal To
  ```
  def number_tester(number):
    if number >= 100:
      return "The number is equal to or greater than 100!"
    if number < 100:
      return "The number is less than 100."
  ```

##### Boolean Operators (`and`, `or`, `not`):
  * `and` requires that __both__ statements be `True` or else it will return `False`.
  ```
  >>> (1 + 1 == 2) and (2 + 2 == 4)
  True
  >>> (1 + 1 == 2) and (2 < 1)
  False
  >>> (1 > 9) and (5 != 6)
  False
  >>> (0 == 10) and (1 + 1 == 1)
  False
  # An example of 'and' with a function:
  def graduation_reqs(gpa, credits):
    if credits >= 120 and gpa >= 2.0:
      return "You meet the requirements to graduate!"
  ```

  * `or` requires that __only one of the statements__ be `True` to return `True`.
  ```
  >>> True or (3 + 4 == 7)
  True
  >>> (1 - 1 == 0) or False
  True
  >>> (2 < 0) or True
  True
  >>> (3 == 8) or (3 > 4)
  False
  # An example of 'or' with a function:
  def graduation_mailer(gpa, credits):
    if gpa >= 2.0 or credits >= 120:
      return True
  ```

  * `not` reverses the value of a boolean.
  ```
  >>> not 1 + 1 == 2
  False
  >>> not 7 < 0
  True
  >>> not (4 + 5 <= 9)
  False
  >>> not (8 * 2) != 20 - 4
  True
  # An example of 'not' with a function:
  ```

  * These Boolean Operators can be used un conjunction with each other:
  ```
  def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
    if (gpa >= 2.0) and not (credits >= 120):
    if not (gpa >= 2.0) and (credits >= 120):
    if not (gpa >= 2.0) and not (credits >= 120):
  ```

##### Else & Else-If Statements:
  * `else` provides a blanket of non specific actions if no provided conditions are met:
  ```
  def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
      return "You meet the requirements to graduate!"
    if (gpa >= 2.0) and not (credits >= 120):
      return "You do not have enough credits to graduate."
    if not (gpa >= 2.0) and (credits >= 120):
      return "Your GPA is not high enough to graduate."
    else:
      return "You do not meet the GPA or the credit requirement for graduation."
  ```
  * `elif` provides alternative checks for `if` before it proceeds with the blanked `else` statement.
  ```
  def grade_converter(gpa):
    grade = "F"
    if gpa >= 4.0:
  	  grade = "A"
    elif gpa >= 3.0:
  	  grade = "B"
    elif gpa >= 2.0:
  	  grade = "C"
    elif gpa >= 1.0:
  	  grade = "D"
    elif gpa >= 0.0:
  	  grade = "F"
    return grade
  ```

##### Try & Except Statements:
  * `try` will attempt an action.
  ```
  try:
    # some statement
  ```
  * `except` will execute a block of code if the action specified before fail and that type of error occurs.
  ```
  except ErrorName:
    # some statement
  ```
  * In use example:
  ```
  def raises_value_error():
    raise ValueError

  try:
  	raises_value_error()
  except ValueError:
  	print("You raised a ValueError!")
  ```

##### Large Function Example up to this point:
  ```
  def cost_ground_shipping(weight):
    if weight <= 2:
      cost = 1.50 * weight + 20.00
    elif weight > 2 and weight <= 6:
      cost = 3.00 * weight + 20.00
    elif weight > 6 and weight <= 10:
      cost = 4.00 * weight + 20.00
    else:
      cost = 4.75 * weight + 20.00
    return cost

  premeium_shipping = 125.00

  def cost_drone_shipping(weight):
    if weight <= 2:
      cost = 4.50 * weight
    elif weight > 2 and weight <= 6:
      cost = 9.00 * weight
    elif weight > 6 and weight <= 10:
      cost = 12.00 * weight
    else:
      cost = 14.25 * weight
    return cost

  def best_shipping_cost(weight):
    g_cost = cost_ground_shipping(weight)
    d_cost = cost_drone_shipping(weight)
    if g_cost < d_cost and g_cost < premeium_shipping:
      return g_cost
    elif d_cost < premeium_shipping:
      return d_cost
    else:
      return premeium_shipping

  print(best_shipping_cost(17))
  #=> 100.75
  print(best_shipping_cost(4.8))
  #=> 34.40
  print(best_shipping_cost(41.5))
  #=> 125.00
  ```

##### Lists (Arrays):
  * A list is an ordered set of objects in Python. A List must include brackets `[]` and commas `,`. It is also considered good practice to add in spaces between commas, but is not required.
  ```
  >>> heights = [61, 70, 67, 64]
  ```
  * Lists can hold Integers, Strings and even additional Lists:
  ```
  >>> heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ["Vik", 68]]
  ```

##### Using List Objects:
  * Lists can be saved as a variable using `zip()`. The zipped object is saved in memory but is accessible by using `list()` on it.
  ```
  >>> names = ['Jenny', 'Alexus', 'Sam', 'Grace']
  >>> dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

  # Here we save the two different Lists as an object.
  >>> names_and_dogs_names = zip(names, dogs_names)

  # Printing now results in an object being returned. I.E: <zip object at 0x7feddcac5348>
  >>> print(names_and_dogs_names)

  # Printing this way results in a List being returned. I.E: [('Jenny', 'Elphonse'), ('Alexus', 'Dr. Doggy DDS'), ('Sam', 'Carter'), ('Grace', 'Ralph')]
  >>> print(list(names_and_dogs_names))

  # The list can be saved as a different and easily accessible List by using 'list()'
  >>> list_of_names_and_dogs_names = list(names_and_dogs_names)
  ```
  * Lists can also be created empty for later use:
  ```
  empty_list_example = []
  ```

##### Updating List Objects:
  * Using `.append()` we can add additional items to the end of a List.
  ```
  # Create a list
  >>> my_list = [1, 2, 3]

  # Append a number
  >>> my_list.append(5)

  >>> print(my_list)
  [1, 2, 3, 5]
  ```
  * You can also combine Lists using `+`. Keep in mind this only works when combining two Lists.
  ```
  >>> orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']
  >>> print(orders)
  ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

  # Create new orders here:
  >>> new_orders = orders + ['lilac', 'iris']
  >>> print(new_orders)
  ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily', 'lilac', 'iris']
  ```
  * In order to combine a single entry __not already in a list__ with another list you would need to surround the entry in brackets:
  ```
  broken_prices = [5, 3, 4, 5, 4] + [4]
  #=> [5, 3, 4, 5, 4, 4]
  ```

##### Lists - Range
  * `range()` allows Python to automatically create a List starting with 0 (default) and ending with the number __before__ the input.
  ```
  >>> my_range = range(10)
  >>> print(my_range)
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```
  * You can also use Ranges with two parameters to begin at a specific number:
  ```
  >>> my_list = range(2, 9)
  >>> print(list(my_list))
  [2, 3, 4, 5, 6, 7, 8]
  ```
  * Ranges can also have a third parameter which will skip that many numbers:
  ```
  >>> my_range2 = range(2, 9, 2)
  >>> print(list(my_range2))
  [2, 4, 6, 8]

  >>> my_range3 = range(1, 100, 10)
  >>> print(list(my_range3))
  [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
  ```

##### Lists - Length
  * `len(list)` allows us to find the number of items in the provided list.
  ```
  my_list = [1, 2, 3, 4, 5]
  print(len(my_list))
  #=> 5
  ```

##### Lists - Select by Index
  * Lists in Python are 0-indexed.
  * By using `[]` after the list object we can select the item at the given index.
  ```
  employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
  index4 = employees[4]
  print(index4)
  #=> Ryan
  print(employees[0])
  #=> Michael
  ```
  * We can also select items from the end of list using negative indexing:
  ```
  shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
  print(len(shopping_list))
  #=> 6
  last_element = shopping_list[-1]
  element5 = shopping_list[5]
  print(last_element, element5)
  #=> cereal cereal
  ```

##### Lists - Slicing
  * `list_name[start:end]` allows us to select a specific start & end index as well as everything inbetween.
  * `start` is the index of the first element that we want to include in our selection.
  * `end` is the index of __one more__ than the last index that we want to include.
  ```
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  sublist = letters[1:6]
  print(sublist)
  #=> ['b', 'c', 'd', 'e', 'f']

  suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
  beginning = suitcase[0:4]
  print(beginning)
  #=> ['shirt', 'shirt', 'pants', 'pants']
  middle = suitcase[2:4]
  print(middle)
  #=> ['pants', 'pants']
  ```
  * Slicing can also be used to select all items from the `start` to the `end` number. I.E.
  ```
  fruits = ['apple', 'banana', 'cherry', 'date']
  print(fruits[:3]) # Omitting the start will select all items from the start up to the designated end point.
  #=> ['apple', 'banana', 'cherry']
  ```
  * We can also do something similar to select the rest of the list from a single starting point. I.E.
  ```
  fruits = ['apple', 'banana', 'cherry', 'date']
  print(fruits[2:]) # Omitting the end point will select all items from the start point to the end of the list.
  #=> ['cherry' , 'date']
  ```
  * The same idea can be applied to selecting from the end of the list using negative indexing.
  ```
  fruits = ['apple', 'banana', 'cherry', 'date']
  print(fruits[-3:]) # This will list everything from the negative index start to the end of the list.
  #=> ['banana', 'cherry', 'date']
  ```

##### Lists - Counting
  * Using `.count()` we can find out how many times a give parameter appears in a list.
  ```
  letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
  num_i = letters.count('i')
  print(num_i)
  #=> 4

  votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
  jake_votes = votes.count('Jake')
  print(jake_votes)
  #=> 9
  ```

##### Lists - Sorting
  * `list.sort()` will sort the list its attached to either numerically or alphabetically depending on the contents. This will __overwrite__ the original list.
  ```
  names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
  names.sort()
  #=> ['Albus', 'Harry', 'Hermione', 'Ron', 'Sirius']

  addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
  addresses.sort()
  print(addresses)
  #=> ['10 Downing St.', '12 Grimmauld Place', '1600 Pennsylvania Ave', '221 B Baker St.', '42 Wallaby Way', '742 Evergreen Terrace']
  ```
  * `new_list = sorted(list)` creates a new list with all the items sorted, while leaving the original list untouched.
  ```
  names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
  sorted_names = sorted(names)
  print(names)
  #=> ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
  print(sorted_names)
  #=> ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

  games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
  games_sorted = sorted(games)
  print(games)
  #=> ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
  print(games_sorted)
  #=> ['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']
  ```

##### Large Lists Example up to this point:
  * Example 1:
  ```
  inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
  inventory_len = len(inventory)
  print(inventory_len)
  #=> 19
  first = inventory[0]
  print(first)
  #=> twin bed
  last = inventory[-1]
  print(last)
  #=> pillow
  inventory_2_6 = inventory[2:6]
  print(inventory_2_6)
  #=> ['headboard', 'queen bed', 'king bed', 'dresser']
  first_3 = inventory[:3]
  print(first_3)
  #=> ['twin bed', 'twin bed', 'headboard']
  twin_beds = inventory.count('twin bed')
  print(twin_beds)
  #=> 3
  inventory.sort()
  print(inventory)
  #=> ['dresser', 'dresser', 'headboard', 'king bed', 'king bed', 'king bed', 'nightstand', 'nightstand', 'pillow', 'pillow', 'queen bed', 'sheets', 'sheets', 'table', 'table', 'twin bed', 'twin bed', 'twin bed', 'twin bed']
  ```
  * Example 2:
  ```
  toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
  prices = [2, 6, 1, 3, 2, 7, 2]
  num_pizzas = len(toppings)
  print("We sell "+str(num_pizzas)+" different kinds of pizza!")
  #=> We sell 7 different kinds of pizza!
  pizzas = list(zip(prices, toppings))
  print(pizzas)
  #=> [('pepperoni', 2), ('pineapple', 6), ('cheese', 1), ('sausage', 3), ('olives', 2), ('anchovies', 7), ('mushrooms', 2)]
  pizzas.sort()
  print(pizzas)
  #=> [(1, 'cheese'), (2, 'mushrooms'), (2, 'olives'), (2, 'pepperoni'), (3, 'sausage'), (6, 'pineapple'), (7, 'anchovies')]
  cheapest_pizza = pizzas[0]
  print(cheapest_pizza)
  #=> (1, 'cheese')
  priciest_pizza = pizzas[-1]
  print(priciest_pizza)
  #=> (7, 'anchovies')
  three_cheapest = pizzas[:3]
  print(three_cheapest)
  #=> [(1, 'cheese'), (2, 'mushrooms'), (2, 'olives')]
  num_two_dollar_slices = prices.count(2)
  print(num_two_dollar_slices)
  #=> 3
  ```

##### Cheatsheet so far:
  ```
  print()
  str()
  True
  False
  def <function_name>(<params>):
  return <value1> <value2>
  and # Both are True
  or # At least one is True
  not # Reverses Boolean Value
  if / elif / else
  try / except
  zip(<list1>, <list2>) # Combines 2 lists into a single object
  list(zip(<list1>, <list2>))
  .append()
  new_list = list1 + [<item1>, <item2>]
  range(<number>)
  len()
  list[index]
  list[start:end]
  list.count(<string or num>)
  list.sort() # Sorts the original list
  new_list = sorted(list) # Creates a new list and sorts it.
  .index()
  ```

##### For Loops
  * Loops allow you to perform an action on each item in a List. This is generally done with the same layout:
  ```
  for <temporary variable> in <list variable>:
      <action>

  # Example:
  board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
  for game in board_games:
  print(game)
  #=> Settlers of Catan
  #=> Carcassone
  #=> Power Grid
  #=> Agricola
  #=> Scrabble
  ```
  * Loops can also iterate a single action a certain number of times using `range`.
  ```
  promise = "I will not chew gum in class"
  for n in range(5):
    print(promise)
  #=> I will not chew gum in class
  #=> I will not chew gum in class
  #=> I will not chew gum in class
  #=> I will not chew gum in class
  #=> I will not chew gum in class
  ```
  * Two lists can be combined into one by looping over a single loop and appending the item to the other List.
  ```
  students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
  students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

  for student in students_period_A:
    students_period_B.append(student)

  print(students_period_B)
  #=> ["Dora", "Minerva", "Alexa", "Obie", "Alex", "Briana", "Cheri", "Daniele"]
  ```

##### For Loops - Breaks & Continues
  * Breaks tell the loop it can stop working. This is usually used when a certain condition has been met and we no longer need to loop over the code anymore.
  ```
  items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", "dinosaur_onesie"]

  # we want to check if the item with ID "knit_dress" is on sale:
  print("Checking the sale list!")
  for item in items_on_sale:
    print(item)
    if item == "knit_dress":
      break
  print("End of search!")

  #======================

  dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
  dog_breed_I_want = 'dalmation'

  for breed in dog_breeds_available_for_adoption:
    print(breed)
    if breed == dog_breed_I_want:
      print("They have the dog I want!")
      break
  ```
  * Continues allow the code to move forward through the remainder of the loop if a condition is met.
  ```
  ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

  for age in ages:
    if age < 21:
      continue
    print(age)
  ```

##### While Loops
  * The while loop performs a set of code until some condition is reached.
  ```
  dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

  index = 0
  while index < len(dog_breeds):
    print(dog_breeds[index])
    index += 1

  #=====================

  all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
  students_in_poetry = []

  while len(students_in_poetry) < 6:
    student = all_students.pop()
    students_in_poetry.append(student)
    print(students_in_poetry)
  ```

##### Looping within Loops
  ```
  project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
  for team in project_teams:
    for student in team:
      print(student)
  #=> Ava
  #=> Samantha
  #=> James
  #=> Lucille
  #=> Zed
  #=> Edgar
  #=> Gabriel

  #=====================

  sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

  scoops_sold = 0

  for location in sales_data:
    print(location)
    for sales in location:
      scoops_sold += sales
      print(scoops_sold)
  ```

##### List Comprehension
  * Shorthand for creating lists using a single line Python loop:
  ```
  new_list_name = [<element_to_append_to_new_list> for <each_element_in_old_list> in <old_list> if <conditional_expression>]

  #=====================

  words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
  usernames = []

  for word in words:
    if word[0] == '@':
      usernames.append(word)

  print(usernames)
  #=> ["@coolguy35", "@kewldawg54", "@matchamom"]

  #=====================

  usernames = [word for word in words if word[0] == '@']

  #=====================

  heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

  can_ride_coaster = [height for height in heights if height > 161]
  print(can_ride_coaster)

  #=====================

  celsius = [0, 10, 15, 32, -5, 27, 3]
  fahrenheit = [c * 9/5 + 32 for c in celsius]
  print(fahrenheit)
  #=> [32.0, 50.0, 59.0, 89.6, 23.0, 80.6, 37.4]
  ```

##### Additional Examples:
  ```
  # Using Range with Loops
  single_digits = range(10)

  # Basic for loop
  for digit in single_digits:
    print(digit)

  # Basic for loop with an additional list.
  squares = [] # New Empty List
  for digit in single_digits:
    squares.append(digit**2)
  print(squares)

  # List Comprehension
  cubes = [cube ** 3 for cube in single_digits]
  print(cubes)
  ```

### Strings
##### Slicing Strings:
  * When we slice a string we are creating a __new__ string that starts at __(and includes)__ the first_index and ends at __(but excludes)__ the last_index.
  ```
  string[first_index:last_index]
      favorite_fruit = 'blueberry'
      favorite_fruit[3:8]
        #=> 'eberr'
  ```
  * We can also have open-ended selections:
    * If we remove the first index, the slice starts at the beginning of the string:
    ```
    favorite_fruit = 'blueberry'
    favorite_fruit[:4]
      #=> 'blue'
    ```
    * If we remove the second index the slice continues to the end of the string.
    ```
    favorite_fruit = 'blueberry'
    favorite_fruit[4:]
      #=> 'berry'
    ```

##### Concatenating Strings:
  * We can also concatenate two existing strings together into a new string.
  * Note: You have to manually add in the spaces when concatenating strings if you want to include them.
  ```
  fruit_prefix = "blue"
  fruit_suffix = "berries"

  favorite_fruit = fruit_prefix + fruit_suffix # No whitespace added.
  print(favorite_fruit)
    #=> 'blueberries'

  fruit_sentence = "My favorite fruit is " + favorite_fruit # Manually added whitespace.
  print(fruit_sentence)
    #=> 'My favorite fruit is blueberries.`
  ```

##### Length of Strings:
  * We can get the length of a string using the `len()` built in method.
  ```
  favorite_fruit = "blueberry"
  print(len(favorite_fruit))
    #=> 9
  ```
  * If you are taking the length of a sentence the spaces are counted as well.
  ```
  fruit_sentence = "I love blueberries"
  len(fruit_sentence)
    #=> 18
  ```

##### Select by Indices(Index) in Strings:
  * You can use indices to select a single letter or multiple letters from a string.
  ```
  fouth_letter = company_motto[3]
  print(fouth_letter)
    #=> e
  first_four_letters = company_motto[:4]
  print(first_four_letters)
    #=> Cope
  ```
  * You can also use negative indices to select a single letter or multiple letters from the end of a string.
  ```
  company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

  second_to_last = company_motto[-2]
  print(second_to_last)
    #=> f
  final_word = company_motto[-4:]
  print(final_word)
    #=> life
  ```

##### String Mutability:
  * Strings in Python are __Immutable__, which means that each string object cannot be altered, but a new string object can be created from it.
  ```
  # THIS EXAMPLE WILL FAIL:
  first_name = "Bob"
  last_name = "Daily"

  first_name[0] = "R"
    #=> TypeError: 'str' object does not support item assignment

  # THIS EXAMPLE IS THE PROPER WAY TO DO IT
  first_name = "Bob"
  last_name = "Daily"

  fixed_first_name = "R" + first_name[1:]
  print(fixed_first_name)
    #=> Rob
  ```

##### String Escape Characters:
  * When working with strings you may find that you want to include characters that already have a special meaning in python. This is where the escape character `\` comes in.
  ```
  # THIS EXAMPLE WILL FAIL:
  favorite_fruit_conversation = "He said, "blueberries are my favorite!""
    #=> SyntaxError: invalid syntax

  # THIS EXAMPLE IS THE PROPER WAY TO DO IT
  favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
  print(favorite_fruit_conversation)
    #=> He said, "blueberries are my favorite!"
  ```

##### Iterating through Strings:
  * Because strings are lists, that means we can iterate through a string using for or while loops.
  ```
  def get_length(word):
    amount = 0
    for letter in word:
      amount += 1
    return amount
  print(get_length("Blaine"))
    #=> 6
  ```

##### Strings: ___ in ___ :
  * This built in method allows you to check if the given letter or string is contained within the given strings. This will return either True or False.
  ```
  # ______ in ____
  # letter in word

  "e" in "blueberry"
    #=> True
  "a" in "blueberry"
    #=> False

  "blue" in "blueberry"
    #=> True
  "blue" in "strawberry"
    #=> False

  def contains(big_string, little_string):
    if little_string in big_string:
      return True
    else:
      return False

  print(contains("watermelon", "melon"))
  	#=> True
  print(contains("watermelon", "berry"))
  	#=> False

  def common_letters(string_one, string_two):
    common_list = []
    for letter1 in string_one:
      if letter1 in string_two:
        if letter1 in common_list:
          continue
        else:
  	      common_list.append(letter1)
    return common_list

  print(common_letters("banana", "cream"))
  	#=> ['a']
  ```

##### Additional Examples:
  ```
  def username_generator(first_name, last_name):
    if len(first_name) < 3 or len(last_name) < 4:
    	f3 = first_name
    	l4 = last_name
    else:
      f3 = first_name[:3]
      l4 = last_name[:4]
    username = f3 + l4
    return username
  print(username_generator("Abe", "Simpson"))
    #=> AbeSimp

  def password_generator(username):
    password = ""
    password = password + username[-1]
    for i in range(len(username)):
    	password = password + username[i]
    password = password[0:-1]
    return password

  print(password_generator(username_generator("Abe", "Simpson")))
    #=> pAbeSim
  ```

### String Built-In Methods:
  *  Including: `.upper()`, `.lower()`, `.title()`, `.split()`, `.join()`, and `.format()`.
  ```
  # Uppercase all letters.
  "Hello world".upper()
    #=> "HELLO WORLD"

  # Lowercase all letters.
  "Hello world".lower()
    #=> "hello world"

  # Uppercase the first letter of each word.
  "Hello world".title()
    #=> "Hello World"

  # Add each string into a list.
  "Hello world".split()
    #=> ["Hello", "world"]

  # Join strings from a list into a single string.
  " ".join(["Hello", "world"])
    #=> "Hello world"

  # Replaces all of the selected letter with the provided letter.
  "Hello world".replace("H", "J")
    #=> "Jello world"

  # Removes all whitespace from a string.
  "     Hello world     ".strip()
    #=> "Hello world"

  # Creates a string using parameters?
  "{} {}".format("Hello", "world")
    #=> "Hello world"
  ```

##### SECTION_BLANK:
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK:
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK:
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK:
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK:
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK:
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK:
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK:
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK:
  * DESCRIPTION_BLANK
  ```
  ```
