from datetime import datetime
import time
import subprocess as sp
import keyboard

def open_file_with_program(program_path, file_name):
    """
    Opens a file with a specified program.
    Args:
        program_path (str): Path to the program executable.
        file_name (str): Name of the file to be opened.
    """
    try:
        sp.Popen([program_path, file_name])
    except Exception as e:
        print(f"Error opening {file_name} with {program_path}: {e}")

def wait_for_user_input(prompt_message="Press Enter when You are done!"):
    """
    Waits for the user to press the Enter key.
    Args:
        prompt_message (str): The message displayed while waiting for user input.
    """
    print(prompt_message)
    while True:
        if keyboard.is_pressed("Enter"):
            break

def process_file(incoming_file, outgoing_file, keyword):
    """
    Processes the incoming file and writes lines starting with a specific keyword to the outgoing file.
    Args:
        incoming_file (str): Path to the file to be read.
        outgoing_file (str): Path to the file where matching lines will be written.
        keyword (str): The keyword to match lines that will be written to the outgoing file.
    """
    try:
        with open(incoming_file, 'r') as file1:
            with open(outgoing_file, 'a') as file2:
                for line in file1:
                    if line.startswith(keyword):
                        file2.write(line)
                        print(line)
    except Exception as e:
        print(f"Error processing files: {e}")

def main():
    program_path = "C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe"
    incoming_file = "Incoming.txt"
    outgoing_file = "Outcoming.txt"
    keyword = "[ WARNING ]"

    # Open Incoming.txt with VS Code
    open_file_with_program(program_path, incoming_file)

    # Wait for user to press Enter after pasting lines
    wait_for_user_input("Press Enter when you are done pasting the lines!")

    # Process the file and extract lines starting with the keyword
    process_file(incoming_file, outgoing_file, keyword)

    # Open Outcoming.txt with VS Code to display the results
    open_file_with_program(program_path, outgoing_file)

    # Print completion message with timestamp
    current_date_time = datetime.now()
    print(f"Finished at {current_date_time}")
    time.sleep(3)

if __name__ == "__main__":
    main()
