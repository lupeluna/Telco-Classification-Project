# include train/validate/test functions


# Include code for missing values


# encode variables as needed


# create any new features if necessary 


# df = df.loc[:, ~df.columns.duplicated()]

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






# train, validate, test = train_validate_test_split(df, seed=123)
# train.head()