class Data:
    def __init__(s,df):
        s.df = df
    
    def read_data(s,data):
        pass
    
    def split_data(s, df, tr_frac, randomise=False, seed=None):
        s.sj_X_train = 1
        s.sj_y_train = 1
        s.sj_X_test = 1
        s.sj_y_test = 1
    
        s.iq_X_train = 1
        s.iq_y_train = 1
        s.iq_X_test = 1
        s.iq_y_test = 1
        
        s.validation = 1 pass
        
    def transform(s, trans_list):
        '''
        trans 
        '''
        pass
        
    def set_model():
        pass
    
    def inverse_transform(s, trans_list):
        for trans in trans_list:
            data = trans(data,'inv')            
            
    def ensemble_fit(model_Luke_NN1, model_Scott_RF1):
        pass
            
class Modelplus:
    def fit(s,dataclass):
        pass
    
    def predict_test(s,dataclass):
        pass
    
    def predict_val(s,dataclass):
        pass
    