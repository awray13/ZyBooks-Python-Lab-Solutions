import time
    
class Limiter:

  def __init__(self, rate, per):
    self.rate = rate
    self.per = per
    self.bucket = rate
    self.last_check = time.time()

  def limit(self, callback_fn):
      current = time.time()
      time_passed = current - self.last_check
      self.last_check = current
      
      # Finish line 18 by writing an expression that determines the value of the bucket
      # Use the following variables in your expression: time_passed, self.bucket, self.rate, and self.per 
      bucket = self.bucket + time_passed * (self.rate - self.bucket) / self.per
      
      if (bucket > self.rate):
          self.bucket = self.rate
      if (bucket < 1):
          pass
      else:
          callback_fn()
          self.bucket = bucket - 1