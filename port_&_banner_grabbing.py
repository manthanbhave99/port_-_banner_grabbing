#!/usr/bin/python3
__author__ = "Manthan & Omprakash aka ManthanOP"

import socket, argparse

parser = argparse.ArgumentParser(description="Alive or not Tool")
parser.add_argument("-host", type=str, help="Resolve DNS", required=True)
parser.add_argument("-port", type=str, help="output to some file", required=True)

b = parser.parse_args()

s = socket.socket()

if b.port:
    print(port)
    def scan():
        try:
            s.connect((b.host, int(port)))
            return True
        except:
            return False
        
        if scan():
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is close")

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((b.host, int(port)))
            e = sock.recv(4096)
            print("Output: ", e)
        except:
            pass
        finally:
            sock.close


if "-" in b.port:
    port_r1 = int(b.port.split("-")[0])
    port_r2 = int(b.port.split("-")[1])
    for port in range(port_r1, port_r2+1):
        print(port)
        def scan():
            try:
                s.connect((b.host, int(port)))
                return True
            except:
                return False

        if scan():
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is close")

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((b.host, int(port)))
            e = sock.recv(4096)
            print("Output: ", e)
        except:
            pass
        finally:
            sock.close


elif "," in b.port:


    for port in b.port.split(","):
        print(port)
        def scan():
            try:
                s.connect((b.host, int(port)))
                return True
            except:
                return False

        if scan():
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is close")

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((b.host, int(port)))
            e = sock.recv(4096)
            print("Output: ", e)
        except:
            pass
        finally:
            sock.close

