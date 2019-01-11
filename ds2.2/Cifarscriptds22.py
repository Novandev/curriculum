import tensorflow as tf
import numpy as np
from sklearn.metrics import confusion_matrix

## Importing the load data from api calls in the load file

from Cifar10DataLoadDs22 import load_test_data,load_training_data,maybe_download_and_extract