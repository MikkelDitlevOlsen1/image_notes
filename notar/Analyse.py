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

#Minimum distance pixel classification (treshold)
def trhold(class1,class2):
    dif=int(np.mean(class1)-np.mean(class2)/2)
    tr=np.mean(class2)+dif
    return tr

#Parametric pixel classification
def pdf_crose(pdf1,pdf2):
    tr=0
    if np.argmax(pdf1) < np.argmax(pdf2):
        for i1,i2 in zip(pdf1[np.argmax(pdf1):],pdf2[np.argmax(pdf1):]):
            if i1 < i2:
                tr=np.where(pdf1==i1)
                break 
    else:
        for i1,i2 in zip(pdf2[np.argmax(pdf2):],pdf1[np.argmax(pdf2):]):
            if i1 < i2:
                print(i1)
                print(i2)
                tr=np.where(pdf2==i1)
                break

    return tr