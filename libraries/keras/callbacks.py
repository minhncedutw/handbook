'''
    File name: pointnet1_pytorch
    Author: minhnc
    Date created(MM/DD/YYYY): 10/1/2018
    Last modified(MM/DD/YYYY HH:MM): 10/1/2018 10:25 AM
    Python Version: 3.5
    Other modules: [tensorflow-gpu 1.3.0]

    Copyright = Copyright (C) 2017 of NGUYEN CONG MINH
    Credits = [None] # people who reported bug fixes, made suggestions, etc. but did not actually write the code
    License = None
    Version = 0.9.0.1
    Maintainer = [None]
    Email = minhnc.edu.tw@gmail.com
    Status = Prototype # "Prototype", "Development", or "Production"
    Code Style: http://web.archive.org/web/20111010053227/http://jaynes.colorado.edu/PythonGuidelines.html#module_formatting
'''

#==============================================================================
# Imported Modules
#==============================================================================
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os.path
import sys
import time

import keras
from keras.callbacks import ModelCheckpoint, TensorBoard, LearningRateScheduler, ReduceLROnPlateau, EarlyStopping, LambdaCallback

#==============================================================================
# Constant Definitions
#==============================================================================
class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))

def callbacks(checkpoint_path, batch_size=None, schedule=None):
    callbacks_list = [
        ModelCheckpoint(
                        filepath='/model.loss.{epoch:02d}.hdf5', # string, path to save the model file.
                        monitor='val_loss', # quantity to monitor.
                        save_best_only=True, # if save_best_only=True, the latest best model according to the quantity monitored will not be overwritten.
                        mode='auto', # one of {auto, min, max}. If save_best_only=True, the decision to overwrite the current save file is made based on either the maximization or the minimization of the monitored quantity. For val_acc, this should be max, for val_loss this should be min, etc. In auto mode, the direction is automatically inferred from the name of the monitored quantity.
                        save_weights_only='false', # if True, then only the model's weights will be saved (model.save_weights(filepath)), else the full model is saved (model.save(filepath)).
                        period=1, # Interval (number of epochs) between checkpoints.
                        verbose=1), # verbosity mode, 0 or 1.
        TensorBoard(log_dir='./outputs/graph', # the path of the directory where to save the log files to be parsed by TensorBoard.
                    histogram_freq=0, # frequency (in epochs) at which to compute activation and weight histograms for the layers of the model. If set to 0, histograms won't be computed. Validation data (or split) must be specified for histogram visualizations.
                    # batch_size=batch_size,
                    write_graph=True, # whether to visualize the graph in TensorBoard. The log file can become quite large when write_graph is set to True.
                    write_grads=False, # whether to visualize gradient histograms in TensorBoard. histogram_freq must be greater than 0.
                    write_images=True, # whether to write model weights to visualize as image in TensorBoard.
                    embeddings_freq=0), # frequency (in epochs) at which selected embedding layers will be saved. If set to 0, embeddings won't be computed. Data to be visualized in TensorBoard's Embedding tab must be passed as embeddings_data.
        LearningRateScheduler(schedule, # a function that takes an epoch index as input (integer, indexed from 0) and current learning rate and returns a new learning rate as output (float).
                              verbose=0), # int. 0: quiet, 1: update messages.
        ReduceLROnPlateau(monitor='val_loss', # quantity to be monitored.
                          factor=0.2, # factor by which the learning rate will be reduced. new_lr = lr * factor
                          patience=4, # number of epochs with no improvement after which learning rate will be reduced.
                          verbose=1, # int. 0: quiet, 1: update messages.
                          mode='min', # In min mode, lr will be reduced when the quantity monitored has stopped decreasing; in max mode it will be reduced when the quantity monitored has stopped increasing; in auto mode, the direction is automatically inferred from the name of the monitored quantity.
                          min_lr=1e-6, # lower bound on the learning rate.
                          cooldown=2), # number of epochs to wait before resuming normal operation after lr has been reduced.
        EarlyStopping(monitor='val_loss', # quantity to be monitored.
                      min_delta=0, # minimum change in the monitored quantity to qualify as an improvement, i.e. an absolute change of less than min_delta, will count as no improvement.
                      patience=20, # number of epochs with no improvement after which training will be stopped.
                      verbose=0, # int. 0: quiet, 1: update messages.
                      mode='auto', # one of {auto, min, max}. In min mode, training will stop when the quantity monitored has stopped decreasing; in max mode it will stop when the quantity monitored has stopped increasing; in auto mode, the direction is automatically inferred from the name of the monitored quantity.
                      baseline=None, # Baseline value for the monitored quantity to reach. Training will stop if the model doesn't show improvement over the baseline.
                      restore_best_weights=False), # whether to restore model weights from the epoch with the best value of the monitored quantity. If False, the model weights obtained at the last step of training are used.
        LambdaCallback(on_epoch_begin=None,
                       on_epoch_end=None,
                       on_batch_begin=None,
                       on_batch_end=None,
                       on_train_begin=None,
                       on_train_end=None),
    ]
    return callbacks_list

#==============================================================================
# Function Definitions
#==============================================================================

#==============================================================================
# Main function
#==============================================================================
def main(argv=None):
    print('Hello! This is XXXXXX Program')

    '''How to use ModelCheckpoint'''
    checkpoint_path = './outputs/model_checkpoints'
    if not os.path.exists(checkpoint_path):
        os.mkdir(checkpoint_path)

    '''How to use Tensorboard'''
    tensorboard_path = './outputs/graph'
    if not os.path.exists(tensorboard_path):
        os.mkdir(tensorboard_path)
    # at terminal type: `activate ENV_NAME` to activate environment python
    # at terminal type: `tensorboard --logdir ./outputs/graph` to monitor tensorboard
    # open browser: `htttp://localhost:6006`


if __name__ == '__main__':
    main()
