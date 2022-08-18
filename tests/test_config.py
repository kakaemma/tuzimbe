from api.tuzimbe import app
from flask_testing import TestCase
import unittest


class TestDevelopmentEnvironmenr(TestCase):
    def create_app(self):
        app.config.from_object('instance.config.DevelopmentEnvironment')
        return app
    
    def test_app_in_development_enc(self):
        self.assertTrue (app.config['DEBUG'])
        
class TestTestingEnv(TestCase):
    def create_app(self):
        app.config.from_object('instance.config.TestingEnvironment')
        return app
    
    def test_app_in_testing_env(self):
        self.assertTrue(['DEBUG'])
        self.assertTrue(['TESTING'])
        
class TestStagingEnv(TestCase):
    def create_app(self):
        app.config.from_object('instance.config.StagingEnvironment')
        return app
    
    def test_app_in_staging_env(self):
        self.assertTrue(['DEBUG'])
        self.assertTrue(['TESTING'])
        