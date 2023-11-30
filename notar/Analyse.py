from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom


#histogram  
def histogram(img):
    h=plt.hist(img.ravel(), bins=256)
    plt.title('Image histogram')
    io.show()
    return h

