#!/usr/bin/env python3

from main.design.arg_options import parse_args
from main.design.notes import print_notes

from colorama import Fore

# Version
app_version = 'Beta'
version_text = '{version : ' + app_version + '}'
# Link to github
github_link = 'https://github.com/xenon-xenon/xegtor'

line_1 = '                 _             '
line_2 = Fore.RED + ' __  __' + Fore.RESET + '___  ' + Fore.RED + '____' + Fore.RESET + '| |_ ___  ____ '
line_3 = Fore.RED + ' \ \/ /' + Fore.RESET + ' _ \\' + Fore.RED + '/ _` ' + Fore.RESET + '| __/ _ \| \'__|' + '       ' + Fore.LIGHTBLUE_EX + version_text + Fore.RESET
line_4 = Fore.RED + '  >  <' + Fore.RESET + '  __' + Fore.RED + '/ (_| ' + Fore.RESET + '| || (_) | |   '
line_5 = Fore.RED + ' /_/\_\\' + Fore.RESET + '___|' + Fore.RED + '\__, ' + Fore.RESET + '|\__\___/|_|   ' + '       ' + Fore.LIGHTCYAN_EX + github_link + Fore.RESET
line_6 = Fore.RED + '           |___/               ' + Fore.RESET

banner_logo = line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + "\n" + line_5 + "\n" + line_6

def print_banner():
    print(banner_logo)
    print_notes()
    parse_args()