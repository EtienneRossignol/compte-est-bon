from itertools import combinations
from time import time

def compte_bon(L,pos):
    global plus_proche,L_resultats
    t=len(L)
    for i,el in enumerate(L):
        if L_resultats==((0,3,0),(0,3,2),(0,1,0),(0,1,1)):
            print("OK")
        if abs(demande-el)<= abs(plus_proche-demande):
            
            if abs(demande-el)!= abs(plus_proche-demande):
                L_resultats=[(None,None)]*(len(nb))
                plus_proche=el
            L_resultats[pos]= (L_operation[:pos],i)
            
    for id1,id2 in combinations(range(t),2):
        nb1,nb2=L[id1],L[id2]
        if nb1< nb2:
            nb1,nb2=nb2,nb1
            id1,id2=id2,id1

        #addition
        L2=L[:]
        L2[id1]+=nb2
        del L2[id2]
        L_operation[pos]=(id1,id2,0)
        compte_bon(L2,pos+1)
        
        #soustraction
        if nb1!=nb2:
            L2=L[:]
            L2[id1]-=nb2
            del L2[id2]
            L_operation[pos]=(id1,id2,1)
            compte_bon(L2,pos+1)

        #multipliquation
        if nb1!=1 and nb2!=1:
            L2=L[:]
            L2[id1]*=nb2
            del L2[id2]
            L_operation[pos]=(id1,id2,2)
            compte_bon(L2,pos+1)

        #division
        if nb1%nb2 or nb2==1:continue
        L2=L[:]
        L2[id1]//=nb2
        del L2[id2]
        L_operation[pos]=(id1,id2,3)
        compte_bon(L2,pos+1)

def afficher_resultat(res, pos):
    
    L=nb[:]
    for id1,id2, opp in res:
        if opp ==0:
            L[id1]='({}+{})'.format(L[id1],L[id2])
        elif opp==1:
            L[id1]='({}-{})'.format(L[id1],L[id2])
        elif opp==2:
            L[id1]='{}*{}'.format(L[id1],L[id2])
        elif isinstance(L[id2],str):
            L[id1]='{}/({})'.format(L[id1],L[id2])
        else:
            L[id1]='{}/{}'.format(L[id1],L[id2])
        del L[id2]

    chaine=L[pos]
    valeur=eval(chaine)
    
    def par():
        L_couple=[-1]*len(chaine)
        pos=0
        L_cour = []
        for i,el in enumerate(chaine):
            if el=='(':
                L_couple[i]=pos
                L_cour.append (pos)
                pos+=1
            elif el==')':
                L_couple[i]= L_cour [-1]
                L_cour.pop ()
        return L_couple
    
    L_couple=par()
    ch=list(chaine)
    for i in range(max(L_couple)+1):
        deb,fin=-1,-1
        for value,el in enumerate(L_couple):
            if el ==i:
                if deb==-1:
                    deb=value
                else:
                    fin=value
                    
                ch[value]=' '
        if valeur!=eval(''.join(ch)):
            ch[deb]='('
            ch[fin]=')'
    return (''.join(ch)).replace(' ','')
        

plus_proche=-1000
demande=int(input("nombre à atteindre :"))
nb=list(map(int, input("liste des nombres disponibles :").split()))
L_operation=[()]*(len(nb)-1)
L_resultats=[]
t1=time()
compte_bon(nb,0)
t2=time()

print('temps : ',t2-t1,' s')
print("résultat : ",plus_proche)
for i,(operations,position) in enumerate(L_resultats):
    if isinstance(position,int):
        print("une solution avec {} opérations : {}".format(i, afficher_resultat(operations,position)))
input()
