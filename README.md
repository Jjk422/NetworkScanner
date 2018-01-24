# NetworkScanner
A simple network (IP/Port) scanner written in Python.

This program aims to be a simple Python port scanner that allows for network scanning.

## Prerequisites
Install Python 3 from https://www.python.org/downloads/

## Main Commands
Displays help:  
*python --help*

Scans the ip address 192.168.1.1 on port 80:  
*python --ips 192.168.1.1 --ports 80*

Scans the IP addresses 127.0.0.1 and 192.168.1.1 on ports 80 and 8080:  
*python --ips 127.0.0.1 192.168.1.1 --ports 80 8080*