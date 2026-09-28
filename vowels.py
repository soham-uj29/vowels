ch = input("enter your character :")

if len(ch) == 1 and ch.isalpha():
    ch_lower = ch.lower()
    if ch_lower == ['a','e','i','o','u']:
        print(f"{ch_lower} is a vowel.")
    else:
        print(f"{ch_lower} is a consnent.")
else:
    print("Invalid character is taken.")