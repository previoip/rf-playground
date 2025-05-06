import os, shutil

def init_folder(path):
  if os.path.exists(path) and os.path.isdir(path):
    shutil.rmtree(path)
  os.makedirs(path)
