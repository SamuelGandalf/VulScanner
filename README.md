# VulScanner

The VulnerabiltiesScanner.py is a simple code to simply scan and return the banners/flags of some ports in metasploitable 
which are printed into the VulDiscoverd file
The VulScanner.py scans the host which is the metasploitable 
and compares the list of some possible vulnerabilities/banners in the VulnerableFlags.txt 
and print out the possible vulnerability/banner that can be exploited in the metasploitable
The VulnerableFlags.txt can be add with more banners.
The Ports to scan are;
21->FTP
22->SSH
23->Telnet
25->SMTP
53->DNS
80->HTTP/443->HTTPS
143->IMAP
69->TFTP   etc
