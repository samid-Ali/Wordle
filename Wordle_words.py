# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:34:02 2022

@author: Samid
"""
import pandas as pd
import os

os.chdir("G:\Samid work\Wordle")
os.getcwd()
df1 = pd.read_csv('G:/Samid work/R/Wordle_Test.csv')

#############       1) Get Word List       ###########

Wordlist = []
for i in range(3):
    list = str(df1[:0]).replace('"','').replace(']','').split(',')
    for word in range(len(list)):
        Wordlist.append(list[word])

delete = []
for word in range(len(Wordlist)):
    if len(Wordlist[word]) !=5:
        delete.append(word)

for i, Del in enumerate(delete):
    delete[i]=  Del - i

for i in range(len(delete)):
    Wordlist.pop(i)
    
        
Worlde_List = pd.DataFrame(
{
 'Words': Wordlist, 

})

Worlde_List.to_csv('Wordle_wordlist.csv',index=False)  

       
#############       2) For each word get letter in position i       ###########

# del a= str(Wordlist).replace('\\nIndex: [','').replace(']','').replace('"','').replace('Empty DataFrame\nColumns: [[','')


df2 = pd.read_csv('Wordle_wordlist.csv')

First = []
Second = []
Third = []
Fourth = []
Fifth = []

Positions =[First, Second, Third, Fourth, Fifth] 


for i in range(len(Positions)):
    for j in range(len(df2)):
        Positions[i].append(str(df2.iloc[j,0])[i])

        
Worlde_Positions = pd.DataFrame(
{
 'Word': Wordlist,
 'First': First,
 'Second': Second, 
 'Third': Third,
 'Fourth': Fourth, 
 'Fifth': Fifth 
})

Worlde_Positions.to_csv('Wordle_positions.csv',index=False)         

#############      3) Get frequencies of each letter for each position      ###########

a = []
b = []
c = []
d = []
e = []

Counts = [a, b, c, d, e]

Letters = pd.read_csv('G:\Samid work\Wordle\Alphabet.csv', header =None)


    
for i in range(len(Positions)):
    for letter in range(len(Letters)):
        Counts[i].append(Positions[i].count(Letters[0][letter]))
               
Worlde_Positions_Frequency = pd.DataFrame(
{
 'Letter': Letters[0],
 'First': pd.Series(a),
 'Second': pd.Series(b), 
 'Third': pd.Series(c),
 'Fourth': pd.Series(d), 
 'Fifth': pd.Series(e)

})



Worlde_Positions_Frequency.to_csv('Wordle_positions_frequency.csv',index=False)         
       