#!/usr/bin/python

import socket
import sys #contains functions to chech the number of arg specified in the command of the program
import os  #contains functions that allow to determine wether the file to compare exist

def Return_Flag(IP, Port):
	try:
		socket.setdefaulttimeout(2)
		sock = socket.socket()
		sock.connect((IP, Port))
		flag = sock.recv(1024) #bytes
		return flag
	except:
		return

def Check_Vulnerabilities(flag, File_Name):
        file = open(File_Name, "r")
        for Every_Line in file.readlines():
                if Every_Line.strip("\n") in flag:
                        print("[**] Server is vulnerable:" + flag.strip("\n"))

def main():
	if len(sys.argv) == 2:    #to check the file which of course are 2(the scanner and the one to compare with())
		File_Name = sys.argv[1]
		if not os.path.isfile(File_Name):
			print("[**] The file does not exits")
			exit(0)
		if not os.access(File_Name, os.R_OK):  #if the user does not have access to the file
			print("[**] Permmission Denied!")
			exit(0)
	else:
		print("[**] Usage Of Program: " + str(sys.argv[0]) + "<Vulnerabilities File>")
		exit(0)

	Port_Lists = [22, 21, 23,25, 53, 80,443,110, 143, 161,69,67, 68,53]
	for X in range(1,6): #255, the number of possible hosts available in a LAN 
		IP = "172.28.11." + str(X)
		for Port in Port_Lists:
			flag = Return_Flag(IP, Port)
			if flag:
				print("[**] " + IP + "/" + str(Port) + ":" + flag)
				Check_Vulnerabilities(flag, File_Name)

main()





