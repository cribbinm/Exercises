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

In checkpostcode.py, there is a class which creates a postcode object. There is then a method in this class called 'validator, which checks the validity of a postcode.

There is a separate RegEx pattern of each of the six allowed postcode formats, namely:
* AA9A 9AA
* A9A 9AA
* A9 9AA
* A99 9AA
* AA9 9AA
* AA99 9AA
 where **A** signifies a letter and **9** a digit.

These RegEx patterns were written according to the following rules:
* As all formats end with 9AA, the first part of a postcode can easily be extracted by ignoring the last three characters
* Areas with only single-digit districts: BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE (although WC is always subdivided by a further letter, e.g. WC1A).
* Areas with only double-digit districts: AB, LL, SO.
* Areas with a district '0' (zero): BL, BS, CM, CR, FY, HA, PR, SL, SS (BS is the only area to have both a district 0 and a district 10).
* The following central London single-digit districts have been further divided by inserting a letter after the digit and before the space: EC1–EC4 (but not EC50), SW1, W1, WC1, WC2, and part of E1 (E1W), N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P).
* The letters QVX are not used in the first position.
* The letters IJZ are not used in the second position.
* The only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A.
* The only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A.
* The final two letters do not use the letters CIKMOV, so as not to resemble digits or each other when hand-written.
* Post code sectors are one of ten digits: 0 to 9 with 0 only used once 9 has been used in a post town


The validator can be used with

```
from postcoder import UK

UK('CO4 3SQ').validator()
```

The tests for this code are in tests/test_postcoder.py. The tests can be run using `py.test` as mentioned above.

