from operator import ne
import sys
import time
import re

## Steo 1
# def grep(pattern, line):
    
#     if re.search(pattern, line):
#         yield line


# def logger(path, pattern):
#    with open(path, "+r") as file:
#     file.read()
#     while True:
#        new_line = file.readline()
#        if not new_line:
#           time.sleep(0.2)
#           continue
#        yield from grep(pattern, new_line)
       

# if __name__ == '__main__':
#    for log in logger('/home/atiyehghm/Desktop/Building-LLM_book/temp.txt', r'run'):
#       print(log)


# # Step 2
# def grep(pattern, line):
#     if re.search(pattern, line):
#         yield line


# def logger(path, pattern1, pattern2):
#    with open(path, "+r") as file:
#     file.read()
#     while True:
#        new_line = file.readline()
#        if not new_line:
#           time.sleep(0.2)
#           continue
#        for line in grep(pattern1, new_line):
#           yield from grep(pattern2, line)
       

# if __name__ == '__main__':
#    for log in logger('/home/atiyehghm/Desktop/Building-LLM_book/temp.txt', r'git', r'branch'):
#       print(log)


## step 3
def grep(pattern, lines):
    for line in lines:
      if re.search(pattern, line):
         yield line


def logger(path):
   with open(path, "+r") as file:
    file.read()
    while True:
       new_line = file.readline()
       if not new_line:
          time.sleep(0.2)
          continue
       yield new_line
       

if __name__ == '__main__':
   log_gen = logger('/home/atiyehghm/Desktop/Building-LLM_book/temp.txt')
   git_filtered = grep(r'git', log_gen)
   branch_filtered = grep(r'branch', git_filtered)
   for log in branch_filtered:
      print(log)
      

