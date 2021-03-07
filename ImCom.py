#!/usr/bin/python
import PIL.Image
import tkinter as tk
from tkinter import *
from tkinter import filedialog 
import winsound
import tkinter.messagebox as mbox
import cv2
import numpy as np
import os
def select_file():
 file.config(state='normal')
 file.delete(0, 'end')
 global source_file
 source_file=filedialog.askopenfilename()#file dialog for select source file
 file.insert(0,source_file)
 file.config(state='readonly')
 return
def select_destination_folder():
 folder.config(state='normal')
 folder.delete(0, 'end')
 global destination_folder
 destination_folder=filedialog.askdirectory()#file dialog for destinastion folder
 folder.insert(0,destination_folder)
 folder.config(state='readonly')
 return
def compress():
 try:
     #get elements
  w=width.get()
  h=height.get()
  f=file.get()
  fd=folder.get()
  desti_file_extension=v.get()
  i=len(f)
  #find source file name from path  
  i-=1
  while(f[i]!="/"):
   i-=1
  j=i+1
  file_name=""
  l=len(f)
  l-=1
  while(j<(l)or j==l):
   file_name=file_name+f[j]
   j+=1
  j=0
  #find source directory name from path
  source_dir_name=""
  while(j<i):
   source_dir_name=source_dir_name+f[j]
   j+=1
  os.chdir(str(source_dir_name))#goto source directory
  img = cv2.imread(file_name)#read image
  compress_file= cv2.resize(img, (int(w),int(h)), interpolation = cv2.INTER_AREA)#resize image with atribute
  result = np.vstack([compress_file])#map the image
  os.chdir(str(fd)) #goto the destination folder
  #find the file name  without extension
  s=len(file_name)
  s-=1
  while(file_name[s]!="."):
   s-=1
  desti_file_name=""
  j=0
  while(j<s):
   desti_file_name=desti_file_name+ file_name[j]
   j+=1
  desti_file_name=desti_file_name+'_imcom'+desti_file_extension#destination file name
  cv2.imwrite(desti_file_name,result)#save the file  at destination folder
  mbox.showinfo("Success","Image compressed succesfuly!")
 #open resized image
  img2=PIL.Image.open(desti_file_name)
  img2.show()
  #open original image 
  os.chdir(str(source_dir_name))
  img1=PIL.Image.open(file_name)
  img1.show()
 except:
   mbox.showinfo("Failed","Please enter valied data!")
 return
def form():
    #disign of window
 global screen
 screen=tk.Tk()
 screen.title('ImCom_Rsizer')
 screen.iconbitmap("logo.ico")
 screen.config(bg="#FA8072")
 screen.minsize(750,550)
 f1=tk.Frame(screen)
 f1.config(bg="#FA8072")
 f1.pack(side=tk.TOP,fill=tk.BOTH)
 l=tk.Label(f1,text="ImCom",bg="brown",fg="yellow",font=('Comic Sans MS',30))
 l.pack(fill=tk.X)
 f2=tk.Frame(screen)
 f2.config(bg="#FA8072")
 f2.pack(fill=tk.BOTH,ipady=20)
 l2=tk.Label(f2,text="Input File :                ",font=('Italic'),bg="yellow")
 l2.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 global file
 file=tk.Entry(f2,bg="burlywood",font=(20),width=50)
 file.config(state='readonly')
 file.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 browsefile=tk.Button(f2,text="BROWSE",bg="blue",fg="white",width=10,height=1,command=select_file)
 browsefile.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 f3=tk.Frame(screen)
 f3.config(bg="#FA8072")
 f3.pack(fill=tk.BOTH,ipady=30)
 l3=tk.Label(f3,text="Destination Folder :",font=('Italic'),bg="yellow")
 l3.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 global folder
 folder=tk.Entry(f3,bg="burlywood",font=(20),width=50)
 folder.config(state='readonly')
 folder.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 browsefolder=tk.Button(f3,text="BROWSE",bg="blue",fg="white",width=10,height=1,command=select_destination_folder)
 browsefolder.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 f4=tk.Frame(screen)
 f4.config(bg="#FA8072")
 f4.pack(fill=tk.BOTH,ipady=30)
 l4=tk.Label(f4,text="Height:",font=('Italic'),bg="yellow")
 l4.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 global height
 height=tk.Entry(f4,bg="burlywood",font=(20),width=15)
 height.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 l5=tk.Label(f4,text="Width:",font=('Italic'),bg="yellow")
 global width
 l5.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 width=tk.Entry(f4,bg="burlywood",font=(20),width=15)
 width.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 f5=tk.Frame(screen)
 f5.config(bg="#FA8072")
 f5.pack(fill=tk.BOTH,ipady=15)
 l6=tk.Label(f5,text="Compress File Type:",font=('Italic'),bg="yellow")
 l6.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 global v
 v=StringVar(screen)
 v.set(".jpeg")
 filetype=tk.OptionMenu(f5,v,'.jpeg','.jpg','.png')
 filetype.config(bg="#f7960a")
 filetype.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 f6=tk.Frame(screen)
 f6.config(bg="#FA8072")
 f6.pack(side=tk.BOTTOM,fill=tk.BOTH)
 can=tk.Button(f6,text="CANCEL",command=destroy,bg="red",fg="white",font=('bold'))
 can.pack(side=tk.RIGHT,pady=10,padx=10)
 com=tk.Button(f6,text="COMPRESS",bg="blue",fg="white",font=('bold'),command=compress)
 com.pack(side=tk.RIGHT,pady=10,padx=10,ipadx=9)
 screen.mainloop()
 return
def destroy():#destroy the window
 winsound.Beep(300,500)
 screen.destroy()
 return
form()#calling function
