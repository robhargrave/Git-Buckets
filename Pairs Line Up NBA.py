import openpyxl as xl 
import heapq as hp
import numpy as np
import pandas as pd

#Start of Fan Duel optimal line up code 
#Imports this weeks nba excel sheet and returns the highest FPPG
# Change Directory by runnnig " cd ~/Desktop" in command window 

S = 60000 #Max Salary 
#MaxPG = 2 #Number of Point Gaurds
#MaxSG = 2 #Number of Shooting Gaurds
#MaxPF = 2 #Number of Power Fowards
#MaxSF = 2 #Number of Small Fowards
#MaxC = 1 #Number of Centers 


#Imports the Player list and makes active worksheet 
A = pd.read_csv('FanDuel-NBA-2017-04-09-18664-players-list (1).csv')
r = A.shape[0]


##################################################################################
#This is the list of FPPG and Salarys PG
PGp = []#This is the list holder of point garud points
PGs = []#List of Point gaurd salary

SGp = []#This is the list holder of shooting points
SGs = []#List of Shooting Gaurd salary

PFp = []#This is the list holder Power Foward 
PFs = []#List of Power Foward salary

SFp = []#This is the list holder Small Foward 
SFs = []#List of Small Foward salary

Cp = []#This is the list holder for Centers
Cs = []#List of Centers

###################################################################################
for i in range (r): 
    #Gets all of the values for lists with people that are playing 
    if A.get_value(i,1,takeable=True) == 'PG' \
    and A.get_value(i,11,takeable=True) != 'O'\
    and A.get_value(i,11,takeable=True) != 'GTD': # Gets PointGaurds 
                                                  #"O is out"
                                                  #"GTD is gametime decision"
     PGp.append(A.get_value(i,5,takeable=True))
     PGs.append(A.get_value(i,7,takeable=True))
    elif A.get_value(i,1,takeable=True) == 'SG'\
    and A.get_value(i,11,takeable=True) != 'O'  \
    and A.get_value(i,11,takeable=True) != 'GTD':
     SGp.append(A.get_value(i,5,takeable=True))
     SGs.append(A.get_value(i,7,takeable=True))
    elif A.get_value(i,1,takeable=True) == 'PF'\
    and A.get_value(i,11,takeable=True) != 'O' \
    and A.get_value(i,11,takeable=True) != 'GTD':
     PFp.append(A.get_value(i,5,takeable=True))
     PFs.append(A.get_value(i,7,takeable=True))
    elif A.get_value(i,1,takeable=True) == 'SF'\
    and A.get_value(i,11,takeable=True) != 'O' \
    and A.get_value(i,11,takeable=True) != 'GTD':
     SFp.append(A.get_value(i,5,takeable=True))
     SFs.append(A.get_value(i,7,takeable=True))
    elif A.get_value(i,1,takeable=True) == 'C'\
    and A.get_value(i,11,takeable=True) != 'O' \
    and A.get_value(i,11,takeable=True) != 'GTD':
     Cp.append(A.get_value(i,5,takeable=True))
     Cs.append(A.get_value(i,7,takeable=True))

##########################################################################     
#Starting the point holder
#This is the main part of the program, it scrolls
#through the lists and finds the best pairs
#This is one way to do it but only goes through about 8 million possible choices 
# out of the 1x10^46 possible outcomes. 
#This other program runs them, but computing times are to slow, and would take
#about 7*10^35 hours to compute. 


maxpoints = 0 #Starting amount of points
count = 0 #Start of counting variable for interation counts
for a in range (len(Cs)): #Scroll through Centers
    for c in range (len(SFs)-1): #Scroll through SFs
        for e in range (len(SGs)-1): #Scroll through SGs
            for g in range (len(PFs)-1): #Scroll through PFs
                for i in range (len(PGs)-1): #Scroll through PGs
                                    #looks to see if the salary is in range 
                                    sal = Cs[a] \
                                    +SFs[c]+SFs[c+1]\
                                    +SGs[e]+SGs[e+1]\
                                    +PFs[g]+PFs[g+1]\
                                    +PGs[i]+PGs[i+1]
                                    if sal > S:
                                        points = 0
                                    elif sal <= S:
                                    #Calculates the points of the set 
                                        points = Cp[a] \
                                    +SFp[c]+SFp[c+1]\
                                    +SGp[e]+SGp[e+1]\
                                    +PFp[g]+PFp[g+1]\
                                    +PGp[i]+PGp[i+1] 
                                        if points > maxpoints:
                                            #Grabs the amount of points and player 
                                            #holders 
                                            salholder = sal
                                            maxpoints = points 
                                            Cholder = a
                                            SFholder1 = c
                                            SFholder2 = c+1
                                            SGholder1 = e
                                            SGholder2 = e+1
                                            PFholder1 = g
                                            PFholder2 = g+1
                                            PGholder1 = i
                                            PGholder2 = i+1
                                    #Counting variable to see how many
                                    #Diffrent sets it went through 
                                    #Used for benchmarks, trying to maximize
                                    #while reducing time         
                                    count = count + 1

#Matches the values from the holder lists to main document                             
for i in range (len(A)):
    pg1 = PGp[PGholder1]
    pg2 = PGp[PGholder2]
    sg1 = SGp[SGholder1]
    sg2 = SGp[SGholder2]
    sf1 = SFp[SFholder1]
    sf2 = SFp[SFholder2]
    pf1 = PFp[PFholder1]
    pf2 = PFp[PFholder2]
    c = Cp[Cholder]
    
    if A.get_value(i,5,takeable=True) == pg1:
        PG1 = A.get_value(i,3,takeable=True)
        PG1s = A.get_value(i,5,takeable=True)
        PG1p = A.get_value(i,7,takeable=True)    
    if A.get_value(i,5,takeable=True) == pg2:
        PG2 =  A.get_value(i,3,takeable=True)
        PG2s = A.get_value(i,5,takeable=True)
        PG2p = A.get_value(i,7,takeable=True)    
    if A.get_value(i,5,takeable=True) == sg1:
        SG1 =  A.get_value(i,3,takeable=True)
        SG1s = A.get_value(i,5,takeable=True)
        SG1p = A.get_value(i,7,takeable=True)    
    if A.get_value(i,5,takeable=True) == sg2:
        SG2 =  A.get_value(i,3,takeable=True)
        SG2s = A.get_value(i,5,takeable=True)
        SG2p = A.get_value(i,7,takeable=True)     
    if A.get_value(i,5,takeable=True) == sf1:
        SF1 =  A.get_value(i,3,takeable=True)
        SF1s = A.get_value(i,5,takeable=True)
        SF1p = A.get_value(i,7,takeable=True)    
    if A.get_value(i,5,takeable=True) == sf2:
        SF2 =  A.get_value(i,3,takeable=True)
        SF2s = A.get_value(i,5,takeable=True)
        SF2p = A.get_value(i,7,takeable=True)    
    if A.get_value(i,5,takeable=True) == pf1:
        PF1 =  A.get_value(i,3,takeable=True)
        PF1s = A.get_value(i,5,takeable=True)
        PF1p = A.get_value(i,7,takeable=True)    
    if A.get_value(i,5,takeable=True) == pf2:
        PF2 =  A.get_value(i,3,takeable=True)
        PF2s = A.get_value(i,5,takeable=True)
        PF2p = A.get_value(i,7,takeable=True)    
    if A.get_value(i,5,takeable=True) == c:
        C =  A.get_value(i,3,takeable=True)
        Css = A.get_value(i,5,takeable=True)
        Cpp = A.get_value(i,7,takeable=True)       
 
#Printing statment that will hopefully be converted to an
#Excel spreadsheet for Readablility. Plan is to take the entire line from
#origonl document an paste into new spreadsheet
print" \t\tNAME - FPPG - SALARY \n %s - %s - %s  \
       \n %s - %s - %s \
       \n %s - %s - %s \
       \n %s - %s - %s \
       \n %s - %s - %s \
       \n %s - %s - %s \
       \n %s - %s - %s \
       \n %s - %s - %s \
       \n %s - %s - %s \
       \n Maxpoints = %s   \
       \n Salary = $%s" %(PG1,PG1s,PG1p,PG2,PG2s,PG2p,SG1,SG1s,SG1p,SG2,SG2s,SG2p,SF1,SF1s,SF1p,SF2,SF2s,SF2p,PF1,PF1s,PF1p,PF2,PF2s,PF2p,C,Css,Cpp,maxpoints,salholder)
       
                 
                                                         
                    

     
     
     