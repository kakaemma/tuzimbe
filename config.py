class MainConfiguration(object):
    """ Parent configuration class"""
    DEBUG = False
    LEVEL = DEBUG
    CSRF_ENABLED = True

class DevelopmentEnvironment(MainConfiguration):
    """ Development configuration

    Args:
        MainConfiguration
    """    
    DEBUG = True

class TestingEnvironment(MainConfiguration):
    """_TestingConfiguration_

    Args:
        MainConfiguration
    """    
    DEBUG = True
    TESTING = True

class StagingEnvironment(MainConfiguration):
    """_StagingConfiguration_

    Args:
        MainConfiguration
    """    
    DEBUG = True

class ProductionEnvironment(MainConfiguration):
    """_ProductionConfiguration_

    Args:
        MainConfiguration
    """    
    DEBUG = False
    TESTING = False

application_config = {
    'MainConfig':MainConfiguration,
    'TestingEnv':TestingEnvironment,
    'DevelopmentEnv':DevelopmentEnvironment,
    'ProductionEnv':ProductionEnvironment
}
