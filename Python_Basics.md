# Python Basics:
  > Learning Python a little at a time.

### Basics:

  * Printing & Type Conversion:
    * Printing: requires it be encased in built in function.
    * Type Conversion: Requires Int to be converted into a string before it will print properly.
    ```
    print() # Print example
    str() # String Conversion example

    # Converting a number into a string and printing it example:
    number = 1000
    print(str(number))
    ```

  * SECTION_BLANK
    * DESCRIPTION_BLANK
    ```
    ```

  * SECTION_BLANK
    * DESCRIPTION_BLANK
    ```
    ```

### Functions:
  * Basic Funtion Setup:
    * Requires `def`, `:`, `()` & __consistant__ indentation. I.E.
    ```
    def function_name_with_underscores():
      # The next line down is required to be indented at least two spaces or a single tab.
    ```

  * Returns:
    * Returns must be explicit or nothing will be returned.
    ```
    def printing_strings():
      string = str("This is a string in Python!")
      return string
    ```

  * Multi-Variable Inputs and Returns:
    * Functions are able to return more than one value at a time, divided by commas. These can be saved __in order__ as you would normally save a functions results.
    ```
    def multiple_results():
      str = str("This is a string.")
      int = str("This is a integer")
      return str, int # This will return two values

    new_str, new_int = multiple_results() # This will save two values in order.
    ```

  * Parameters:
    * Python functions take parameters in their `()`.
    ```
    def parameter_exmaple(x, y, z):
      print(x)
      print(y)
      print(z)
    ```

  * Comparator Statements:
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

  * SECTION_BLANK
    * DESCRIPTION_BLANK
    ```
    ```

  * SECTION_BLANK
    * DESCRIPTION_BLANK
    ```
    ```
