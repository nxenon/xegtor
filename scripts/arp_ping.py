#!/usr/bin/env python3

'''
this script is for network hosts scanning --> ARP scan
'''

from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.l2 import ARP
from argparse import ArgumentParser

class ArpPing:
    def __init__(self ,ip_range ,timeout):
        self.ip_range = ip_range
        try:
            self.timeout = float(timeout)
        except ValueError :
            print()
            print('error : timeout must be float or integer e.g 3.5 [--script-help or -sh for help]')
            exit()

    def start(self):
        self.check_range()
        self.run_arp_ping()

    def check_range(self):
        range_parts = self.ip_range.split('/')
        if (len(range_parts) == 2):
            pass
        else:
            print('Invalid Range : e.g. 192.168.1.0/24 [--script-help or -sh for help]')
            exit()

    def run_arp_ping(self):
        dest = 'ff:ff:ff:ff:ff:ff'
        print('Scanning... --> timeout : ' + str(self.timeout) + ' secs')
        ans, unans = srp(Ether(dst=dest) / ARP(pdst=self.ip_range), timeout=self.timeout,verbose=1)
        ans.summary(lambda s_r: s_r[1].sprintf("IP : %ARP.psrc% ,Mac : %Ether.src%"))

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