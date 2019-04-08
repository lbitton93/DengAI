'''

Fitting to different data types, is this done in Modelplus, or MP_xx? 

'''

import numpy as np
import pandas as pd
import os

class Data:
    '''
    General data class for ML analysis of dengue fever.
    Note, all functions are in-place. To create a new copy
    of a class instance, use deepcopy(class_instance).
    
    Functions that begin with an underscore are internal
    functions, and are typically designed to be called by other
    class functions, not by the runtime user.
    '''
    def __init__(s,directory=None):
        if type(directory) != type(None):
            s.read_data(directory)
        s.cities = ['sj','iq']
        return
    
    def read_data(s,directory):
        s.df      = pd.read_csv(os.path.join(directory,'dengue_features_train.csv'))
        s.y_tr    = pd.read_csv(os.path.join(directory,'dengue_labels_train.csv'))
        s.df_valid = pd.read_csv(os.path.join(directory,'dengue_features_test.csv'))
        
        s.df['total_cases'] = s.y_tr['total_cases'] / 1
        del(s.y_tr)
        
        s.df['time'] = s.df.index
        s.df.loc[(s.df['city']=='iq'), 'time'] -= s.df[s.df['city']=='iq'].index.min()
        
        s.df['cat_cases'] = 0
        s.df.loc[(s.df['total_cases']>10),'cat_cases']=1
        s.df.loc[(s.df['total_cases']>40),'cat_cases']=2
        
        s.df.fillna(method='ffill')
        return
        
    def df_to_arr(s):
        # Extra columns to drop. Maybe make this a transform.
        extraDrop = [
        #'reanalysis_avg_temp_k',
        #'reanalysis_max_air_temp_k'
        ]
        
        # To avoid having 2 copies of every array for the two cities,
        # I have made all relevant arrays into lists of two arrays.
        # e.g. s.X_train_full[0] is the full train matrix for SJ, and
        # s.X_train_full[1] is for IQ.
        
        s.X_train_full = []
        s.y_train_full = []
        
        s.X_train = []
        s.y_train = []
        
        s.X_test  = []
        s.y_test  = []
        
        s.X_valid = []
        
        for i_city,city in enumerate(s.cities):
            s.dfC = s.df[s.df['city']==city]
            s.dfC_valid = s.df_valid[s.df_valid['city']==city]
            
            for col in ['year','week_start_date','cat_cases','time']+extraDrop:
                if col in list(df):
                    s.dfC = s.dfC.drop(columns=[col]).reset_index(drop=1)
                    s.dfC_valid = s.dfC_valid.drop(columns=[col]).reset_index(drop=1)
            
            s.y_train_full = df['total_cases'].values
            dfC = dfC.drop(columns=['city'])
            dfC_valid = dfC_valid.drop(columns=['city'])
            s.X_train_full = dfC.values
            s.X_valid = dfC_valid.values
        return
    
    def split_data(s, tr_frac=0.7, randomise=False, seed=None):
        train_cut = int(len(s.X_train_full)*tr_frac)
        
        if randomise:
            pass
        
        for i_city in enumerate(s.cities):
            s.X_train[i_city] = s.X_train_full[i_city][:train_cut]
            s.y_train[i_city] = s.y_train_full[i_city][:train_cut]
            
            s.X_test[i_city] = s.X_train_full[i_city][train_cut:]
            s.y_test[i_city] = s.y_train_full[i_city][train_cut:]
        return 
        
    def transform(s, trans_list, kwargs_list=None, _direction='for'):
        if type(trans_list)!=type([]):
            trans_list = [trans_list]
        if type(kwargs_list)!=type([]):
            kwargs_list = [kwargs_list]
            
        if type(kwargs_list)!=type(None) and len(kwargs_list)!=len(trans_list):
            print('Error in options list')
            raise 
            
        for trans,kwargs in zip(trans_list,kwargs_list):
            trans(s,_direction,**kwargs)
        return 
    
    def inverse_transform(s, trans_list, kwargs_list):
        s.transform(trans_list[::-1], kwargs_list[::-1], _direction='inv')
        return 

class Modelplus:
    def __init__(s,model_sj=None,model_sj=None):
        if type(model)==type(None:)
            print('''
            Overwrite this function with the child class. Or, 
            call Modelplus with an argument of a model.
            Child class's __init__ must create an attribute 
            called s.model, typically by calling an 
            sklearn or keras model. However, these may also be 
            custom-defined.
            ''')
        else:
            s.model_sj = model_sj
            s.model_sj = model_sj
        return
    
    def fit(s,dataclass):
        '''
        Fit to both SJ and IQ.
        '''
        pass
    
    def predict_test(s,dataclass):
        pass
    
    def predict_val(s,dataclass):
        pass
    
    def val_to_file(s,dataclass):
        pass
    
    def plotting_funcs(s,dataclass):
        pass
    
def ensemble_fit(data,model_list):
    pass

def hyperparam_fit(data,model_list):
    pass
