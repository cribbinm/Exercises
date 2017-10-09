"""
Tests are performed using the pytest package. To do this, run py.test 
in the root directory of the project.
"""

import pytest
from postcoder import CheckPostcode

# Function to create an instance of a postcode object, and check the validator method
def check_postcodes(postcode):
	postcode_instance = CheckPostcode(postcode)
	return postcode_instance.validator()

# Run tests of some postcodes. Valid postcodes for testing were found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom
def test_check_postcodes():
	assert check_postcodes('e20 3el') == True # Olympic Velodrome
	assert check_postcodes('EH12 1HQ') == True # Royal Bank of Scotland headquarters
	assert check_postcodes('CV4 8UW') == True # University of Warwick
	assert check_postcodes('AA1 1AA') == True  # True in format
	assert check_postcodes('CO4 3SQ') == True  # University of Essex
	assert check_postcodes('SW1A 2AA') == True # 10 Downing Street
	assert check_postcodes('SW1W 0!T') == False # Invalid
	assert check_postcodes('W11 2X') == False  # Invalid
	assert check_postcodes('W1 A 2X') == False  # Invalid