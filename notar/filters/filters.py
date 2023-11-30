from skimage import color, io, measure, img_as_ubyte

#with colormap (cmap)
def cmap(img):
    io.imshow(img, cmap="jet")
    io.show()

#with gray level scaling
def scale(img,minn,maxx):
    io.imshow(img, vmin=minn, vmax=maxx)
    io.show()

#creat mask
def masks(p,img):
    mask = p(img)
    io.imshow(mask)
    io.show()
    return mask

def p(img):
    return img < 150

#roi mask
def roi_values(roi_img,dicom):
    # convert to boolean image
    img_mask = roi_img > 0
    roi_values = dicom[img_mask]
    return img_mask,roi_values


