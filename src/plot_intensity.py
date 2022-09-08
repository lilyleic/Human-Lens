import marplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticket import LinearLocator
import numpy as np

from skimage import data

def plot_intensity(image, rgb_index):
    """
    Given an image and rgb index (in range 0 to 2 )
    Returns plot object of intensity for that rgb value
    """

    assert 0 <= rgb <=2
    assert len(image.size) == 3
    assert image.size[-1] == 3
    # Gather the Data
    rows,cols,colors = image.size
    intesity = np.zeros(rows,cols)
    intesity[:, :] = image[:, :,rgb]
    
    rows, columns = image.size
    
fig, ax = plt.subplots(subplot kw=("projection": "3d"))

