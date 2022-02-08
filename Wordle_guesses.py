    # -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:58:43 2022

@author: Samid
"""

import pandas as pd
import random
import numpy as np


freq = pd.read_csv("G:\Samid work\Wordle\Wordle_positions_frequency.csv", header =None)
words =pd.read_csv("G:\Samid work\Wordle\Wordle_wordlist.csv")
pos = pd.read_csv("G:\Samid work\Wordle\Wordle_positions.csv")

letters = pd.read_csv("G:\Samid work\Wordle\Alphabet.csv")

"""Guessing
"""

wordlist = words['Words'].to_list()
posible = wordlist.copy()

exclude = []
include = wordlist.copy()
        
Letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

def Not_Letter(letter):
    global exclude
    global include
    delete_array =[]
    Deleted = 0
    for i in range(len(include)):
        if letter in include[i]:
            exclude.append(include[i])
            delete_array.append(i)
    if len(delete_array)>0:
        for i in range(len(delete_array)):
            include.pop(delete_array[i]- Deleted)
            Deleted = Deleted +1    
    print('Removed words with letter ', letter)


def Letter_Not_in_position(letter,pos):
    global exclude
    global include
    delete_array =[]
    Deleted = 0
    # delete words with letter in position y
    for i in range(len(include)):
        if (include[i][pos-1] == letter)|(letter not in include[i]):
            exclude.append(include[i])
            delete_array.append(i)
    #delete words if letter not in word
    if len(delete_array)>0:
        for i in range(len(delete_array)):
            include.pop(delete_array[i]- Deleted)
            Deleted = Deleted +1
    print('Deleted words without ',letter, 'or with' ,letter, 'in position', pos)

   
def Letter_in_position(letter,pos):
    global exclude
    global include
    delete_array =[]
    Deleted = 0
    for i in range(len(include)):
        if (include[i][pos-1] != letter):
            exclude.append(wordlist[i])
            delete_array.append(i)
    if len(delete_array)>0:
        for i in range(len(delete_array)):
            include.pop(delete_array[i]- Deleted)
            Deleted = Deleted +1  
    print('Deleted words without ',letter, 'in position', pos)
  
"""    
#Guess 1
guess = np.where((pos['First']=='b') & (pos['Fourth']=='e') &(pos['Fifth']=='s'))[0]
guesses =[]
for i in range(len(guess)):
    guesses.append(wordlist[i])
    
guesses[random.randint(1,len(guesses))]    
    
       
#Get word suggestion    
include[random.randint(1,len(include))]
    
#Example feedback from first guess
Letter_in_position('r',2)
Not_Letters = ['b','k']
Letter_Not_in_position('e', 3)
Letter_Not_in_position('a', 4)

#if multiple words aren't in the answer, can use a list to loop through, as below
for i in range(len(Not_Letters)):
   Not_Letter(Not_Letters[i])
"""


