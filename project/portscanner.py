import nmap

nm = nmap.PortScanner()

target = "192.168.7.45"
options = "-sV -sC scan_results"
#options is used for how we wanna used nmap what things we needed
#sv is used for services and sc stands for standard script for nmap

nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print('Host: %s (%s)' % (host, nm[host].hostname()))
    print('State: %s' % nm[host].state())
    for protocol in nm[host].all_protocols():
        print('Protocol: %s' % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():                                                       
            print('port: %s\tstate: %s' % (port, state))
            