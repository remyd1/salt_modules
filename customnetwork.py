def ifacestartswith(cidr):
    '''
    Retrieve the interface name from a specific CIDR

    CLI Example:

    .. code-block:: bash
        
        salt '*' customnetwork.ifacestartswith 10.0
    '''
    net_list =  __salt__['network.interfaces']()
    intfnames = []
    pattern = str(cidr)
    size = len(pattern)
    for ifname,ifval in net_list.iteritems():
        if ifval.has_key('inet'):
            for inet in ifval['inet']:
                if inet['address'][0:size] == pattern:
                    intfnames.append(inet['label'])
    return intfnames

def iphexval(ip):
    '''
    Retrieve the interface name from a specific CIDR

    CLI Example:

    .. code-block:: bash
              
        salt '*' customnetwork.iphexval 10.0.0.1
    '''
    a = ip.split('.')
    return '{:02X}{:02X}{:02X}{:02X}'.format(*map(int, a))
