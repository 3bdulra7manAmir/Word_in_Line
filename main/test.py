import csv
import re

def find_words(file_name, words, output_file_name):
  with open(file_name, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
      for word in words:
        if word in row:
          line = ','.join(row)
          with open(output_file_name, 'a') as outfile:
            outfile.write(line + '\n')

if __name__ == '__main__':
  #words = ['loaded_sound', 'sound', 'xmodel', 'xanim', 'image', 'material']
  #words = ['fx', 'vfx']
  words = ['xmodel,']
  #words = ['sound,h2_wpn','sound,wpn_h2','sound,wpn_h1','sound,weap_','sound,h1_wpn']
  file_name = "E:\\h1\\dump\\iw5_delta_force\\iw5_delta_force.csv"
  output_file_name = "/main\\output2.txt"
  find_words(file_name, words, output_file_name)
