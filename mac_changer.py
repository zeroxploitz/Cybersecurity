#!/usrs/bin/env python
import subprocess

from pip._vendor.distlib.compat import raw_input

interface = raw_input("interface >")
new_mac = raw_input("new MAC >")

print("[+] Changing Mac address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
