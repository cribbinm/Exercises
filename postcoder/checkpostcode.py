# checkpostcode.py

import re

class UK(object):
    """Creates a postcode object. Information can then be drawn from this object, namely the 
    validity of the postcode in our case. The choice to use a class here was optional, but as
    it would be possible to use an external library such as 'postcodes' or 'postcodeinfo',
    to add more information to a postcode object, I decided to go for it.
    All methods take the argument self.postcode (string)
    """

    def __init__(self,postcode):
        # Remove whitespace from beginning and end of input
        self.postcode = postcode.strip() 

        # The outward code patterns for the six different postcode forms are given below
        self.AA9A_PATTERN = r'^(^(WC[12]|EC[1-4]|SW1)[ABEHMNPRVWXY]$|SE1P|NW1W)$'
        self.A9A_PATTERN = r'^(E1W|N1[CP]|W1[ABCDEFGHJKPSTUW])$' 
        self.A9_PATTERN = r'^([BEGLMNSW][1-9])$'
        self.A99_PATTERN = r'^([BEGLMNSW][1-9]\d)$'
        self.AA9_PATTERN = r'^(((?!AB|LL|SO)[A-PR-UWYZ][A-HK-Y][1-9])|((BL|BS|CM|CR|FY|HA|PR|SL|SS)\d))$'
        self.AA99_PATTERN  = r'^(((?!BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[A-PR-UWYZ][A-HK-Y][1-9]\d))$'

        # Space between inward and outward code is read as part of inward code
        self.INCODE_PATTERN = r'^ \d[A-BD-HJLNPQ-UW-Z]{2}$'

    # Check validity of outward code
    def outcode_validator(self):
        # The inward code is always three digits, so we can obtain the outward code by removing the last three digits and the space
        outcode = self.postcode[:-4]

        # Combining the different outcode patterns with an 'OR' operator
        OUTCODE_PATTERN = '|'.join((self.AA9A_PATTERN,self.A9A_PATTERN,self.A9_PATTERN,self.A99_PATTERN,self.AA9_PATTERN,self.AA99_PATTERN))
        OUTCODE_REGEX = re.compile(OUTCODE_PATTERN)
        if OUTCODE_REGEX.match(outcode) != None:
            return True
        else:
            print('Outward code is incorrect')
            return False

    # Check validity of inward code
    def incode_validator(self):
        # The inward code will always be the last 3 digits  of the postcode. We include the space as part of the inward code so that a code without a space will not return True
        incode = self.postcode[-4:]
        INCODE_REGEX = re.compile(self.INCODE_PATTERN)
        if  incode[0] != ' ':
            print('There is no space separating the inward and outward code')
            return False
        elif INCODE_REGEX.match(incode) != None:
            return True
        else:
            print('Inward code is incorrect')
            return False

    # Check validity of entire postcode
    def validator(self):
        """
        If postcode is valid, this will return True, otherwise False.
        """
        if len(self.postcode) > 8:
            print('Postcode is too long')
            return False
        elif len(self.postcode) < 6:
            print('Postcode is too short')
            return False
        else:
            return self.outcode_validator() & self.incode_validator()