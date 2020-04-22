# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:01:21 2020

@author: snice
"""

import numpy as np
from SudokuList import SUDOKU
from PIL import Image, ImageDraw, ImageFont
import os

str_grid=SUDOKU[0]

board =[[7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]
 


def create_grid(str_grid):
    """Converti le soduko d'un string en matrice 9x9"""
    grid=np.array([[0]*9]*9)
    for k in range(len(str_grid)):
        if str_grid[k]!='.':
            i,j=k//9,k%9
            grid[i][j]=str_grid[k]
    return grid

maingrid=create_grid(str_grid)
L=9

def draw_grid(grid):
    """Dessine le sudoku à partir d'une matrice"""
    for i in range(L):
        if i%3==0 and i!=0:
            print('------ ------- ------')
        for j in range(L):
            if j%3==0 and j!=0:
                print("| ",end="") #On reste sur la même ligne
            if j==L-1:
                print(grid[i][j])
            else:
                print(str(grid[i][j])+" ",end ="")

             
def create_image_grid(grid,nb,pos,step,colour):
    font = ImageFont.truetype("arial.ttf", 20)    
    image=Image.new('RGB',(256,256),'white')   
    draw = ImageDraw.Draw(image)

    y_start = 0
    y_end = image.height
    step_size = int(image.width / L)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        if x%(3*step_size)==0:
            draw.line(line,fill=(0,0,0),width=5)
        else:
            draw.line(line,fill=(0,0,0))

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        if y%(3*step_size)==0:
            draw.line(line,fill=(0,0,0),width=5)
        else:
            draw.line(line,fill=(0,0,0))
        
    for i in range(L):
        for j in range(L):
            if grid[i][j]!=0:
                draw.text(((j+0.25)*step_size, (i+0.25)*step_size),str(grid[i][j]),(0,0,0),font=font)
    draw.text(((pos[1]+0.25)*step_size,(pos[0]+0.25)*step_size), str(nb),colour,font=font)        
    image.save(r'C:\Users\snice\OneDrive\Bureau\Computer Stuff\Python Projects\Sudoku\SudokuSteps\Step_'+str(step)+'.png',"PNG")                
    
                
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
                



def solve(grid,step):
    """Résoud la grille si possible"""
    step+=1
    find=find_empty(grid)
    if not find: #if find==None
        return True
    else:
        a,b=empty_pos(grid)
        for nb in range(1,10):
            if is_valid(grid,nb,(a,b)):
                
                grid[a][b]=nb
                pos=(a,b)
                create_image_grid(grid,nb,pos,step,(255,0,0))
                #draw_grid(grid)
                if solve(grid,step):
                    return True
                grid[a][b]=0
                #os.remove(r'C:\Users\snice\OneDrive\Bureau\Computer Stuff\Python Projects\Sudoku\SudokuSteps\Step_'+str(step)+'.png')
                #step-=1
        return False  
    
def resolution(grid):
    create_image_grid(grid,1,(0,0),0,(255,255,255))
    step=0
    return solve(grid,step)