from general_funcs import Modelplus
    
class MP_RF(Modelplus):
    def __init__(s,kwargs_sj=None,kwargs_iq=None):
        from sklearn.ensemble import RandomForestRegressor
        s.model_sj = RandomForestRegressor(**kwargs_sj)
        s.model_iq = RandomForestRegressor(**kwargs_iq)
        return
        
class MP_NN(Modelplus):
    def __init__(s,kwargs_sj=None,kwargs_iq=None):
        from sklearn.neural_network import MLPRegressor
        s.model_sj = MLPRegressor(**kwargs_sj)
        s.model_iq = MLPRegressor(**kwargs_iq)
        return
        
    def fit(s,data):
        'Overwrite fit if necessary'
        pass
    