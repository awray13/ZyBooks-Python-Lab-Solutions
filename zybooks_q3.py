import logging
import sys

import logging
import sys

#log division by zero error to the log, the output is printed to the screen 
def divideByZeroError(dividend, divisor):

    logging.basicConfig(stream=sys.stdout,format='%(levelname)s:%(message)s')
    
    try:

       quotient = dividend/divisor  
       print (quotient)
        
    except Exception as e:

        #logging error here, use str(e) as part of the output
        logging.error(f" The exception that occurred is: {str(e)}")

if __name__ == '__main__': 

    dividend = int(input())
    divisor = int(input())
    
    divideByZeroError(dividend,divisor)