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

    # ----------------------------------------------------------------------------
    # Part 1
    # ----------------------------------------------------------------------------
    path = os.path.join(pylearn2.__path__[0], 'scripts', 'tutorials', 'multilayer_perceptron', 'mlp_tutorial_part_2.yaml')
    dirname = os.path.abspath(os.path.dirname(path))
    with open(path, 'r') as f:
        train = f.read()
    hyper_params = {'train_stop' : 50000,
                    'valid_stop' : 60000,
                    'dim_h0' : 500,
                    'max_epochs' : 10000,
                    'save_path' : '.'}
    train = train % (hyper_params)
    print train

    _save_yaml(yaml_str=train,
               base_dir=dirname,
               sbk_train_yaml='sbk_mlp_tutorial_part_2.yaml',
               show_msg=False)

    # ----------------------------------------------------------------------------
    # Part 2
    # ----------------------------------------------------------------------------
    path = os.path.join(pylearn2.__path__[0], 'scripts', 'tutorials', 'multilayer_perceptron', 'mlp_tutorial_part_3.yaml')
    dirname = os.path.abspath(os.path.dirname(path))
    with open(path, 'r') as f:
        train_2 = f.read()
    hyper_params = {'train_stop' : 50000,
                    'valid_stop' : 60000,
                    'dim_h0' : 500,
                    'dim_h1' : 1000,
                    'sparse_init_h1' : 15,
                    'max_epochs' : 10000,
                    'save_path' : '.'}
    train_2 = train_2 % (hyper_params)
    print train_2

    _save_yaml(yaml_str=train_2,
               base_dir=dirname,
               sbk_train_yaml='sbk_mlp_tutorial_part_3.yaml',
               show_msg=False)

    # ----------------------------------------------------------------------------
    # Part 3
    # ----------------------------------------------------------------------------
    path = os.path.join(pylearn2.__path__[0], 'scripts', 'tutorials', 'multilayer_perceptron', 'mlp_tutorial_part_4.yaml')
    dirname = os.path.abspath(os.path.dirname(path))
    with open(path, 'r') as f:
        train_3 = f.read()
    hyper_params = {'train_stop' : 50000,
                    'valid_stop' : 60000,
                    'dim_h0' : 500,
                    'dim_h1' : 1000,
                    'sparse_init_h1' : 15,
                    'max_epochs' : 10000,
                    'save_path' : '.'}
    train_3 = train_3 % (hyper_params)
    print train_3

    _save_yaml(yaml_str=train_3,
               base_dir=dirname,
               sbk_train_yaml='sbk_mlp_tutorial_part_4.yaml',
               show_msg=True)

if __name__ == '__main__':
    main()