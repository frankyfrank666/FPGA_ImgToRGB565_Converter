import numpy as np
from imageio import imread

def read_image(path):
  img = imread(path)
  res = []
  for row in img:
    ln = []
    for R,G,B,*_ in row:
      ln.append([R,G,B])
    res.append(ln)
  return res

img = read_image('Capture.PNG')

a= np.core.numeric.ones((len(img),len(img[0])),'int32')

for i in range(len(img)):
    for j in range(len(img[0])):
        R = img[i][j][0]>>3
        G = img[i][j][1]>>2
        B = img[i][j][2]>>3
        rgb = (R<<11)|(G<<5)|B
        
        a[i][j] = rgb


np.savetxt('IMG.mem',a,fmt='%04x',delimiter=' ', newline='\n')