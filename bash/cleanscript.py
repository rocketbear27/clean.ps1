#!/bin/python
import sys
import os

how_many_times_we_should_clean = 0
deleted_files = []

dir = sys.argv[0]

class FileCache {
  def __init__(dir):
    self.dir = dir
    self.file_cache = []
  def cache(filename):
    #Assume the file is in the dir
    with open( dir + "/" + filename, "r" ) as file:
      self.file_cache.append( file.read() )
  def file_is_in_cache(filename):
    file_content = ""
    with open(dir + "/" + filename, "r" ) as file:
      file_content = file.read()
    if file_content in self.file_cache:
      return True
    return False
}

def is_heavy_or_useless(filename):
  #If it is a shortcut
  if filename.split(".")[-1] == ".desktop":
    return True
  
  #Put more cases here
  
  return False


def delete_file_or_folder(filename):
  os.remove(filename)
  #For convenience, we'll log all our deleted files and folders and show them to the user
  deleted_files.append(filename)
  
def scan_and_clean(dir):
  how_many_times_we_should_clean += 1
  file_cache = FileCache( dir )
  for i in os.listdir(dir):
    #Make sure not to get stuck in recursion or overstep our boundaries
    if i in [".",".."]:
      continue
    
    path_to_file = dir + "/" + i
    
    #If it is a directory
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


#Finally, run the program
for i in range(how_many_times_we_should_clean):
  scan_and_clean(dir)
