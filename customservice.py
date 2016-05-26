def status(name):
    '''
    Retrieve the status of the desired service name.
    Adding the service name in the output.

    CLI Example:

    .. code-block:: bash
        
        salt '*' customservice.status apache2
    '''
    sanitize_name = str(name)
    status_func =  __salt__['service.status'](sanitize_name)
    ret = []
    ret.extend([sanitize_name, status_func])
    return ret

def get_process_info(name, x=None):
    '''
    Retrieve the PID and informations of the given name.
    The exact optional parameter will do a "pgrep -x "
    It works exactly as "ps.pgrep" but it gives back the 
    name of the process and the number of occurences in 
    stdout.

    CLI Example:

    .. code-block:: bash
        
        salt '*' customservice.get_process_info apache2 [exact]
    '''
    sanitize_name = str(name)
    if x is not None:
        pid_count =  __salt__['cmd.run']("pgrep -c -x " + sanitize_name)
        status_func =  __salt__['cmd.run']("pgrep -x " + sanitize_name)
    else:
        pid_count =  __salt__['cmd.run']("pgrep -c " + sanitize_name)
        status_func =  __salt__['cmd.run']("pgrep " + sanitize_name)
    pid_count = pid_count + " occurence(s)."
    ret = []
    ret.extend([sanitize_name, status_func, pid_count])
    return ret

def get_process_lsof(name):
    '''
    Retrieve the lsof informations of the given process name.

    CLI Example:

    .. code-block:: bash
        
        salt '*' customservice.get_process_lsof apache2
    '''
    sanitize_name = str(name)
    lsof_infos =  __salt__['cmd.run']("lsof -c " + sanitize_name)
    ret = []
    ret.extend([sanitize_name, lsof_infos])
    return ret

def get_process_netstat(name):
    '''
    Retrieve the netstat informations of the given process name.

    CLI Example:

    .. code-block:: bash
        
        salt '*' customservice.get_process_netstat apache2
    '''
    sanitize_name = str(name)
    netstat_infos =  __salt__['cmd.run']("netstat -nap")
    found_infos = []
    ret = []
    for info in netstat_infos.splitlines():
        if info.find(sanitize_name) != -1:
            found_infos.append(info)
    ret.extend([sanitize_name, found_infos])
    return ret
