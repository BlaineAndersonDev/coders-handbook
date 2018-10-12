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

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```
