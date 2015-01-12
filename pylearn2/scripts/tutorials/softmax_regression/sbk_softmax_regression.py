#!/usr/bin/env python
#coding:utf-8
"""
 Author:  Sandeep Bhat --<sandeepkbhat@eyenuk.com>
 Created: 01/08/2015 10:19:15 AM
 Copyright 2014 Eyenuk LLC

 Description: This is a single script containing the code from the ipython
 notebook

"""

import os
import pylearn2

##################################################################################
def _save_yaml(yaml_str, base_dir, sbk_train_yaml):
    """
    Save the yaml string to a specified file
    Author: Sandeep Bhat --<sandeepkbhat@eyenuk.com>
    Created: 01/08/2015 02:48:39 PM
    """
    with open(os.path.join(base_dir, sbk_train_yaml), 'w') as f:
            f.write(yaml_str)
    print "The above YAML string saved to ", sbk_train_yaml

    display_msg = \
        """
        After you have setup Pylearn2, and run the Quick Start example you should
        be able to do the following to use the %(sbk_train_yaml)s file.
          $ train.py %(sbk_train_yaml)s
        The training step will take about 10-15 mins. You can then view the
        results as follows.
          $ print_monitor.py softmax_regression_besk.pkl
        Your results should be comparable to that listed in the ipython notebook.
        You can visualize the Weights as follows.
          $ show_weights.py softmax_regression_besk.pkl
        You should see 10 mini-images in a large image.
        """ % locals()
    print display_msg


##################################################################################
def main():

    dirname = os.path.abspath(os.path.dirname('softmax_regression.ipynb'))

    # ----------------------------------------------------------------------------
    # Setup dataset
    # ----------------------------------------------------------------------------
    with open(os.path.join(dirname, 'sr_dataset.yaml'), 'r') as f:
        dataset = f.read()
    hyper_params = {'train_stop' : 50000}
    dataset = dataset % (hyper_params)
    print "# DATASET ------------------------------------------------------------"
    print dataset

    # ----------------------------------------------------------------------------
    # Setup model
    # ----------------------------------------------------------------------------
    with open(os.path.join(dirname, 'sr_model.yaml'), 'r') as f:
        model = f.read()
    print "# SOFTMAX MODEL ------------------------------------------------------"
    print model

    # ----------------------------------------------------------------------------
    # Setup training algorithm
    # ----------------------------------------------------------------------------
    with open(os.path.join(dirname, 'sr_algorithm.yaml'), 'r') as f:
        algorithm = f.read()
    hyper_params = {'batch_size' : 10000,
                    'valid_stop' : 60000}
    algorithm = algorithm % (hyper_params)
    print "# TRAIN ALGORITHM ----------------------------------------------------"
    print algorithm

    # ----------------------------------------------------------------------------
    # Setup overall train object
    # ----------------------------------------------------------------------------
    with open(os.path.join(dirname, 'sr_train.yaml'), 'r') as f:
        train = f.read()
    save_path = '.'
    train = train %locals()
    print "# TRAIN OBJECT -------------------------------------------------------"
    print train

    # ----------------------------------------------------------------------------
    # Save the training yaml file
    # ----------------------------------------------------------------------------
    _save_yaml(yaml_str=train,
               base_dir=dirname,
               sbk_train_yaml='sbk_sr_train.yaml')


if __name__ == '__main__':
    main()