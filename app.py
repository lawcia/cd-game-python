from tkinter import *
import tkinter as tk
import random
from time import sleep
x=0
alltheletters= []
count=30
class mainthing:
    def __init__(self,window,title,geometry):
        self.window=window
        self.window.title(title)
        self.window.geometry(geometry)
        self.window.resizable(False,False)
        self.pageshow=StarterPage(self,self.window)
    def change(self,page):
        self.page=page
        if self.page == 0:
            self.pageshow = StarterPage
        if self.page == 1:
            self.pageshow= Round1(self,self.window)
#starterpage
class StarterPage():
    def __init__(self,parent,window):
        self.parent=parent
        self.frame=Frame(window,bg="#0797DD")
        self.frame.pack()
        window.configure(bg="#0797DD")
        

        self.welcome= Label(self.frame, text='WELCOME TO COUNTDOWN',font=("Georgia",40),bg="#0797DD", fg="white")
        self.welcome.grid(column=1,row=0)

        self.name= Label(self.frame, text='YOUR NAME:',font=("Ariel",20),bg="#0797DD", fg="white")
        self.name.grid(column=1,row=1)

        self.namebar= Entry(self.frame)
        self.namebar.grid(column=1,row=2,ipadx=70,ipady=10)

        self.submit = Button(self.frame, text='NEXT',command=self.clicked,font=("Ariel",20),bg="#0797DD", fg="white")
        self.submit.grid(column=1,row=3)
    def clicked(self):
        self.frame.destroy()
        self.parent.change(1)
    
#thelettergame
class Round1():
    def __init__(self,parent,window):
     
        self.parent=parent
        self.frame=Frame(window)
        self.frame.pack()
        global x
        global alltheletters
        
    
        
    
        #grid
        self.box0=Label(window,text="",bg="#FFFFFF",fg="black")
        self.box0.place(x=220,y=250,width=50,height=40)
        self.box1=Label(window,text="",bg="#FFFFFF",fg="black")
        self.box1.place(x=280,y=250,width=50,height=40)
        self.box2=Label(window,text="",bg="#FFFFFF",fg="black")
        self.box2.place(x=340,y=250,width=50,height=40)
        self.box3=Label(window,text="",bg="#FFFFFF",fg="black")
        self.box3.place(x=400,y=250,width=50,height=40)
        self.box4=Label(window,text="",bg="#FFFFFF",fg="black")
        self.box4.place(x=460,y=250,width=50,height=40)
        self.box5=Label(window,text="",bg="#FFFFFF",fg="black")
        self.box5.place(x=520,y=250,width=50,height=40)
        self.box6=Label(window,text="",bg="#FFFFFF",fg="black")
        self.box6.place(x=580,y=250,width=50,height=40)
        self.box7=Label(window,text="",bg="#FFFFFF",fg="black")
        self.box7.place(x=640,y=250,width=50,height=40)
        self.box8=Label(window,text="",bg="#FFFFFF",fg="black")
        self.box8.place(x=700,y=250,width=50,height=40)
        #end of grid
        #buttons for vowels and constant
        self.btn1=Button(window, text="Vowels", fg='Black',bg="#328fa8",font=("Normal",12),command=self.vowel_click)
        self.btn1.place(x=145, y=250)
        self.btn2=Button(window,text="Consonants", fg='Black',bg="#328fa8",font=("Normal",12),command=self.consonants_click)
        self.btn2.place(x=760,y=250)
        #end o fbuttons for vowels and constant
        #label
        self.lbl1=Label(window, text="Welcome to Countdown", fg='white', font=("Ariel",30),bg="#328fa8")
        self.lbl1.place(x=305, y=100)
    #what happens when you click the vowels button
        seconds=StringVar()
        seconds.set("00")
        self.timer=Entry(window,textvariable=seconds)
        self.timer.place(x=450,y=300,width=50,height=40)
    def timer(self):
        global seconds
        times=int(seconds.get())
        window.update()
        time.sleep(1)
        if times==0:
            print("Time is up")
        times-=1
        
        

    def vowel_click(self):
        global x
        global alltheletters
        global count
        global timer
     
        consonants=["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T",'V','W','X','Y','Z']
        number=random.randint(0,4)
        vowels=["A","E","I","O","U"]
        chosenvowel=vowels[number]
        print(chosenvowel)
  
        if (len((self.box0['text']))== 0) and self.box0['text'] != consonants :
            self.box0.config(text=chosenvowel)
            alltheletters.append(chosenvowel)
            x=x+1
            
        elif (len((self.box1['text']))== 0) and self.box0['text'] != consonants :
            self.box1.config(text=chosenvowel)
            alltheletters.append(chosenvowel)
            x=x+1

        elif (len((self.box2['text']))== 0) and self.box0['text'] != consonants :
            self.box2.config(text=chosenvowel)
            alltheletters.append(chosenvowel)
            x=x+1
   
        elif (len((self.box3['text']))== 0) and self.box0['text'] != consonants :
            self.box3.config(text=chosenvowel)
            alltheletters.append(chosenvowel)
            x=x+1

        elif (len((self.box4['text']))== 0) and self.box0['text'] != consonants :
            self.box4.config(text=chosenvowel)
            x=x+1

        elif (len((self.box5['text']))== 0) and self.box0['text'] != consonants :
            self.box5.config(text=chosenvowel)
            alltheletters.append(chosenvowel)
            x=x+1

        elif (len((self.box6['text']))== 0) and self.box0['text'] != consonants :
            self.box6.config(text=chosenvowel)
            alltheletters.append(chosenvowel)
            x=x+1
 
        elif (len((self.box7['text']))== 0) and self.box0['text'] != consonants :
            self.box7.config(text=chosenvowel)
            alltheletters.append(chosenvowel)
            x=x+1
   
        elif (len((self.box8['text']))== 0) and self.box0['text'] != consonants :
            self.box8.config(text=chosenvowel)
            alltheletters.append(chosenvowel)
            x=x+1

        elif x==9:
            self.btn1.config(state=DISABLED)
            self.btn2.config(state=DISABLED)
            print(alltheletters)
            self.timer()
            
            
            
    
                
            
        #for x in range(0,8):
            #if len((self.box[x]['text']))== 1:
                #print("YES")
            #else:
                #print("NO")
                #self.box0.config(text=chosenvowel)
                    
                
                
        
    #what happend when you click the consonant button
    def consonants_click(self):
        global x
        global alltheletters
        global count
        vowels=["A","E","I","O","U"]
        number= random.randint(0,20)
        consonants=["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T",'V','W','X','Y','Z']
        chosenconsonants= consonants[number]
        print(chosenconsonants)
        if (len((self.box0['text']))== 0) and self.box0['text'] != vowels :
            self.box0.config(text=chosenconsonants)
            alltheletters.append(chosenconsonants)
            x=x+1
            
        elif (len((self.box1['text']))== 0) and self.box0['text'] != vowels :
            self.box1.config(text=chosenconsonants)
            alltheletters.append(chosenconsonants)
            x=x+1

        elif (len((self.box2['text']))== 0) and self.box0['text'] != vowels :
            self.box2.config(text=chosenconsonants)
            alltheletters.append(chosenconsonants)
            x=x+1
        elif (len((self.box3['text']))== 0) and self.box0['text'] != vowels :
            self.box3.config(text=chosenconsonants)
            alltheletters.append(chosenconsonants)
            x=x+1
        elif (len((self.box4['text']))== 0) and self.box0['text'] != vowels :
            self.box4.config(text=chosenconsonants)
            alltheletters.append(chosenconsonants)
            x=x+1
        elif (len((self.box5['text']))== 0) and self.box0['text'] != vowels :
            self.box5.config(text=chosenconsonants)
            alltheletters.append(chosenconsonants)
            x=x+1
        elif (len((self.box6['text']))== 0) and self.box0['text'] != vowels :
            self.box6.config(text=chosenconsonants)
            alltheletters.append(chosenconsonants)
            x=x+1
        elif (len((self.box7['text']))== 0) and self.box0['text'] != vowels :
            self.box7.config(text=chosenconsonants)
            alltheletters.append(chosenconsonants)
            x=x+1
        elif (len((self.box8['text']))== 0) and self.box0['text'] != vowels :
            self.box8.config(text=chosenconsonants)
            alltheletters.append(chosenconsonants)
            x=x+1
        elif x==9:
            self.btn1.config(state=DISABLED)
            self.btn2.config(state=DISABLED)
            print(alltheletters)
            timer()
                
            

        
        

        
def main():
    window = Tk()
    mainthing(window,"Countdown","1000x500")
    window.mainloop
if __name__ == "__main__":
    
    main()
    
    #window=Tk()
    #main= Round1(window)
    #window.title("Countdown")
    #window.geometry("1000x500")
    #window.config(bg="#328fa8")
    #window.mainloop()
    
    
#Entry_box=Entry(window,text="Enter your word",bg="#328fa8")
#Entry_box.place(x=290 ,y=300,height = 50 , width = 460)



# data = Entry_box.get() to store the data of entry box
# btn/destroy()to delete the buttons