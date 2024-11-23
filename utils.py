import datetime

LOG_FILE = "logs.txt"

def log_event(event_message):
    """
    Logs an event with a timestamp to the log file.

    Args:
        event_message (str): The message to be logged.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {event_message}"
    print(log_message)  # Also print the log to the console
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_message + "\n")
