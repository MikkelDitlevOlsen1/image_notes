from skimage import color, io, measure, img_as_ubyte


def load_im(dir):
    im_org = io.imread(dir)
    print(f"Shape of image is {im_org.shape}")
    print(f" data {im_org.dtype}")
    io.imshow(im_org)
    io.show()
    return im_org

def zoom(img,zoomx:tuple,zoomy:tuple):
    zoom_im=img[zoomx[0]:zoomx[1],zoomy[0]:zoomy[1]]
    print(f"Shape of image is {zoom_im.shape}")
    print(f" data {zoom_im.dtype}")
    io.imshow(zoom_im)
    io.show()
    return zoom_im

    