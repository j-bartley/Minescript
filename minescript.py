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

count = 0

for x in servers:
    print(str(x) + '. ' + servers[x]['name'])
    count = count + 1

print('\n')
choice = input("Selection Number: ")

#Make a function to make this variable use.
if choice >= 0 and choice <= count:
    print("Selected " + servers[choice]['name'] + " to load.")
    print("Switching to directory " + servers[choice]['loc'] + " to load.")
    os.system("konsole -e 'bash -c \"sudo sh " + servers[choice]['loc'] + "ServerStart.sh" + "; exec bash\"'")


#choose server
#check java version
#--fix java version if not working
#start server
