import os
os.environ['KERAS_BACKEND'] = "tensorflow"

import pathlib
import random
import re
import string
import numpy as np

import keras
import tensorflow as tf
import tensorflow.data as tf_data
from tensorflow import strings as tf_strings
from keras import layers
#from keras import ops as ops
from keras.layers import TextVectorization