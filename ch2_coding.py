
from cProfile import label
from Chapter2.CreateDataset import CreateDataset
from util.VisualizeDataset import VisualizeDataset
from util import util
from pathlib import Path
import pandas as pd 
import copy
import os
import sys



DATASET_PATH = Path('')
RESULT_PATH = Path('./intermediate_datafiles/')
RESULT_FNAME1 = 'chapter2_result_database_own05s.csv'
RESULT_FNAME2 = 'chapter2_result_database_own1s.csv'

GRANULARITIES = [200, 1000]

[path.mkdir(exist_ok=True, parents=True) for path in [DATASET_PATH, RESULT_PATH]]

print("start building the datasets...")




datasets = []
for milliseconds_per_instance in GRANULARITIES:

    dataset = CreateDataset(DATASET_PATH, milliseconds_per_instance)
    dataset.add_numerical_dataset('Accelerometer_exp.csv', 'Time (ns)', ['Acceleration x (m/s^2)','Acceleration y (m/s^2)','Acceleration z (m/s^2)'], 'avg')
    dataset.add_numerical_dataset('Gyroscope_exp.csv', 'Time (ns)', ['Gyroscope x (rad/s)', 'Gyroscope y (rad/s)', 'Gyroscope z (rad/s)'], 'avg')
    dataset.add_numerical_dataset('Linear_Acceleration_exp.csv', 'Time (ns)', ["Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)"], 'avg')
    print(dataset)
    dataset.add_event_dataset('labels_exp_processed.csv', "start_ns", 'end_ns', 'label', 'binary')
    

    colnames = {'Acceleration x (m/s^2)': 'acc_phone_x', 'Acceleration y (m/s^2)':'acc_phone_y', 'Acceleration z (m/s^2)':'acc_phone_z','Gyroscope x (rad/s)': 'gyr_phone_x',
       'Gyroscope y (rad/s)': 'gyr_phone_y', 'Gyroscope z (rad/s)': 'gyr_phone_z', "Linear Acceleration x (m/s^2)":'lin_acc_x', "Linear Acceleration y (m/s^2)": 'lin_acc_y', "Linear Acceleration z (m/s^2)": 'lin_acc_z'}

    
    dataset = dataset.data_table
    dataset.rename(columns = colnames, inplace = True)

    print(dataset.columns)

    DataViz = VisualizeDataset(__file__)

    # Boxplot
    DataViz.plot_dataset_boxplot(dataset, ['acc_phone_x', 'acc_phone_y', 'acc_phone_z'], figname= str(milliseconds_per_instance) + ' acc')
    DataViz.plot_dataset_boxplot(dataset, ['gyr_phone_x', 'gyr_phone_y', 'gyr_phone_z'], figname= str(milliseconds_per_instance) + ' gyr')
    DataViz.plot_dataset_boxplot(dataset, ['lin_acc_x', 'lin_acc_y', 'lin_acc_z'], figname= str(milliseconds_per_instance) + ' lin')

    DataViz.plot_dataset(dataset, ['acc_phone', 'gyr_phone', 'lin', 'label'],
                         ['like', 'like', 'like', 'like'],
                         ['line', 'line', 'line', 'points'], figname=str(milliseconds_per_instance) +' all' )

    util.print_statistics(dataset)
    datasets.append(copy.deepcopy(dataset))
    print('dataset done')

util.print_latex_table_statistics_two_datasets(datasets[0], datasets[1])

datasets[0].to_csv(RESULT_PATH / RESULT_FNAME1 )
datasets[1].to_csv(RESULT_PATH / RESULT_FNAME2 )

print(datasets[1])
