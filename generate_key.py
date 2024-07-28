import hashlib
import hmac

def generate_key(serialized_data):
  # Generates a hash key from the serialized data
  return hmac.new(b'shared-key', serialized_data, hashlib.sha1).hexdigest() 