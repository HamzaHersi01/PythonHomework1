# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:51:33 2022

@author: Hamza Hersi
"""
import os
import csv

csvpath = os.path.join('election_data.csv')

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # skip the headers
   
    a= ['Charles Casper Stockham']
    b= ['Diana DeGette']
    b= ['Raymon Anthony Doane']
    Charles = 0
    Diana = 0
    Raymon = 0
    vote_count = 0
    temp =''
    winner=''
    
    for row in csvreader:
        
        vote_count = vote_count + 1
        
        
        temp = row[2]
        if temp in a:
            Charles = Charles + 1
        elif temp in b:
            Diana = Diana +1
        else:
            Raymon = Raymon + 1
            
    if Charles > Diana & Charles > Raymon:
        winner = 'Charles Casper Stockham'
            
    elif Diana > Charles & Diana > Raymon:
        winner = 'Diana DeGette'
            
    else:
        winner = 'Raymon Anthony Doane'
        
    print("Election Results")
    print("-------------------")
    print("Total votes: ",vote_count)
    print("-------------------")
    print("Charles Casper Stockham: ",Charles/vote_count *100,"% (",Charles,")")
    print("Diana DeGette: ",Diana/vote_count *100,"% (",Diana,")")
    print("Raymon Anthony Doane: ",Raymon/vote_count *100,"% (",Raymon,")")
    print("-------------------")
    print("Winner: ",winner)
    print("-------------------")
    
with open('results.txt', 'w') as f:
    f.write("Election Results"+"\n")
    f.write("-------------------"+"\n")
    f.write("Total votes: "+str(vote_count)+"\n")
    f.write("-------------------"+"\n")
    f.write("Charles Casper Stockham: "+str(Charles/vote_count *100)+"% ("+str(Charles)+")"+"\n")
    f.write("Diana DeGette: "+str(Diana/vote_count *100)+"% ("+str(Diana)+")"+"\n")
    f.write("Raymon Anthony Doane: "+str(Raymon/vote_count *100)+"% ("+str(Raymon)+")"+"\n")
    f.write("-------------------"+"\n")
    f.write("Winner: "+str(winner)+"\n")
    f.write("-------------------"+"\n")           
        
        
            
            
        
        
        
        
            
        
        