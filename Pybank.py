# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:51:33 2022

@author: Hamza Hersi
"""
import os
import csv

csvpath = os.path.join('budget_data.csv')

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # skip the headers
    #adds 1 to track how many months there are in the file
    m_count = 0
    p_total = 0
    p_temp = 0
    inc_temp = 0
    dec_temp = 0
    avg = 0
    i_date =""
    d_date = ""
    for row in csvreader:

        m_count = m_count + 1
    #adds the profit or loss made to the varaible then adds it to the total 
        p_temp = int(row[1])
        p_total= p_total + p_temp
    
    #find greatest increase 
        if p_temp > 0 and p_temp> inc_temp:
            inc_temp = p_temp
            i_date = row[0]
        
    #finds greatest decrease
        if p_temp < 0 and p_temp < dec_temp:
            dec_temp = p_temp
            d_date = row[0]

        
        avg=p_total/m_count
            
    
    
print("Finacial Analysis")
print("---------------------------")  
print("Total months: ",m_count)  
print("Total: ",p_total)   
print("Average change: ",avg)
print("Greatest Increase in profit: ",i_date," (",inc_temp,")")
print("Greatest Decrease in profit: ",d_date," (",dec_temp,")")    
        
        
        
        
