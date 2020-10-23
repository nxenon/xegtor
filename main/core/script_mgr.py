#!/usr/bin/env python3

class ScriptManager:
    def __init__(self,script_name):
        self.script_name = script_name

    def run_script(self):
        if self.script_name == 'acp.py':
            import scripts.acp