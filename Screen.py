import tkinter as tk
from PIL import ImageTk,Image
import subprocess
import pygame


#--------Membuat GUI
root = tk.Tk()
root.title('Login')
root.config(bg='#979cd2')
root.geometry('400x680')
root.resizable(False,False)

#--------Music
pygame.mixer.init()
pygame.mixer.music.load('music2.wav')
pygame.mixer.music.play(loops=-1)



#--------Membuat Frame Utama   
frame=tk.Frame(root)
frame.grid(row=0,column=0)

#-------Menambahkan background Frame
image = Image.open('love and joy.png')
image_login = ImageTk.PhotoImage(image)
label_img = tk.Label(frame, image=image_login, border=0)
label_img.grid()


#--------membuat frame untuk tombol
mainframe=tk.Frame(frame,bg='#979cd2')
mainframe.grid(row=0,column=0)

#--------Membuat fungsi play
def play():
    pygame.mixer.music.stop()
    root.destroy()
    subprocess.run(["python", "Project UAS.py"])   

#--------Membuat fungsi help   
def help():
    #--------Membuat fungsi back
    def back():
        pygame.mixer.music.stop()
        root.destroy()
        subprocess.run(["python", "Screen.py"])
    frame.destroy()
    
    help_screen= tk.Frame(root,background='#979cd2')
    help_screen.pack()
    #--------Halaman 1
    def page_1():
        image1=Image.open('1.png')
        image_help=ImageTk.PhotoImage(image1)
        image1_label=tk.Label(help_screen,image=image_help,border=0,justify='center')
        image1_label.grid(row=0,column=0,columnspan=3)
    
        back_button=tk.Button(help_screen,text='back',command=back,width=20,border=0,bg='white')
        back_button.grid(row=1,column=0,pady=40)
    
        next_button=tk.Button(help_screen,text='next',command=page_2,width=20,border=0,bg='white')
        next_button.grid(row=1,column=2,pady=40)
        help_screen.mainloop()

    #--------Halaman 2
    def page_2():
        image2=Image.open('2.png')
        image_help=ImageTk.PhotoImage(image2)
        image2_label=tk.Label(help_screen,image=image_help,border=0,justify='center')
        image2_label.grid(row=0,column=0,columnspan=3)
    
        back_button=tk.Button(help_screen,text='back',command=page_1,width=20,border=0,bg='white')
        back_button.grid(row=1,column=0,pady=40)
    
        next_button=tk.Button(help_screen,text='next',command=page_3,width=20,border=0,bg='white')
        next_button.grid(row=1,column=2,pady=40)
        help_screen.mainloop()
    
    #--------Halaman 3
    def page_3():
        image3=Image.open('3.png')
        image_help=ImageTk.PhotoImage(image3)
        image3_label=tk.Label(help_screen,image=image_help,border=0,justify='center')
        image3_label.grid(row=0,column=0,columnspan=3)
    
        back_button=tk.Button(help_screen,text='back',command=page_2,width=20,border=0,bg='white')
        back_button.grid(row=1,column=0,pady=40)
    
        next_button=tk.Button(help_screen,text='next',command=page_4,width=20,border=0,bg='white')
        next_button.grid(row=1,column=2,pady=40)
        help_screen.mainloop()
    
    #--------Halaman 4
    def page_4():
        image4=Image.open('4.png')
        image_help=ImageTk.PhotoImage(image4)
        image4_label=tk.Label(help_screen,image=image_help,border=0,justify='center')
        image4_label.grid(row=0,column=0,columnspan=3)
    
        back_button=tk.Button(help_screen,text='back',command=page_3,width=20,border=0,bg='white')
        back_button.grid(row=1,column=0,pady=40)
    
        next_button=tk.Button(help_screen,text='next',command=page_5,width=20,border=0,bg='white')
        next_button.grid(row=1,column=2,pady=40)
        help_screen.mainloop()

    #--------Halaman 5
    def page_5():
        image5=Image.open('5.png')
        image_help=ImageTk.PhotoImage(image5)
        image5_label=tk.Label(help_screen,image=image_help,border=0,justify='center')
        image5_label.grid(row=0,column=0,columnspan=3)
    
        back_button=tk.Button(help_screen,text='back',command=page_4,width=20,border=0,bg='white')
        back_button.grid(row=1,column=0,pady=40)
    
        next_button=tk.Button(help_screen,text='next',command=page_6,width=20,border=0,bg='white')
        next_button.grid(row=1,column=2,pady=40)
        help_screen.mainloop()
    
    #--------Halaman 6
    def page_6():
        image6=Image.open('6.png')
        image_help=ImageTk.PhotoImage(image6)
        image6_label=tk.Label(help_screen,image=image_help,border=0,justify='center')
        image6_label.grid(row=0,column=0,columnspan=3)
    
        back_button=tk.Button(help_screen,text='back',command=page_5,width=20,border=0,bg='white')
        back_button.grid(row=1,column=0,pady=40)
    
        next_button=tk.Button(help_screen,text='next',command=page_7,width=20,border=0,bg='white')
        next_button.grid(row=1,column=2,pady=40)
        help_screen.mainloop()
    
    #--------Halaman 7
    def page_7():
        image7=Image.open('7.png')
        image_help=ImageTk.PhotoImage(image7)
        image7_label=tk.Label(help_screen,image=image_help,border=0,justify='center')
        image7_label.grid(row=0,column=0,columnspan=3)
    
        back_button=tk.Button(help_screen,text='back',command=page_6,width=20,border=0,bg='white')
        back_button.grid(row=1,column=0,pady=40)
    
        next_button=tk.Button(help_screen,text='next',command=page_8,width=20,border=0,bg='white')
        next_button.grid(row=1,column=2,pady=40)
        help_screen.mainloop()

    #--------Halaman 8
    def page_8():
        image8=Image.open('8.png')
        image_help=ImageTk.PhotoImage(image8)
        image8_label=tk.Label(help_screen,image=image_help,border=0,justify='center')
        image8_label.grid(row=0,column=0,columnspan=3)
    
        back_button=tk.Button(help_screen,text='back',command=page_7,width=20,border=0,bg='white')
        back_button.grid(row=1,column=0,pady=40)
    
        next_button=tk.Button(help_screen,text='next',command=page_9,width=20,border=0,bg='white')
        next_button.grid(row=1,column=2,pady=40)
        help_screen.mainloop()
    
    #--------Halaman 9
    def page_9():
        image9=Image.open('9.png')
        image_help=ImageTk.PhotoImage(image9)
        image9_label=tk.Label(help_screen,image=image_help,border=0,justify='center')
        image9_label.grid(row=0,column=0,columnspan=3)
    
        back_button=tk.Button(help_screen,text='back',command=page_8,width=20,border=0,bg='white')
        back_button.grid(row=1,column=0,pady=40)
    
        next_button=tk.Button(help_screen,text='next',command=page_10,width=20,border=0,bg='white')
        next_button.grid(row=1,column=2,pady=40)
        help_screen.mainloop()

    #--------Halaman 10
    def page_10():
        image10=Image.open('10.png')
        image_help=ImageTk.PhotoImage(image10)
        image10_label=tk.Label(help_screen,image=image_help,border=0,justify='center')
        image10_label.grid(row=0,column=0,columnspan=3)
    
        back_button=tk.Button(help_screen,text='back',command=page_9,width=20,border=0,bg='white')
        back_button.grid(row=1,column=0,pady=40)
    
        next_button=tk.Button(help_screen,text='next',command=page_11,width=20,border=0,bg='white')
        next_button.grid(row=1,column=2,pady=40)
        help_screen.mainloop()

    #--------Halaman 11
    def page_11():
        image11=Image.open('11.png')
        image_help=ImageTk.PhotoImage(image11)
        image10_label=tk.Label(help_screen,image=image_help,border=0,justify='center')
        image10_label.grid(row=0,column=0,columnspan=3)
    
        back_button=tk.Button(help_screen,text='back',command=page_10,width=20,border=0,bg='white')
        back_button.grid(row=1,column=0,pady=40)
    
        next_button=tk.Button(help_screen,text='finish',command=back,width=20,border=0,bg='white')
        next_button.grid(row=1,column=2,pady=40)
        help_screen.mainloop()
    
    page_1()

#--------Fungsi EXIT 
def exit():
    root.destroy()
    
#--------Tombol tombol(Play,Help,Exit)   
play_button=tk.Button(mainframe, text='Play',bg='#979cd2',anchor='center',border=0,font=('Santai',20),activebackground='white'
                      ,command=play)
play_button.grid(row=0,column=0)

help_button=tk.Button(mainframe,text='Help',bg='#979cd2',anchor='center',border=0,font=('Santai',20),activebackground='white'
                      ,command=help)
help_button.grid(row=1,column=0)

exit_button=tk.Button(mainframe,text='EXIT',bg='#979cd2',anchor='center',border=0,font=('Santai',20),activebackground='white'
                      ,command=exit)
exit_button.grid(row=2,column=0)

root.mainloop()
