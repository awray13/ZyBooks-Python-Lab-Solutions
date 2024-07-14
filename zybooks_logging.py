"""Write a program to log messages at all 5 levels. The program should go on and query the log file based on the supplied logging level. The program will accept as input, 2 values; the first will be the file name for the log file and the second value will be the logging level to query. The message entries for each level should be:

DEBUG – “10:Debug test…”

INFO – “20:Program successful!”

WARNING - “30:Warning, there could be errors…”

ERROR - “40:Program encountered and error!”

CRITICAL – “50:The program has stopped working!”

For example, when the user enters:

log 30

Output should be:

Warning, there could be errors…\n
"""
import logging

def setup_logging(log_file):
    """Setup logging configuration and log messages at different levels."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(message)s\n',
        handlers=[
            logging.FileHandler(log_file, mode='w')
        ]
    )

    # Log messages at different levels
    logging.debug("10: Debug test…")
    logging.info("20: Program successful!")
    logging.warning("30: Warning, there could be errors…")
    logging.error("40: Program encountered and error!")
    logging.critical("50: The program has stopped working!")

def query_log(file_name, level_number):
    """Query the log file for messages at the specified logging level number."""
    level_prefixes = {
        '10': 'DEBUG',
        '20': 'INFO',
        '30': 'WARNING',
        '40': 'ERROR',
        '50': 'CRITICAL'
    }
    
    if level_number not in level_prefixes:
        print(f"Invalid logging level number: {level_number}")
        return
    
    level_prefix = f"{level_number}:"
    
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith(level_prefix):
                print(line[len(level_prefix):].strip(), end='\n')

def main():
    # Accept user input for the file name and logging level number on one line
    try:
        user_input = input()
        file_name, level_number = user_input.split()
        
        # Setup logging and log messages
        setup_logging(file_name)

        # Query the log file based on user input
        query_log(file_name, level_number)
    except EOFError:
        print("No input received. Please run the script again and provide input.")
    except ValueError:
        print("Invalid input format. Please provide the log file name and logging level number separated by a space.")

# Entry point for the program
if __name__ == "__main__":
    main()
