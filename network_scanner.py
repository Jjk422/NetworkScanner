import argparse
import socket
import threading
import re

# Function Definitions


def scan_port(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip_address, port))

        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port: {port}: Closed")
        sock.close()

    except KeyboardInterrupt:
        print("Ctrl+C pressed exiting program")
        exit(0)

    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        exit(0)

    except socket.error:
        print("Couldn't connect to server")
        exit(0)


def get_ips_from_comma_sep_string(comma_seperated_ips_string):
    return comma_seperated_ips_string.split(',')


def get_ports_from_comma_sep_string(comma_seperated_ports_string):
    return comma_seperated_ports_string.split(',')


def scan_ip_address_ports(ip_address, ports):
    print(f"Testing ports for {socket.gethostbyname(ip_address)}")
    for port in ports:
        scan_port(socket.gethostbyname(ip_address), int(port))

help_banner = "Welcome to NetScan, a simple network scanner."

parser = argparse.ArgumentParser(description=help_banner)
parser.add_argument('--ips', help='IP address of the machine to scan.', nargs='+', required=True)
parser.add_argument('--ports', help='Port number to connect to.', nargs='+', required=True)
parser.add_argument('--connection-type', help='Connection protocol to use, e.g. ICMP, TCP, UDP, HTTP.')

args = parser.parse_args()

# Create a raw ICMP socket
# socket_icmp = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))
socket_icmp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp_ip = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ip_address = socket.gethostbyname(args.ip_address)
# port = args.ports

# for port in range(1, 1025):
#     scan_port('192.168.1.1', port)

ip_addresses = []
ports = []

for ip_address in args.ips:
    # if "-" in ip_address:
    #     ip_address.split("-")
    #     scan_ip_address_ports(ip_address, args.ports)
    #
    # else:
        scan_ip_address_ports(ip_address, args.ports)