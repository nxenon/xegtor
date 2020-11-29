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

    def add_log_header(self ,log_name):
        header = '''
                 _
 __  _____  ____| |_ ___  ____
 \ \/ / _ \/ _` | __/ _ \| '__|
  >  <  __/ (_| | || (_) | |
 /_/\_\___|\__, |\__\___/|_|
           |___/
        '''
        self.log(header)

    def add_log_delimiter(self):
        delimiter = '\n*--------------------------------*\n'
        self.log(delimiter)

    def add_time(self):
        time_now = datetime.datetime.now()  # time in log
        time_now_formatted = time_now.strftime('%Y-%m-%d %H:%M:%S')
        time = 'time : ' + time_now_formatted
        self.log(time)