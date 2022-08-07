import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# script assumes you downloaded https://raw.githubusercontent.com/matplotlib/matplotlib/master/doc/_static/stinkbug.png
# to the location ./data/stinkbug

if __name__ == '__main__':
    
    try:
        img = mpimg.imread('./data/stinkbug.png')
        print(img)
    except:
        print('issue opening file. Are you calling the script in the \'Human-Lens\' directory?')
        
    
        