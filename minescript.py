#Must install modules:
#   sudo apt install python-pip
#   pip install pyyaml
#   pip install pyfiglet

import yaml
import sys
import os
from pyfiglet import Figlet

f = Figlet(font='slant')
print f.renderText('Minescript')

with open("servers.yaml", 'r') as stream:
    try:
        servers = yaml.safe_load(stream)
        print("Loading Servers...")
    except yaml.YAMLError as exc:
        print("Servers failed to load with error: ")
        print(exc)

print("Servers loaded." + '\n')
print("Which server would you like to use?" + '\n')

for x in servers:
    print(str(x) + '. ' + servers[x]['name'])

print('\n')
choice = input("Selection Number: ")

#Make a function to make this variable use.
if choice == 1:
    print("Selected " + servers[1]['name'] + " to load.")
