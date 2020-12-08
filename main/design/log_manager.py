#!/usr/bin/env python3

'''
this script is for managing logs folder and files (checking existence ,creation)
'''

from os.path import isdir,isfile
from os import mkdir
from modules.logger import Logger

class LogManager:
    def __init__(self ,log_name=None ,script_name=None):
        self.log_name = log_name
        self.logs_dir_path = 'logs/'
        self.script_name = script_name

    def overall_check(self):
        # an overall check for logs
        self.check_logs_dir()
        self.check_main_log_file()

    def check_logs_dir(self):
        # check logs directory existence
        if not isdir(self.logs_dir_path):
            self.create_logs_directory()

    def create_logs_directory(self):
        mkdir('logs')

    def check_main_log_file(self):
        # check xegtor.log existence
        path = self.logs_dir_path + 'xegtor.log'
        if not isfile(path) :
            self.create_main_log_file()

    def create_main_log_file(self):
        path = self.logs_dir_path + 'xegtor.log'
        file = open(path ,'w')
        file.close()
        # create log header
        logger = Logger(log_file=path)
        logger.add_log_header()

    def check_log_file(self):
        # check specific log file existence
        path = self.logs_dir_path + self.log_name
        if not isfile(path) :
            self.create_log_file()

    def create_log_file(self):
        # create specific log file existence
        path = self.logs_dir_path + self.log_name
        file = open(path ,'w')
        file.close()