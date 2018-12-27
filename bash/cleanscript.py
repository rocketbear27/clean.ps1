#!/usr/bin/env python3
import sys
import os
import re

file_regex = ""

def load_settings():
  with open("/lib/cleanscript/cleanscript_settings.txt","r") as file:
    content = file.read()
    file_regex = content.split("\n")[1]

load_settings()

file_regex = re.compile(file_regex)

how_many_times_we_should_clean = 0
deleted_files = []

class FileCache:
  def __init__(self, _dir):
    self._dir = _dir
    self.file_cache = []
  def cache(self, filename):
    #Assume the file is in the _dir
    with open( self._dir + "/" + filename, "r" ) as file:
      self.file_cache.append( file.read() )
  def file_is_in_cache(self, filename):
    file_content = ""
    with open(self._dir + "/" + filename, "r" ) as file:
      file_content = file.read()
    if file_content in self.file_cache:
      return True
    return False


def is_heavy_or_useless(filename):
  #If the file matches the regex, delete it
  if file_regex.match(filename) != None:
    return True
  
  #Put more cases here if needed
  
  return False


def delete_file_or_folder(filename):
  if os.path.isdir(filename):
    os.rmdir(filename)
  else:
    os.remove(filename)
  #For convenience, we'll log all our deleted files and folders and show them to the user
  deleted_files.append(filename)
  
def scan_and_clean(_dir):
  global how_many_times_we_should_clean
  
  print(_dir)
  how_many_times_we_should_clean += 1
  file_cache = FileCache( _dir )
  for i in os.listdir(_dir):
    #Make sure not to get stuck in recursion or overstep our boundaries
    if i in [".",".."]:
      continue
    
    path_to_file = _dir + "/" + i
    
    #If it is a _directory
    if os.path.isdir(path_to_file):
      if len( os.listdir(path_to_file) ) == 0:
        delete_file_or_folder(path_to_file)
      else:
        scan_and_clean(path_to_file)
    
    #Otherwise, it's a file
    else:
      #Is it a duplicate or a "heavy or useless" file?
      is_duplicate = file_cache.file_is_in_cache( i )
      is_hev_or_usels = is_heavy_or_useless( i )
      #Delete if it is
      if is_duplicate or is_hev_or_usels:
        delete_file_or_folder( path_to_file )
      #Otherwise, just cache it and continue
      else:
        file_cache.cache( i )
  return


#Finally, run the program on all the given directories
for i in range( 1, len(sys.argv) ):
  scan_and_clean(i)
  for j in range(how_many_times_we_should_clean):
    scan_and_clean(i)
  how_many_times_we_should_clean = 0
