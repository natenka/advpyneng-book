import resource

from base_ssh import BaseSSH

memory_start = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

ip_list = ['192.168.100.1', '192.168.100.2', '192.168.100.3']*5
sessions = [BaseSSH(ip, 'cisco', 'cisco') for ip in ip_list]

memory_end = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

print('Start ', memory_start)
print('End   ', memory_end)
print(sessions)
