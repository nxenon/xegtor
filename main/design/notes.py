#!/usr/bin/env python3

from colorama import Fore

note_1 = Fore.RED + '*** ' + Fore.RESET + 'You have to run this script with root privileges' + Fore.RED + ' ***' + Fore.RESET
note_2 = Fore.RED + '*** ' + Fore.RESET + 'You should have enabled ip forwarding on your machine (for MITM attacks)' + Fore.RED + ' ***' + Fore.RESET

notes = note_1 + '\n' + note_2

def print_notes():
    print(notes)
