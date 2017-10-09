import re

class CheckPostcode(object):
    """Creates a postcode object. Information can then be drawn from this object, namely the 
    validity of the postcode in our case. The choice to use a class here was optional, but as
    it would be possible to use an external library such as 'postcodes' or 'postcodeinfo',
    to add more information to a postcode object, I decided to go for it."""

    def __init__(self,postcode):
        # The following RegEx pattern is provided by the UK Government and was taken from
        # https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
        # Note that the guidelines do note state that postcodes are case sensitive, and the RegEx will accept lower case letters as valid.
        self.postcode = postcode
        self.pattern = '^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|' + \
        '(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|' + \
        '([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$' 

    def validator(self):
        """
        Check if a postcode is valid
        Key arguments:
        self.postcode -- postcode from postcode object (string)
        If postcode is valid, this will return True, otherwise False.
        """
        POSTCODE_REGEX = re.compile(self.pattern)
        postcode = self.postcode.strip()# Remove whitespace character from beginning and end.
        return POSTCODE_REGEX.match(postcode) != None

    # def formatter(self):

