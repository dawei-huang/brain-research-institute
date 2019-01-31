#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:56:01 2018

@author: daweihuang
"""
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import datetime
import csv



time = ""
colors = ['red', 'blue', 'green', 'brown', 'orange', 'violet', 'teal', 'yellow']
headers = []
    
def createBin_Data(dataset, threshold):

    res = {}
    n = len(dataset[headers[-1]])
    
    for j in range(len(headers)):
        if j == 0 or j == 1:
            continue
        
        region = headers[j]
        print(region)
        region_bin = np.zeros(n)
        
        col = dataset[region]
        
        for i in range(n):
            
            if col[i] >= threshold:
                region_bin[i] = 1
        
        res[region] = region_bin
                
    return pd.DataFrame(data=res)

    '''new_res = {}
    for j in range(len(headers)):
        if j == 0 or j == 1:
            continue
        
        region = headers[j]
        
        new_res[region] = np.zeros(n)
        
        for period in res[region]:
            start = period[0]
            end = period[1]
            
            new_res[region][start:end] = 1
        

    ret = pd.DataFrame(data=new_res)
    #print(ret)
    return ret'''
                
                
        

def addDerivativesColumn(dataset):
    
    dt = np.diff(dataset[time])[0]

    d_regions = {}
    for i in range(len(headers)):
        if i == 0 or i == 1:
            continue
        
        region = headers[i]
        d_region = np.diff(dataset[region])/dt
        d_region = np.append(d_region, 0)
        d_regions[region] = d_region
    

    '''additional_columns = pd.DataFrame({ "Ovary": d_ovary,
                                        "L.O.": d_lo,
                                        "Upper CO": d_upper_CO,
                                        "Middle CO": d_middle_CO,
                                        "Uterus": d_uterus,
                                        "Spermatheca": d_spermatheca,
                                        "S.R.": d_SR })
    
    dataset = additional_columns.join(dataset["time (seconds)"])'''
    
    #print(dataset)
    
    return pd.DataFrame(d_regions)

def normalizeData(dataset):
    for header in headers:
        mean_dataset = np.array(dataset[header]).mean()
        std_dataset = np.array(dataset[header]).std(ddof=1)
        dataset[header] = (dataset[header] - mean_dataset)/ std_dataset
        #print(mean_dataset, std_dataset)
        #print(dataset[header])
        
    return dataset

if __name__ is "__main__":
    
    filename = sys.argv[1]
    threshold = float(sys.argv[2])
    
    dataset = pd.read_csv(filename)
    headers = list(dataset.columns.values)
    time = headers[1]

    dataset = normalizeData(dataset)
    

    #deriv_region = addDerivativesColumn(dataset)
    #print(dataset)
    
    bin_data = createBin_Data(dataset, threshold)

    bin_data.to_csv('bin___' + str(filename), sep='\t')
    
    

    