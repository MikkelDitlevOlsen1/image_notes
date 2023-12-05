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
    """
    Load an iamge
    """
    im_org = io.imread(dir)
    print(f"Shape of image is {im_org.shape}")
    print(f" data {im_org.dtype}")
    io.imshow(im_org)
    io.show()
    return im_org


def rgb2gray(img):
    grayimg= color.rgb2gray(img) 
    grayimg=img_as_ubyte(grayimg)
    print(f" data type {grayimg.dtype}")
    print(f"val range {np.min(grayimg)} - {np.max(grayimg)}")
    return grayimg


def load_dicom(path):
    """
    Load an dicom image
    """
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

#HCV 
def rgb2hcv(im_org):
    hsv_img = color.rgb2hsv(im_org)
    hue_img = hsv_img[:, :, 0]
    value_img = hsv_img[:, :, 2]
    saturation_img = hsv_img[:, :, 2]
    fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(8, 2))
    ax0.imshow(im_org)
    ax0.set_title("RGB image")
    ax0.axis('off')
    ax1.imshow(hue_img, cmap='hsv')
    ax1.set_title("Hue channel")
    ax1.axis('off')
    ax2.imshow(value_img)
    ax2.set_title("Value channel")
    ax2.axis('off')

    fig.tight_layout()
    io.show()
    return hsv_img