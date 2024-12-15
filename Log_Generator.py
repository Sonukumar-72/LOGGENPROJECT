import random
import string
import time
import logging

# Setting up logging for error handling
logging.basicConfig(filename="log_generator_errors.log", level=logging.ERROR)

# List the level of logs
LOG_LEVELS = ["INFO", "DEBUG", "ERROR", "WARNING"]

# List of possible actions
ACTIONS = ["Login", "Logout", "Data Request", "File Upload", "Download", "Error"]

# Function to generate a random string for logs
def generate_random_string(length=10):
    """
    Generates a random string of given length (default length is 10 characters).
    """
    try:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    except Exception as e:
        logging.error(f"Error in generate_random_string: {e}")
        return "ERROR"

# Function to generate a random log entry
def generate_log_entry():
    """
    Generates a random log entry with a timestamp, log level, action, and user.
    """
    try:
        log_level = random.choice(LOG_LEVELS)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        action = random.choice(ACTIONS)
        user = generate_random_string(8)
        log_entry = f"{timestamp} - {log_level} - {action} - User: {user}"
        return log_entry
    except Exception as e:
        logging.error(f"Error in generate_log_entry: {e}")
        return "Error"

# Function to write logs to a file
def write_logs_to_file(log_filename, num_entries=100):
    """
    Writes a specified number of random logs to the given file.
    """
    try:
        with open(log_filename, 'w') as file:
            for _ in range(num_entries):
                log = generate_log_entry()
                if log != "Error":
                    file.write(log + '\n')
        print(f"Logs have been successfully written to {log_filename}")
    except Exception as e:
        logging.error(f"Error in write_logs_to_file: {e}")
        print("An error occurred while writing logs to the file.")

# Generate and write 200 random entries
if __name__ == "__main__":
    write_logs_to_file('generated_logs.txt', num_entries=200)  # Change the number of entries if required
