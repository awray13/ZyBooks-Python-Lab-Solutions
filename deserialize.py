import pickle

def deserialize(serialized_data):

  # Use dumps to convert the object to a serialized string
  return pickle.loads(serialized_data)