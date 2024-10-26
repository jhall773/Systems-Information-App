import pandas as pd
import wmi
import ctypes
from ctypes import wintypes

#import xml.etree.ElementTree as ET
#systemsInfo = pd.read_csv("Computer System Info.CSV")
#print(systemsInfo.head(500))
#print("/n"+systemsInfo.columns)


# The functions/classes below, including using PowerShell to get all WMI classes
# were created with the help of Bing's AI, Copiolot. There is documentation for all the conversations with Copiolot 
# in which we include its code.

import wmi
import subprocess

# Use PowerShell to get all WMI classes
result = subprocess.run(["powershell", "-Command", "Get-WmiObject -Namespace root\\cimv2 -List | Select-Object Name"], capture_output=True, text=True)

# Print the output
print(result.stdout)

def get_cpu_usage():
    c = wmi.WMI()
    print(f"Information in Processor Class:\n")
    for cpu in c.Win32_Processor():
        print(f"{cpu}")

def get_gpu_usage():
    c = wmi.WMI()
    print(f"Information in VideoController Class:\n")
    for gpu in c.Win32_VideoController():
        print(f"{gpu}")

#get_class_data()
#get_cpu_usage()
#get_gpu_usage()






