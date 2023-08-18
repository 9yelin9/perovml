#!/usr/bin/env python3

from perovml import config, data

import os
num_thread = config.num_thread
os.environ['OMP_NUM_THREADS'] = str(num_thread)
os.environ['OPENBLAS_NUM_THREADS'] = str(num_thread)

import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
# data
parser.add_argument('-a', '--abx3', action='store_true', help='GenABX3')
args = parser.parse_args()                                                                     

d = data.Data()
# data
if args.abx3: d.GenABX3()
else: parser.print_help()
