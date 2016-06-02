#!/usr/bin/env python

import salt.wheel.key
import salt.client


def rm_key(host):
    '''
    Delete the key corresponding to the specify host

    CLI Example:

    .. code-block:: bash
                
        salt '*' customkeys.rm_key my_minion
    '''
    minion2manage = str(host)
    client = salt.client.LocalClient()
    salt.wheel.key.__opts__ = client.opts
    ret = salt.wheel.key.delete(minion2manage)
    return ret


def add_key(host):
    '''
    Add the key corresponding to the specify host

    CLI Example:

    .. code-block:: bash
                
        salt '*' customkeys.add_key my_minion
    '''
    minion2manage = str(host)
    client = salt.client.LocalClient()
    salt.wheel.key.__opts__ = client.opts
    ret = salt.wheel.key.accept(minion2manage)
    return ret


def list_keys(host=None):
    '''
    List the keys (corresponding eventually to the specify host)
    or list all the keys, if no host supplied.

    CLI Example:

    .. code-block:: bash
                
        salt '*' customkeys.list_keys [my_minion]
    '''
    client = salt.client.LocalClient()
    salt.wheel.key.__opts__ = client.opts
    if host is None:
        ret = salt.wheel.key.list_all()
    else:
        minion2manage = str(host)
        ret = "Actually list function does not work for a single minion"
        #ret = salt.wheel.key.list(minion2manage)
    return ret
