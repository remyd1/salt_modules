def getothermountpoints(to_ignore=[]):
    '''
    Retrieve non standard mountpoint

    CLI Example:

    To get all mountpoint except the [ standard ones + /media/disk1 and /scratch ]
    .. code-block:: bash
        
        salt '*' custommount.getothermountpoints "[/media/disk1, /scratch]"
    '''
    mount_list =  __salt__['mount.active']()
    all_ignore_mountpoints = []
    mountnames = []
    standard_mountpoints = ['/tmp','/usr','/var','/boot','/opt','/','/proc','/sys','/run','/run/shm','/run/lock','/home','/dev','/dev/pts','/run/user','/sys/fs/cgroup','/sys/fs/pstore','/sys/fs/cgroup/systemd','/sys/fs/fuse/connections','/sys/fs/pstore','/sys/kernel/debug','/sys/kernel/security','/etc','/etc/pve','/proc/vz/beancounter','/proc/vz/container','/proc/vz/fairsched','/var/lib/vz','/var/lib/nfs/rpc_pipefs','/root','/dev/mqueue','/sys/fs/cgroup/blkio','/sys/fs/cgroup/memory','/cgroup/freezer','/cgroup/net_cls','/cgroup/devices','/sys/fs/cgroup/cpu','/sys/fs/cgroup/cpuset','/sys/fs/cgroup/cpuacct','/sys/fs/cgroup/perf_event','/run/rpc_pipefs','/dev/shm','/cgroup/memory','/cgroup/cpu','/proc/fs/nfsd','/cgroup/cpuacct','/var/lib/ganglia/rrds','/sys/kernel/config','/sys/fs/cgroup/devices','/sys/fs/cgroup/net_cls,net_prio','/proc/sys/fs/binfmt_misc','/boot/efi','/cgroup/blkio','/var/lib/docker/aufs','/sys/fs/cgroup/hugetlb','/sys/fs/cgroup/cpu,cpuacct','/sys/fs/cgroup/freezer','/dev/hugepages','/run/cgmanager/fs','/run/vmblock-fuse','/sys/kernel/debug/tracing','/cgroup/cpuset']
    all_ignore_mountpoints = standard_mountpoints + to_ignore
    for mountname,mountval in mount_list.iteritems():
        if mountname not in all_ignore_mountpoints:
            mountnames.append(mountname)
    return mountnames
