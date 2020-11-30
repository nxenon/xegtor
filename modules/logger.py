#!/usr/bin/env python3

'''
script for managing logs
'''

import logging
import datetime

class Logger:
    def __init__(self ,log_file ,filemode='a'):
        self.log_file = log_file
        self.filemode = filemode
        logging.basicConfig(filename=self.log_file ,filemode=self.filemode ,format='%(message)s')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    def log(self ,message):
        try:
            self.logger.info(message)
        except:
            pass

    def add_log_header(self ,log_name=None):
        header = '''
*--------------------------------*
                 _
 __  _____  ____| |_ ___  ____
 \ \/ / _ \/ _` | __/ _ \| '__|
  >  <  __/ (_| | || (_) | |
 /_/\_\___|\__, |\__\___/|_|
           |___/
           
This file contains xegtor attacks and scanning logs
*--------------------------------*
        '''
        if log_name :
            header += ' ({})'.format(log_name)
        self.log(header)

    def add_script_name(self ,script_name):
        msg = 'Script : ' + script_name
        self.log(msg)

    def add_log_delimiter(self):
        delimiter = '\n*--------------------------------*\n'
        self.log(delimiter)

    def add_time(self):
        time_now = datetime.datetime.now()  # time in log
        time_now_formatted = time_now.strftime('%Y-%m-%d %H:%M:%S')
        time = 'time : ' + time_now_formatted
        self.log(time)

    def add_log_path(self):
        msg = 'Log Path : ' + self.log_file
        self.log(msg)

    def check_logs(self):
        from main.design.log_manager import LogManager
        log_manager = LogManager()
        log_manager.overall_check()