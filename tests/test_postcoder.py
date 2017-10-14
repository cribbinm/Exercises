# test_postcoder.py

"""
Tests are performed using the pytest package. To do this, run py.test 
in the root directory of the project.
"""

import pytest
from postcoder import UK

# Function to create an instance of a postcode object, and check the validator method
def check_postcodes(postcode):
    postcode_instance = UK(postcode)
    return postcode_instance.validator()

# Run tests of some postcodes. Valid postcodes for testing were found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom
def test_check_postcodes():
    # assert check_postcodes('E20 3El') == True # Olympic Velodrome
    assert check_postcodes('EH12 1HQ') == True # Royal Bank of Scotland headquarters
    assert check_postcodes('CV4 8UW') == True # University of Warwick
    assert check_postcodes('AA1 1AA') == True  # True in format
    assert check_postcodes('CO4 3SQ') == True  # University of Essex
    assert check_postcodes('SW1A 2AA') == True # 10 Downing Street
    assert check_postcodes('PA23 8PX') == True # Randomly generated postcode from https://www.doogal.co.uk/PostcodeGenerator.php
    assert check_postcodes('TF13 6DT') == True # Randomly generated postcode from https://www.doogal.co.uk/PostcodeGenerator.php
    assert check_postcodes('CA24 3HU') == True  # Randomly generated postcode from https://www.doogal.co.uk/PostcodeGenerator.php
    assert check_postcodes('CO4 3SQ') == True  # Randomly generated postcode from https://www.doogal.co.uk/PostcodeGenerator.php
    assert check_postcodes('SS9 3BX') == True # Randomly generated postcode from https://www.doogal.co.uk/PostcodeGenerator.php
    assert check_postcodes('RM3 9NS') == True # Randomly generated postcode from https://www.doogal.co.uk/PostcodeGenerator.php
    assert check_postcodes('BB94 0AA') == True # Randomly generated postcode from https://www.doogal.co.uk/PostcodeGenerator.php

    assert check_postcodes('WR16AE') == False # No space separating inward and outward code
    assert check_postcodes('AB1 1AA') == False  # AB is a double digit only district
    assert check_postcodes('SW1W 0!T') == False # Invalid character in inward code
    assert check_postcodes('W11 2X') == False  # Invalid inward code length
    assert check_postcodes('W1 A 2X') == False  # Invalid format
    assert check_postcodes('wr13 6ae') == False    # Lowercase
    assert check_postcodes('WA1A 2ABR') == False    # Too long
    assert check_postcodes('BR21 1AA') == False    # BR is a single-digit district only
    assert check_postcodes('AB2 6BS') == False    # AB is a double-digit district only
    assert check_postcodes('HP0 8YH') == False    # Areas with a district '0' (zero): BL, BS, CM, CR, FY, HA, PR, SL, SS
    assert check_postcodes('GH1W 7YY') == False    # Only zones with digit at end of outward code are: EC1–EC4 (but not EC50), SW1, W1, WC1, WC2, and part of E1 (E1W), N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P).
    assert check_postcodes('QK8 9AC') == False    # The letters QVX are not used in the first position.
    assert check_postcodes('WI9 8BA') == False    # The letters IJZ are not used in the second position.
    assert check_postcodes('A1I 8GH') == False    # The only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A.
    assert check_postcodes('AW1O 6AX') == False    # The only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A.
    assert check_postcodes('W1 2AV') == False    # The final two letters do not use the letters CIKMOV, so as not to resemble digits or each other when hand-written.
    assert check_postcodes('DS1 DBH') == False    # Post code sectors are one of ten digits: 0 to 9
