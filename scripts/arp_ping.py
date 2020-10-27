#!/usr/bin/env python3

'''
this script is for network hosts scanning --> ARP scan
'''

from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.l2 import ARP
from argparse import ArgumentParser

class ArpPing:
    def __init__(self, ip_range):
        self.ip_range = ip_range

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
        print('Scanning....')
        ans, unans = srp(Ether(dst=dest) / ARP(pdst=self.ip_range), timeout=3.5,verbose=0)
        ans.summary(lambda s,r: r.sprintf("IP : %ARP.psrc% ,Mac : %Ether.src%"))


def print_parser_help():
    help_text = '''
optional arguments:
  --script-help, -sh  Show Script Help
  --range x.x.x.x/yy  Range To Scan
    '''
    print(help_text)


parser = ArgumentParser(usage='sudo python3 %(prog)s --script arp_ping.py [--script-help or -sh for help] [--range network_range]',allow_abbrev=False)
parser.add_argument('--script-help','-sh',help='Show Script Help',action='store_true',)
parser.add_argument('--range',help='Range To Scan',metavar='x.x.x.x/yy')
args ,unknown = parser.parse_known_args()

if ((args.script_help is not None) and (args.script_help is True)):
    print_parser_help()

if (args.range != None):
    pass
else:
    parser.print_usage()
    exit()

arp_ping = ArpPing(args.range)
arp_ping.start()