1. source file:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Description
'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__author__      = "CONG-MINH NGUYEN"
__copyright__   = "Copyright (C) ${YEAR}, ${PROJECT_NAME}"
__credits__     = ["CONG-MINH NGUYEN"]
__license__     = "GPL"
__version__     = "1.0.1"
__date__        = "${DATE}"
__maintainer__  = "CONG-MINH NGUYEN"
__email__       = "minhnc.edu.tw@gmail.com"
__status__      = "Development" # ["Prototype", "Development", or "Production"]
# Project Style: https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6
# Code Style: http://web.archive.org/web/20111010053227/http://jaynes.colorado.edu/PythonGuidelines.html#module_formatting

#==============================================================================
# Imported Modules
#==============================================================================
import argparse
import os.path
import sys
import time

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "" # The GPU id to use, usually either "0" or "1"

#==============================================================================
# Constant Definitions
#==============================================================================

#==============================================================================
# Function Definitions
#==============================================================================

#==============================================================================
# Main function
#==============================================================================
def _main_(args):
    print('Hello World! This is {:s}'.format(args.desc))

    # config_path = args.conf
    # with open(config_path) as config_buffer:    
    #     config = json.loads(config_buffer.read())
    
    '''**************************************************************
    I. Set parameters
    '''
    
    '''**************************************************************
    II. Prepare the data
    '''
    # 1: Instantiate two `DataGenerator`

    '''**************************************************************
    III. Create the model
    '''
    # 1: Build the model architecture.
    
    # 2: Load some weights into the model.
    
    # 3: Instantiate an optimizer and the SSD loss function and compile the model.
    
    '''**************************************************************
    IV. Kick off the training
    '''
    # 1: Define model callbacks.
    
    # 2: Train model
    
    '''**************************************************************
    V. Test & Evaluate
    '''
    # 1: Instantiate generator for the test/evaluation.
    
    # 2: Generate samples.
    
    # 3: Make predictions.
    
    # 4: Decode the raw predictions into labels.
    
    # 5: Display predicted results
    
    # 6: Run evaluation.

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Your program name!!!')
    argparser.add_argument('-d', '--desc', help='description of the program', default='${PROJECT_NAME}')
    # argparser.add_argument('-c', '--conf', default='config.json', help='path to configuration file')
    
    args = argparser.parse_args()
    _main_(args)

```

1. class learner
```python
import tensorflow as tf
from keras.models import Model
from keras.layers import Input, Conv2D, Activation, BatchNormalization, MaxPool2D, Flatten, Dense, Reshape, Lambda
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard


class $class$(object):
    def __init__(self, input_shape, verbose=1):
        """
        Description:
        :param NAME: TYPE, MEAN
        :return: TYPE, MEAN
        """
        '''**************************************************************
        I. Set parameters
        '''

        '''**************************************************************
        II. Make the model
        '''
        # 1: Build the model architecture.
        # 1.a: make the feature extractor layers
        
        # 1.b: make the detection layer
        
        # 1.c: build model
        
        # 2: Load some weights into the model.
        
        # print a summary of the whole model
        if verbose: self.model.summary()

    def custom_loss(self, y_true, y_pred):
        """
        Description:
        :param NAME: TYPE, MEAN
        :return: TYPE, MEAN
        """
        return

    def custom_callbacks(self, checkpoint_dir, log_dir):
        """
        Description:
        :param NAME: TYPE, MEAN
        :return: TYPE, MEAN
        """
        checkpoint = ModelCheckpoint(checkpoint_dir,
                                     monitor='val_loss',
                                     verbose=1,
                                     save_best_only=True,
                                     mode='min',
                                     period=1)

        early_stop = EarlyStopping(monitor='val_loss',
                                   min_delta=0.001,
                                   patience=3,
                                   mode='min',
                                   verbose=1)

        tensorboard = TensorBoard(log_dir=os.path.expanduser(log_dir),
                                  histogram_freq=0,
                                  write_graph=True,
                                  write_images=False)

        return [checkpoint, early_stop, tensorboard]

    def load_weights(self, weight_path):
        """
        Description:
        :param NAME: TYPE, MEAN
        :return: TYPE, MEAN
        """
        self.model.load_weights(filepath=weight_path)
        return

    def train(self, train_data, valid_data,
              batch_size, nb_epoch,
              learning_rate,
              saving_weights_name='best_weights.h5',
              debug=False):
        """
        Description:
        :param NAME: TYPE, MEAN
        :return: TYPE, MEAN
        """
        '''**************************************************************
        I. Set training parameters
        '''

        '''**************************************************************
        II. Declare data and generator
        '''

        '''**************************************************************
        III. Compile the model
        '''

        '''**************************************************************
        IV. Kick off the training
        '''
        # 1: Define model callbacks.

        # 2: Train model

        '''**************************************************************
        V. Evaluate on validation set
        '''

        return

    def evaluate(self):
        """
        Description:
        :param NAME: TYPE, MEAN
        :return: TYPE, MEAN
        """
        return

    def predict(self):
        """
        Description:
        :param NAME: TYPE, MEAN
        :return: TYPE, MEAN
        """
        # 1: Preprocess the data.
        
        # 2: Make prediction.
        
        # 3: Standard the output.
        
        return
```

2. docstring:
```python
"""
Description: 
:param NAME: TYPE, MEAN
:return: TYPE, MEAN
"""
```
