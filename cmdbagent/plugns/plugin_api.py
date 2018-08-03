# -*- coding:utf-8 -*-
def LinuxSysInfo():
    from linux import sysinfo

    return sysinfo.collect()


def WindowsSysInfo():
    from windows import sysinfo
    # return data
    return sysinfo.collect()
