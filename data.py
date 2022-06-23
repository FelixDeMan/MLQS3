import pandas as pd
import glob



def unzip_data():
    gzfiles = glob.glob('datasets/new/*.csv.gz')
    print(gzfiles)
    for i, file in enumerate(gzfiles):
        traffic_df = pd.read_csv(file, compression='gzip',
                                 header=0, sep=',', quotechar='"')
        #print(traffic_df)
        #print(traffic_df.head())
        #print(traffic_df.columns)
        traffic_df.to_csv('datasets/new_csv/patient_'+ str(i) + '.csv')

def explore():
    data = pd.read_csv('chapter5_result_own.csv')
    print(data.isnull().sum())
    print(data.describe(include = 'all'))
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(data.isnull().sum())
        #print(data[['acc_phone_x_temp_std_ws_2', 'gyr_phone_x_temp_std_ws_2', 'mag_phone_x_temp_std_ws_2']])]


data = pd.read_csv('chapter5_result_own.csv')
data6 = pd.read_csv('chapter5_same_cluster.csv')

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(data6.columns)


data2 = data.join(data6[['mag_phone_cluster6',
       'mag_phone_silhouette6', 'gyr_phone_cluster6', 'gyr_phone_silhouette6',
       'acc_watch_cluster6', 'acc_watch_silhouette6']])
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(data2.columns)
data2.to_csv('chapter5_experiment_setup.csv')