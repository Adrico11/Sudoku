# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:17:11 2020

@author: snice
"""

import numpy as np
from SudokuList import SUDOKU

str_grid=SUDOKU[0]


def create_grid(str_grid):
    """Converti le soduko d'un string en matrice 9x9"""
    grid=np.zeros((9,9))
    for k in range(len(str_grid)):
        if str_grid[k]!='.':
            i,j=k//9,k%9
            grid[i][j]=int(str_grid[k])
    #print(grid)
    return grid

maingrid=create_grid(str_grid)
L=9

def draw_grid(grid):
    """Dessine le sudoku à partir d'une matrice"""
    for i in range(L):
        if i%3==0 and i!=0:
            print('--- --- ---   --- --- ---   --- --- ---')
        for j in range(L):
            if j%3==0 and j!=0:
                print("| ",end="") #On reste sur la même ligne
            if j==L-1:
                print(grid[i][j])
            else:
                print(str(grid[i][j])+" ",end ="")
                
                
def find_empty(grid):
    """Renvoie une position vide"""
    for i in range (L):
        for j in range (L):
            if grid[i][j]==0:
                return(i,j)
    return None    

def possible_nb(i,j,grid):
    """Donne tous les chiffres possibles à une certaine position"""
    possible=[]
    for nb in range(1,10):
        if is_valid(grid,nb,(i,j)):
            possible.append(nb)
    return possible

def empty_pos(grid):
    """Renvoi la liste des cases vides dans une grid classées par nb de possibilités croissantes"""
    empty={}
    for i in range (L):
        for j in range (L):
            if grid[i][j]==0:
                empty[(i,j)]=possible_nb(i,j,grid)
    sorted_empty = sorted(empty.items(), key=lambda x: len(x[1]))
    #print(sorted_empty)            
    #sorted_empty_list = [x[0] for x in sorted_empty]      
    #return sorted_empty_list
    return sorted_empty[0][0]
            
def is_valid(grid,nb,pos):
    """Défini si un nb est potentiellement au bon endroit"""
    a,b=pos
    #Check row
    for j in range(L):
        if grid[a][j]==nb and j!=b:
            return False
    #Check column
    for i in range(L):
        if grid[i][b]==nb and i!=a:
            return False
    #Check square
    box_i=a//3
    box_j=b//3
    for i in range(3*box_i,3*box_i+3):
        for j in range(3*box_j,3*box_j+3):
            if grid[i][j]==nb and (i,j)!=(a,b):
                return False
    return True #La position est correcte (a priori)        
                
solutiontot=[]

def solve(grid):
    """Résoud la grille si possible"""
    solutiontot.append(grid)
    print(solutiontot)
    #draw_grid(grid)
    #print(" ")
    find=find_empty(grid)
    if not find: #if find==None
        return True
    else:
        a,b=empty_pos(grid)
        #print(find)
        for nb in range(1,10):
            if is_valid(grid,nb,(a,b)):
                grid[a][b]=nb
                if solve(grid):
                    return True
                grid[a][b]=0
        return False   
    
