import csv
import re
import os

def find_words(file_name, words, output_file_name):
    """
    Searches for specific words in a CSV file and writes matching lines to an output file.
    Args:
        file_name (str): The CSV file to search through.
        words (list): A list of words to search for.
        output_file_name (str): The file where matching lines will be written.
    """
    # Ensure the output file is opened once for appending, to avoid frequent open/close operations
    try:
        with open(file_name, 'r') as f, open(output_file_name, 'a') as outfile:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                line = ','.join(row)  # Join the CSV row into a string
                if any(word in line for word in words):  # Check if any word from the list is in the line
                    outfile.write(line + '\n')
                    print(f"Matching line written: {line}")
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    except Exception as e:
        print(f"An error occurred while processing files: {e}")


def validate_output_directory(output_file_name):
    """
    Ensures the output directory exists for the output file.
    Args:
        output_file_name (str): The output file path.
    """
    output_dir = os.path.dirname(output_file_name)
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"Output directory created: {output_dir}")
        except Exception as e:
            print(f"Error creating output directory {output_dir}: {e}")


if __name__ == '__main__':
    words = ['xmodel,']
    file_name = "E:\\h1\\dump\\iw5_delta_force\\iw5_delta_force.csv"
    output_file_name = "main\\output2.txt"

    # Validate or create the output directory if needed
    validate_output_directory(output_file_name)

    # Search for words and write matching lines to the output file
    find_words(file_name, words, output_file_name)
