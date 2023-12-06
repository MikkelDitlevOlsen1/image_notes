from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom



def show_comparison(original, modified, modified_name):
    "compare 2 plots"
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4), sharex=True,
                                   sharey=True)
    ax1.imshow(original)
    ax1.set_title('Original')
    ax1.axis('off')
    ax2.imshow(modified)
    ax2.set_title(modified_name)
    ax2.axis('off')
    io.show()

#histogram  
def histogram(img):
    h=plt.hist(img.ravel(), bins=256)
    plt.title('Image histogram')
    io.show()
    return h

#Minimum distance pixel classification (treshold)
def trhold(class1,class2):
    """
    fineds the treshold betwene two clases using Minimum distance pixel classification ruelse
    """
    dif=int(np.mean(class1)-np.mean(class2)/2)
    tr=np.mean(class2)+dif
    return tr

#Parametric pixel classification
def pdf_crose(pdf1,pdf2):

    """
    finde the value where 2 PDf's(normal destrabutien) croses
    """
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


#blob features analyse
def blobanalyse(img_open):
    label_img = measure.label(img_open)
    n_labels = label_img.max()
    print(f"Number of labels: {n_labels}")

    region_props = measure.regionprops(label_img)
    areas = np.array([prop.area for prop in region_props])
    plt.hist(areas, bins=50)
    plt.show()

    return label_img 


#BLOB classification by area
def blob_clas_by_arear(label_img,max_a,min_a):
    """
    Returne a mask img
    finde all blobs that are biger then min_a and smaler then min_b 
    max_a and min_a is max and min area we wont for a blob
    """
    #more values can be found here 
    #https://github.com/scikit-image/scikit-image/blob/v0.22.0/skimage/measure/_regionprops.py#L1048-L1331

        # Create a copy of the label_img
    label_img_filter = label_img.copy()
    region_props = measure.regionprops(label_img)
    for region in region_props:
        # Find the areas that do not fit our criteria

        #this is the place we wont to change if not clacyfi after areqa but shape
        if region.area > max_a or region.area < min_a:
            # set the pixels in the invalid areas to background
            for cords in region.coords:
                label_img_filter[cords[0], cords[1]] = 0
    
    # Create binary image from the filtered label image
    i_area = label_img_filter > 0

    return i_area

#BLOB Circularity
# ex 13 opg 5 

#disce score
def calculate_dice_coefficient(predicted, true):
    # Ensure the input arrays have the same shape
    assert predicted.shape == true.shape, "Input arrays must have the same shape"

    # Calculate the intersection and sizes of the sets
    intersection_size = np.sum(predicted & true)
    predicted_size = np.sum(predicted)
    true_size = np.sum(true)

    # Calculate the Dice coefficient
    dice_coefficient = (2.0 * intersection_size) / (predicted_size + true_size)

    return dice_coefficient


def show_comparison(original, transformed, transformed_name):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4), sharex=True,
                                   sharey=True)
    ax1.imshow(original)
    ax1.set_title('Original')
    ax1.axis('off')
    ax2.imshow(transformed)
    ax2.set_title(transformed_name)
    ax2.axis('off')
    io.show()