#!/usr/bin/env python3

class ScriptManager:
    def __init__(self,script_name):
        self.script_name = script_name

    def run_script(self):
        if self.script_name == 'arp_spoof.py':
            from scripts.arp_spoof import main
            main()
        elif self.script_name == 'arp_ping.py':
            from scripts.arp_ping import main
            main()
        elif self.script_name == 'icmp_ping.py':
            from scripts.icmp_ping import main
            main()
        elif self.script_name == 'syn_flood.py':
            from scripts.syn_flood import main
            main()
        elif self.script_name == 'tcp_ps_syn.py':
            from scripts.tcp_ps_syn import main
            main()
        elif self.script_name == 'tcp_ps_ack.py':
            from scripts.tcp_ps_ack import main
            main()
        else:
            print('error : invalid script name [-h for help] [--show-scripts to show scripts names]')