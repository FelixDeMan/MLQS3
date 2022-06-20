import pandas as pd
import glob

gzfiles = glob.glob('datasets/new/*.csv.gz')
print(gzfiles)
for i, file in enumerate(gzfiles):
    traffic_df = pd.read_csv(file, compression='gzip',
                             header=0, sep=',', quotechar='"')
    #print(traffic_df)
    #print(traffic_df.head())
    #print(traffic_df.columns)
    traffic_df.to_csv('datasets/new_csv/patient_'+ str(i) + '.csv')


