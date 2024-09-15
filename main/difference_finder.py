import difflib
import os


def find_differences(file1, file2):
    """
    Compares two text files and returns a list of differences using the unified diff format.
    Args:
        file1 (str): Path to the first file to be compared.
        file2 (str): Path to the second file to be compared.
    Returns:
        list: A list containing the lines of differences between the two files.
    """
    # Open both files and read their contents line by line
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Use difflib to compare the two files and get the differences
        diff = difflib.unified_diff(
            f1.readlines(),  # Lines from the first file
            f2.readlines(),  # Lines from the second file
            fromfile=file1,  # Name of the first file in the diff output
            tofile=file2  # Name of the second file in the diff output
        )
        # Return the differences as a list
        return list(diff)


def write_differences_to_file(differences, output_file):
    """
    Writes the differences to a specified output file, with each difference on a new line.
    Args:
        differences (list): A list of differences to write to the file.
        output_file (str): Path to the output file where differences will be saved.
    """
    # Open the output file in write mode
    with open(output_file, 'w') as f:
        # Write each difference line to the output file
        for diff in differences:
            f.write(diff)
            f.write('\n')  # Add a newline after each diff for better formatting


def check_file_existence(file1, file2):
    """
    Checks if both files exist before performing the comparison.
    Args:
        file1 (str): Path to the first file.
        file2 (str): Path to the second file.
    Returns:
        bool: True if both files exist, False otherwise.
    """
    if not os.path.exists(file1):
        print(f"Error: {file1} does not exist.")
        return False
    if not os.path.exists(file2):
        print(f"Error: {file2} does not exist.")
        return False
    return True


def main():
    # Main function to compare two files, find their differences, and write the differences to an output file.

    # Paths to the files to be compared
    file1 = "E:\\h1\\zonetool\\mod\\xmodel\\body_arab_desert_assault_mp_camo.xmb"
    file2 = "E:\\h1\\dump\\ood\\xmodel\\body_arab_desert_assault_mp_camo.xmb"

    # Path to the output file where differences will be saved
    output_file = 'output.txt'

    # Check if both files exist before proceeding
    if not check_file_existence(file1, file2):
        return  # Exit if one or both files do not exist

    # Find the differences between the two files
    differences = find_differences(file1, file2)

    # Check if there are any differences to write
    if differences:
        # Write the differences to the output file
        write_differences_to_file(differences, output_file)
        print(f"Differences written to {output_file}")
    else:
        # If no differences were found, notify the user
        print("No differences found.")


# Entry point of the script
if __name__ == "__main__":
    main()
