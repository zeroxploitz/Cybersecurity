#!/usrs/bin/env python
import subprocess

interface = "wlan0"
new_mac = "00:11:22:33:44:77"

print("[+] Changing Mac address for " + interface + " to " + new_mac)

subprocess.call("sudo ifconfig " + interface + " down ", shell=True)
subprocess.call("sudo ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("sudo ifconfig " + interface + " up ", shell=True)
