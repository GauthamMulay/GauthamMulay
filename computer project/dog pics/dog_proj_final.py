import sys
import tkinter as tk
from tkinter import ttk
#from PIL import ImageTk,Image

breedinfo={}
breedlist=[]
cmpr=[]
categlst=[]

def importbreedlist():
    blreadlist=[]
    bllist=[]
    blsublist=[]
    blfile=open("breedlist.txt")
    blreadlist=blfile.readlines()
    blfile.close()

    for i in blreadlist:
        bllist=i.split(";")
        for j in bllist:
            blsublist.append(j.split(":"))        
        breedinfo[bllist[0][5::]]=dict(blsublist)
    global breedlist,categlst
    breedlist=list(breedinfo.keys())
    breedlist=sorted(breedlist)
    categlst=list(breedinfo["Cane Corso"].keys())

importbreedlist()#import all breed info from notepad to a dictionary in the programme

def inpch():
    global breedinfo,categlst

    cmpr.clear()
    ctr=0
    for i in combo:#loop appends the selected combobox options to a separate list as well as get images for these options
        cmpr.append(i.get())
        t[ctr].delete("1.0","end")
        if "\n" in breedinfo[i.get()]["image"]:
            im[ctr]=ImageTk.PhotoImage(Image.open("dog_images/"+breedinfo[i.get()]["image"][:-1:]))
        else:
            im[ctr]=ImageTk.PhotoImage(Image.open("dog_images/"+breedinfo[i.get()]["image"]))    
        ctr+=1
   
    ctr=0
'''  for i in t:#loop to insert images into canvas and details/info into the text box
        dogdct=breedinfo[cmpr[ctr]]
       # c[ctr].create_image(175,100,image=im[ctr])
        
        for j in categlst[:-1:]:
            i.insert(tk.END,j+":"+dogdct[j]+"\n")
        ctr+=1'''

        
win = tk.Tk() 
win.geometry('300x50')
win.title("DOG BREED COMPARER")
combo=[0,1,2]
t=[0,1,2]
c=[0,1,2]
im=[0,1,2]

win.geometry('1200x700')
win.title("DOG BREED PICKER")  
 
 
tk.Label(win,text = "Choose breed 1:",bg="light blue").grid(column=0, row=0)
tk.Label(win,text = "Choose breed 2:",bg="light blue").grid(column=1, row=0)
tk.Label(win,text = "Choose breed 3:",bg="light blue").grid(column=2, row=0)


combo[0] = ttk.Combobox(win,values=breedlist) 
combo[0].grid(column=0,row=1)

combo[1] = ttk.Combobox(win,values=breedlist) 
combo[1].grid(column=1,row=1)

combo[2] = ttk.Combobox(win,values=breedlist) 
combo[2].grid(column=2,row=1)

 
bch =tk.Button(win,text="compare",bg="cyan",command=inpch,padx=20,pady=10).grid(column=4,row=2)


c[0] = tk.Canvas(win,height = 200,width = 350) 
c[0].grid(column=0,row=2)

c[1] = tk.Canvas(win,height = 200,width = 350) 
c[1].grid(column=1,row=2)

c[2] = tk.Canvas(win,height = 200,width = 350) 
c[2].grid(column=2,row=2)


t[0] = tk.Text(win,height = 25,width = 45,bg="light blue") 
t[0].grid(column=0,row=3)

t[1] = tk.Text(win,height = 25,width = 45,bg="light blue") 
t[1].grid(column=1,row=3)

t[2] = tk.Text(win,height = 25,width = 45,bg="light blue") 
t[2].grid(column=2,row=3)

win.configure(background="blue")
win.mainloop()



