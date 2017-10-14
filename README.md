A few exercises with tests. All written using python3.6. Dependencies can be installed with

`pip3 install -r requirements.txt`

To run tests, simply run 

`py.test`

in the root directory of the project.

ThreeFive
=========
> Write a program that prints the numbers from 1 to 100. But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. For numbers which are multiples of both three and five print “ThreeFive”.

The solution to this is found by running `python threefive/threefive.py`. The tests for this code are in tests/test_threefive.py. The tests can be run using `py.test` as mentioned above.

Postcoder
=========

> Write a library that supports validating and formatting post codes for UK. The details of which post codes are valid and which are the parts they consist of can be found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting. The API that this library provides is your choice.

In checkpostcode.py, there is a class which creates a postcode object. There is then a method in this class called 'validator, which checks the validity of a postcode using the below pattern provided by the UK government.

`^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$`
 
The validator can be used with

```
from postcoder import CheckPostcode

CheckPostcode('CO4 3SQ').validator()
```

The tests for this code are in tests/test_postcoder.py. The tests can be run using `py.test` as mentioned above.
