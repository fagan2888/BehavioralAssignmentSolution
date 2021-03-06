# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 7/5/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, scipy, matplotlib
Using cmd line py -3,6 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
from Implementations.compute_mean import *
from Implementations.compute_var import *
from Implementations.Backtesing.mean_return import *
from Implementations.Backtesing.variance_return import *

'''===================================================================================================
File content:
provide optimization target function fitness_sharpe, like cost
==================================================================================================='''

def sharpe_ratio(R, rf, freq='annually'):
	'''==============================================================================================
	Arguments:
	R 	-- list, past expected returns of strategy
	rf 	--	double, risk-free return rate
	freq	-- string, the frequency of computation

	Returns:
	res -- double, u=(mean-rf)/sqrt(var)
	=============================================================================================='''
	# Preparation Phrase
	mean = mean_return(R, freq);
	var = variance_return(R, freq);

	# Handling Phrase
	res = (mean-rf)/var

	# Checking Phrase
	return res

