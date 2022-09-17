# Copyright (c) AGI.__init__. All Rights Reserved.
#
# This source code is licensed under the MIT license found in the
# MIT_LICENSE file in the root directory of this source tree.
from Sweeps.Templates import template
from Sweeps.Templates import convert_to_attr_dict


runs = template('Example')  # The plotting directory will be called "Example"

runs.Example.sweep = [
    'experiment=Test1 task=classify/mnist train_steps=2000'
]

runs.Example.plots = [
    ['Test1'],
]
runs.Example.title = 'A Good Ol\' Test'


"""
Structure of runs:

-> Sweep Group:
        -> Sweep & Plots & Plots Metadata
"""


runs = convert_to_attr_dict(runs)  # Necessary if runs is defined as a dict!
