from pysphere import VIServer
import time
import sys
import os

server = VIServer()

with open(os.getenv('HOME') + '/.esxpy.cfg') as fd:
    config = dict(line.strip().split(None, 1) for line in fd)

server.connect(config['hostname'], config['username'], config['password'])

def guest_status():
    state = guest.get_status()
    if state == 'POWERED OFF':
        status = 'Guest is Powered OFF'
    elif state == 'POWERED ON':
        status = 'Guest is Powered ON'
    elif state == 'POWERING ON':
        status = 'Guest is Powering ON'
    elif state == 'POWERING OFF':
        status = 'Guest is Powering OFF'
    elif state == 'SUSPENDING':
        status = 'Guest is Suspending'
    elif state == 'RESETTING':
        status = 'Guest is Resetting'
    else:
        status = 'Guest is in an Unknown state!'

    return status

def guest_power(cmd):
    
    if cmd == 'reboot':
        guest.reboot_guest(sync_run=False)
    elif cmd == 'on':
        guest.power_on(sync_run=False)
    elif cmd == 'off':
        guest.power_off(sync_run=False)
    elif cmd == 'shutdown':
        guest.shutdown_guest()
    elif cmd == 'reset':
        guest.reset(sync_run=False)
    elif cmd == 'hard':
        guest.terminate_process()
    else:        
        print 'Unrecognized Command!'

if len(sys.argv) == 1:
    print ''' 
    commandline : esxpy.py 'GuestName' 'option'
    The available options are: 'REBOOT', 'ON', 'OFF', 'SHUTDOWN', 'RESET',
    or 'HARD' (which terminates the process of a stuck VM).

    If no option is given the status of the Guest is returned.
    
    Currently available VM's are:
    '''
    for i in server.get_registered_vms():
        print '\t' + i
    #print server.get_registered_vms()
    sys.exit(0)

guest = server.get_vm_by_path(sys.argv[1])

print "The guest's current state is: \n %s\n" % guest_status()

if sys.argv[2:]:
    guest_power(sys.argv[2].lower())

