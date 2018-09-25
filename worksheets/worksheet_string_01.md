# worksheet_string_01
###### Ruby Enumerable Challenge Worksheet
> This is one of a number of worksheets created by [Blaine Anderson](https://github.com/BlaineAndersonDev) to upkeep his enumerable skills. For a full list of Common Enumerables, Examples & other Worksheets click [here](https://github.com/BlaineAndersonDev/coders-handbook/blob/master/ruby_enumerable_challenge.md).

> There is an answer-free section of this worksheet intended for Copy Pasting it into your local machine, or using [Repl.it](Repl.it) to work through it entirely.

> This worksheet is ordered exactly as the [Enumerable Notes](https://github.com/BlaineAndersonDev/coders-handbook/blob/master/ruby_enumerable_challenge.md) section is and can be solved by walking through it hand in hand with the notes.

> This worksheet is leveled: __Beginner__.

___

## Github Worksheet with Answers:

1.) Use an Enumerable to Capitalize the sentence below:

   `"hello world"`
   > Goal: `"Hello"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello".capitalize    #=> "Hello"

  </p></details>

___

2.) Use an Enumerable to divide the sentence below into an array of characters:

   `"hello world"`
   > Goal: `["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello".chars    #=> ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]

  </p></details>

___

3.) Use an Enumerable to remove part of the sentence below:

   `"hello world"`
   > Goal: `"hello "`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello world".chomp("world")    #=> "hello "

  </p></details>

___

4.) Use an Enumerable to remove only the last letter the sentence below:

   `"hello world"`
   > Goal: `"hello worl"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello world".chop    #=> "hello worl"

  </p></details>

___

5.) Use an Enumerable to add "world" to the sentence below:

   `"hello "`
   > Goal: `"hello world"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello ".concat("world")    #=> "hello world"

  </p></details>

___

6.) Use an Enumerable to find the exact number of "o"'s the sentence below:

   `"hello world"`
   > Goal: `2`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello world".count    #=> 2

  </p></details>

___

7.) Use an Enumerable to remove the three two "l"'s from the sentence below:

   `"hello"`
   > Goal: `"heo"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello".delete("l")    #=> "heo"

  </p></details>

___

8.) Use an Enumerable to make all letters in the sentence below lowercase:

   `"HeLlO wOrLd"`
   > Goal: `"hello world"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "HeLlO wOrLd".downcase    #=> "hello world"

  </p></details>

___

9.) Use an Enumerable to 'print' every character the sentence below:

   `"hello"`
   > Goal: `h e l l o`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello".each_char {|char| print char, ' ' }    #=> h e l l o

  </p></details>

___

10.) Use an Enumerable to check if the sentence below is empty:

   `"hello"`
   > Goal: `false`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello".empty?    #=> false

  </p></details>

___

11.) Use an Enumerable to see if the sentence below is equal to "hello world":

   `"hello world"`
   > Goal: `true`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello world".eql?("hello world")    #=> true

  </p></details>

___

12.) Use an Enumerable to remove the "h" from the sentence below and replace it with nothing:

   `"hello world"`
   > Goal: `"ello world"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello world".gsub("h", '')    #=> "ello world"

  </p></details>

___

13.) Use an Enumerable to see if the sentence below includes the letter "b":

   `"hello world"`
   > Goal: `false`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello world".include?("b")    #=> false

  </p></details>

___

14.) Use an Enumerable to find the letter index number of the letter "e" in the sentence below:

   `"hello world"`
   > Goal: `1`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello".index("e")    #=> 1

  </p></details>

___

15.) Use an Enumerable to add the letter "X" in front of the sentence below:

   `"hello"`
   > Goal: `"Xhello"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello".insert(0, "X")    #=> "Xhello"

  </p></details>

___

16.) Use an Enumerable to find how many characters are in the sentence below:

   `"hello world"`
   > Goal: `11`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello world".length    #=> 11

  </p></details>

___

17.) Use an Enumerable & Regex to select only the letters in the sentence below. The regex is provided (/(hello)/):

   `"hello"`
   > Goal: `"hello"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "123hello".match(/(hello)/) #=> "hello"

  </p></details>

___

18.) Use an Enumerable & Regex to check if the provided regex (/(hello)/) is included in the sentence below:

   `"hello world"`
   > Goal: `true`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "123hello".match?(/(hello)/)    #=> true

  </p></details>

___

19.) Use an Enumerable to reverse the sentence below:

   `"hello world"`
   > Goal: `"dlrow olleh"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello world".reverse    #=> "dlrow olleh"

  </p></details>

___

20.) Use an Enumerable to return a range of letter from the sentence below:

   `"hello world"`
   > Goal: `"ello"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello world".slice(1..4)    #=> "ello"

  </p></details>

___

21.) Use an Enumerable to divide the sentence below into an array:

   `"hello world"`
   > Goal: `"Hello"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello world".split    #=> ["hello", "world"]

  </p></details>

___

22.) Use an Enumerable to remove any whitespaces from the sentence below:

   `"       hello world       "`
   > Goal: `"hello world"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "       hello world       ".strip    #=> "hello world"

  </p></details>

___

23.) Use an Enumerable to switch the case of all the letters in the sentence below:

   `"HELLO world"`
   > Goal: `"hello WORLD"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "HELLO world".swapcase    #=> "hello WORLD"

  </p></details>

___

24.) Use an Enumerable to force all letters the sentence below to be uppercase:

   `"hello world"`
   > Goal: `"HELLO WORLD"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "hello world".upcase    #=> "HELLO WORLD"

  </p></details>

___

25.) Use an Enumerable to make the sentence below into an integer (Note that only numbers will remain, letters will be removed):

   `"123hello"`
   > Goal: `123`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    "123hello".to_i    #=> 123

  </p></details>

___

## Local/Repl.it Answer Free Worksheet:

```
# 1.) Use an Enumerable to Capitalize the sentence below:
  "hello world"._____  #=> "Hello"


# 2.) Use an Enumerable to divide the sentence below into an array of characters:
  "hello world"._____  #=> `["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]`


# 3.) Use an Enumerable to remove "world" in the sentence below:
  "hello world"._____  #=> "hello "


# 4.) Use an Enumerable to remove only the last letter the sentence below:
  "hello world"._____  #=> "hello worl"


# 5.) Use an Enumerable to add "world" to the sentence below:
  "hello "._____  #=> "hello world "


# 6.) Use an Enumerable to find the exact number of "o"'s the sentence below:
  "hello world"._____  #=> 2


# 7.) Use an Enumerable to remove the three two "l"'s from the sentence below:
  "hello"._____  #=> "heo"


# 8.) Use an Enumerable to make all letters in the sentence below lowercase:
  "HeLlO wOrLd"._____    #=> "hello world"


# 9.) Use an Enumerable to 'print' every character the sentence below:
  "hello"._____    #=> h e l l o


# 10.) Use an Enumerable to check if the sentence below is empty:
  "hello"._____    #=> false


# 11.) Use an Enumerable to see if the sentence below is equal to "hello world":
  "hello world"._____    #=> true


# 12.) Use an Enumerable to remove the "h" from the sentence below and replace it with nothing:
  "hello world"._____    #=> "ello world"


# 13.) Use an Enumerable to see if the sentence below includes the letter "b":
  "hello world"._____    #=> false


# 14.) Use an Enumerable to find the letter index number of the letter "e" in the sentence below:
  "hello"._____    #=> 1


# 15.) Use an Enumerable to add the letter "X" in front of the sentence below:
  "hello"._____    #=> "Xhello"


# 16.) Use an Enumerable to find how many characters are in the sentence below:
  "hello world"._____    #=> 11


# 17.) Use an Enumerable & Regex to select only the letters in the sentence below. The regex is provided (/(hello)/):
  "123hello"._____ #=> "hello"


# 18.) Use an Enumerable & Regex to check if the provided regex (/(hello)/) is included in the sentence below:
  "123hello"._____    #=> true


# 19.) Use an Enumerable to reverse the sentence below:
  "hello world"._____    #=> "dlrow olleh"


# 20.) Use an Enumerable to return a range of letter from the sentence below:
  "hello world"._____    #=> "ello"


# 21.) Use an Enumerable to divide the sentence below into an array:
  "hello world"._____    #=> ["hello", "world"]


# 22.) Use an Enumerable to remove any whitespaces from the sentence below:
  "       hello world       "._____    #=> "hello world"


# 23.) Use an Enumerable to switch the case of all the letters in the sentence below:
  "HELLO world"._____    #=> "hello WORLD"


# 24.) Use an Enumerable to force all letters the sentence below to be uppercase:
  "hello world"._____    #=> "HELLO WORLD"


# 25.) Use an Enumerable to make the sentence below into an integer (Note that only numbers will remain, letters will be removed):
  "123hello"._____    #=> 123


```
