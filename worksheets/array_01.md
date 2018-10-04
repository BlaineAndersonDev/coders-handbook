# Worksheet Array 01
###### Ruby Enumerable Challenge:
> This is one of a number of worksheets created by [Blaine Anderson](https://github.com/BlaineAndersonDev) to upkeep his enumerable skills. For a full list of Common Enumerables, Examples & other Worksheets click [here](https://github.com/BlaineAndersonDev/coders-handbook/blob/master/ruby_enumerable_challenge.md).

> There is an answer-free section of this worksheet intended for Copy Pasting it into your local machine, or using [Repl.it](Repl.it) to work through it entirely.

> This worksheet is ordered exactly as the [Enumerable Notes](https://github.com/BlaineAndersonDev/coders-handbook/blob/master/ruby_enumerable_challenge.md) section is and can be solved by walking through it hand in hand with the notes.

> This worksheet is leveled: __Beginner__.

___

## Github Worksheet with Answers:

1.) Use an Enumerable to check if a number is in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `true`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr.any?(Integer)    #=> true

  </p></details>

  ___

2.) Use an Enumerable to return the letter "c" using an index location in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `"c"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr.at(2)    #=> "c"

  </p></details>

  ___

3.) Use an Enumerable to remove all elements in in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `[]`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr.clear    #=> []

  </p></details>

  ___

4.) Use an Enumerable to add a "?" to all elements in the array below:

   `arr = ["a", "b", "c"]`
   > Goal: `["a?", "b?", "c?"]`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr.collect { |element| element + "?" }    #=> ["a?", "b?", "c?"]

  </p></details>

  ___

5.) Use an Enumerable to combine the arrays below:

   `arr_1 = ["a", "b", "c", 25]`
   `arr_2 = ["d", "e", "f", 50]`
   > Goal: `["a", "b", "c", 25, "d", "e", "f", 50]`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr_1.concat(arr_2)    #=> ["a", "b", "c", 25, "d", "e", "f", 50]

  </p></details>

  ___

6.) Use an Enumerable to find the number of elements in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `4`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr.count    #=> 4

  </p></details>

  ___

7.) Use an Enumerable to remove all "b"'s in the array below:

   `arr = ["a", "b", "c", "b", "b", 25, "b"]`
   > Goal: `["a", "c", 25]`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr.delete("b")    #=> ["a", "c", 25]

  </p></details>

  ___

8.) Use an Enumerable to remove the element "c" using it's index location in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `["a", "b", 25]`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr.delete_at(2)    #=> ["a", "b", 25]

  </p></details>

  ___

9.) Use an Enumerable to remove all integers above 10 in the array below:

   `arr = [1, 2, 5, 7, 9, 10, 15, 18, 23, 25, 30, 100]`
   > Goal: `[1, 2, 5, 7, 9, 10]`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr.delete_if { |int| int > 10 }    #=> [1, 2, 5, 7, 9, 10]

  </p></details>

  ___

10.) Use an Enumerable to remove the first element in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `["b", "c", 25]`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr.drop    #=> ["b", "c", 25]

  </p></details>

  ___

11.) Use an Enumerable to print a "-" between every element in the array below:

   `arr = ["a", "b", "c"]`
   > Goal: `a-b-c-`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr._____ { || print }   #=> a-b-c-

  </p></details>

  ___

12.) Use an Enumerable to return false by finding if the array below has elements:

   `arr = []`
   > Goal: `true`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr..empty?    #=> true

  </p></details>

  ___

13.) Use an Enumerable to return the element at index position `1` in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `"b"`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr.fetch(1)    #=> "b"

  </p></details>

  ___

14.) Use an Enumerable to return the index of the element "c" in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `2`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr.index("c")    #=> 2

  </p></details>

  ___

______.) Use an Enumerable to _______ in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `_____`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr._____    #=> _____

  </p></details>

  ___

______.) Use an Enumerable to _______ in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `_____`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr._____    #=> _____

  </p></details>

  ___

______.) Use an Enumerable to _______ in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `_____`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr._____    #=> _____

  </p></details>

  ___

______.) Use an Enumerable to _______ in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `_____`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr._____    #=> _____

  </p></details>

  ___

______.) Use an Enumerable to _______ in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `_____`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr._____    #=> _____

  </p></details>

  ___

______.) Use an Enumerable to _______ in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `_____`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr._____    #=> _____

  </p></details>

  ___

______.) Use an Enumerable to _______ in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `_____`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr._____    #=> _____

  </p></details>

  ___

______.) Use an Enumerable to _______ in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `_____`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr._____    #=> _____

  </p></details>

  ___

______.) Use an Enumerable to _______ in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `_____`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr._____    #=> _____

  </p></details>

  ___

______.) Use an Enumerable to _______ in the array below:

   `arr = ["a", "b", "c", 25]`
   > Goal: `_____`

  <details><summary>Answer:</summary><p><!-- Spacing Required -->

    arr._____    #=> _____

  </p></details>

  ___

## Local/[Repl.it](Repl.it) Answer Free Worksheet:

  ```
  # 1.) Use an Enumerable to check if a number is in the array below:
    arr = ["a", "b", "c", 25]
    arr._____  #=> true

  # 2.) Use an Enumerable to return the letter "c" using an index location in the array below:
    arr = ["a", "b", "c", 25]
    arr._____  #=> "c"

  # 3.) Use an Enumerable to remove all elements in in the array below:
    arr = ["a", "b", "c", 25]
    arr._____  #=> []

  # 4.) Use an Enumerable to add a "?" to all elements in the array below (Includes a block argument):
    arr = ["a", "b", "c", 25]
    arr._____ { || }  #=> ["a?", "b?", "c?"]

  # 5.) Use an Enumerable to combine the arrays below:

    arr_1 = ["a", "b", "c", 25]     
    arr_2 = ["d", "e", "f", 50]     
    arr_1._____  #=> ["a", "b", "c", 25, "d", "e", "f", 50]

  # 6.) Use an Enumerable to find the number of elements in the array below:
    arr = ["a", "b", "c", 25]
    arr._____  #=> 4

  # 7.) Use an Enumerable to remove all "b"'s in the array below:
    arr = ["a", "b", "c", "b", "b", 25, "b"]
    arr._____  #=> ["a", "c", 25]

  # 8.) Use an Enumerable to remove the element "c" using it's index location in the array below:
    arr = ["a", "b", "c", 25]
    arr._____  #=> ["a", "b", 25]

  # 9.) Use an Enumerable to remove all integers above 10 in the array below (Requires a block argument):
    arr = [1, 2, 5, 7, 9, 10, 15, 18, 23, 25, 30, 100]
    arr._____  #=> [1, 2, 5, 7, 9, 10]

  # 10.) Use an Enumerable to remove the first element in the array below:
    arr = ["a", "b", "c", 25]
    arr._____  #=> ["b", "c", 25]

  # 11.) Use an Enumerable to print a "-" between every element in the array below (Requires a block argument using print):
    arr = ["a", "b", "c"]
    arr._____  #=> a-b-c-

  # 12.) Use an Enumerable to return false by finding if the array below has elements:
    arr = []
    arr._____  #=> true

  # 13.) Use an Enumerable to return the element at index position 1 in the array below:
    arr = ["a", "b", "c", 25]
    arr._____  #=> "b"

  # 14.) Use an Enumerable to return the index of the element "c" in the array below:
    arr = ["a", "b", "c", 25]
    arr._____  #=> 2

  # _______.) Question
    arr = ["a", "b", "c", 25]
    arr._____  #=> ____

  # _______.) Question
    arr = ["a", "b", "c", 25]
    arr._____  #=> ____

  # _______.) Question
    arr = ["a", "b", "c", 25]
    arr._____  #=> ____

  # _______.) Question
    arr = ["a", "b", "c", 25]
    arr._____  #=> ____

  # _______.) Question
    arr = ["a", "b", "c", 25]
    arr._____  #=> ____

  # _______.) Question
    arr = ["a", "b", "c", 25]
    arr._____  #=> ____

  # _______.) Question
    arr = ["a", "b", "c", 25]
    arr._____  #=> ____


  ```
