#!/usr/bin/env python3

'''
this script generates ip range list
'''

import ipaddress

def ip_list_generator(ip_range):
    try:
        ips_list = list(ipaddress.ip_network(ip_range).hosts())
    except:
        print('error : invalid ip range format : x.x.x.x/yy e.g 192.168.1.0/24 [--script-help or -sh for help]')
        exit()
    else:
        return ips_list