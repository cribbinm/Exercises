import pytest
from threefive import threefive


# Run tests of some numbers we know the result of
def test_replace():
    assert threefive.replace(4) == '4'
    assert threefive.replace(6) == 'Three'
    assert threefive.replace(90) == 'ThreeFive'
    assert threefive.replace(15) == 'ThreeFive'
    assert threefive.replace(91) == '91'
    assert threefive.replace(25) == 'Five'
