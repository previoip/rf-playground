from IPython.display import Image
from uuid import uuid4

def ipynb_display_image(path):
  from IPython.display import Image
  return Image(url=path + '?' + uuid4().hex)
