
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
from env import host, user, password
from pydataset import data
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import classification_report, confusion_matrix,mean_squared_error, accuracy_score
from sklearn.dummy import DummyClassifier
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
# import logistic_regression_util
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from tqdm import tqdm
from matplotlib.colors import ListedColormap


# Check out the distributions of numeric columns - these are the categorical variables
def num_dist(df):
    for col in df.columns:
        if df[col].dtype != 'object':
            plt.hist(df[col])
            plt.title(f'Distribution of {col}')
            plt.show()
            
            
            
            
def telco_split(df):
    '''
    This function takes in the telco data acquired by get_telco_data,
    performs a split and stratifies churn column.
    Returns train, valudate, and test dataframes
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=254, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=254, 
                                   stratify=train_validate.churn)
    return train, validate, test





def prep_telco(df):
    '''
    This will be the prepare function that will include the prep for telco
    '''
    df = df.drop_duplicates()
    df['total_charges'] = df['total_charges'] + '0'
    df['total_charges'] = df['total_charges'].astype('float')
    col_list = list(df.select_dtypes('object').columns)[1:]
    dummy_df = pd.get_dummies(df[col_list])
    df = pd.concat([df, dummy_df], axis=1)
    
    return df



# train, validate, test = train_validate_test_split(df, seed=123)
# train.head()

## hello

## hello