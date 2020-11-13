# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:29:52 2020

@author: VIDYA
"""


import subprocess
import os

def bagExtractor(ip,op):
    topList=subprocess.check_output("rostopic list -b "+ip)
    topList=topList.split("\r\n")
    for topic in topList:
        tList=topic.split("/")
        try:
            if tList[1] == "mavros":
                command="rostopic echo -b IMU.bag -p "+topic+" > "+op+tList[-1]+".csv"
                print(command)
                os.system(command)
        except:
            pass
    return("Cos brooki rocks")