import pandas as pd
from datetime import datetime

labels = pd.read_csv('datasets/exp/labels_exp.csv')
print(labels)
labels['label_start_datetime'] = pd.to_datetime(labels['label_start_datetime'], dayfirst=True)
#times = datetime(labels['label_start_datetime'])
#print(times)
#labels['start_ns'] = times.timestamp()

labels['start_ns'] = labels['label_start_datetime'].values.astype('int64')
print(labels['start_ns'])

labels['label_end_datetime'] = pd.to_datetime(labels['label_end_datetime'], dayfirst= True)
labels['end_ns'] = labels['label_end_datetime'].values.astype('int64')
print(labels['end_ns'])

labels.to_csv('labels_exp_processed.csv')

filepaths = ['datasets/exp/Accelerometer_exp.csv', 'datasets/exp/Gyroscope_exp.csv',  'datasets/exp/Linear_Acceleration_exp.csv']
for i, file in enumerate(filepaths):

    acc = pd.read_csv(file)
    filename = file.split('/')[-1]

    print(filename)
    print(acc)
    print(acc.columns)
    print(acc.dtypes)
    acc['Time (ns)'] = (acc['Time (s)'] * float(10**9) + 1654617840000000000)
    print(acc['Time (ns)'])
    acc.to_csv(filename)
