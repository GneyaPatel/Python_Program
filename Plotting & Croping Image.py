from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm

ex_file=("fig1.jpg")
image = imread(ex_file, as_gray=True)
plt.imshow(image, cmap=cm.gray)
plt.show()
print("img:1) data type: %s, shape: %s" % (type(image), image.shape))

image2 = image[5:3000,0:3000]
plt.imshow(image2, cmap=cm.gray)
plt.show()
print("img:2) data type: %s, shape: %s" % (type(image2), image.shape))

image3 = resize(image2, (3000, 5000), mode='symmetric')
plt.imshow(image3, cmap=cm.gray)
plt.show()
print("img:3) data type: %s, shape: %s" %(type(image3), image3.shape))