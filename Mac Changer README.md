Mac Changer changes the mac address and outputs the results

h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interface to change its Mac address
  -m NEW_MAC, --mac=NEW_MAC
                        New Mac address

example: 
root:
python mac_changer.py -i lo  -m 00:11:22:33:44:33
non-root user:
sudo python mac_changer.py -i lo  -m 00:11:22:33:44:33


