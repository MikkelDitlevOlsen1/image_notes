from skimage import color, io, measure, img_as_ubyte
from skimage import io, color
from skimage.morphology import binary_closing, binary_opening
from skimage.morphology import disk
import matplotlib.pyplot as plt
import numpy as np
from skimage import measure
from skimage.color import label2rgb
import pydicom as dicom
from scipy.stats import norm
from scipy.spatial import distance


def load_im(dir):
    im_org = io.imread(dir)
    print(f"Shape of image is {im_org.shape}")
    print(f" data {im_org.dtype}")
    io.imshow(im_org)
    io.show()
    return im_org

def load_dicom(path):
    ct = dicom.read_file(path)
    img = ct.pixel_array
    print(img.shape)
    print(img.dtype)
    print(np.max(img))
    io.imshow(img)
    return img


def zoom(img,zoomx:tuple,zoomy:tuple):
    zoom_im=img[zoomx[0]:zoomx[1],zoomy[0]:zoomy[1]]
    print(f"Shape of image is {zoom_im.shape}")
    print(f" data {zoom_im.dtype}")
    io.imshow(zoom_im)
    io.show()
    return zoom_im

