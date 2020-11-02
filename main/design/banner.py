#!/usr/bin/env python3

from colorama import Fore
from random import randint

# Version
app_version = 'Beta'
version_text = '{version : ' + app_version + '}'
# Link to github
github_link = 'https://github.com/xenon-xenon/xegtor'

color_list = [Fore.RED,Fore.CYAN,Fore.YELLOW,Fore.GREEN,Fore.LIGHTRED_EX,Fore.LIGHTYELLOW_EX,Fore.MAGENTA]
random_color = color_list[randint(0,len(color_list)-1)]

line_1 = '                 _             '
line_2 = random_color + ' __  __' + Fore.RESET + '___  ' + random_color + '____' + Fore.RESET + '| |_ ___  ____ '
line_3 = random_color + ' \ \/ /' + Fore.RESET + ' _ \\' + random_color + '/ _` ' + Fore.RESET + '| __/ _ \| \'__|' + '       ' + Fore.LIGHTBLUE_EX + version_text + Fore.RESET
line_4 = random_color + '  >  <' + Fore.RESET + '  __' + random_color + '/ (_| ' + Fore.RESET + '| || (_) | |   '
line_5 = random_color + ' /_/\_\\' + Fore.RESET + '___|' + random_color + '\__, ' + Fore.RESET + '|\__\___/|_|   ' + '       ' + Fore.LIGHTCYAN_EX + github_link + Fore.RESET
line_6 = random_color + '           |___/               ' + Fore.RESET

banner_logo = line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + "\n" + line_5 + "\n" + line_6

def print_banner():
    print(banner_logo)