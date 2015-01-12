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
def _save_yaml(yaml_str, base_dir, sbk_train_yaml, show_msg=True):
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
    if show_msg:
        print display_msg

##################################################################################
def main():

    path = os.path.join(pylearn2.__path__[0], 'scripts', 'tutorials', 'convolutional_network', 'conv.yaml')
    dirname = os.path.abspath(os.path.dirname(path))
    train = open(path, 'r').read()
    train_params = {'train_stop': 50000,
                    'valid_stop': 60000,
                    'test_stop': 10000,
                    'batch_size': 100,
                    'output_channels_h2': 64,
                    'output_channels_h3': 64,
                    'max_epochs': 500,
                    'save_path': '.'}
    train = train % (train_params)
    print train

    _save_yaml(yaml_str=train,
               base_dir=dirname,
               sbk_train_yaml='sbk_conv.yaml',
               show_msg=True)


if __name__ == '__main__':
    main()