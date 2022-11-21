from tkinter import *
import random
from time import sleep


class Mainthing:
    def __init__(self,window,title,geometry):
        self.window=window
        self.window.title(title)
        self.window.geometry(geometry)
        self.window.resizable(False,False)
        self.pageshow=StarterPage(self,self.window)

    def change(self,page):
        self.page=page
        if self.page == 0:
            self.pageshow = StarterPage(self, self.window)
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
    # here I have defined the variables I know I want to use in this round
    # it will be available throughout the class using "self"
    x=0
    alltheletters= []
    count=30
    vowels=["A","E","I","O","U"]
    consonants=["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T",'V','W','X','Y','Z']

    def __init__(self,parent,window):
     
        self.parent=parent
        self.frame=Frame(window)
        self.frame.pack()
        
        # we need to assign window to this class,
        # so we can access it later in this program 
        # docs [https://www.programiz.com/article/python-self-why]
        self.window = window
    
        #grid
        self.boxes = [
            Label(window, text="", bg="#FFFFFF", fg="black"),
            Label(window, text="", bg="#FFFFFF", fg="black"),
            Label(window, text="", bg="#FFFFFF", fg="black"),
            Label(window, text="", bg="#FFFFFF", fg="black"),
            Label(window, text="", bg="#FFFFFF", fg="black"),
            Label(window, text="", bg="#FFFFFF", fg="black"),
            Label(window, text="", bg="#FFFFFF", fg="black"),
            Label(window, text="", bg="#FFFFFF", fg="black"),
            Label(window, text="", bg="#FFFFFF", fg="black"),
        ]
        x_pos = 220
        for box in self.boxes:
            box.place(x=x_pos, y=250, width=50, height=40)
            x_pos += 60

        #end of grid

        #buttons for vowels and constant
        # should rename variables so that is easy to understand
        self.vowel_btn=Button(window, text="Vowels", fg='Black',bg="#328fa8",font=("Normal",12),command=self.vowel_click)
        self.vowel_btn.place(x=145, y=250)
        self.consonants_btn=Button(window,text="Consonants", fg='Black',bg="#328fa8",font=("Normal",12),command=self.consonants_click)
        self.consonants_btn.place(x=760,y=250)

        #end o fbuttons for vowels and constant
        #label
        self.lbl1=Label(window, text="Welcome to Countdown", fg='white', font=("Ariel",30),bg="#328fa8")
        self.lbl1.place(x=305, y=100)
        #what happens when you click the vowels button

        # since we are working with classes,
        # use "self" instead of global 
        # to assign seconds to the class
        # then we can access seconds from within our class using "self.seconds"
        self.seconds=StringVar()
        self.seconds.set("00")

        # it has been renamed to timer_entry to avoid name clashing 
        # since below we have defined a timer method that will have
        # different logic
        self.timer_entry=Entry(window,textvariable=self.seconds)
        self.timer_entry.place(x=450,y=300,width=50,height=40)

        self.word_entry=Entry(window)
    
    # this method uses "self.window" and "self.seconds"
    def timer(self):
        times=int(self.seconds.get())
        self.timer_entry.config(state="readonly")
        
        self.word_entry.place(x=350,y=450)
        
        
        while times >= 0:
            self.seconds.set("{0:2d}".format(times))
            self.window.update()
            sleep(1)
            if (times== 0):
                entry = Label(text="Time Over", bg="black", fg="white")
                # Place it within the window.
                entry.place(x=350,y=350)

                # Once Timer has ended check if word is in dictionary
                self.check_word()
            times-=1

    def vowel_click(self):
        number=random.randint(0,4)
        chosenvowel=self.vowels[number]
        print(chosenvowel)
        self.update_box(chosenvowel)

    #what happend when you click the consonant button
    def consonants_click(self):
        number=random.randint(0,20)
        chosenconsonant=self.consonants[number]
        print(chosenconsonant)
        self.update_box(chosenconsonant)


    def update_box(self, chosenletter):
        if self.x < 9:
            self.boxes[self.x].config(text=chosenletter)
            self.alltheletters.append(chosenletter)
            self.x += 1
        else:
            self.vowel_btn.config(state=DISABLED)
            self.consonants_btn.config(state=DISABLED)
            print(self.alltheletters)
            
            # start the timer
            self.timer()        
            
    
    # check if the word the user entered is in dictionary
    def check_word(self):
        word = self.word_entry.get()
        self.word_entry.config(state=DISABLED)
        print(word)
        # write code here to check if word is in dictionary
        
        

        
def main():
    window = Tk()
    # since its a class, normally it starts with a capital letter, like Mainthing
    Mainthing(window,"Countdown","1000x500")
    # mainloop is a function, it should be window.mainloop()
    window.mainloop()
if __name__ == "__main__":  
    main()
    

    