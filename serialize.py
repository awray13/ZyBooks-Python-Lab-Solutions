import pickle

def serialize(data):

  # Use dumps to convert the object to a serialized string
  return pickle.dumps(data)