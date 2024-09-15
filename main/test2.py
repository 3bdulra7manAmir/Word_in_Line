import re
import os

def delete_lines(file_name, words, output_dir):
  with open(file_name, 'r') as f:
    lines = f.readlines()

  with open(os.path.join(output_dir, 'output2.txt'), 'w') as outfile:
    for line in lines:
      for word in words:
        if word in line:
          outfile.write(line)
          break

if __name__ == '__main__':
  #words = ['masada', 'cheytac', 'melee']
  words = ['']
  file_name = "/main\\output.txt"
  output_dir = "/main\\"
  delete_lines(file_name, words, output_dir)
