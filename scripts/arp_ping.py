#!/usr/bin/env python3

'''
this script is for network hosts scanning --> ARP scan
'''

from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.l2 import ARP
from argparse import ArgumentParser
from modules.logger import Logger
from os.path import isfile

logs_dir = 'logs/'
SCRIPT_NAME = 'arp_ping.py'
log_file_name = 'arp_ping_py.log'
log_file_path = logs_dir + log_file_name

if isfile(log_file_path) :
    logger = Logger(log_file=log_file_path, filemode='a')
else:
    logger = Logger(log_file=log_file_path, filemode='w')
    logger.add_log_header(script_name=SCRIPT_NAME)

class ArpPing:
    def __init__(self ,ip_range ,timeout):
        self.ip_range = ip_range
        try:
            self.timeout = float(timeout)
        except ValueError :
            error_msg = 'error : timeout must be float or integer e.g 3.5 [--script-help or -sh for help]'
            print()
            logger.log(error_msg)
            exit()

    def start(self):
        logger.add_log_delimiter()
        logger.add_log_path()
        logger.add_script_name('arp_ping.py')
        logger.add_time()
        self.check_range()
        self.run_arp_ping()

    def check_range(self):
        range_parts = self.ip_range.split('/')
        if (len(range_parts) == 2):
            pass
        else:
            error_msg = 'Invalid Range : e.g. 192.168.1.0/24 [--script-help or -sh for help]'
            logger.log(error_msg)
            exit()

    def run_arp_ping(self):
        dest = 'ff:ff:ff:ff:ff:ff'
        header = 'Scanning... --> timeout : ' + str(self.timeout) + ' secs'
        logger.log(header)
        ans, unans = srp(Ether(dst=dest) / ARP(pdst=self.ip_range), timeout=self.timeout,verbose=1)
        for a in ans:
            answer = 'IP : ' + a[1].psrc + ' ,Mac : ' + a[1].hwsrc
            logger.log(answer)

    def __del__(self):
        # when scan is finished add a log delimiter into log file
        logger.add_log_delimiter()

def run_from_gui(argument_values):
    arp_ping = ArpPing(ip_range=argument_values['range'] ,timeout=argument_values['timeout'])
    arp_ping.start()

def print_parser_help():
    help_text = '''
optional arguments:
  --script-help, -sh  Show Script Help
  --range x.x.x.x/yy  Range To Scan *
  --timeout default 3.5 secs  Time Out For Scan
    '''
    print(help_text)

def main():
    parser = ArgumentParser(usage='sudo python3 %(prog)s --script arp_ping.py [--script-help or -sh for help] [--range network_range] [--timeout secs]',allow_abbrev=False)
    parser.add_argument('--script-help','-sh',help='Show Script Help',action='store_true',)
    parser.add_argument('--range',help='Range To Scan',metavar='x.x.x.x/yy')
    parser.add_argument('--timeout',help='Time Out For Scan',metavar='default : 3.5 secs',default=3.5)
    args ,unknown = parser.parse_known_args()

    if ((args.script_help is not None) and (args.script_help is True)):
        print_parser_help()

    if (args.range != None):
        pass
    else:
        parser.print_usage()
        exit()

    arp_ping = ArpPing(args.range,args.timeout)
    arp_ping.start()