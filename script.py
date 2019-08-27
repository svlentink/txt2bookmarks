#!/usr/bin/env python3

# based on https://msdn.microsoft.com/en-us/ie/aa753582(v=vs.94)

import os
from sys import argv

def parseBookmarks(path: str):
  return '''<!DOCTYPE NETSCAPE-Bookmark-file-1>
<DL>
''' + parsePath(path) + '</DL>'

def parseLine(line: str):
  l = line.split(' ')
  if len(l) < 1:
    return ''
  href = l[0]
  desc = ' '.join(l[1:])
  if len(l) == 1:
    desc = href
  if href[:4] != 'http':
    href = 'http://' + href
  return '    <DT><A HREF="' + href + '">' + desc +'</A>'

def parsePath(path: str):
  pre = '<DT><H3 FOLDED>' + path + '''</H3> 
  <DL><p>
'''
  post = '''
  </DL><p>
'''
  if os.path.isdir(path):
    return pre + '\n'.join([parsePath(path + '/' + p) for p in os.listdir(path)]) + post
  elif os.path.isfile(path):
    if path[-4:] != '.txt':
      return '    <!-- Ignoring non .txt file ' + path + ' -->'
    lines = list()
    with open(path, "r") as myfile:
      for line in myfile:
        lines.append(line.strip())
    return pre + '\n'.join([parseLine(line) for line in lines]) + post
  else: 
    return "    <!-- Ignoring special file (socket, FIFO, device file) " + inp + '-->'

if len(argv) != 2:
  print("USAGE: " + argv[0] + " ./some/path")
else:
  print(parseBookmarks(argv[1]))
