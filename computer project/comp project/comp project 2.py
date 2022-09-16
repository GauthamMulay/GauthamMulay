import sys
import tkinter as tk
from tkinter import ttk,PIL

from PIL import ImageTK,Image

breedinfo={}
breedlist=[]
cmpr=[]
categlst=['NAME', 'ORIGINE', 'CLASS', 'SIZE', 'PERSONALITY', 'HEIGHT', 'WEIGHT', 'LIFE EXPECTANCY', 'SHEDDING', 'GROOMING REQUIREMENT', 'ENERGY LEVEL', 'EXERCISE NEEDS', 'APARTMENT FRIENDLY', 'HEAT TOLERANCE', 'COLD TOLERANCE', 'HEALTH PROBLEMS', 'DROOLING TENDANCY']
#breedinfo={"Cane Corso":{"NAME":"Cane Corso","ORIGINE":"Italy","CLASS":"Working dog","SIZE":"Large","PERSONALITY":"loyal,courageous,quiet,alert",'HEIGHT':'Males 24"-27"& Females 23"-25"',"WEIGHT":"Males 45kg-50kg & Females 40-45kg","LIFE EXPECTANCY":"10-12 years","SHEDDING":"Morderate","GROOMING REQUIREMENT":"Minimal","ENERGY LEVEL":"High","EXERCISE NEEDS":"Medium","APARTMENT FRIENDLY":"Not recommended","HEAT TOLERANCE":"Good","COLD TOLERANCE":"Good","HEALTH PROBLEMS":"bloat,hip-displaysia","DROOLING TENDANCY":"Morderate-High"}}
#NAME:Cane Corso;ORIGINE:Italy;CLASS:Working dog;SIZE:Large;PERSONALITY:loyal,courageous,quiet,alert;HEIGHT:Males 24"-27"& Females 23"-25";WEIGHT:Males 45kg-50kg & Females 40-45kg;LIFE EXPECTANCY:10-12 years;SHEDDING:Morderate;GROOMING REQUIREMENT:Minimal;ENERGY LEVEL:High;EXERCISE NEEDS:Medium;APARTMENT FRIENDLY:Not recommended;HEAT TOLERANCE:Good;COLD TOLERANCE:Good;HEALTH PROBLEMS:bloat,hip-displaysia;DROOLING TENDANCY:Morderate-High
def importbreedlist():
    blreadlist=[]
    bllist=[]
    blsublist=[]
    blfile=open("dog breed.txt")
    blreadlist=blfile.readlines()
    blfile.close()

    for i in blreadlist:
        bllist=i.split(";")
        for j in bllist:
            blsublist.append(j.split(":"))        
        breedinfo[bllist[0][5::]]=dict(blsublist)
    global breedlist
    breedlist=list(breedinfo.keys())
    categlst=list(breedinfo["Cane Corso"].keys())
"""  
def uploadbreedlist():
    ctr=0
    file=open("breedlist.txt","w")
    for i in breedinfo.items():
        d=(list(i)[1])
        string=""
        for j in d.keys():
            string=string+j+":"+d[j]+";"
        file.write(string[:-1:])
    file.close()
"""
def printlist():
    global breedlist
    breedlist.sort()
    for i in breedlist:
        print(i,"-")
        for j in breedinfo[i].items():
            print(list(j)[0],":",list(j)[1])

def breedadder():
    global categlst
    name=""
    win2=tk.Tk()
   
    #val=tk.StringVar()
    def getter():
        name=ent.get()
        print(name)
       
    lab=tk.Label(win2,text=categlst[0]+":").grid(row=0,column=0)
    ent=tk.Entry().grid(row=0,column=1)
    lab=tk.Button(win2,text="save",command=getter).grid(row=0,column=2)
   
    """
    n=input("enter breed name:").title()
    if n in breedlist:
        print("breed already present in records.")
    else:
        string="\n"+"NAME:"+n+";"
        for i in categlst[1::]:
            n=input(i).title()
            string=string+i+":"+n+";"
           
        print(string)    
        file=open("breedlist.txt","a")
        file.write(string[:-1:])
        file.close()
    """  
    win2.mainloop()

importbreedlist()

def inpch():
    global breedinfo,categlst
    #compare appender
    cmpr.clear()
    for i in combo:
        cmpr.append(i.get())
    #print(cmpr)
    #text printer
    ctr=0
    for i in t:
        dogdct=breedinfo[cmpr[ctr]]
        for j in categlst:
            i.insert(tk.END,j+":"+dogdct[j]+"\n")
        ctr+=1
       




#from PIL import ImageTk, Image

#back=0
 
win = tk.Tk()
win.geometry('1200x700')
bopt1=tk.Button(win,text="Add Breed",command=breedadder).grid(column=0,row=0)
#bopt2=tk.Button(win,text="compare breeds",command=comparebreeds).grid(column=1,row=0)
#bopt3=tk.Button(win,text="pick breeds",command=inpch).grid(column=2,row=0)

#def comparebreeds():
   
combo=[0,1,2]
t=[0,1,2]
 
tk.Label(win,text = "Choose breed 1:").grid(column=0, row=1)
tk.Label(win,text = "Choose breed 2:").grid(column=1, row=1)
tk.Label(win,text = "Choose breed 3:").grid(column=2, row=1)
#tk.Label(win,text = "Choose breed 4:").grid(column=3, row=0)

combo[0] = ttk.Combobox(win,values=breedlist)
combo[0].grid(column=0,row=2)

combo[1] = ttk.Combobox(win,values=breedlist)
combo[1].grid(column=1,row=2)

combo[2] = ttk.Combobox(win,values=breedlist)
combo[2].grid(column=2,row=2)

#combo[3] = ttk.Combobox(win,values=breedlist)
#combo[3].grid(column=3,row=1)
 
bch =tk.Button(win,text="compare",command=inpch).grid(column=4,row=2)

t[0] = tk.Text(win,height = 40,width = 45)
t[0].grid(column=0,row=3)

t[1] = tk.Text(win,height = 40,width = 45)
t[1].grid(column=1,row=3)

t[2] = tk.Text(win,height = 40,width = 45)
t[2].grid(column=2,row=3)

#t[3] = tk.Text(win,height = 40,width = 35)
#t[3].grid(column=3,row=2)

win.mainloop()

#print(cmpr)
#win.mainloop()
