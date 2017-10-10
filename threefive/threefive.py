
# Function which will replace multiples of 3 with 'Three', multiples of 5 with 'Five', and multiples of 3 and 5 with 'ThreeFive'
def replace(num):
    """
    Input: number (int)
    Output: replaced number (string)
    """
    sub = ''
    if num % 3 == 0:
        sub += 'Three'
    if num % 5 == 0:
        sub += 'Five'
    return sub or str(num)

# When this script (threefive.py) is run, the numers from 1 to 100 will be printed line by line, with multiples of three and five replaced accordingly    
if __name__ == "__main__":
    print("\n".join(replace(num) for num in range(1,101)))