import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'So secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql://fvbymlxs:40n2_e8Kk5vnnaap3h4LFXVKPaQCCW14@batyr.db.elephantsql.com/fvbymlxs'
    
