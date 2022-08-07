from scipy import ndimage, misc
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def left_right_image_apply(img,img_function,plt_file_name):
    fig = plt.figure()
    plt.gray()
    ax1 = fig.add_subplot(121) #left side
    ax2 = fig.add_subplot(122) #right side
    result = img_function(img)
    ax1.imshow(img)
    ax2.imshow(result)
    plt.savefig(plt_file_name)
    
    
if __name__== '__main__':

    #try with a default image
    try:
        img =  mpimg.imread('./data/1.5m.png')
    
        #try a bunch of plots
        gaussian_magnitude = lambda img: ndimage.gaussian_gradient_magnitude(img,sigma=20)
        left_right_image_apply(img,gaussian_magnitude,'results/gaussian_gradient.png')
    
        left_right_image_apply(img,
                           lambda img:ndimage.minimum_filter(img,size=20),'results/minimum_filter.png')
        left_right_image_apply(img,
                           lambda img: ndimage.median_filter(img,size=20),
                           'results/median_filter.png'
                           )
        left_right_image_apply(img,
                           lambda img: ndimage.percentile_filter(img, percentile=20,size=20),
                           'results/percentile_filter.png'
                           )
        left_right_image_apply(img,
                            ndimage.prewitt,
                            'results/prewitt.png')
    
    except:
        print('Error during plot routine. Did you call the script from the \'Human-Lens\' directory?')