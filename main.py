
from tkinter import *
import random

global questions_answers
names_list = []
asked =[]
score =0



question_answers = {
  1: ["What must you do when you see blue and red flashing light   behind you?",'Speed up to get out the way','Slow down and drive carefully','Slow down and stop','Drive on as usual','Slow down and drive',3],
  2: ["You may stop on a motorway only",'if there is an emergency','To let down or pick up passengers','To make a U-turn','To stop and take a photo','If there is an emergency',1],
  3: ["When coming up to a pedestrian crossing without a raised traffic island, what must you do?","Speed up before the predestrians cross",'Stop and give way to the pedestrians on any part of the crossing',"Sound the horn on your vehicle to warn the pedestrians","Slow down to 30 Kms",'Stop and give way to the pedestrians on any part of the crossing',2],
  4: ["can you stop on a bus stop in a private motor vehicle", 'Only between midnight and 6am', "Under no circumstances", "When dropping off passengers", 'Only if it is less than 5 minutes', "Under no cirumstances", 2],
  5: ["what is the maximum speed you can drive if you have a 'space saver wheel' fitted? (km/h)", '70 km/h', "100 km/h so you do not hold up traffic", "80 km/h and if the wheel spacer displays a lower limit that applies", "90 km/h", "80 km/h and if the wheel spacer displays a lower limit that applies",3],
  6: ["When following another vehicle on a dusty road, You should?",'Speed up to get passed',"Turn your vehicle's windscreen wipers on","Stay back from the dust cloud",'Turn your vehicles headlights on',"Stay back from the dust cloud",3],
  7: ["What does the sign containing the letters 'LSZ' mean", 'Low safety zone', "Low stability zone", "Lone star zone", 'Limited speed zone', 'Limited speed zone',4],
  8: ["What speed are you allowed to pass a school bus that has stopped to let students on or off?", '20 km/h', "30 km/h", "70 km/h", '10 km/h','20 km/h',1],
  9: ["What is the maximum distance a load may extend in front of a car?", '2 meters forward of the front seat', "4 meters forward of the front edge of the front seat", "3 meters forward of the front egde of the front seat", '2.5 meters forward of the front edge of the front seat', '3 meters forward of the front edge of the front seat',3],
  10: ["To avoid being blinded by the headlights of another vehicle coming towards you what should you do?", 'Look to the left of the road', "Look to the centre of the road", "Wear sunglasses that have sufficient strength", 'Look to the right side of the road', 'Look to the left of the road',1],
}

def randomiser():
  global qnum 
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()

class QuizStarter:
    def __init__(self, parent): 
        background_color="deeppink"
        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()    
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="NZ Road Rules", font=("TimesNewRoman","18"        ,"bold"),bg=background_color)
        self.heading_label.grid(row=0, padx=20) 
        self.var1=IntVar()   
        #label for username~        
        self.user_label=Label(self.quiz_frame, text="Please enter your username below: ", font=("Times New Roman","16"),bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20)        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="lightcyan", command=self.name_collection)
        self.continue_button.grid(row=3,  padx=20, pady=20)        
        
        #image
        #log  o = PhotoImage(file="road.gif")
        #self.logo = Label(self.quiz_frame, image=logo)  
        #self.logo.grid(row=4,padx=20, pady=20)   
       

    def name_collection(self):
        name=self.entry_box.get()
        names_list.append(name) #add name to names list declared at the beginning
        self.continue_button.destroy()
        self.entry_box.destroy() #Destroy name frame then open the quiz runner
        
      
        

class Quiz:
  def _init_(self, parent):
    
    #color selection
    background_color="deeppink"

    self.quiz_frame=Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()
    #question
    self.question_label=Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Tw Cen Mt","16"),bg=background_color)
    self.question_label.grid(row=1, padx=10, pady=10)

   #holds value of radio buttons
    self.var1=IntVar()

    #radio button 1
    self.rb1= Radiobutton(self.quiz_frame, text=questions_asnwers[qnum][1], font=("Helvetica","12"), bg=background_color,value=1,padx=10,pady=10,
    variable=self.var1, indicator = 0, background = "light blue")
    self.rb1.grid(row=2, sticky=w)

     # radio button 2
    self.rb2= Radiobutton(self.quiz_frame, text=questions_asnwers[qnum][2], font=("Helvetica","12"), bg=background_color,value=2,padx=10,pady=10,
    variable=self.var1, indicator = 0, background = "light blue")
    self.rb2.grid(row=3, sticky=w)

     #radio button 3
    self.rb3= Radiobutton(self.quiz_frame, text=questions_asnwers[qnum][3], font=("Helvetica","12"), bg=background_color,value=3,padx=10,pady=10,
    variable=self.var1, indicator = 0, background = "light blue")
    self.rb3.grid(row=4, sticky=w)

     # radio button 4
    self.rb4= Radiobutton(self.quiz_frame, text=questions_asnwers[qnum][4], font=("Helvetica","12"), bg=background_color,value=4,padx=10,pady=10,
    variable=self.var1, indicator = 0, background = "light blue")
    self.rb4.grid(row=5, sticky=w)

    #confirm button
    self.quiz_instance= Button(self.quiz_frame, text="Confirm", font=("Helvetica", "13", "bold"), bg="SpringGreen3")
    self.quiz_instance.grid(row=7, padx=5, pady=5)

    #score label
    self.score_label=Label(self.quiz_frame, text="SCORE", font=("Tw Cen MT","16"),bg=background_color,)
    self.score_label.grid(row=8, padx=10, pady=1)


randomiser()
if __name__ == "__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz") 
    quiz_ins = QuizStarter(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear
          
    
          