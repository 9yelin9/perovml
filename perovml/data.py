from . import config

import os
import re
import sys
import ctypes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
from scipy import interpolate
from timeit import default_timer as timer

class Data:
	def GenABX3(self):
		df_mp = pd.read_csv('data/mp.csv')

		df_mp.dropna(axis=1, inplace=True)
		df_mp.drop(['builder_meta', 'composition_reduced', 'formula_anonymous', 'has_props', 'property_name', 'material_id', 'last_updated', 'origins', 'warnings', 'structure', 'task_ids'], axis=1, inplace=True)
		df_mp['elements'] = df_mp['elements'].str.replace('Element ', '', regex=True)
		df_mp['types_of_magnetic_species'] = df_mp['types_of_magnetic_species'].str.replace('Element ', '', regex=True)
		df_mp['symmetry'] = df_mp['symmetry'].str.replace("crystal.+: '|'>.+", '', regex=True)
		
		df = df_mp[df_mp['composition'].str.match('[A-Za-z]+1 [A-Za-z]+1 [A-Za-z]+3$') == True].copy(deep=True)
		for idx, d in df.iterrows():
			x = 0
			for ion in d['possible_species']:
				if re.search('[+]', ion): x += 1
			if x < 2: df.drop(idx, axis=0, inplace=True)
		df.reset_index(drop=True, inplace=True)

		print(df)
		df.to_csv('data/mp_ABX3.csv')
