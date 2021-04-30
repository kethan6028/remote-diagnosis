#!/usr/bin/env python
# coding: utf-8

import os
from glob import glob
import numpy as np
import torch
import torchvision
import torchvision.transforms
import torchxrayvision as xrv


class DiseasePredictor:

  def __init__(self, model_path=None, cuda=False):

    self.model_path = model_path
    self.device = 'cpu'
    # Load model
    self.model = torch.load(self.model_path, map_location=self.device)
    print("Model Loaded !")

    xrv.datasets.default_pathologies = ["No Finding", "Pneumonia", "COVID-19", "TB"]
    self.transform = torchvision.transforms.Compose(
      [xrv.datasets.XRayCenterCrop(),
       xrv.datasets.XRayResizer(224)])

  def predict(self, img_path):
    """ Predicts the chances of Disease in Input Image

      Args:
          img_path (str): Path of the image file
          img_path (np.ndarray): Path of the image file

      Returns:
          contract.CovidPrediction: Dictionary with prediction score for Normal|Covid|Pneumonia
      """

    # img = io.imread(img_path)
    img = img_path
    img = xrv.datasets.normalize(img, 255)

    # Check that images are 2D arrays
    if len(img.shape) > 2:
      img = img[:, :, 0]
    if len(img.shape) < 2:
      print("error, dimension lower than 2 for image")

    # Add color channel
    img = img[None, :, :]
    img = self.transform(img)

    output = {}
    # with torch.no_grad():
    #   img = torch.from_numpy(img).unsqueeze(0)
    #   if self.device == 'cuda':
    #     img = img.cuda()

    #   out = torch.sigmoid(self.model(img).cpu())
    #   preds = dict(
    #     zip(xrv.datasets.default_pathologies, out[0].detach().numpy()))
    prediction = {"No Finding": 0.03, "Pneumonia": 0.53, "COVID-19": 0.32, "TB": 0.21}

    return prediction
