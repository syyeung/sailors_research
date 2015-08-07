import numpy as np
from skimage import io

class ThresholdModel:

  # set a reference matrix
  def set_ref_mat(self, ref_mat):
    self.ref_mat = ref_mat

  # set thresholds
  def set_pixel_change_threshold(self, threshold):
    self.pixel_change_threshold = threshold
    
  def set_image_score_threshold(self, threshold):
    self.image_score_threshold = threshold

  def set_crop(self, xstart, xend, ystart, yend):
    self.cropx_start = xstart
    self.cropx_end = xend
    self.cropy_start = ystart
    self.cropy_end = yend 

  def predict(self, image_file):
    """
    Predict the label for an image
    Inputs:
    - image_file: filename of the image to predict
    Outputs:
    - return 1 if the image is positive, 0 if negative
    """
    return 0, image_score
