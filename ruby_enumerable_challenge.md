# Ruby Enumerable Challenge
> A small Ruby Enumerable worksheet I created to test myself daily for a few weeks, until I have all the common enumerable memorized (or at least committed to memory enough that I can mostly recall how to use them properly).

## Enumerable Examples:
> I've included a full set of examples here, as well as a number of different worksheets in the [worksheets]() folder. They can also be accessed via the table below:


| Difficulty | Enumerable Type | Worksheet |
| --- | --- | --- |
| __Beginner__ | String | [string_01](https://github.com/BlaineAndersonDev/coders-handbook/blob/master/worksheets/string_01.md) |


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
    "hEllO".downcase   #=> "hello"
    "cYbEr_PuNk11".downcase   #=> "cyber_punk11"
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

  * __[.eql?](http://ruby-doc.org/core-2.5.1/String.html#method-i-eql-3F)__ [Deeper Explanation](https://stackoverflow.com/a/7157051/10090036)
    ```
    # Two strings are equal if they have the same length and content.
    # NOTE: This does not work the same on integers.
    "a".eql?("a")              #=> true
    "test".eql?("test")        #=> true
    "a".eql?("b")              #=> false
    "test".eql?("not test")    #=> false
    ```

  * __[.gsub](http://ruby-doc.org/core-2.5.1/String.html#method-i-gsub)__ [Regex Tutorial](http://www.rubyguides.com/2015/06/ruby-regex/) [Regex Editor](http://rubular.com/)
    ```
    # Returns a copy of str with all occurrences of pattern substituted for the second argument.
    # .gsub is usually used with Regex.
    "hello world".gsub("h", '')                   #=> "ello world"
    "hello".gsub(/[aeiou]/, '*')                  #=> "h*ll*"
    "hello".gsub(/([aeiou])/, '<\1>')             #=> "h<e>ll<o>"
    "hello".gsub(/./) {|s| s.ord.to_s + ' '}      #=> "104 101 108 108 111 "
    "hello".gsub(/(?<foo>[aeiou])/, '{\k<foo>}')  #=> "h{e}ll{o}"
    'hello'.gsub(/[eo]/, 'e' => 3, 'o' => '*')    #=> "h3ll*"
    # Using '.gsub!' will return nil if no substitutions are made. Use with caution.
    "hello".gsub!("b")                            #=> nil
    ```

  * __[.include?](http://ruby-doc.org/core-2.5.1/String.html#method-i-include-3F)__
    ```
    # Returns true if str contains the given string or character.
    "hello".include?("e")   #=> true
    "hello".include?("lo")   #=> true
    "hello".include?("b")   #=> false
    "hello".include?("ol")   #=> false
    ```

  * __[.index](http://ruby-doc.org/core-2.5.1/String.html#method-i-index)__
    ```
    # Returns the index of the first occurrence of the given substring or pattern (regexp) in str.
    # Returns nil if not found.
    # If the second parameter is present, it specifies the position in the string to begin the search.
    # .index can be used with Regex.
    "hello".index('e')             #=> 1
    "hello".index('lo')            #=> 3
    "hello".index('a')             #=> nil
    "hello".index(?e)              #=> 1
    "hello".index(/[aeiou]/, -3)   #=> 4
    ```

  * __[.insert](http://ruby-doc.org/core-2.5.1/String.html#method-i-insert)__
    ```
    # Inserts other_str before the character at the given index, modifying str.
    # Negative indices count from the end of the string, and insert after the given character.
    "abcd".insert(0, 'X')    #=> "Xabcd"
    "abcd".insert(3, 'X')    #=> "abcXd"
    "abcd".insert(4, 'X')    #=> "abcdX"
    "abcd".insert(-3, 'X')   #=> "abXcd"
    "abcd".insert(-1, 'X')   #=> "abcdX"
    ```

  * __[.length](http://ruby-doc.org/core-2.5.1/String.html#method-i-length)__
    ```
    # Returns the character length of str.
    "Hello".length             #=> 5
    "Hello World".length       #=> 11
    " ".length                 #=> 1
    "Hello...World!".length    #=> 14
    ```

  * __[.match](http://ruby-doc.org/core-2.5.1/String.html#method-i-match)__
    ```
    # Converts pattern to a Regexp (if it isn't already one), then invokes its match method on str.
    # If the second parameter is present, it specifies the position in the string to begin the search.
    '123hello'.match(/(hello)/) #=> "hello"
    'hello'.match('(.)\1')      #=> #<MatchData "ll" 1:"l">
    'hello'.match('(.)\1')[0]   #=> "ll"
    'hello'.match(/(.)\1/)[0]   #=> "ll"
    'hello'.match(/(.)\1/, 3)   #=> nil
    'hello'.match('xx')         #=> nil
    ```

  * __[.match?](http://ruby-doc.org/core-2.5.1/String.html#method-i-match-3F)__
    ```
    # Converts pattern to a Regexp (if it isn't already one), then returns a true or false indicates whether the regexp is matched str or not without updating $~ and other related variables.
    # If the second parameter is present, it specifies the position in the string to begin the search.
    '123hello'.match?(/(hello)/) #=> true
    "Ruby".match?(/R.../)        #=> true
    "Ruby".match?(/R.../, 1)     #=> false
    "Ruby".match?(/P.../)        #=> false
    $&                           #=> nil
    ```

  * __[.replace](http://ruby-doc.org/core-2.5.1/String.html#method-i-replace)__
    ```
    # Replaces the contents and taintedness of str with the corresponding values in other_str.
    s = "hello"         #=> "hello"
    s.replace "world"   #=> "world"
    ```

  * __[.reverse](http://ruby-doc.org/core-2.5.1/String.html#method-i-reverse)__
    ```
    # Returns a new string with the characters from str in reverse order.
    "stressed".reverse      #=> "desserts"
    "mom".reverse           #=> "mom"
    # Using '.reverse!' will overwrite the original word or variable. Use with caution.
    variable = "stressed"
    variable               #=> "stressed"
    variable.reverse!      #=> "desserts"
    variable               #=> "desserts"
    ```

  * __[.slice](http://ruby-doc.org/core-2.5.1/String.html#method-i-slice)__
    ```
    # If passed a single index, returns a substring of one character at that index.
    # If passed a start index and a length, returns a substring containing length characters starting at the start index.
    # If passed a range, its beginning and end are interpreted as offsets delimiting the substring to be returned.

    string = "this is a string"
    string.slice(0)        #=> "t"
    string.slice(4..6)     #=> " is "
    string.slice(-2)       #=> "n"
    # Using '.slice!' will overwrite the original word or variable. Use with caution.
    string.slice!(2)        #=> "i"
    string.slice!(3..6)     #=> " is "
    string.slice!(/s.*t/)   #=> "sa st"
    string.slice!("r")      #=> "r"
    string                  #=> "thing"
    ```

  * __[.split](http://ruby-doc.org/core-2.5.1/String.html#method-i-split)__
    ```
    # Divides str into substrings based on a delimiter, returning an array of these substrings.
    " now's  the time".split        #=> ["now's", "the", "time"]
    " now's  the time".split(' ')   #=> ["now's", "the", "time"]
    " now's  the time".split(/ /)   #=> ["", "now's", "", "the", "time"]
    "1, 2.34,56, 7".split(%r{,\s*}) #=> ["1", "2.34", "56", "7"]
    "hello".split(//)               #=> ["h", "e", "l", "l", "o"]
    "hello".split(//, 3)            #=> ["h", "e", "llo"]
    "hi mom".split(%r{\s*})         #=> ["h", "i", "m", "o", "m"]

    "mellow yellow".split("ello")   #=> ["m", "w y", "w"]
    "1,2,,3,4,,".split(',')         #=> ["1", "2", "", "3", "4"]
    "1,2,,3,4,,".split(',', 4)      #=> ["1", "2", "", "3,4,,"]
    "1,2,,3,4,,".split(',', -4)     #=> ["1", "2", "", "3", "4", "", ""]

    "1:2:3".split(/(:)()()/, 2)     #=> ["1", ":", "", "", "2:3"]

    "".split(',', -1)               #=> []
    ```

  * __[.strip](http://ruby-doc.org/core-2.5.1/String.html#method-i-strip)__
    ```
    # Returns a copy of str with leading and trailing whitespace removed.
    # Whitespace is defined as any of the following characters: null, horizontal tab, line feed, vertical tab, form feed, carriage return, space.
    "    hello    ".strip         #=> "hello"
    "\tgoodbye\r\n".strip         #=> "goodbye"
    "\x00\t\n\v\f\r ".strip       #=> ""
    # Using '.strip!' will return nil if no changes are made. Use with caution.
    "hello".strip!                #=> nil
    ```

  * __[.swapcase](http://ruby-doc.org/core-2.5.1/String.html#method-i-swapcase)__
    ```
    # Returns a copy of str with uppercase alphabetic characters converted to lowercase and lowercase characters converted to uppercase.
    "Hello".swapcase          #=> "hELLO"
    "cYbEr_PuNk11".swapcase   #=> "CyBeR_pUnK11"
    # Using '.swapcase!' will return nil if no changes are made. Use with caution.
    "hello".swapcase!               #=> nil
    ```

  * __[.upcase](http://ruby-doc.org/core-2.5.1/String.html#method-i-upcase)__
    ```
    # Returns a copy of str with all lowercase letters replaced with their uppercase counterparts.
    "hEllO".upcase   #=> "HELLO"
    "cYbEr_PuNk11".upcase   #=> "CYBER_PUNK11"
    # Using '.upcase!' will return nil if no changes are made. Use with caution.
    "hello".upcase!               #=> nil
    ```

  * __[.to_i](http://ruby-doc.org/core-2.5.1/String.html#method-i-to_i)__
    ```
    # Returns the result of interpreting leading characters in str as an integer.
    # If there is not a valid number at the start of str, 0 is returned.
    "12345".to_i             #=> 12345
    "99 red balloons".to_i   #=> 99
    "0a".to_i                #=> 0
    "0a".to_i(16)            #=> 10
    "hello".to_i             #=> 0
    "1100101".to_i(2)        #=> 101
    "1100101".to_i(8)        #=> 294977
    "1100101".to_i(10)       #=> 1100101
    "1100101".to_i(16)       #=> 17826049
    ```

#### Array Enumerable Examples
  * [Ruby-Docs: Array Enumerables](http://ruby-doc.org/core-2.5.1/Array.html)

  * __[.ENUM](http://ruby-doc.org/core-2.5.1/String.html#method-i-ENUM)__
    ```
    # ENUM_DESCRIPT
    ENUM_EXAMPLES
    ```

#### Math Enumerable Examples
  * [Ruby-Docs: Math Enumerables](http://ruby-doc.org/core-2.5.1/Math.html)

  * __[.ENUM](http://ruby-doc.org/core-2.5.1/String.html#method-i-ENUM)__
    ```
    # ENUM_DESCRIPT
    ENUM_EXAMPLES
    ```

## Enumerable Worksheet string_01:
