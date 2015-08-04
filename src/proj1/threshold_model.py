import numpy as np
import skimage

class ThresholdModel:

  # set a reference matrix
  def set_ref_mat(self, ref_mat):
    self.ref_mat = ref_mat

  # set a threshold
  def set_threshold(self, threshold):
    self.threshold = threshold

  def predict(self, image_file):
    """
    Predict the label for an image
    Inputs:
    - image_file: filename of the image to predict
    Outputs:
    - return 1 if the image is positive, 0 if negative
    """
    return 0