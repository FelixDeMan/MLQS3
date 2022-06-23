import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def drop_columns():
    data = pd.read_csv('datasets/new_csv/patient_2.csv', header = 0)
    print(data.columns)
    label_columns = [col for col in data.columns if 'label' in col]
    print(label_columns)
    prime_labels = ['label:LYING_DOWN', 'label:SITTING', 'label:FIX_walking', 'label:BICYCLING', 'label:OR_standing','label:OR_exercise']
    to_del = [label for label in label_columns if label not in prime_labels]
    dropped_labels = data.drop(columns=to_del)
    print(dropped_labels)

    label_count = [dropped_labels[label].sum() for label in prime_labels]
    plt.bar(x = np.arange(len(label_count)), height = label_count,tick_label = prime_labels)
    plt.xticks(rotation = 'vertical')
    plt.show()
    dropped_labels.to_csv('data3.csv')
drop_columns()
data = pd.read_csv('data3.csv')
acc_cols = [col for col in data.columns if 'acc' in col]
gyr_cols = [col for col in data.columns if 'gyr' in col]
mag_cols = [col for col in data.columns if 'mag' in col]
watchacc_cols = [col for col in data.columns if 'watch_acceleration:' in col]
print(gyr_cols)

desired = ['timestamp','raw_acc:3d:mean_x', 'raw_acc:3d:mean_y', 'raw_acc:3d:mean_z', 'proc_gyro:3d:mean_x', 'proc_gyro:3d:mean_y', 'proc_gyro:3d:mean_z',  'raw_magnet:3d:mean_x', 'raw_magnet:3d:mean_y', 'raw_magnet:3d:mean_z', 'watch_acceleration:3d:mean_x', 'watch_acceleration:3d:mean_y', 'watch_acceleration:3d:mean_z','label:LYING_DOWN', 'label:SITTING', 'label:FIX_walking', 'label:BICYCLING', 'label:OR_standing','label:OR_exercise']
chosen = data[desired]
print(chosen)
chosen['timestamp'] = pd.to_datetime(chosen['timestamp'], unit='s')
chosen = chosen.set_index('timestamp')
cols ={'raw_acc:3d:mean_x': 'acc_phone_x', 'raw_acc:3d:mean_y':'acc_phone_y', 'raw_acc:3d:mean_z': 'acc_phone_z', 'proc_gyro:3d:mean_x': 'gyr_phone_x', 'proc_gyro:3d:mean_y': 'gyr_phone_y', 'proc_gyro:3d:mean_z': 'gyr_phone_z',  'raw_magnet:3d:mean_x': 'mag_phone_x', 'raw_magnet:3d:mean_y': 'mag_phone_y', 'raw_magnet:3d:mean_z': 'mag_phone_z', 'watch_acceleration:3d:mean_x': 'acc_watch_x', 'watch_acceleration:3d:mean_y': 'acc_watch_y', 'watch_acceleration:3d:mean_z': 'acc_watch_z', 'label:OR_standing': 'label:STANDING','label:OR_exercise':'label:EXERCISE', 'label:FIX_walking': 'label:FIX_WALKING'}
chosen = chosen.rename(columns = cols)
print(chosen)
chosen.to_csv('chosen_cols.csv')

