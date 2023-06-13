class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    
    OPENAI_KEY ='OPEN_AI_KEY'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
