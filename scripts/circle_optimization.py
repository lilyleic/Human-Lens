#Credit goes to https://stackoverflow.com/a/28287741
# Trying to copy over stuff from https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_label.html#sphx-glr-auto-examples-segmentation-plot-label-py
from configparser import Interpolation
from statistics import median
from skimage import filters, io, color, measure, draw, img_as_bool
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

input_file = 'results/prewitt.png'
#take only the blue component
image = io.imread(input_file)
thresh = filters.threshold_otsu(image)
image_binary = image <= thresh
regions = measure.regionprops(measure.label(image_binary))
bubble = regions[0]

y0, x0 = bubble.centroid
r = bubble.major_axis_length/2

def cost(params):
    x0,y0,r = params
    coords = draw.disk((y0,x0),r,shape=img.shape)
    template = np.zeros_like(img)
    template[coords] = 1
    return -np.sum(template == image_binary)

x0,y0,r = optimize.fmin(cost,(x0,y0,r))

f, ax = plt.subplots()
circle = plt.Circle((x0, y0), r)
ax.imshow(image_binary, cmap='gray',interpolation='nearest')
ax.add_artist(circle)
plt.savefig('results/circle_fit.png')