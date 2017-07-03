__author__ = 'sunny.yu2'
from Configs.Config import Config
import os

class AccountManage:
    config = Config.get_instance()
    userName = ''
    password = ''
    url=''

    def __init__(self,environment='qa'):
     if(environment=='qa'):
       cf = self.load_config_file()
     else:
       cf = self.load_staging_config_file()
     AccountManage.userName = cf.get("configuration", "username")
     AccountManage.password = cf.get("configuration", "password")
     AccountManage.url=cf.get("configuration", "url")

    def load_config_file(self):
       config_file = self.get_relative_path("Configs", "Configs.ini")
       self.config.read(config_file)
       return self.config

    def load_staging_config_file(self):
        config_file = self.get_relative_path("Configs", "Configs_staging.ini")
        self.config.read(config_file)
        return self.config

    def get_relative_path(self, path, file_name):
        prepath = os.getcwd()
        return os.path.join(prepath, path, file_name)