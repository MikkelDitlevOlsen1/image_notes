from skimage import color, io, measure, img_as_ubyte ,img_as_float
from skimage.filters import threshold_otsu,median
from scipy.ndimage import correlate
import numpy as np


#with colormap (cmap)
def cmap(img):
    io.imshow(img, cmap="jet")
    io.show()

#with gray level scaling
def scale(img,minn,maxx):
    io.imshow(img, vmin=minn, vmax=maxx)
    io.show()

#creat mask
def masks(p,img,plot=False):
    """
    p is a function
    """
    mask = p(img)
    if plot:
        print(f"mask of p is ")
        io.imshow(mask)
        io.show()
    return mask


def grayscale_mask(img1,vmin,vmax):
    """
    scales a gray scale image so that vmin is 0 and vmax is 255 and the
    """
    img=img1.copy() 
    def p1(img):
        return img > vmax
    
    def p2(img):
        return img < vmin
    
    imgmask1=masks(p1,img)
    imgmask2=masks(p2,img)

    img[imgmask1]=vmax
    img[imgmask2]=vmin
    
    img=(img-vmin)/(vmax-vmin)
    img=img_as_ubyte(img)

    return img





def p(img):
    return img < 150

#roi mask
def roi_values(roi_img,dicom):
    """
    takes a roi image and a dicom and gives the roi_values as a list and the img_mask true where the roi image is and falsh where its not
    """
    # convert to boolean image
    img_mask = roi_img > 0
    roi_values = dicom[img_mask]
    return img_mask,roi_values


#Non-linear pixel value mapping
def gama_map(img,gamma):
    """
    γ-mapping
    g(x,y)=f(x,y)^γ

    """
    img_float=img_as_float(img)
    img_out=np.power(img_float,gamma)
    return img_as_ubyte( img_out)

def threshold_image(img_in, thres):
    """
    Apply a threshold in an image and return the resulting image
    :param img_in: Input image
    :param thres: The treshold value in the range [0, 255]
    :return: Resulting image (unsigned byte) where background is 0 and foreground is 255
    """
    mask=img_in > thres
    return img_as_ubyte(mask)


#Otsu's method
#This method finds the threshold, that minimizes the combined variance of the foreground and background.
#https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.threshold_otsu
def Otsu(img):
    """
    Apply a threshold in an image and return the resulting image and the threshold
    """
    threshold=threshold_otsu(img)
    imgnew=threshold_image(img,threshold)
    return imgnew,threshold
    

#correlate
#eksampel 
#from scipy.ndimage import correlate
#input_img = np.arange(25).reshape(5, 5)
#print(input_img)
# weights = [[0, 1, 0],
# 		   [1, 2, 1],
# 		   [0, 1, 0]]
#res_img = correlate(input_img, weights)
#borader is a miro by defoult


#border handling
#res_img = correlate(input_img, weights, mode="constant", cval=10)


#mean filter
def mean_filter(size):
    """
    returns a weighte that can be aplayed in correlate(input_img, weights)
    """
    weighets=np.ones([size,size])
    weighets=weighets/np.sum(weighets)
    return weighets 

#median filtering

def median_filter(size,img):
    """
    returns a image where the filter is aplayed on 
    """
    fotprint=np.ones([size,size])
    imgnew=median(img,fotprint)
    return imgnew 


# Gaussian filter

# from skimage.filters import gaussian
## and do the filtering:

# sigma = 1
# gauss_img = gaussian(im_org, sigma)


#Edge filters
# from skimage.filters import prewitt_h
# from skimage.filters import prewitt_v
# from skimage.filters import prewitt
#prewitt(img)


#Morphology
# from skimage.morphology import erosion, dilation, opening, closing
# from skimage.morphology import disk 
# footprint=disk(2)

#erosion(bin_img, footprint)
#erosion takes the smales value in the disk at set it to the curent target (makes objects smaler or desepere)


#dilation(bin_img, footprint)
#dilation takes the higest value in the disk at set it to the curent target (makes objects biggermoke hoelse desepere)


#opening(bin_img, footprint)
#removes small objects without changing the size of the remaining objects.
#works by first erosion and then dilation

#closed = closing(bin_img, footprint)
#closes holes in objects without changing the size of the remaining objects.
#works by first dilation and then erosion
