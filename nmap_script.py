#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome to Simple Nmap Scan Tool.")
print("-----------------------------------------------")

ip_addr = input("Please enter the IP Address to Scan:")
print("The IP entered is:", ip_addr)
 # Check the type of ip_addr
print("Type of ip_addr:", type(ip_addr))

resp = input("""\nPlease Enter the Type of Scan you Need:
   1. SYN Scan
   2. UDP Scan
   3. Comprehensive Scan\n""")

print("You have Selected:", resp)

resp_dict = {'1': ['-sV -sS -vv', 'tcp'], '2': ['-sV -sU -vv', 'udp'], '3': ['-sV -sS -vv -0 -A -sC', 'tcp']}

if resp not in resp_dict.keys():
    print("Please Enter a Valid Option.")
else:
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, "1-1024", resp_dict[resp][0])

    if scanner[ip_addr].state() == 'up':
        print("\nHost is up, scanning results:")

        for proto in scanner[ip_addr].all_protocols():
            print("\nProtocol : {}". format(proto))
            print("Open Ports : {}".format(', '.join(map(str, scanner[ip_addr][proto].keys()))))

            for port, info in scanner[ip_addr][proto].items():
                print("\nPort : {}\nservice : {}\nstate : {}".format(port, info['name'], info['state']))