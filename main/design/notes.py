#!/usr/bin/env python3

note_1 = '''***You have to run this script with root privileges***'''
note_2 = '''***You should have enabled ip forwarding on your machine***'''

notes = note_1 + '\n' + note_2

def print_notes():
    print(notes)
