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
