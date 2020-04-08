import numpy as np
import random
import sys
x=9999999
sys.setrecursionlimit(x)
#grille=np.zeros((9,9))
#grille=np.array([[6,0,5,0,0,0,2,0,3],
#[0,7,2,0,0,1,0,0,0],
#[4,0,0,0,0,2,0,9,0],
#[0,5,0,0,0,4,3,0,1],
#[8,0,4,1,0,3,5,0,9],
#[2,0,3,8,0,0,0,7,0],
#[0,2,0,4,0,0,0,0,7],
#[0,0,0,3,0,0,8,6,0],
#[7,0,6,0,0,0,1,0,2]])
#print(grille)
r=[k for k in range(1,10)]
random.shuffle(r)


def enregistrer(l_grilles):
	f=open("grilles","w+")
	for grille in l_grilles:
		l_lignes=[]
		i=0
		for ligne in grille:
			k=0
			str_ligne=""
			for el in ligne:
				if random.random()<0.38:
					
					str_ligne+=str(int(el))
				else:str_ligne+=' '
				if k == 2 or k ==5: str_ligne+="  |  "
				else: str_ligne+="  "
				k+=1
			str_ligne+='\n         |           |         \n'
			l_lignes+=[str_ligne]
			if i==2 or i ==5: l_lignes+=["-------------------------------\n"]
			else : l_lignes+=["         |           |         \n"]
			i+=1
		f.writelines(l_lignes[:-1])
		f.writelines("\n\n\n\n\t      ====\n\n\n\n")
	


def possible(grille,val,x,y):
	for k in range(9): #verification ligne et colonne
		if (grille[x,k]==val) or (grille[k,y]==val):
			return False
	#verification carre
	x0,y0=x//3,y//3
	for i in range(3):
		for j in range(3):
			if grille[3*x0+i,3*y0+j]==val:
				return False	
	return True

def resolveur(grille,init=True):
	global trouve
	if init :
		trouve = False
	for i in range(9):
		for j in range(9):
			if grille[i,j]==0:
				for v_possible in r:
					if possible(grille,v_possible,i,j):
						grille[i,j]=v_possible
						if not(0 in grille):
							trouve=True
						resolveur(grille,False)
						if not(trouve) : 
							grille[i,j]=0
						else: return grille

				if not(trouve): 
					return
	 				

l_grille=[resolveur(np.zeros((9,9)),True) for k in range(10000)]
#print(l_grille)
enregistrer(l_grille)