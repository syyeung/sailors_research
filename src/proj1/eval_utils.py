def evaluate_accuracy(filelist, labels, model):
  """
  Evaluate accuracy on a list of image files
  Inputs:
  - filelist: a list of image filenames
  - labels: a list of ground truth labels corresponding to the filelist
  - model: the methold will call model.predict on each image in the filelist
  Outputs:
  - predictions: a list of predicted labels corresponding to the filelist
  - accuracy: computed accuracy of the predictions based on the ground truth labels

  """
  num_images = len(filelist)
  num_correct = 0
  predictions = []
  for img_idx in xrange(num_images):
    image_file = filelist[img_idx]
    image_label = labels[img_idx]
    image_prediction = model.predict(image_file)
    predictions.append(image_prediction)
    if (image_label == image_prediction):
      num_correct += 1
  accuracy = float(num_correct) / num_images
  return predictions, accuracy



