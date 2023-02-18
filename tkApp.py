from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox
import imageio
from threading import Thread
import random

root = Tk()
root.title("MAP")
root.geometry('600x570')

score = 0

# update score 
def update_score():
    total_score.place(relx=0.01,rely=0.1)
    score_label.config(text='Your Score: '+ str(score))
    score_label.place(relx=0.01,rely=0.15)
    if(score>=15):
        congo_frame = Tk()
        final_label=Label(congo_frame, text="CONGRATULATION!! YOU WON THIS GAME",bg = 'white',fg='green',font=('helvetica',20))
        final_label.pack(padx=150,pady=75) 
        Button(congo_frame , text='Quit' , command=congo_frame.quit,padx=10,pady=10).pack(padx=20,pady=20,ipadx=15)

def hide():
    # delete intro page label
    img_label.pack_forget()

    # hiding the correct label
    correct_label.grid_forget()
    #deleting the entrybox
    entry_box.delete(0,END)
    # clearing the frame 
    for widget in img_frame.winfo_children():
        widget.destroy()


# submit button  
def submit():
    global score
    if(entry_box.get().lower() == name):
        correct_label.config(text='CONGRATULATION!! your answer is correct...' , fg='green')
        correct_label.grid(row=5 , column=1 , pady=15,padx=20)
        submit_btn.config(state=DISABLED)
        score+=2
    else:
        correct_label.config(text='SORRY!! your answer is wrong...', fg='red')
        correct_label.grid(row=5 , column=1 , pady=15,padx=20)
        score-=1

    update_score()    

def quiz():
   global quiz_root
   quiz_root = Tk()
   quiz_root.geometry('600x570')
   quiz_root.title("QUIZ GAME")

   root_menu = Menu(quiz_root)
   quiz_root.config(menu = root_menu,bg='whitesmoke')

   quiz_exit = Menu(root_menu)
   root_menu.add_cascade(label='Exit',command=quiz_root.destroy)

    

def info():
    messagebox.showinfo('Information' , 'WE ARE WORKING ON NEWER UPDATES.\nTHANKS FOR YOUR CONCERN')
# state game def 
def india_state():
    submit_btn.config(state=NORMAL)
    hide()
    path='C:\\Users\\Sumit\\Documents\\Py codes\\tkinter app\\'
    img_frame.grid(padx=140,pady=5,row=0,column=1,columnspan=3)

    # list of images 
    lst_img = ['andaman and nicobar','andhra pradesh','arunachal pradesh','assam','bihar','chhattisgarh','goa','gujarat','haryana','himachal pradesh','jharkhand','karnataka','kerala','lakshadeep','madhya pradesh','maharashtra','manipur','meghalaya','mizoram','nagaland','odisha','punjab','rajasthan','sikkim','tamil nadu','tripura','uttar pradesh','uttarakhand','west bengal']
    
    global name
    global state_image
    name = random.choice(lst_img)
    pic =Image.open(path+name+'.png')   
    state_image = ImageTk.PhotoImage(pic.resize((300,300)))
    img_label = Label(img_frame,image=state_image,bg='whitesmoke')
    img_label.pack()

    text_label.grid(row=1 , column=1,pady=5)
    entry_box.grid(row=2,column=1,pady=10)
    submit_btn.grid(row=3,column=1,padx=50,pady=5, ipadx=9)
    button_next.grid(row=4,column=1,pady=5, padx=255,ipadx=15)
    # greet_label.grid(row=6 , column=1,sticky='s')
    greet_label.place(rely=0.95,relx=0.4)
    

my_menu = Menu(root)
root.config(menu = my_menu,bg='whitesmoke')

map_menu = Menu(my_menu, background='white',activebackground='red')
my_menu.add_cascade(label='Map' ,menu=map_menu)
map_menu.add_command(label="India" , command = india_state)
map_menu.add_separator()
map_menu.add_command(label='Other' , command=info)

quiz_menu = Menu(my_menu, background='white',activebackground='red')
my_menu.add_cascade(label='Quiz',menu=quiz_menu)
quiz_menu.add_command(label='Quiz Game' , command= quiz)

exit_menu = Menu(my_menu, background='white',activebackground='red')
my_menu.add_cascade(label='Exit',command=root.quit)

# Label(root,text='hello',bg='#2A2C2B',fg='white',font=('helvetica',12)).pack()

# labels in indian state def
img_frame = Frame(root, width=300,height=300)
button_next = Button(root ,text='NEXT' , command=india_state) 
entry_box=Entry(root,width=30, font=('helvetica',12))
submit_btn = Button(root,text='SUBMIT', command=submit)
text_label = Label(root ,bg='whitesmoke', text="what the name of the state ?", font=('helvetica',12))
correct_label = Label(root,text="",bg='whitesmoke', font=('helvetica',16))
greet_label= Label(root , text='Made with pure love' , bg='whitesmoke' , fg='#6488ea')
score_label = Label(root , text="" ,bg='whitesmoke',fg='green',font=('helvetica',11))
total_score = Label(root,text="Required Score: 15" , bg = 'whitesmoke' , fg='#003153',font=('helvetica',11))



my_label = Label(root)
my_label.pack()
videoname = video_name = "C:\\Users\\Sumit\\Documents\\Py codes\\tkinter app\\intro.mp4"
video = imageio.get_reader(videoname)


def play(label):
    for image in video.iter_data():
      frame = ImageTk.PhotoImage(Image.fromarray(image))
      my_label.config(image=frame)
      my_label.image=frame

    my_label.pack_forget()
   
thread = Thread(target=play , args=(my_label,))
thread.start()
img = ImageTk.PhotoImage(Image.open('C:\\Users\\Sumit\\Documents\\Py codes\\tkinter app\\drop_page.jpg').resize((600,670)))

img_label = Label(image= img)
img_label.pack()


root.mainloop()





