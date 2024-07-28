"""
To protect against remote code execution, it is important to validate incoming data for deserialization . One way to ensure the integrity of incoming data is to validate it using generated digest keys.

Using the provided template code, complete the function to validate incoming serialized data. For the purpose of this lab, you have access to the generate_key() and deserialize() functions.

Your function should return the result of deserialize() if it passes validation, otherwise it should raise an Exception

"""
from generate_key import generate_key
from deserialize import deserialize 
from serialize import serialize

def safe_deserialize(key, serialized_data):

    new_key = generate_key(serialized_data) # replace the empty string with a newly generated key
    
    try:
        if key == new_key:
            return deserialize(serialized_data) # return deserialized data when validation passes
        else:
            raise Exception('New key does not match old key')
    except Exception as error:
        print('Error:', error)
        
    return False

# Example usage

grades = {'Alice': 89, 'Bob': 72, 'Charles': 87}
serialized_data = serialize(grades)
deserialized_data = safe_deserialize(generate_key(serialized_data), serialized_data)
