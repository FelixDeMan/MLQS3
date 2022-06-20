##############################################################
#                                                            #
#    Mark Hoogendoorn and Burkhardt Funk (2017)              #
#    Machine Learning for the Quantified Self                #
#    Springer                                                #
#    Chapter 3                                               #
#                                                            #
##############################################################
import lightgbm as lgb
import numpy as np
import pandas as pd

# Simple class to impute missing values of a single columns.
class ImputationMissingValues:

    # Impute the mean values in case if missing data.
    def impute_mean(self, dataset, col):
        dataset[col] = dataset[col].fillna(dataset[col].mean())
        return dataset

    # Impute the median values in case if missing data.
    def impute_median(self, dataset, col):
        dataset[col] = dataset[col].fillna(dataset[col].median())
        return dataset

    # Interpolate the dataset based on previous/next values..
    def impute_interpolate(self, dataset, col):
        dataset[col] = dataset[col].interpolate()
        # And fill the initial data points if needed:
        dataset[col] = dataset[col].fillna(method='bfill')
        return dataset


    def impute_model(self, dataset, col):
        #train_data = dataset.drop(col, 1)
        print(dataset)
        print(col)
        print(dataset[col].isnull())


        to_predict = dataset[dataset[col].isna()]


        training_data = dataset[~dataset[col].isna()]
        print(to_predict)
        print(training_data)

        labels_training = training_data[col]
        ds = lgb.Dataset(training_data.drop(columns= col), label = labels_training)
        params = {'objective' : 'regression'}
        bst = lgb.train(params = params, train_set = ds)
        predictions = bst.predict(to_predict.drop(columns = col))   
        print(predictions)
        to_predict[col] = predictions

        result = pd.concat([training_data, to_predict], axis=1)
        result = result.sort_index('index')
        print(result)




        return result
