#!/usr/bin/env python
import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")

parser.parse_args()

interface = input("interface >")
new_mac = input("new MAC >")

print("[+] Changing Mac address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
