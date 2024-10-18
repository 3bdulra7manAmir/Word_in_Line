import os


def remove_lines_without_words(file_path, words, output_file):
    """
    Removes all lines from a file that do not contain any of the given words.

    Args:
        file_path (str): The path to the file to be searched.
        words (list): A list of words to search for.
        output_file (str): The path to the output file.

    Returns:
        None.
    """
    try:
        # Read lines from the input file
        with open(file_path, "r") as f:
            lines = f.readlines()

        # Filter lines that contain any of the specified words
        new_lines = [line for line in lines if any(word in line for word in words)]

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_file)
        os.makedirs(output_dir, exist_ok=True)

        # Write the filtered lines to the output file
        with open(output_file, "w") as f:
            f.writelines(new_lines)

        print(f"Filtered lines written to {output_file}.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # Prompt the user for the input file path
    file_path = input("Enter the path to the input file: ").strip()

    # Define the words to search for
    words = ["xmodel,"]

    # Construct the output file path in the same directory as the input file
    output_file = os.path.join(os.path.dirname(file_path), "new_file2.txt")

    remove_lines_without_words(file_path, words, output_file)


if __name__ == "__main__":
    main()
