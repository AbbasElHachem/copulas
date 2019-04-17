# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: EL Hachem Abbas,
Institut fuer Wasser- und Umweltsystemmodellierung - IWS
"""

'''
Construct Bivariate Copulas between rainfall and temperature
'''
import os
import time
import timeit


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats


print('\a\a\a\a Started on %s \a\a\a\a\n' % time.asctime())
START = timeit.default_timer()  # to get the runtime of the program

main_dir = os.path.join(r'X:\hiwi\ElHachem\AdvancedPython\Copulas')
os.chdir(main_dir)

in_ppt_file = os.path.join(main_dir, r'SA_pr_1901_2015.csv')
in_temp_file = os.path.join(main_dir, r'SA_temp_data_1901_2015.csv')


in_ppt_df = pd.read_csv(in_ppt_file, index_col=0, sep=';', parse_dates=True)
in_temp_df = pd.read_csv(in_temp_file, index_col=0, sep=';', parse_dates=True)


def transform_variables_to_uniform_marginals(varx, vary, plot=False):

    xvals = np.squeeze(varx)
    yvals = np.squeeze(vary)

    ranks_R1i = (len(xvals) - stats.rankdata(xvals) + 0.5) / len(xvals)
    ranks_S1i = (len(yvals) - stats.rankdata(yvals) + 0.5) / len(yvals)

    if plot:
        _, (ax1, ax2) = plt.subplots(
            1, 2, sharey=True, sharex=True)  # , projection='3d')
        ax1.scatter(ranks_S1i, ranks_R1i, c='b', marker='o', alpha=0.5)

        ax2.hist2d(ranks_S1i, ranks_R1i, bins=10, normed=True)
        ax1.set_xlabel('Normed Ranked Temp')
        ax2.set_xlabel('Normed Ranked Temp')
        ax1.set_ylabel('Normed Ranked Ppt')
        plt.savefig(os.path.join(main_dir, 'test_ppt_temp.png'))
    return


transform_variables_to_uniform_marginals(in_ppt_df.values,
                                         in_temp_df.values,
                                         plot=True)


STOP = timeit.default_timer()  # Ending time
print(('\n\a\a\a Done with everything on %s. Total run time was'
       ' about %0.4f seconds \a\a\a' % (time.asctime(), STOP - START)))
