#!/usr/bin/env python3

class ScriptManager:
    def __init__(self,script_name,gui_args=None):
        self.script_name = script_name.lower()
        # gui_args is a dictionary containing arguments and values for script if the script is running from web interface
        self.gui_args = gui_args

    def run_script(self):
        if self.script_name == 'arp_spoof.py':
            if self.gui_args :
                from scripts.arp_spoof import run_from_gui
                run_from_gui(self.gui_args)
            else:
                from scripts.arp_spoof import main
                main()
        elif self.script_name == 'arp_ping.py':
            if self.gui_args :
                from scripts.arp_ping import run_from_gui
                run_from_gui(self.gui_args)
            else:
                from scripts.arp_ping import main
                main()
        elif self.script_name == 'icmp_ping.py':
            if self.gui_args :
                from scripts.icmp_ping import run_from_gui
                run_from_gui(self.gui_args)
            else:
                from scripts.icmp_ping import main
                main()
        elif self.script_name == 'syn_flood.py':
            if self.gui_args :
                from scripts.syn_flood import run_from_gui
                run_from_gui(self.gui_args)
            else:
                from scripts.syn_flood import main
                main()
        elif self.script_name == 'tcp_ps_syn.py':
            if self.gui_args :
                from scripts.tcp_ps_syn import run_from_gui
                run_from_gui(self.gui_args)
            else:
                from scripts.tcp_ps_syn import main
                main()
        elif self.script_name == 'tcp_ps_ack.py':
            if self.gui_args :
                from scripts.tcp_ps_ack import run_from_gui
                run_from_gui(self.gui_args)
            else:
                from scripts.tcp_ps_ack import main
                main()
        else:
            print('error : invalid script name [-h for help] [--show-scripts to show scripts names]')