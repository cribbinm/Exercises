# Function which will replace 
def replace(num):
    sub = ''
    if num % 3 == 0:
        sub += 'Three'
    if num % 5 == 0:
        sub += 'Five'
    return sub or str(num)

# When this script (threefive.py) is run, the numers from 1 to 100 will be printed line by line, with multiples of three and five replaced accordingly    
if __name__ == "__main__":
    print("\n".join(replace(num) for num in range(1,101)))