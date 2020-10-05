# nama   : khairul Umam
# NIM    : 171011400073
# Kelas  : 07TPLE002
# Matkul : UAS - Kecerdasan Buatan

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io

from copy import deepcopy
koala=io.imread('koala.jpg')

red_channel= deepcopy(koala)
green_channel= deepcopy(koala)
blue_channel= deepcopy(koala)

red_channel[:,:,1]=0
red_channel[:,:,2]=0

green_channel[:,:,0]=0
green_channel[:,:,2]=0

blue_channel[:,:,0]=0
blue_channel[:,:,1]=0


fig, ax = plt.subplots(ncols=2, nrows=2)

ax[0,0].imshow(koala)
ax[0,0].set_title('')

ax[0,1].imshow(red_channel)
ax[0,1].set_title('')

ax[1,0].imshow(green_channel)
ax[1,0].set_title('')

ax[1,1].imshow(blue_channel)
ax[1,1].set_title('')

plt.show()
