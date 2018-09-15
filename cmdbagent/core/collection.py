#_*_coding:utf-8_*_


from plugins import plugin_api
import json,platform,sys


class InfoCollection(object):
    def __init__(self):
        pass


    def get_platform(self):

        os_platform = platform.system()

        return os_platform #Windows|Linux


    def collect(self):
        os_platform = self.get_platform()
        try:
            func = getattr(self,os_platform)
            #func=Windows
            info_data = func()    # Windows()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError as e:
            sys.exit("Error:MadKing doens't support os [%s]! " % os_platform)
    def Linux(self):
        sys_info = plugin_api.LinuxSysInfo()
        print(sys_info)
        return sys_info

    def Windows(self):
        sys_info = plugin_api.WindowsSysInfo()
        print(sys_info)
        return sys_info
    def build_report_data(self,data):

        #add token info in here before send

        return data
