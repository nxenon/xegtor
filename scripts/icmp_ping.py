#!/usr/bin/env python3

'''
this script is for network hosts scanning --> ICMP ping scan
'''

from argparse import ArgumentParser
from threading import Thread
import subprocess
from modules.logger import Logger
from os.path import isfile

logs_dir = 'logs/'
SCRIPT_NAME = 'icmp_ping.py'
log_file_name = 'icmp_ping_py.log'
log_file_path = logs_dir + log_file_name

if isfile(log_file_path) :
    logger = Logger(log_file=log_file_path, filemode='a')
else:
    logger = Logger(log_file=log_file_path, filemode='w')
    logger.add_log_header(script_name=SCRIPT_NAME)

class IcmpPingScan():

    def __init__(self ,ip_range):
        self.ip_range = ip_range
        self.check_os()

    def start(self):
        logger.add_log_delimiter()
        logger.add_log_path()
        logger.add_script_name('icmp_ping.py')
        logger.add_time()

        scanning_msg = 'scanning...'
        print(scanning_msg)
        logger.log(scanning_msg)

        self.get_ip_list()
        self.sys_os = self.check_os()
        if self.sys_os == 'windows':
            self.count_param = '-n'
        elif self.sys_os == 'linux':
            self.count_param = '-c'

        self.start_ping_scan()

    def get_ip_list(self):
        # get ip range list from ip_range argument
        from modules.ip_range_list import ip_list_generator
        self.IPs_list = ip_list_generator(self.ip_range)

    def check_os(self):
        from modules.check_os import what_is_os
        return what_is_os()

    def start_ping_scan(self):
        for ip in self.IPs_list :
            Thread(target=self.ping,args=(ip,)).start()

    def ping(self,ip):
        # count_param is (-c or -n) based on os
        error_code = subprocess.run(['ping',self.count_param,'1',str(ip)],stdout=subprocess.DEVNULL).returncode
        if error_code == 0 :
            host_is_up_msg = '[+] host ' + str(ip) + ' is up'
            print(host_is_up_msg)
            logger.log(host_is_up_msg)

    def __del__(self):
        # when scan is finished add a log delimiter into log file
        logger.add_log_delimiter()

def run_from_gui(argument_values):
    scan = IcmpPingScan(ip_range=argument_values['range'])
    scan.start()

def print_parser_help():
    help_text = '''
optional arguments:
  --script-help, -sh  Show Script Help
  --range x.x.x.x/yy  Range To Scan *
    '''
    print(help_text)

def main():
    parser = ArgumentParser(usage='sudo python3 %(prog)s --script icmp_ping.py [--script-help or -sh for help] [--range network_range x.x.x.x/yy]',allow_abbrev=False)
    parser.add_argument('--script-help', '-sh', help='Show Script Help', action='store_true')
    parser.add_argument('--range', help='Range To Scan', metavar='x.x.x.x/yy')
    args, unknown = parser.parse_known_args()

    if ((args.script_help is not None) and (args.script_help is True)):
        print_parser_help()

    if (args.range != None):
        pass
    else:
        parser.print_usage()
        exit()

    scan = IcmpPingScan(args.range)
    scan.start()