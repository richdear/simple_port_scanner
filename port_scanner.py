import socket
import termcolor


def scan(ip, port):
    try:
        sock = socket.socket()
        sock.connect((ip, int(port)))
        print(termcolor.colored(("[+] OPEN: {port}".format(port=port)),"red"))
        sock.close()
    except Exception as e:
        print("[-] CLOSED: {port}".format(port=port))
        sock.close()
        # print("[-] Exception {exception}".format(str(e)))


ips = input("Enter targets (sep: ,):")
ports = input("Enter ports:")
ips = ips.split(",")
for ip in ips:
    print("-----------------------------------")
    print(termcolor.colored(("[*] Scanning {ip}".format(ip=ip)),"green"))
    print("-----------------------------------")
    for port in range(1, int(ports)):
        scan(ip, port)
    print("-----------------------------------")
    print("\n\r")
