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

##### Range
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

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```

##### SECTION_BLANK
  * DESCRIPTION_BLANK
  ```
  ```