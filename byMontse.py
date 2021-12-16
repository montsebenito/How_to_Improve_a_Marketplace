import pandas as pd
import numpy as np
from collections import defaultdict
#import ALookAtTheDataSolns as s # I guess notebooks that call these functions?

def display_gif(fn):
    return '<img src="{}">'.format(fn)



def datasummary(data):
    print("Dataset Shape:",data.shape)
    summary=data.describe(include='all', datetime_is_numeric=True).transpose()
    summary.insert(0,'dtypes',data.dtypes)
    summary.insert(3, 'missing', data.isnull().sum().values)
    #df.insert(2, 'new-col', data)
    summary['First Value'] = data.loc[0].values
    return summary

def missingsummary(data,column_of_interest):
    missing_cols=[]
    for col in data.columns:
        if data[col].isnull().any():
            missing_cols.append(col)
    msummary=pd.DataFrame(index=data[column_of_interest].unique())
    for mis_col in missing_cols:
        msummary[mis_col]=data.loc[data[mis_col].isnull()][column_of_interest].value_counts()
    msummary.replace(np.nan,' ', inplace=True)
    return msummary

def datetomonthyear(dateseries): ####BORRAR?
    newdataseries = dateseries.dt.to_period('M')
    return newdataseries


def plot_dist(values, log_values, title, color="#D84E30"):
    fig, axis = plt.subplots(1, 2, figsize=(12,4))
    axis[0].set_title("{} - linear scale".format(title))
    axis[1].set_title("{} - logn scale".format(title))
    ax1 = sns.distplot(values, color=color, ax=axis[0])
    ax2 = sns.distplot(log_values, color=color, ax=axis[1])
    
    
def tukey_rule(data_frame, column_name):
    """Returns Dataframe with values in the IQR"""
    data = data_frame[column_name]
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    max_value = Q3 + 1.5 * IQR
    min_value = Q1 - 1.5 * IQR
    return data_frame[(data_frame[column_name] < max_value) & (data_frame[column_name] > min_value)]


def black_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")

def green_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(99,100%, 27%)")

def red_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(5,100%, 26%)")

def blue_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(243,100%, 38%)")





#def variabletype(data):
#    no_info= [c for c in list(data) if data[c].nunique() =1]] #no info columns
#    id_cols= [c for c in list(data) if data[c].nunique() == data.shape[0]] #columns with all unique values - no info, but id
#    cat_data = data.select_dtypes(include=['object'])# Subset to a dataframe only holding the categorical columns
#    cat_cols=cat_data.columns
#    num_data = data.select_dtypes(include=['float','int'])# Subset to a dataframe only holding the numerical columns
#    num_cols=num_data.columns
    
    #dollar_cols = ['price', 'weekly_price', 'monthly_price', 'extra_people', 'security_deposit', 'cleaning_fee']
    #for col in dollar_cols:
        #df[col] = df[col].replace('[\$,]', '', regex=True).astype(float) # Remove '$' and ',' from dollar columns
        # let's check if info in '_url' columns may provide any info
    #zip_cols=[col for col in data.columns if "_zip" in col] #zip columns if any
    #for col in zip_cols:
        #print(col+':'+ str(listings_df[col].isnull().sum()))
        #
    
#    return no_info, id_cols, cal_cols, num_cols