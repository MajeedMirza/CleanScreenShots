import os

DESKTOP = 'PUT DESKTOP PATH HERE' + '/'
SSHOT = DESKTOP + 'ScreenShots/' #Create a folder called "ScreenShots" on Desktop before use
for fname in os.listdir(DESKTOP):
    if "Screen Shot" in fname and ".png" in fname:
       os.rename(DESKTOP + fname, SSHOT + fname)
       print "Moved " + fname + " to " + SSHOT
