# Ruby Enumerable Challenge
> A small Ruby Enumerable worksheet I created to test myself daily for a few weeks, until I have all the common enumerable memorized (or at least committed to memory enough that I can mostly recall how to use them properly).

## Enumerable Examples:
> I've included a full set of examples here, as well as a few different BLANK worksheets underneath. I recommend Copy Pasting into your local machine, or using [Repl.it](Repl.it) to test each problem.

#### [String Enumerable](https://ruby-doc.org/core-2.5.1/String.html) Examples:
  * __[.capitalize](http://ruby-doc.org/core-2.5.1/String.html#method-i-capitalize)__
    ```
    # Returns a copy of str with the first character converted to uppercase and the remainder to lowercase.
    "hello".capitalize    #=> "Hello"
    "HELLO".capitalize    #=> "Hello"
    "123ABC".capitalize   #=> "123abc"

    # Using '.capitalize!' will returns nil if no changes are made. Use with caution.
    "Hello".capitalize!   #=> nil
    ```

  * __[.chars](http://ruby-doc.org/core-2.5.1/String.html#method-i-capitalize)__
    ```
    # Returns an array of characters in str. This is a shorthand for `str.each_char.to_a`.
    "hello".chars    #=> ["h", "e", "l", "l", "o"]
    "HELLO".chars    #=> ["H", "E", "L", "L", "O"]
    "123ABC".chars   #=> ["1", "2", "3", "A", "B", "C"]
    ```

  * __[.chomp](http://ruby-doc.org/core-2.5.1/String.html#method-i-chomp)__
    ```
    # Returns a new String with the given record separator or parameter removed from the end of str (if present).
    # If the selector has not been specified, then chomp will remove carriage return characters (that is it will remove \n, \r, and \r\n).
    "hello".chomp                #=> "hello"
    "hello\n".chomp              #=> "hello"
    "hello\r\n".chomp            #=> "hello"
    "hello\n\r".chomp            #=> "hello\n"
    "hello".chomp("llo")         #=> "he"

    # Using '.chomp!' will returns nil if no changes are made. Use with caution.
    "hello".chomp!               #=> nil
    ```

  * __[.chop](http://ruby-doc.org/core-2.5.1/String.html#method-i-chop)__
    ```
    # Returns a new String with the last character removed. If the string ends with \r\n, both characters are removed.
    # Applying .chop to an empty string returns an empty string.
    "hello\r\n".chop   #=> "hello"
    "hello\n\r".chop   #=> "hello\n"
    "hello\n".chop     #=> "hello"
    "hello".chop       #=> "hell"
    "x".chop           #=> ""
    ```

  * __[.chars](http://ruby-doc.org/core-2.5.1/String.html#method-i-capitalize)__
    ```
    # Returns an array of characters in str. This is a shorthand for `str.each_char.to_a`.
    "hello".chars    #=> ["h", "e", "l", "l", "o"]
    "HELLO".chars    #=> ["H", "E", "L", "L", "O"]
    "123ABC".chars   #=> ["1", "2", "3", "A", "B", "C"]
    ```

  * __[.chars](http://ruby-doc.org/core-2.5.1/String.html#method-i-capitalize)__
    ```
    # Returns an array of characters in str. This is a shorthand for `str.each_char.to_a`.
    "hello".chars    #=> ["h", "e", "l", "l", "o"]
    "HELLO".chars    #=> ["H", "E", "L", "L", "O"]
    "123ABC".chars   #=> ["1", "2", "3", "A", "B", "C"]
    ```

#### Array Enumerable Examples
  * [Ruby-Docs: Array Enumerables](http://ruby-doc.org/core-2.5.1/Array.html)

#### Math Enumerable Examples
  * [Ruby-Docs: Math Enumerables](http://ruby-doc.org/core-2.5.1/Math.html)

## Enumerable Worksheet 01:
