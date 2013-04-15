###Basic control of ESXi 4.x and 5.x guests via Python.

_Uses the pysphere Python module._

Command Line : 
    esxpy.py 'GuestName' 'option'

The available options are:

'REBOOT',
'ON',
'OFF',
'SHUTDOWN',
'RESET',
'HARD' (which terminates the process of a stuck VM).

If no option is given the status of the Guest is returned.

__Requires__: pysphere. Can be installed via pip or easy_install or
with pip install -f requirements.txt

A configuration file must be created in the user's home directory.
The file must be named '.esxpy.cfg' and contain:  

hostname vmware_server_ip  
username vmware_server_username  
password vmware_server_password  
