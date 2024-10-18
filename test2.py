import os


def delete_lines(file_name, words, output_dir):
    """
  Deletes lines from a file that contain specific words and writes those lines to an output file.

  Args:
      file_name (str): The input file to read from.
      words (list): A list of words to search for in the lines.
      output_dir (str): The directory where the output file will be saved.
  """
    try:
        # Read all lines from the input file
        with open(file_name, 'r') as f:
            lines = f.readlines()

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Write matching lines to the output file
        output_file_path = os.path.join(output_dir, 'output2.txt')
        with open(output_file_path, 'w') as outfile:
            for line in lines:
                if any(word in line for word in words):  # Check if any word from the list is in the line
                    outfile.write(line)
                    print(f"Matching line written: {line.strip()}")  # Print the line without trailing newline

    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    words = ['masada', 'cheytac', 'melee']  # Define the words to search for
    file_name = "/main/output.txt"  # Input file path
    output_dir = "/main/"  # Output directory path

    delete_lines(file_name, words, output_dir)
