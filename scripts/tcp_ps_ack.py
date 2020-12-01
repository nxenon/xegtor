#!/usr/bin/env python3

'''
this script performs tcp port scan (ack method)
'''

from argparse import ArgumentParser
from threading import Thread
from time import sleep
from scapy.all import *
from scapy.layers.inet import *
from random import randint
from colorama import Fore
from modules.logger import Logger

log_file_path = 'logs/xegtor.log'
logger = Logger(log_file=log_file_path ,filemode='a')
logger.check_logs()

class TcpAckPortScanner:
    def __init__(self,target_ip,port,timeout):
        self.target_ip = target_ip
        self.port_argument = port
        try:
            self.timeout = float(timeout)
        except ValueError :
            error_msg = 'error : invalid timeout [e.g 0.1] [--script-help or -sh for help]'
            print(error_msg)
            logger.log(error_msg)
            exit()

    def start(self):
        logger.add_log_delimiter()
        logger.add_log_path()
        logger.add_script_name('tcp_ps_ack.py')
        logger.add_time()

        self.is_firewall = {'exists' : None ,'scan_is_finished' : False}
        self.ports_list = [] # ports which should be scanned

        target_header_msg = 'target : ' + self.target_ip
        print(target_header_msg)
        logger.log(target_header_msg)

        timeout_header_msg = 'timeout : ' + str(self.timeout)
        print(target_header_msg)
        logger.log(timeout_header_msg)

        self.check_port() # check port argument and adds ports in self.ports_list var
        self.open_ports_list = [] # a list that contains open ports
        self.get_random_ports() # get random port for source port
        for p in self.ports_list :
            try:
                t = Thread(target=self.scan_ack ,args=(p,))
                t.setDaemon(True)
                t.start()
            except KeyboardInterrupt :
                attack_stop_msg = 'Attack stopped !'
                print(attack_stop_msg)
                logger.log(attack_stop_msg)
                exit()

        sleep(self.timeout + 1)

        self.is_firewall['scan_is_finished'] = True # when scan is finished
        self.get_sf_firewall_state()

    def check_port(self):

        if ',' in self.port_argument: # for specific ports
            self.ports_to_check = self.port_argument.split(',')
            num = 0
            for p in self.ports_to_check :
                try:
                    int(p)
                except:
                    print()
                    error_msg = 'error : invalid port ---> e.g 80,22 or 1-65535 [--script-help or -sh for help]'
                    print(error_msg)
                    logger.log(error_msg)
                    exit()
                else:
                    if (num < 1):
                        print('ports : ',end='')
                        num += 1
                    self.ports_list.append(int(p))
                    print(p + ' ',end='')

            logger.log('ports : ' + str(self.ports_list))

        elif '-' in self.port_argument : # for ports range
            try :
                port_start = int(self.port_argument.split('-')[0])
                port_end = int(self.port_argument.split('-')[1])
            except :
                print()
                error_msg = 'error : invalid port ---> e.g 80,22 or 1-65535 [--script-help or -sh for help]'
                print(error_msg)
                logger.log(error_msg)
                exit()
            else:
                self.ports_list = list(range(port_start,port_end + 1))
                ports_range_msg = 'ports : ' + str(port_start) + ' to ' + str(port_end)
                print(ports_range_msg)
                logger.log(ports_range_msg)

        else: # for single port
            try :
                int(self.port_argument)
            except ValueError:
                print()
                error_msg = 'error : invalid port ---> e.g 80,22 or 1-65535 [--script-help or -sh for help]'
                print(error_msg)
                logger.log(error_msg)
                exit()
            else:
                self.ports_list.append(int(self.port_argument))
        print()

    def get_random_ports(self):
        all_ports = list(range(1024,65535))
        self.random_ports_list = []
        while (len(all_ports) != 0) :
            random_index_number = randint(0 ,len(all_ports) -1)
            port = all_ports.pop(random_index_number)
            self.random_ports_list.append(port)

    def scan_ack(self,port):
        random_sport = self.random_ports_list.pop(randint(0,len(self.random_ports_list) - 1))
        network_layer = IP(dst=self.target_ip)
        transport_layer = TCP(sport=random_sport ,dport=port ,flags='A')
        packet = network_layer / transport_layer
        ans = sr1(packet ,timeout=self.timeout ,verbose=0)
        if ans is not None :
            # print(ans.show())
            if ans.haslayer(TCP) :
                if ans[TCP].flags == 'R':
                    self.is_firewall['exists'] = False
                    if ans[TCP].window == 0: # RST flag and 0 window size ---> closed port
                        print(' [' + Fore.RED + '-' + Fore.RESET + '] Port ' + Fore.MAGENTA + str(port) + Fore.RESET +'/TCP is' + Fore.RED +  ' closed !\n' + Fore.RESET ,end='')
                        open_port_msg = '[-] Port ' + str(port) + '/TCP is closed !'
                        logger.log(open_port_msg)
                    elif ans[TCP].window > 0 : # RST flas and + window size ---> open port
                        print(' [' + Fore.GREEN + '+' + Fore.RESET + '] Port ' + Fore.MAGENTA + str(port) + Fore.RESET + '/TCP is' + Fore.GREEN + ' open !\n' + Fore.RESET ,end='')
                        open_port_msg = '[+] Port ' + str(port) + '/TCP is open !'
                        logger.log(open_port_msg)
                    else :
                        print(' [' + Fore.LIGHTWHITE_EX + '?' + Fore.RESET + '] Port ' + Fore.MAGENTA + str(port) + Fore.RESET + '/TCP is' + Fore.LIGHTWHITE_EX + ' unfiltered !\n' + Fore.RESET ,end='')
                        open_port_msg = '[?] Port ' + str(port) + '/TCP is unfiltered !'
                        logger.log(open_port_msg)

    def get_sf_firewall_state(self):
        # if stateful firewall exists print message
        if (self.is_firewall['exists'] is False) and (self.is_firewall['scan_is_finished'] == True) :
            stateful_firewall_existence_msg = ' there is no stateful firewall'
            print(Fore.GREEN + stateful_firewall_existence_msg + Fore.RESET)
            logger.log(stateful_firewall_existence_msg)
            
        elif (self.is_firewall['exists'] is not None) and (self.is_firewall['scan_is_finished'] == True) :
            stateful_firewall_existence_msg = 'maybe there is a stateful firewall'
            print(Fore.RED + stateful_firewall_existence_msg + Fore.RESET)
            logger.log(stateful_firewall_existence_msg)

    def __del__(self):
        # when scan is finished add a log delimiter into log file
        logger.add_log_delimiter()

def run_from_gui(argument_values):
    scanner = TcpAckPortScanner(target_ip=argument_values['target'] ,port=argument_values['port'] ,timeout=argument_values['timeout'])
    scanner.start()

def print_parser_help():
    help_text = '''
optional arguments:
  --script-help, -sh           Show Script Help
  --target                     Target To Attack *
  --port   x,y,z, x-z          Port Number(s) To Attack *
  --timeout default 1 sec    Timeout For Response
    '''
    print(help_text)

def main():
    parser = ArgumentParser(usage='sudo python3 %(prog)s --script tcp_ps_ack.py [--script-help or -sh for help] [--target TARGET] [--port PORT(S)] [--timeout sec (default 1 sec)]',allow_abbrev=False)
    parser.add_argument('--script-help', '-sh', help='Show Script Help', action='store_true')
    parser.add_argument('--target', help='Target To Attack', metavar='')
    parser.add_argument('--port','-p',help='Port Numbers To Attack', metavar='x,y,z')
    parser.add_argument('--timeout', help='Timeout For Response', metavar='default : 0.1 sec',default=1)
    args, unknown = parser.parse_known_args()

    if ((args.script_help is not None) and (args.script_help is True)):
        print_parser_help()

    if ((args.target != None) and (args.port != None)):
        pass
    else:
        parser.print_usage()
        exit()

    scanner = TcpAckPortScanner(target_ip=args.target,port=args.port,timeout=args.timeout)
    scanner.start()