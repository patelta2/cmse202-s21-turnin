from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# Finish the new Observer class!
class Observer():
    '''
    This class creates an artificial night sky observer.
    '''
    
    # This function will get called automatically
    # when a new "observer" is created
    def __init__(self,im1_filename,im2_filename):
        '''
        When initializing the observer, the "red" image should be given
        as the first input argument and the "ir" image should be the second input
        '''
        self.im1_filename = im1_filename
        self.im2_filename = im2_filename
        #self.load_images(im1_filename,im2_filename)
        
    def load_images(self):
        '''
        This function is incomplete! It is missing the appropriate input vales
        and the "pass" should be replaced with the appropriate code.
        Update this docstring to explain what the function does (or should do).
        
        Open red then infrared file using fits.
        Save the data for the two images as a dictionary
        '''
        im1_data = fits.getdata(self.im1_filename, ext = 0)
        im2_data = fits.getdata(self.im2_filename, ext = 0)
        
        self.im1_data = im1_data
        self.im2_data = im2_data
        
        
    
    
    def calc_stats(self):
        '''
        Print mean and std for both images and print names of 
        each file.
        '''
        
        print(self.im1_filename)
        print("Image mean:",round(np.mean(self.im1_data),2))
        print("Image standard deviation:",round(np.std(self.im1_data),2))
        
        print(self.im2_filename)
        print("Image mean:",round(np.mean(self.im2_data),2))
        print("Image standard deviation:",round(np.std(self.im2_data),2))
        
       

    
    def make_composite(self):
        '''
        This function is incomplete! Make sure to finish it and
        then update this docstring to explain what the function does!
        '''
        
        # Define the array for storing RGB values
        rgb = np.zeros((self.im1_data.shape[0],self.im1_data.shape[1],3))
        
        # Define a normalization factor for our denominator using the R filter image
        norm_factor = self.im1_data.astype("float").max()
        
        # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = 1.5 * (self.im2_data.astype("float")/norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
        
        # Compute the green channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,1] = ((self.im2_data.astype("float") + self.im1_data.astype("float"))/2)/norm_factor
        rgb[:,:,1][rgb[:,:,1] > 1.0] = 1.0
    
        # Compute the blue channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,2] = (self.im1_data.astype("float"))/norm_factor
        rgb[:,:,2][rgb[:,:,2] > 1.0] = 1.0
        
        plt.imshow(rgb, origin = "lower")
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        