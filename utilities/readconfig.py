import configparser
import os
from pathlib import Path

config=configparser.RawConfigParser()
config.read(r'/home/chinmayee/PycharmProjects/nopcommerce/Configuration/config.ini')



class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password