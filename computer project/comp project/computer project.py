from tkinter import *

canecorso={"NAME":"Cane Corso","ORIGINE":"Italy","CLASS":"Working dog"}#,"SIZE":"Large","PERSONALITY":"loyal,courageous,quiet,alert","HEIGHT":'Males 24"-27"\nFemales 23"-25"',"WEIGHT":'Males 45kg-50kg\nFemales 40-45kg',"LIFE EXPECTANCY":"10-12 years","SHEDDING":"Morderate","GROOMING REQUIREMENT":"Minimal","ENERGY LEVEL":"High","EXERCISE NEEDS":"Medium","APARTMENT FRIENDLY":"Not recommended","HEAT TOLERANCE":"Good","COLD TOLERANCE":"Good","HEALTH PROBLEMS":"bloat,hip-displaysia","DROOLING TENDANCY":"Morderate-High" }
doberman={"NAME":"doberman","ORIGINE":"Germany","CLASS":"Working dog"}#,"SIZE":,"PERSONALITY":,"HEIGHT":,"WEIGHT":,"LIFE EXPECTANCY":,"SHEDDING":,"GROOMING REQUIREMENT":,"ENERGY LEVEL":,"EXERCISE NEEDS":,"APARTMENT FRIENDLY":,"HEAT TOLERANCE":,"COLD TOLERANCE":,"HEALTH PROBLEMS":,"DROOLING TENDANCY":,  }
doglist=[canecorso,doberman]
cmpr=[]
cmpr.clear()
v=[1,2,3,4,5]#variable for each dog
c=[1,2,3,4,5]#checkbutton for each dog
l=[1,2,3,4,5]#label for each dog
ctr=0 



"""
def breedadder (name,orig,clas):
    name=dict()

"""
   
def apnd(dg):
    cmpr.append(dg)

w=Tk()
w.geometry("1000x700")

for i in doglist:
 v[ctr]=StringVar()
 c[ctr]= Checkbutton(w,text=doglist[ctr]["NAME"],onvalue=2,offvalue=3,command= apnd(str(doglist[ctr]["NAME"])),variable=v[ctr])
 c[ctr].grid(row=0,column=ctr)
 #c[ctr]= Checkbutton(w,text="doberman",command= apnd("doberman"))
 #c[ctr].grid(row=0,column=1)
 ctr+=1

ctr=0
for i in cmpr:
 l[ctr]=Label(w,text="Name:"+doglist[ctr]["NAME"])
 l[ctr].grid(row=1,column=ctr)
 ctr+=1
l[ctr]=Label(w,text="Origine:"+canecorso["ORIGINE"])
l[ctr].grid(row=2,column=0)
l[ctr]=Label(w,text="Class:"+canecorso["CLASS"])
l[ctr].grid(row=3,column=0)
l4=Label(w,text="Name:"+doberman["NAME"])
l4.grid(row=1,column=1)
l5=Label(w,text="Name:"+doberman["ORIGINE"])
l5.grid(row=2,column=1)
l6=Label(w,text="Name:"+doberman["CLASS"])
l6.grid(row=3,column=1)




w.mainloop()

print(cmpr)
