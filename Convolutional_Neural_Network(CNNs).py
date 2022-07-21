import imageio
import matplotlib.pyplot as plt
#matplotlib inline
# Read image
im = imageio.imread("lena.png")
print("Shape of the image tensor: {}".format(im.shape))
plt.imshow(im)