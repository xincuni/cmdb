# -*- coding:utf-8 -*-
'''
这个脚本主要的功能是收集我们的硬件信息
'''

import platform
import win32com
import wmi
import os
import json


def collect():
    data = {
        'os_type': platform.system(),
        'os_release': "%s %s  %s " % (platform.release(), platform.architecture()[0], platform.version()),
        'os_distribution': 'Microsoft',
        'asset_type': 'server'
    }
    # data.update(cpuinfo())
    win32obj = Win32Info()
    data.update(win32obj.get_cpu_info())
    data.update(win32obj.get_ram_info())
    data.update(win32obj.get_server_info())
    data.update(win32obj.get_disk_info())
    data.update(win32obj.get_nic_info())
    print('-----------><>>>>>>>')
    # print (json.dumps(data))


    # for k,v in data.items():
    #    print k,v
    return data


class Win32Info(object):
    def __init__(self):
        self.wmi_obj = wmi.WMI()
        self.wmi_service_obj = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        self.wmi_service_connector = self.wmi_service_obj.ConnectServer(".", "root\cimv2")

    def get_cpu_info(self):
        data = {}
        cpu_lists = self.wmi_obj.Win32_Processor()
        # print(cpu_lists)
        cpu_core_count = 0

        for cpu in cpu_lists:
            cpu_core_count += cpu.NumberOfCores
            cpu_model = cpu.Name
        data["cpu_model"] = cpu_model
        data["cpu_core_count"] = cpu_core_count
        data["cpu_count"] = len(cpu_lists)
        # print(data)
        return data

    def get_ram_info(self):
        data = []
        ram_collections = self.wmi_service_connector.ExecQuery("Select * from Win32_PhysicalMemory")
        for item in ram_collections:
            item_data = {}
            # print(item.Capacity)
            # print('打印内存信息')
            # print(item.Capacity)

            # print(item.Caption)
            # print(item.DeviceLocator)
            # print(item.Manufacturer)
            mb = int(1024 * 1024)
            ram_size = int(item.Capacity) / mb
            # print ram_size
            item_data = {
                "slot": item.DeviceLocator.strip(),
                "capacity": ram_size,
                "model": item.Caption,
                "manufactory": item.Manufacturer,
                "sn": item.SerialNumber,
            }
            print (item_data['slot'])
            data.append(item_data)
        # for i in data:
        #    print i
        return {"ram": data}

    def get_server_info(self):
        computer_info = self.wmi_obj.Win32_ComputerSystem()[0]
        system_info = self.wmi_obj.Win32_OperatingSystem()[0]
        # print system_info
        data = {}
        data['manufactory'] = computer_info.Manufacturer
        data['model'] = computer_info.Model
        data['wake_up_type'] = computer_info.WakeUpType
        data['sn'] = system_info.SerialNumber
        # print data
        return data

    def get_disk_info(self):
        data = []
        for disk in self.wmi_obj.Win32_DiskDrive():
            # print(disk.Model)
            # # print disk
            # print disk.Index
            # print disk.Model
            # print '硬盘大小'
            # print disk.Size
            # print '设备的id'
            # print disk.DeviceID
            # print 'disk名字'
            # print disk.Name
            # # print disk.Indexdisk.Description
            # print disk.SerialNumber
            # print disk.SystemName
            # print disk.Description
            item_data = {}
            iface_choices = ["SAS", "SCSI", "SATA", "SSD"]
            for iface in iface_choices:
                if iface in disk.Model:
                    # print '硬盘接口类型'
                    # print iface
                    item_data['iface_type'] = iface
                    break
            else:
                item_data['iface_type'] = 'unknown'
            item_data['slot'] = disk.Index
            #
            # print item_data['slot']
            item_data['sn'] = disk.SerialNumber
            item_data['model'] = disk.Model
            item_data['manufactory'] = disk.Manufacturer
            item_data['capacity'] = int(disk.Size) / (1024 * 1024 * 1024)
            data.append(item_data)
        return {'physical_disk_driver': data}

    def get_nic_info(self):
        data = []
        for nic in self.wmi_obj.Win32_NetworkAdapterConfiguration():
            # print(nic)
            if nic.MACAddress is not None:
                item_data = {}
                item_data['macaddress'] = nic.MACAddress
                item_data['model'] = nic.Caption
                item_data['name'] = nic.Index
                if nic.IPAddress is not None:
                    item_data['ipaddress'] = nic.IPAddress[0]
                    item_data['netmask'] = nic.IPSubnet
                else:
                    item_data['ipaddress'] = ''
                    item_data['netmask'] = ''
                bonding = 0
                # print nic.MACAddress ,nic.IPAddress,nic.ServiceName,nic.Caption,nic.IPSubnet
                # print item_data
                data.append(item_data)
                # print(json.dumps(data))
        return {'nic': data}


if __name__ == "__main__":
    collect()
