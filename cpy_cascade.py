from shutil import copy2
from cv2.data import haarcascades

file = "haarcascade_frontalface_default.xml"
copy2(haarcascades + file, "data/" + file)
