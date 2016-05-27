def pgrep(name, x=None):
    '''
    Retrieve the PID and informations of the given process name.
    The exact optional parameter will do a "pgrep -x "
    It works exactly as "ps.pgrep" but it gives back the name of
    the process and the number of occurences in stdout.

    CLI Example:

    .. code-block:: bash
        
        salt '*' customps.pgrep apache2 [exact]
    '''
    sanitize_name = str(name)
    if x is not None:
        status_func =  __salt__['cmd.run']("pgrep -x " + sanitize_name)
        #pid_count =  __salt__['cmd.run']("pgrep -c -x " + sanitize_name)
    else:
        status_func =  __salt__['cmd.run']("pgrep " + sanitize_name)
        #pid_count =  __salt__['cmd.run']("pgrep -c " + sanitize_name)
    # last line does not contain "\n"
    pid_count = status_func.count("\n") + 1
    pid_count = str(pid_count) + " occurence(s)."
    ret = []
    ret.extend([sanitize_name, status_func, pid_count])
    return ret


def lsof(name):
    '''
    Retrieve the lsof informations of the given process name.

    CLI Example:

    .. code-block:: bash
        
        salt '*' customps.lsof apache2
    '''
    sanitize_name = str(name)
    lsof_infos =  __salt__['cmd.run']("lsof -c " + sanitize_name)
    ret = []
    ret.extend([sanitize_name, lsof_infos])
    return ret


def netstat(name):
    '''
    Retrieve the netstat informations of the given process name.

    CLI Example:

    .. code-block:: bash
        
        salt '*' customps.netstat apache2
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


def psaux(name):
    '''
    Retrieve information corresponding to a "ps aux" filtered
    with the given pattern. It could be just a name or a regular
    expression (using python search from "re" module).

    CLI Example:

    .. code-block:: bash
                
        salt '*' customps.psaux www-data.+apache2
    '''
    import re
    sanitize_name = str(name)
    pattern = re.compile(sanitize_name)
    ps_aux =  __salt__['cmd.run']("ps aux")
    found_infos = []
    ret = []
    nb_lines = 0
    for info in ps_aux.splitlines():
        found = pattern.search(info)
        if found is not None:
            # remove 'salt' command from results
            if info.find("salt") == -1:
                nb_lines += 1
                found_infos.append(info)
    pid_count = str(nb_lines) + " occurence(s)."
    ret = []
    ret.extend([sanitize_name, found_infos, pid_count])
    return ret
    
