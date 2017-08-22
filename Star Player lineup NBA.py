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

player = raw_input("Player Name: ")
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
#Placing player in position 
for i in range (r):
    if player == A.get_value(i,4,takeable=True):
        position = A.get_value(i,1,takeable=True) #Player position 
        playsal = A.get_value(i,7,takeable=True) #Player Salary 
        playpoint = A.get_value(i,5,takeable=True)
 
        
###################################################################################
for i in range (r): 
    #Gets all of the values for lists with people that are playing 
    if A.get_value(i,1,takeable=True) == 'PG' \
    and A.get_value(i,11,takeable=True) != 'O'\
    and A.get_value(i,11,takeable=True) != 'GTD' \
    and A.get_value(i,7,takeable=True) > 4000: # Gets PointGaurds 
                                                  #"O is out"
                                                  #"GTD is gametime decision"
                                                  #4000 is my salary cap to reduce
                                                  #the amount of people
     PGp.append(A.get_value(i,5,takeable=True))
     PGs.append(A.get_value(i,7,takeable=True))
    elif A.get_value(i,1,takeable=True) == 'SG'\
    and A.get_value(i,11,takeable=True) != 'O'  \
    and A.get_value(i,11,takeable=True) != 'GTD' \
    and A.get_value(i,7,takeable=True) > 4000:
     SGp.append(A.get_value(i,5,takeable=True))
     SGs.append(A.get_value(i,7,takeable=True))
    elif A.get_value(i,1,takeable=True) == 'PF'\
    and A.get_value(i,11,takeable=True) != 'O' \
    and A.get_value(i,11,takeable=True) != 'GTD'\
    and A.get_value(i,7,takeable=True) > 4000:
     PFp.append(A.get_value(i,5,takeable=True))
     PFs.append(A.get_value(i,7,takeable=True))
    elif A.get_value(i,1,takeable=True) == 'SF'\
    and A.get_value(i,11,takeable=True) != 'O' \
    and A.get_value(i,11,takeable=True) != 'GTD' \
    and A.get_value(i,7,takeable=True) > 4000:
     SFp.append(A.get_value(i,5,takeable=True))
     SFs.append(A.get_value(i,7,takeable=True))
    elif A.get_value(i,1,takeable=True) == 'C'\
    and A.get_value(i,11,takeable=True) != 'O' \
    and A.get_value(i,11,takeable=True) != 'GTD'\
    and A.get_value(i,7,takeable=True) > 4000:
     Cp.append(A.get_value(i,5,takeable=True))
     Cs.append(A.get_value(i,7,takeable=True))
     
l1 = len(PGp)
l2 = len(SGp)
l3 = len(PFp)
l4 = len(Cp)

totplay = l2 +l3 + l4

totposs = 2**(totplay)

tottime = totposs/10000000

print('estimated time is %sm') %(tottime)

##########################################################################     
#Starting the point holder
#Builds team around inputted player
if position == 'PG':
    for u in range(len(PGp)):
        if playpoint == PGp[u]:
            PGholder1 = u
    maxpoints = 0 #Starting amount of points
    count = 0 #Start of counting variable for interation counts
    for i in range(len(PGp)):
        for j in range(len(SGp)):
            for k in range(len(SGp)):
                for l in range(len(SFp)):
                    for m in range(len(SFp)):
                        for n in range(len(PFp)):
                            for o in range(len(PFp)):
                                for p in range(len(Cp)):
                               #looks to see if the salary is in range
                                            
                                    sal = playsal \
                                    +SFs[l]+SFs[m]\
                                    +SGs[j]+SGs[k]\
                                    +PFs[n]+PFs[o]\
                                    +PGs[i]+Cs[p]
                                    if sal > S:
                                            points = 0
                                    if sal <= S:
                                        if o == n:
                                            points = 0
                                        if m == l:
                                            points = 0
                                        if k == j:
                                            points = 0
                                        if n == o:
                                            points = 0
                                        if l == m:
                                            points = 0
                                        if j == k:
                                            points = 0
                                        #Calculates the points of the set 
                                        points = playpoint \
                                        +SFp[l]+SFp[m]\
                                        +SGp[j]+SGp[k]\
                                        +PFp[n]+PFp[o]\
                                        +PGp[i]+Cp[p]
                                        if o == n:
                                            points = 0
                                        if m == l:
                                            points = 0
                                        if k == j:
                                            points = 0
                                        if n == o:
                                            points = 0
                                        if l == m:
                                            points = 0
                                        if j == k:
                                            points = 0
                                        if points > maxpoints:
                                                    #Grabs the amount of points and player 
                                                    #holders 
                                                    salholder = sal
                                                    maxpoints = points 
                                                    Cholder = p
                                                    SFholder1 = l
                                                    SFholder2 = m
                                                    SGholder1 = j
                                                    SGholder2 = k
                                                    PFholder1 = n
                                                    PFholder2 = o
                                                    PGholder2 = i
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
       
                 
                                                         
                    

     
     
     