#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:07:24 2021

@author: boyangzhang
"""

# import os
# import subprocess


# os.system("echo Hello from the other side!")

# list_files = subprocess.run(["ls", "-l"])
# print("The exit code was: %d" % list_files.returncode)
import subprocess

import os
binpath = "/mnt/NFS/boyang/Aug/bam_sorted/bins_dir/"
reportPrefix = "kraken_report_"
filePrefix = ""
txtFix = ".txt"

firstPart = "kraken2 --db $rumenBacteria/mnt/NFS/boyang/kraken --thread 80 --output "


counter = 0

for root, dirs, files in os.walk(binpath):
    for filename in files:
        if filename[-2:] == "fa":
            print(filename)
            counter += 1
            
            reportName = " --report "+ reportPrefix + filename + txtFix
            binpathName = binpath+filename
            commandOut = firstPart + filename + txtFix + reportName + " "+binpathName
            print(commandOut)
            
            
            cp = subprocess.run(commandOut, shell = True)
            if counter ==5:
                break
