import glob
import time
import os

print "Process Starting."

# Remove all gz log files
for gz in glob.glob("/var/log/*.gz"):
    os.remove(gz)
time.sleep (2)

# Remove all gz log files
for gz in glob.glob("/var/log/letsencrypt/*.gz"):
    os.remove(gz)
time.sleep (2)

# Remove all gz log files
for gz in glob.glob("/var/log/apache2/*.gz"):
    os.remove(gz)
time.sleep (2) 
	

# Remove all old log files /var/log
for old in glob.glob("/var/log/*.old"):
    os.remove(old)
time.sleep (2)

# Remove all gz files /var/log/cups
for gz in glob.glob("/var/log/cups/*.gz"):
    os.remove(gz)
time.sleep (2)

# Remove all gz files in /var/log/upstart
for gz in glob.glob("/var/log/upstart/*.gz"):
    os.remove(gz)
time.sleep (2)

# Remove all crash files in /var/crash
for crash in glob.glob("/var/crash/*.crash"):
    os.remove(crash)
time.sleep (2)

# Remove all gz  files in /var/log/apt
for gz in glob.glob("/var/log/apt/*.gz"):
    os.remove(gz)
time.sleep (2)

# Remove all gz  files in /var/log/pgl
for gz in glob.glob("/var/log/pgl/*.gz"):
    os.remove(gz)
time.sleep (2)

# Remove all crash files in /var/log/samba
for gz in glob.glob("/var/log/samba/*.gz"):
    os.remove(gz)
time.sleep (2)

# Remove all log files in /var/log
for log in glob.glob("/var/log/*.log"):
    os.remove(log)
time.sleep (2)

print "Process Completed."

