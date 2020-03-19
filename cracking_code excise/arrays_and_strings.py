'''
determine if a string has all unique characters, using only arrays and stringbuilders
'''
# dict itself is hash

def contains_no_duplicates(string):
    letters = {}
    for letter in string:
        if letter in letters:
            return False
        letters[letter] = True
        # key is letter, value is boolean
    return True


if __name__ == "__main__":
    import sys
    print(contains_no_duplicates('jkasdiure'))
