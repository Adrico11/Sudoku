# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:51:24 2020

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
            grid[i][j]=str_grid[k]
    #print(grid)
    return grid

grid = create_grid(str_grid)   


def square(square_nb,grid):
    """Renvoi la liste des chiffres d'un carré"""
    i,j=square_nb//3,square_nb%3
    box=grid[3*i:3*i+3,3*j:3*j+3]
    square=[x for minirow in box for x in minirow] #Entonnoir (x for ...)
    return square

def row(row_nb,grid):
    """Renvoi la ligne désignée"""
    return grid[row_nb,:]

def col(col_nb,grid):
    """Renvoi la colonne désignée"""
    return grid[:,col_nb]
  
      
def draw_grid(str_grid):
    """Dessine le sudoku"""
    draw=[str_grid[i:i+3] for i in range(0,len(str_grid),3)]
    for i in range(9):
        row=[draw[j] for j in range(3*i,3*i+3)]
        s='|'
        print(s.join(row))
        if (i+1)%3==0 and i!=8:
            print('_'*3+' '+'_'*3+' '+'_'*3)
            print(' '*9)
            
def empty_pos(grid):
    """Renvoi la liste des cases vides dans une grid classées par nb de possibilités croissantes"""
    empty={}
    for i in range (9):
        for j in range (9):
            if grid[i][j]==0:
                empty[(i,j)]=possible_nb(i,j,grid)
    sorted_empty = sorted(empty.items(), key=lambda x: len(x))            
    return sorted_empty            
    
            
            
def is_valid_pos(nb,i,j,grid):
    """Un chiffre peut-il être placé à cet endroit du sudoku ?"""
    assert 1<=nb<=9, "Choose a number between 1 and 9 !"
    square_nb=3*(i//3)+j//3
    if grid[i][j]!=0:
        return False
    elif nb in square(square_nb,grid):
        return False
    elif nb in row(i,grid):
        return False
    elif nb in col(j,grid):
        return False
    else:
        return True
    
def sudoku_done(grid):
    """Vérifie si le sudoku est correctement rempli"""
    for i in range(9):
        for j in range(9):
            if is_valid_pos(grid[i][j],i,j,grid)==False:
                return False
    return True        
         
def possible_nb(i,j,grid):
    """Donne tous les chiffres possibles à une certaine position"""
    possible=[]
    for nb in range(1,10):
        if is_valid_pos(nb,i,j,grid):
            possible.append(nb)
    return possible

def sudoku_possible(grid):
    """Dit s'il reste des possibilités de jeu"""
    for i in range(9):
        for j in range(9):
            if possible_nb(i,j,grid)!=[]:
                return True
    return False        
    

def sudoku_solve(grid):
    sorted_empty=empty_pos(grid)
    visited=[grid]
    parent={}
    parent[grid]=None
    
    if len(sorted_empty)==0 or not sudoku_possible:
        return grid
    
    else:
        print(sorted_empty)
        x,possible=sorted_empty.pop(0)
        i,j=x
        if len(possible)>0:          
            for nb in possible:
                grid1=grid.copy()
                print(grid1)
                grid1[i][j]=nb
                if grid1 not in visited:
                    visited.append(grid1)
                    possible.remove(nb)
                    sudoku_solve(grid1)
                    
        
    
    
       
