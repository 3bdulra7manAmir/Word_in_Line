import os
import re

def remove_lines_without_words(file_path, words, output_file):
  """
  Removes all lines from a file that do not contain any of the given words.

  Args:
    file_path: The path to the file to be searched.
    words: A list of words to search for.
    output_file: The path to the output file.

  Returns:
    None.
  """

  with open(file_path, "r") as f:
    lines = f.readlines()

  new_lines = []
  for line in lines:
    for word in words:
      if word in line:
        new_lines.append(line)
        break

  with open(output_file, "w") as f:
    f.writelines(new_lines)

def main():
  file_path = "/main\\iw5_delta_force.txt"
  words = ["xmodel,"]
  output_file = "/main\\new_file2.txt"

  remove_lines_without_words(file_path, words, output_file)

if __name__ == "__main__":
  main()
