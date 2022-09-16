import tkinter 
root = tkinter.Tk()
root.title("Links-Shortcut")
root.configure(background="gray99")
sw= tkinter.Scrollbar(root) 
sw.pack(side=RIGHT, fill=Y)


os.chdir("C:\Bo_Link")
with open('Bo_ol_links.csv', 'r', newline='') as fo:
    lis=[line.strip('\r\n').split(',') for line in fo]        # create a list of lists
lis=sorted(lis)
    #print (lis)

for i,x in enumerate(lis):
    btn = tkinter.Button(root,height=1, width=20,relief=tkinter.FLAT,bg="gray99",fg="purple3",font="Dosis",text=lis[i][0],command=lambda i=i,x=x: openlink(i))
    btn.pack(padx=10,pady=5,side=tkinter.TOP)

def openlink(i):
    os.startfile(lis[i][1])

root.mainloop()
