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
