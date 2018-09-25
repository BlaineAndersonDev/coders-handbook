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
    # Using '.capitalize!' will return nil if no changes are made. Use with caution.
    "Hello".capitalize!   #=> nil
    ```

  * __[.chars](http://ruby-doc.org/core-2.5.1/String.html#method-i-chars)__
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
    # Using '.chomp!' will return nil if no changes are made. Use with caution.
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
    # Using '.chop!' will return nil if no changes are made (I.E. The string is empty). Use with caution.
    "".chop!          #=> nil
    ```

  * __[.concat](http://ruby-doc.org/core-2.5.1/String.html#method-i-concat)__
    ```
    # Concatenates the given object(s) to str. If an object is an Integer, it is considered a [codepoint (unicode symbols)](https://www.unicode.org/charts/) and converted to a character before concatenation.
    # UTF-8 is the default encoding implemented in Ruby since version 2.0.0. All codepoints are based off this assumption.
    a = "hello "
    a.concat("world", 33)      #=> "hello world!"
    a                          #=> "hello world!"

    b = "sn"
    b.concat("_", b, "_", b)   #=> "sn_sn_sn"

    # Side note: For a fun list of UTF-8 characters, use the following and run it :) (Based on this [post](https://stackoverflow.com/a/36375301/10090036)). Warning: This is a large list.
    [*32..65535].map do |e|
      e.chr(Encoding::UTF_8).tap do |char|
        char =~ /\p{Alnum}|\p{Punct}/ || raise
      end rescue nil # rescuing both conversion and self-raised
    end.compact
    ```

  * __[.count](http://ruby-doc.org/core-2.5.1/String.html#method-i-count)__
    ```
    # Returns the number of matching characters based on the parameter. No spaces or delimiters required.
    a = "hello world"
    a.count("o")                   #=> 2
    a.count("H")                   #=> 1
    a.count("l")                   #=> 3
    a.count("lo")                  #=> 5
    ```

  * __[.delete](http://ruby-doc.org/core-2.5.1/String.html#method-i-delete)__
    ```
    # Returns a copy of str with all characters in the intersection of its arguments deleted.
    "hello".delete("l","lo")        #=> "heo"
    "hello".delete("lo")            #=> "he"
    # Using '.delete!' will return nil if no changes are made. Use with caution.
    "hello".delete!("b")            #=> nil
    ```

  * __[.downcase](http://ruby-doc.org/core-2.5.1/String.html#method-i-downcase)__
    ```
    # Returns a copy of str with all uppercase letters replaced with their lowercase counterparts.
    "hEllO".downcase                #=> "hello"
    "Hello".downcase                #=> "hello"
    "HeLlO".downcase                #=> "hello"
    # Using '.downcase!' will return nil if no changes are made. Use with caution.
    "hello".downcase!               #=> nil
    ```

  * __[.each_char](http://ruby-doc.org/core-2.5.1/String.html#method-i-each_char)__
    ```
    # Passes each character in str to the given block, or returns an enumerator if no block is given.
    # combines the use of .split and .each .
    "hello".each_char {|c| print c, ' ' }     #=> h e l l o
    "hello world".each_char {|c| print c, ' ' }     #=> h e l l o
    ```

  * __[.empty?](http://ruby-doc.org/core-2.5.1/String.html#method-i-empty-3F)__
    ```
    # Returns true if str has a length of zero.
    "hello".empty?   #=> false
    " ".empty?       #=> false
    "".empty?        #=> true
    ```

  * __[.eql?](http://ruby-doc.org/core-2.5.1/String.html#method-i-eql-3F)__       _[Deeper Explanation](https://stackoverflow.com/a/7157051/10090036)_
    ```
    # Two strings are equal if they have the same length and content.
    # NOTE: This does not work the same on integers.
    "a".eql?("a")              #=> true
    "test".eql?("test")        #=> true
    "a".eql?("b")              #=> false
    "test".eql?("not test")    #=> false
    ```

  * __[.ENUM](http://ruby-doc.org/core-2.5.1/String.html#method-i-ENUM)__
    ```
    # ENUM_DESCRIPT
    ENUM_EXAMPLES
    ```

  * __[.ENUM](http://ruby-doc.org/core-2.5.1/String.html#method-i-ENUM)__
    ```
    # ENUM_DESCRIPT
    ENUM_EXAMPLES
    ```

  * __[.ENUM](http://ruby-doc.org/core-2.5.1/String.html#method-i-ENUM)__
    ```
    # ENUM_DESCRIPT
    ENUM_EXAMPLES
    ```

  * __[.ENUM](http://ruby-doc.org/core-2.5.1/String.html#method-i-ENUM)__
    ```
    # ENUM_DESCRIPT
    ENUM_EXAMPLES
    ```

  * __[.ENUM](http://ruby-doc.org/core-2.5.1/String.html#method-i-ENUM)__
    ```
    # ENUM_DESCRIPT
    ENUM_EXAMPLES
    ```

#### Array Enumerable Examples
  * [Ruby-Docs: Array Enumerables](http://ruby-doc.org/core-2.5.1/Array.html)

#### Math Enumerable Examples
  * [Ruby-Docs: Math Enumerables](http://ruby-doc.org/core-2.5.1/Math.html)

## Enumerable Worksheet 01:
