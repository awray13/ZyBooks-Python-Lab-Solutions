"""
You are being asked to check that the user input is valid before accepting it. As part of this process, you will validate that the data received is of the expected length.

Using the provided template code, validate that the length of a password meets length requirements. Create a conditional statement that checks if the length of a password input is greater than or equal to 8 characters. Output the correct statement depending on the length of the user's password.

"""

# check if the length of the password is at least 8 characters

if __name__ == '__main__': 
        
    password = input()
    
    # write an if / else statement to evaluate passwords length
    if len(password) >= 8:
        print("Password meets length requirements")
    else:
        print("Password does not meet length requirements")