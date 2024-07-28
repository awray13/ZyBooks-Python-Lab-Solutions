"""
It is important to ensure that user input is valid before acceptance to verify that the data received is of the expected data type.

Using the provided template code, validate that the zip code input by the user is an integer data type.

"""
#check if the zipcode input is numeric

if __name__ == '__main__': 
        
    zipCode = input()
    try:
        # check if zip code is an integer value
        int(zipCode)
        print(f'Your zip code is {zipCode}.')
        

    except:
        print('Please use numeric digits for the zip code.')