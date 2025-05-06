import subprocess
from time import sleep
from shared.ipynbutils import ipynb_display_image

def export_frames_as_gif(folder, prefix, export_filepath, frame_rate):
  subprocess.Popen([
    'ffmpeg',
    '-y',
    # '-loglevel', 'quiet',
    '-f', 'image2',
    '-framerate', str(frame_rate),
    '-i', f'{folder}/{prefix}%04d.webp',
    export_filepath
  ]).wait()
  sleep(.2)
  return ipynb_display_image(export_filepath)


def export_frames_as_mp4(folder, prefix, export_filepath, frame_rate, loop=0):
  subprocess.Popen([
    'ffmpeg',
    '-y',
    '-loglevel',
    'quiet',
    '-f', 'image2',
    '-framerate', str(frame_rate),
    *(['-stream_loop', str(loop)] if loop > 0 else []),
    '-i', f'{folder}/{prefix}%04d.webp',
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    '-preset', 'faster',
    export_filepath
  ]).wait()
