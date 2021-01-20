#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:11:27 2021

@author: boyang zhang zhang.7077@osu.edu
"""
from pathlib import Path
import numpy as np
import pandas as pd
import argparse

if __name__ == "__main__":
    
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-fadir", "--f", help=".fa file dir. e.g. /Users/Downloads/")
    parser.add_argument("-depthdir", "--d", help="depth file dir. e.g. /Users/Result/")
    
    args = parser.parse_args()
    
    print( "fa file is in: {} depth file is in {} ".format(
            args.f,
            args.d
            ))


    #mypath = '/Users/boyangzhang/Downloads/'
    #myDepthPath = '/Users/boyangzhang/OneDrive - The Ohio State University/2021/Spring/demicResult/'
    
    mypath = str(args.f)
    myDepthPath = str(args.d)

    count = 0
    lineMax = 100
    dictKmerToBin = {} 
    entries = Path(mypath)
    for entry in entries.iterdir():
        
        if entry.name[-2:] == "fa":
            #print(entry.name)
            curFaFile = entry.name
            #print()
    
            # Using readline() 
            file1 = open(mypath + curFaFile, 'r') 
            
            
            while True: 
                count += 1
              
                # Get next line from file 
                line = file1.readline().strip()
                if not line: 
                    break
              
                # if line is empty 
                # end of file is reached
                
                if line[0] == ">":
                    #print("Line{}: {}".format(count, line))
                    dictKmerToBin[line[1:]] = curFaFile
            file1.close()
                    
                
            #print(dictKmerToBin)
            
      
    #print(dictKmerToBin)
            
    def lineToAbundance(line, dictKmerToBin):
        if line.split("\t")[0] not in dictKmerToBin:
            print("Cannot find bin for " + line.split("\t")[0])
            return False, [], None, 0
        
        linesplited = line.split("\t")
        lengthK = float(linesplited[1])
        
        arrTemp = []
        for i in range(3,len(linesplited), 1):
            
            if i % 2 == 1:
                #print(i)
                arrTemp.append(float(linesplited[i]))
        #print(arrTemp)
            
        return True, arrTemp, dictKmerToBin[line.split("\t")[0]], lengthK
    counter = 0
    lineMax = 4
    file2 = open(myDepthPath + "depth.txt", 'r')
    dictBinLength = {}
    dictSampleNames = []
    dictAbund = {}
    while True: 
        counter += 1
        line = file2.readline()
        if not line: 
            break
        
      
        # Get next line from file
        if counter == 1:
            colNames = line.split("\t")
            for colName in colNames:
                #print(colName)
                if colName[-3:] == "bam":
                    dictSampleNames.append(colName[:-4])
    
            #print(dictAbund)
        else:
            #print(line.split("\t"))
            findedBin, abundArr, bins, lengthOfK = lineToAbundance(line, dictKmerToBin)
            if findedBin:
                #print(abundArr)
                #print(lengthOfK)
                if bins not in dictBinLength:
                    dictBinLength[bins] = lengthOfK
                else:
                    dictBinLength[bins] += lengthOfK
                
                if bins not in dictAbund:
                    dictAbund[bins] = np.array(abundArr)*lengthOfK
                else:
                    dictAbund[bins] += np.array(abundArr)*lengthOfK
                
    for key, valueArr in dictAbund.items():
            # print(key, '->', valueArr)
            if key not in dictBinLength:
                continue
            valueArr /= dictBinLength[key]
    
    dfNotScaled = pd.DataFrame.from_dict(dictAbund)
    
    dfNotScaled.index=dictSampleNames
    
    dfScaled = dfNotScaled.div(dfNotScaled.sum(axis=1), axis=0)
    dfScaled.to_csv("relativeAbundance.csv", index=True)
        # print(line)
        # print(line.split("\t")[1])
        # for col in line.split(" "):
        #     print(col)
    

    
    
     

    

        
        
    

        




