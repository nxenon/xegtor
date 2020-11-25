#!/usr/bin/env python3

class ScriptManager:
    def __init__(self,script_name):
        self.script_name = script_name

    def run_script(self):
        if self.script_name == 'arp_spoof.py':
            import scripts.arp_spoof
        elif self.script_name == 'arp_ping.py':
            import scripts.arp_ping
        elif self.script_name == 'icmp_ping.py':
            import scripts.icmp_ping
        elif self.script_name == 'syn_flood.py':
            import scripts.syn_flood
        elif self.script_name == 'tcp_ps_syn.py':
            import scripts.tcp_ps_syn
        elif self.script_name == 'tcp_ps_ack.py':
            import scripts.tcp_ps_ack
        else:
            print('error : invalid script name [-h for help] [--show-scripts to show scripts names]')