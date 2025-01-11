import tkinter as tk
from tkinter import messagebox
import subprocess
import pygame




window=tk.Tk()
window.title('HoM')
window.geometry('400x680')
window.resizable(False,False)
window.configure(background='#C5DFF8')

pygame.mixer.init()
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(loops=-1)

frame=tk.Frame(window)
frame.pack(pady=10)

#--------Initial Value
a=0
b=0
c=0
d=1
e=0

label=tk.Label(frame,text="House of Multiplication",font=("Santai", 15),bg='#C5DFF8')
label.pack()


def disablebutton():
    button1['state']=tk.DISABLED
    button2['state']=tk.DISABLED
    button3['state']=tk.DISABLED
    button4['state']=tk.DISABLED
    button5['state']=tk.DISABLED
    button6['state']=tk.DISABLED
    button7['state']=tk.DISABLED
    button8['state']=tk.DISABLED
    button9['state']=tk.DISABLED
    button10['state']=tk.DISABLED
    button11['state']=tk.DISABLED
    button12['state']=tk.DISABLED
    button13['state']=tk.DISABLED
    button14['state']=tk.DISABLED
    button15['state']=tk.DISABLED
    button16['state']=tk.DISABLED
    button17['state']=tk.DISABLED
    button18['state']=tk.DISABLED
    button19['state']=tk.DISABLED
    button20['state']=tk.DISABLED
    button21['state']=tk.DISABLED
    button22['state']=tk.DISABLED
    button23['state']=tk.DISABLED
    button24['state']=tk.DISABLED
    button25['state']=tk.DISABLED
    button26['state']=tk.DISABLED
    button27['state']=tk.DISABLED
    button28['state']=tk.DISABLED
    button29['state']=tk.DISABLED
    button30['state']=tk.DISABLED
    button31['state']=tk.DISABLED
    button32['state']=tk.DISABLED
    button33['state']=tk.DISABLED
    button34['state']=tk.DISABLED
    button35['state']=tk.DISABLED
    button36['state']=tk.DISABLED
    button37['state']=tk.DISABLED
    button38['state']=tk.DISABLED
    button39['state']=tk.DISABLED
    button40['state']=tk.DISABLED
    button41['state']=tk.DISABLED
    button42['state']=tk.DISABLED
    button43['state']=tk.DISABLED
    button44['state']=tk.DISABLED
    button45['state']=tk.DISABLED
    button46['state']=tk.DISABLED
    button47['state']=tk.DISABLED
    button48['state']=tk.DISABLED
    button49['state']=tk.DISABLED
    button50['state']=tk.DISABLED
    button51['state']=tk.DISABLED
    button52['state']=tk.DISABLED
    button53['state']=tk.DISABLED
    button54['state']=tk.DISABLED
    button55['state']=tk.DISABLED
    button57['state']=tk.DISABLED
    button58['state']=tk.DISABLED
    button59['state']=tk.DISABLED
    button60['state']=tk.DISABLED
    button61['state']=tk.DISABLED
    button62['state']=tk.DISABLED
    button63['state']=tk.DISABLED
    button64['state']=tk.DISABLED
    button65['state']=tk.DISABLED
    button66['state']=tk.DISABLED
    button67['state']=tk.DISABLED
    button68['state']=tk.DISABLED
    button69['state']=tk.DISABLED
    button70['state']=tk.DISABLED
    button71['state']=tk.DISABLED
    button72['state']=tk.DISABLED
    button73['state']=tk.DISABLED
    button74['state']=tk.DISABLED
    button75['state']=tk.DISABLED
    button76['state']=tk.DISABLED
    button77['state']=tk.DISABLED
    button78['state']=tk.DISABLED
    button79['state']=tk.DISABLED
    button80['state']=tk.DISABLED
    button81['state']=tk.DISABLED
    button82['state']=tk.DISABLED
    

#--------Back Button

def back():
    #--------Right Answe
    pygame.mixer.music.stop()
    window.destroy()
    subprocess.run(["python", "Screen.py"])
   
     
#--------Reset Button Config
def reset():
    global a,b,c,d,e
    a=0
    b=0
    c=0
    d=1
    e=0
    button1['bg']='white'
    button2['bg']='white'
    button3['bg']='white'
    button4['bg']='white'
    button5['bg']='white'
    button6['bg']='white'
    button7['bg']='white'
    button8['bg']='white'
    button9['bg']='white'
    button10['bg']='white'
    button11['bg']='white'
    button12['bg']='white'
    button13['bg']='white'
    button14['bg']='white'
    button15['bg']='white'
    button16['bg']='white'
    button17['bg']='white'
    button18['bg']='white'
    button19['bg']='white'
    button20['bg']='white'
    button21['bg']='white'
    button22['bg']='white'
    button23['bg']='white'
    button24['bg']='white'
    button25['bg']='white'
    button26['bg']='white'
    button27['bg']='white'
    button28['bg']='white'
    button29['bg']='white'
    button30['bg']='white'
    button31['bg']='white'
    button32['bg']='white'
    button33['bg']='white'
    button34['bg']='white'
    button35['bg']='white'
    button36['bg']='white'
    button37['bg']='white'
    button38['bg']='white'
    button39['bg']='white'
    button40['bg']='white'
    button41['bg']='white'
    button42['bg']='white'
    button43['bg']='white'
    button44['bg']='white'
    button45['bg']='white'
    button46['bg']='white'
    button47['bg']='white'
    button48['bg']='white'
    button49['bg']='white'
    button50['bg']='white'
    button51['bg']='white'
    button52['bg']='white'
    button53['bg']='white'
    button54['bg']='white'
    button55['bg']='white'
    button57['bg']='white'
    button58['bg']='white'
    button59['bg']='white'
    button60['bg']='white'
    button61['bg']='white'
    button62['bg']='white'
    button63['bg']='white'
    button64['bg']='white'
    button65['bg']='white'
    button66['bg']='white'
    button67['bg']='white'
    button68['bg']='white'
    button69['bg']='white'
    button70['bg']='white'
    button71['bg']='white'
    button72['bg']='white'
    button73['bg']='white'
    button74['bg']='white'
    button75['bg']='white'
    button76['bg']='white'
    button77['bg']='white'
    button78['bg']='white'
    button79['bg']='white'
    button80['bg']='white'
    button81['bg']='white'
    button82['bg']='white'

    buttona['bg']='white'
    buttonb['bg']='white'
    buttonc['bg']='white'
    buttond['bg']='white'
    buttone['bg']='white'
    buttonf['bg']='white'
    buttong['bg']='white'
    buttonh['bg']='white'
    buttoni['bg']='white'
    buttonj['bg']='white'
    buttonk['bg']='white'
    buttonl['bg']='white'
    buttonm['bg']='white'
    buttonn['bg']='white'
    buttono['bg']='white'
    buttonp['bg']='white'
    buttonq['bg']='white'
    buttonr['bg']='white'

    button1['text']="64"
    button2['text']='24'
    button3['text']='5'
    button4['text']='16'
    button5['text']='45'
    button6['text']='18'
    button7['text']='72'
    button8['text']='36'
    button9['text']='8'
    button10['text']='4'
    button11['text']='9'
    button12['text']='18'
    button13['text']='56'
    button14['text']='20'
    button15['text']='49'
    button16['text']='2'
    button17['text']='21'
    button18['text']='54'
    button19['text']='63'
    button20['text']='30'
    button21['text']='3'
    button22['text']='28'
    button23['text']='6'
    button24['text']='24'
    button25['text']='15'
    button26['text']='30'
    button27['text']='24'
    button28['text']='15'
    button29['text']='8'
    button30['text']='42'
    button31['text']='8'
    button32['text']='54'
    button33['text']='21'
    button34['text']='9'
    button35['text']='7'
    button36['text']='16'
    button37['text']='12'
    button38['text']='18'
    button39['text']='24'
    button40['text']='4'
    button41['text']='1'
    button42['text']='35'
    button43['text']='5'
    button44['text']='12'
    button45['text']='81'
    button46['text']='35'
    button47['text']='3'
    button48['text']='10'
    button49['text']='25'
    button50['text']='14'
    button51['text']='63'
    button52['text']='42'
    button53['text']='9'
    button54['text']='45'
    button55['text']='16'
    button57['text']='40'
    button58['text']='6'
    button59['text']='2'
    button60['text']='27'
    button61['text']='12'
    button62['text']='72'
    button63['text']='28'
    button64['text']='4'
    button65['text']='7'
    button66['text']='32'
    button67['text']='48'
    button68['text']='6'
    button69['text']='40'
    button70['text']='36'
    button71['text']='18'
    button72['text']='48'
    button73['text']='56'
    button74['text']='10'
    button75['text']='8'
    button76['text']='27'
    button77['text']='14'
    button78['text']='28'
    button79['text']='6'
    button80['text']='32'
    button81['text']='54'
    button82['text']='12'

    button1['state']=tk.NORMAL
    button2['state']=tk.NORMAL
    button3['state']=tk.NORMAL
    button4['state']=tk.NORMAL
    button5['state']=tk.NORMAL
    button6['state']=tk.NORMAL
    button7['state']=tk.NORMAL
    button8['state']=tk.NORMAL
    button9['state']=tk.NORMAL
    button10['state']=tk.NORMAL
    button11['state']=tk.NORMAL
    button12['state']=tk.NORMAL
    button13['state']=tk.NORMAL
    button14['state']=tk.NORMAL
    button15['state']=tk.NORMAL
    button16['state']=tk.NORMAL
    button17['state']=tk.NORMAL
    button18['state']=tk.NORMAL
    button19['state']=tk.NORMAL
    button20['state']=tk.NORMAL
    button21['state']=tk.NORMAL
    button22['state']=tk.NORMAL
    button23['state']=tk.NORMAL
    button24['state']=tk.NORMAL
    button25['state']=tk.NORMAL
    button26['state']=tk.NORMAL
    button27['state']=tk.NORMAL
    button28['state']=tk.NORMAL
    button29['state']=tk.NORMAL
    button30['state']=tk.NORMAL
    button31['state']=tk.NORMAL
    button32['state']=tk.NORMAL
    button33['state']=tk.NORMAL
    button34['state']=tk.NORMAL
    button35['state']=tk.NORMAL
    button36['state']=tk.NORMAL
    button37['state']=tk.NORMAL
    button38['state']=tk.NORMAL
    button39['state']=tk.NORMAL
    button40['state']=tk.NORMAL
    button41['state']=tk.NORMAL
    button42['state']=tk.NORMAL
    button43['state']=tk.NORMAL
    button44['state']=tk.NORMAL
    button45['state']=tk.NORMAL
    button46['state']=tk.NORMAL
    button47['state']=tk.NORMAL
    button48['state']=tk.NORMAL
    button49['state']=tk.NORMAL
    button50['state']=tk.NORMAL
    button51['state']=tk.NORMAL
    button52['state']=tk.NORMAL
    button53['state']=tk.NORMAL
    button54['state']=tk.NORMAL
    button55['state']=tk.NORMAL
    button57['state']=tk.NORMAL
    button58['state']=tk.NORMAL
    button59['state']=tk.NORMAL
    button60['state']=tk.NORMAL
    button61['state']=tk.NORMAL
    button62['state']=tk.NORMAL
    button63['state']=tk.NORMAL
    button64['state']=tk.NORMAL
    button65['state']=tk.NORMAL
    button66['state']=tk.NORMAL
    button67['state']=tk.NORMAL
    button68['state']=tk.NORMAL
    button69['state']=tk.NORMAL
    button70['state']=tk.NORMAL
    button71['state']=tk.NORMAL
    button72['state']=tk.NORMAL
    button73['state']=tk.NORMAL
    button74['state']=tk.NORMAL
    button75['state']=tk.NORMAL
    button76['state']=tk.NORMAL
    button77['state']=tk.NORMAL
    button78['state']=tk.NORMAL
    button79['state']=tk.NORMAL
    button80['state']=tk.NORMAL
    button81['state']=tk.NORMAL
    button82['state']=tk.NORMAL

    player_label['text']='Player-1 Turn'
    player_label['bg']='green'
 

#--------Config Answer Frame

def buttonclick(x):
    global a,b,c,d,e
    if x==1 and d==1 and button1['text']=='64':
        button1['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=64
        d=0
        e+=1
        if a!=8 or b!=8:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==1 and d==0 and button1['text']=='64':
        button1['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=64
        d=1
        e+=1
        if a!=8 or b!=8:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==2 and d==1 and button2['text']=='24':
        button2['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=64
        d=0
        e+=1
        if (a==4 and b==6 or a==6 and b==4 or a==3 and b==8 or a==8 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()
        
    elif x==2 and d==0 and button2['text']=="24":
        button2['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=24
        d=1
        e+=1
        if (a==4 and b==6 or a==6 and b==4 or a==3 and b==8 or a==8 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==3 and d==1 and button3['text']=='5':
        button3['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=5
        d=0
        e+=1
        if a==5 or b==5:
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==3 and d==0 and button3['text']=="5":
        button3['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=5
        d=1
        e+=1
        if a==5 or b==5:
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==4 and d==1 and button4['text']=='16':
        button4['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=16
        d=0
        e+=1
        if (a==4 and b==4 or b==4 and a==4 or a==2 and b==8 or b==2 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==4 and d==0 and button4['text']=="16":
        button4['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=16
        d=1
        e+=1
        if (a==4 and b==4 or b==4 and a==4 or a==2 and b==8 or b==2 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==5 and d==1 and button5['text']=='45':
        button5['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=45
        d=0
        e+=1
        if (a==9 and b==5 or b==9 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==5 and d==0 and button5['text']=="45":
        button5['bg']="red"
        player_label['bg']='green'
        player_label['text']='Player-1 Turn'
        c=45
        d=1
        e+=1
        if (a==9 and b==5 or b==9 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==6 and d==1 and button6['text']=='18':
        button6['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=18
        d=0
        e+=1
        if (a==9 and b==2 or b==9 and a==2 or a==3 and b==6 or a==6 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==6 and d==0 and button6['text']=="18":
        button6['bg']="red"
        player_label['bg']='green'
        player_label['text']='Player-1 Turn'
        c=18
        d=1
        e+=1
        if (a==9 and b==2 or b==9 and a==2 or a==3 and b==6 or a==6 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==7 and d==1 and button7['text']=='72':
        button7['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=72
        d=0
        e+=1
        if (a==9 and b==8 or b==9 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==7 and d==0 and button7['text']=="72":
        button7['bg']="red"
        player_label['bg']='green'
        player_label['text']='player-1 Turn'
        c=72
        d=1
        e+=1
        if (a==9 and b==8 or b==9 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==8 and d==1 and button8['text']=='36':
        button8['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=36
        d=0
        e+=1
        if (a==9 and b==4 or b==9 and a==4 or a==6 and b==6 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==8 and d==0 and button8['text']=="36":
        button8['bg']="red"
        player_label['bg']='green'
        player_label['text']='player-1 Turn'
        c=36
        d=1
        e+=1
        if (a==9 and b==4 or b==9 and a==4 or a==6 and b==6):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==9 and d==1 and button9['text']=='8':
        button9['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=8
        d=0
        e+=1
        if (a==8 and b==1 or b==8 and a==1 or a==2 and b==4 or a==4 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==9 and d==0 and button9['text']=="8":
        button9['bg']="red"
        player_label['bg']='green'
        player_label['text']='Player-1 Turn'
        c=8
        d=1
        e+=1
        if (a==8 and b==1 or b==8 and a==1 or a==2 and b==4 or a==4 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()
    elif x==10 and d==1 and button10['text']=='4':
        button10['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=4
        d=0
        e+=1
        if (a==4 and b==1 or b==4 and a==1 or a==2 and b==2 or a==2 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==10 and d==0 and button10['text']=="4":
        button10['bg']="red"
        
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=4
        d=1
        e+=1
        if (a==4 and b==1 or b==4 and a==1 or a==2 and b==2 or a==2 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==11 and d==1 and button11['text']=='9':
        button11['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=9
        d=0
        e+=1
        if (a==9 and b==1 or b==9 and a==1 or a==3 and b==3 or a==3 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==11 and d==0 and button11['text']=="9":
        button11['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=9
        d=1
        e+=1
        if (a==9 and b==1 or b==9 and a==1 or a==3 and b==3 or a==3 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==12 and d==1 and button12['text']=='18':
        button12['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=18
        d=0
        e+=1
        if (a==9 and b==2 or b==9 and a==2 or a==3 and b==6 or a==6 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==12 and d==0 and button12['text']=="18":
        button12['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=18
        d=1
        e+=1
        if (a==9 and b==2 or b==9 and a==2 or a==3 and b==6 or a==6 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==13 and d==1 and button13['text']=='56':
        button13['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=56
        d=0
        e+=1
        if (a==8 and b==7 or b==8 and a==7 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==13 and d==0 and button13['text']=="56":
        button13['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=56
        d=1
        e+=1
        if (a==8 and b==7 or b==8 and a==7 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==14 and d==1 and button14['text']=='20':
        button14['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=20
        d=0
        e+=1
        if (a==4 and b==5 or b==4 and a==5 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==14 and d==0 and button14['text']=="20":
        button14['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=20
        d=1
        e+=1
        if (a==4 and b==5 or b==4 and a==5 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==15 and d==1 and button15['text']=='49':
        button15['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=49
        d=0
        e+=1
        if (a==7 and b==7 or b==7 and a==7 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==15 and d==0 and button15['text']=="49":
        button15['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=49
        d=1
        e+=1
        if (a==4 and b==5 or b==4 and a==5 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==16 and d==1 and button16['text']=='2':
        button16['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=2
        d=0
        e+=1
        if (a==2 and b==1 or b==2 and a==1 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==16 and d==0 and button16['text']=="2":
        button16['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=2
        d=1
        e+=1
        if (a==2 and b==1 or b==2 and a==1 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==17 and d==1 and button17['text']=='21':
        button17['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=21
        d=0
        e+=1
        if (a==7 and b==3 or b==7 and a==3 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==17 and d==0 and button17['text']=="21":
        button17['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=21
        d=1
        e+=1
        if (a==7 and b==3 or b==7 and a==3 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==18 and d==1 and button18['text']=='54':
        button18['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=54
        d=0
        e+=1
        if (a==6 and b==9 or b==6 and a==9 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==18 and d==0 and button18['text']=="54":
        button18['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=54
        d=1
        e+=1
        if (a==6 and b==9 or b==6 and a==9 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==19 and d==1 and button19['text']=='63':
        button19['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=63
        d=0
        e+=1
        if (a==7 and b==9 or b==7 and a==9 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()


    elif x==19 and d==0 and button19['text']=="63":
        button19['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=63
        d=1
        e+=1
        if (a==7 and b==9 or b==7 and a==9 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==20 and d==1 and button20['text']=='30':
        button20['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=30
        d=0
        e+=1
        if (a==6 and b==5 or b==6 and a==5 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()


    elif x==20 and d==0 and button20['text']=="30":
        button20['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=30
        d=1
        e+=1
        if (a==6 and b==5 or b==6 and a==5 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==21 and d==1 and button21['text']=='3':
        button21['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=3
        d=0
        e+=1
        if (a==3 and b==1 or b==3 and a==1 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==21 and d==0 and button21['text']=="3":
        button21['bg']="red" 
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=3
        d=1
        e+=1
        if (a==3 and b==1 or b==3 and a==1 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==22 and d==1 and button22['text']=='28':
        button22['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=28
        d=0
        e+=1
        if (a==7 and b==4 or b==7 and a==4 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==22 and d==0 and button22['text']=="28":
        button22['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=28
        d=1
        e+=1
        if (a==7 and b==4 or b==7 and a==4 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==23 and d==1 and button23['text']=='6':
        button23['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=6
        d=0
        e+=1
        if (a==6 and b==1 or b==6 and a==1 or a==3 and b==2 or a==2 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==23 and d==0 and button23['text']=="6":
        button23['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=6
        d=1
        e+=1
        if (a==6 and b==1 or b==6 and a==1 or a==3 and b==2 or a==2 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==24 and d==1 and button24['text']=='24':
        button24['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=24
        d=0
        e+=1
        if (a==6 and b==4 or b==6 and a==4 or a==3 and b==8 or a==8 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==24 and d==0 and button24['text']=="24":
        button24['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=24
        d=1
        e+=1
        if (a==6 and b==4 or b==6 and a==4 or a==3 and b==8 or a==8 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()


    elif x==25 and d==1 and button25['text']=='15':
        button25['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=15
        d=0
        e+=1
        if (a==5 and b==3 or b==5 and a==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==25 and d==0 and button25['text']=="15":
        button25['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=15
        d=1
        e+=1
        if (a==5 and b==3 or b==5 and a==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==26 and d==1 and button26['text']=='30':
        button26['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=30
        d=0
        e+=1
        if (a==5 and b==6 or b==5 and a==6):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==26 and d==0 and button26['text']=="30":
        button26['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=30
        d=1
        e+=1
        if (a==5 and b==6 or b==5 and a==6):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
            
    elif x==27 and d==1 and button27['text']=='24':
        button27['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=24
        d=0
        e+=1
        if (a==6 and b==4 or b==6 and a==4 or a==3 and b==8 or a==8 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==27 and d==0 and button27['text']=="24":
        button27['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=24
        d=1
        e+=1
        if (a==6 and b==4 or b==6 and a==4 or a==3 and b==8 or a==8 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==28 and d==1 and button28['text']=='15':
        button28['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=15
        d=0
        e+=1
        if (a==5 and b==3 or b==5 and a==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==28 and d==0 and button28['text']=="15":
        button28['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=15
        d=1
        e+=1
        if (a==5 and b==3 or b==5 and a==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==29 and d==1 and button29['text']=='8':
        button29['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=8
        d=0
        e+=1
        if (a==8 and b==1 or b==8 and a==1 or a==2 and b==4 or a==4 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==29 and d==0 and button29['text']=="8":
        button29['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=8
        d=1
        e+=1
        if (a==8 and b==1 or b==8 and a==1 or a==2 and b==4 or a==4 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==30 and d==1 and button30['text']=='42':
        button30['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=42
        d=0
        e+=1
        if (a==7 and b==6 or b==7 and a==6 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==30 and d==0 and button30['text']=="42":
        button30['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=42
        d=1
        e+=1
        if (a==7 and b==6 or b==7 and a==6 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==31 and d==1 and button31['text']=='8':
        button31['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=8
        d=0
        e+=1
        if (a==8 and b==1 or b==8 and a==1 or a==2 and b==4 or a==4 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==31 and d==0 and button31['text']=="8":
        button31['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=8
        d=1
        e+=1
        if (a==8 and b==1 or b==8 and a==1 or a==2 and b==4 or a==4 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==32 and d==1 and button32['text']=='54':
        button32['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=54
        d=0
        e+=1
        if (a==6 and b==9 or b==6 and a==9 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==32 and d==0 and button32['text']=="54":
        button32['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=54
        d=1
        e+=1
        if (a==6 and b==9 or b==6 and a==9 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==33 and d==1 and button33['text']=='21':
        button33['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=21
        d=0
        e+=1
        if (a==7 and b==3 or b==7 and a==3 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==33 and d==0 and button33['text']=="21":
        button33['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=21
        d=1
        e+=1
        if (a==7 and b==3 or b==7 and a==3 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==34 and d==1 and button34['text']=='9':
        button34['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=9
        d=0
        e+=1
        if (a==9 and b==1 or b==9 and a==1 or a==3 and b==3 or a==3 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==34 and d==0 and button34['text']=="9":
        button34['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=9
        d=1
        e+=1
        if (a==9 and b==1 or b==9 and a==1 or a==3 and b==3 or a==3 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==35 and d==1 and button35['text']=='7':
        button35['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=7
        d=0
        e+=1
        if (a==7 and b==1 or b==7 and a==1):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==35 and d==0 and button35['text']=="7":
        button35['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=7
        d=1
        e+=1
        if (a==7 and b==1 or b==7 and a==1):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==36 and d==1 and button36['text']=='16':
        button36['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=16
        d=0
        e+=1
        if (a==4 and b==4 or b==4 and a==4 or a==2 and b==8 or b==2 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==36 and d==0 and button36['text']=="16":
        button36['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=16
        d=1
        e+=1
        if (a==4 and b==4 or b==4 and a==4 or a==2 and b==8 or b==2 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==37 and d==1 and button37['text']=='12':
        button37['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=12
        d=0
        e+=1
        if (a==4 and b==3 or b==4 and a==3 or a==2 and b==6 or b==6 and a==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==37 and d==0 and button37['text']=="12":
        button37['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=12
        d=1
        e+=1
        if (a==4 and b==3 or b==4 and a==3 or a==2 and b==6 or b==6 and a==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==38 and d==1 and button38['text']=='18':
        button38['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=18
        d=0
        e+=1
        if (a==9 and b==2 or b==9 and a==2 or a==3 and b==6 or a==6 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==38 and d==0 and button38['text']=="18":
        button38['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=18
        d=1
        e+=1
        if (a==9 and b==2 or b==9 and a==2 or a==3 and b==6 or a==6 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==39 and d==1 and button39['text']=='24':
        button39['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=24
        d=0
        e+=1
        if (a==4 and b==6 or a==6 and b==4 or a==3 and b==8 or a==8 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==39 and d==0 and button39['text']=="24":
        button39['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=24
        d=1
        e+=1
        if (a==4 and b==6 or a==6 and b==4 or a==3 and b==8 or a==8 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    elif x==40 and d==1 and button40['text']=='4':
        button40['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=4
        d=0
        e+=1
        if (a==4 and b==1 or b==4 and a==1 or a==2 and b==2 or a==2 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()


    elif x==40 and d==0 and button40['text']=="4":
        button40['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=4
        d=1
        e+=1
        if (a==4 and b==1 or b==4 and a==1 or a==2 and b==2 or a==2 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()

    if x==41 and d==1 and button41['text']=='1':
        button41['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=1
        d=0
        e+=1
        if a!=1 or b!=1:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    if x==41 and d==0 and button41['text']=="1":
        button41['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=1
        d=1
        e+=1
        if a!=1 or b!=1:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The Winner is Player 1")
            disablebutton()
    
    elif x==42 and d==1 and button42['text']=='35':
        button42['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=35
        d=0
        e+=1
        if (a==7 and b==5 or b==7 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()


    elif x==42 and d==0 and button42['text']=="35":
        button42['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=35
        d=1
        e+=1
        if (a==7 and b==5 or b==7 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==43 and d==1 and button43['text']=='5':
        button43['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=5
        d=0
        e+=1
        if (a==1 and b==5 or b==1 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==43 and d==0 and button43['text']=="5":
        button43['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=5
        d=1
        e+=1
        if (a==1 and b==5 or b==1 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==44 and d==1 and button44['text']=='12':
        button44['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=12
        d=0
        e+=1
        if (a==4 and b==3 or b==4 and a==3 or a==2 and b==6 or b==6 and a==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==44 and d==0 and button44['text']=="12":
        button44['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=12
        d=1
        e+=1
        if (a==4 and b==3 or b==4 and a==3 or a==2 and b==6 or b==6 and a==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==45 and d==1 and button45['text']=='81':
        button45['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=81
        d=0
        e+=1
        if (a==9 and b==9 or b==9 and a==9):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==45 and d==0 and button45['text']=="81":
        button45['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=81
        d=1
        e+=1
        if (a==1 and b==5 or b==1 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
            
    elif x==46 and d==1 and button46['text']=='35':
        button46['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=35
        d=0
        e+=1
        if (a==7 and b==5 or b==7 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==46 and d==0 and button46['text']=="35":
        button46['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=35
        d=1
        e+=1
        if (a==7 and b==5 or b==7 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==47 and d==1 and button47['text']=='3':
        button47['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=3
        d=0
        e+=1
        if (a==3 and b==1 or b==3 and a==1 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==47 and d==0 and button47['text']=="3":
        button47['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=3
        d=1
        e+=1
        if (a==3 and b==1 or b==3 and a==1 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==48 and d==1 and button48['text']=='10':
        button48['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=10
        d=0
        e+=1
        if (a==5 and b==2 or b==5 and a==2 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()
        


    elif x==48 and d==0 and button48['text']=="10":
        button48['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=10
        d=1
        e+=1
        if (a==5 and b==2 or b==5 and a==2 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==49 and d==1 and button49['text']=='25':
        button49['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=25
        d=0
        e+=1
        if (a==5 and b==5 or b==5 and a==5 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()


    elif x==49 and d==0 and button49['text']=="25":
        button49['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=25
        d=1
        e+=1
        if (a==5 and b==5 or b==5 and a==5 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==50 and d==1 and button50['text']=='14':
        button50['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=14
        d=0
        e+=1
        if (a==7 and b==2 or b==7 and a==2 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()


    elif x==50 and d==0 and button50['text']=="14":
        button50['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=14
        d=1
        e+=1
        if (a==7 and b==2 or b==7 and a==2 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    
    elif x==51 and d==1 and button51['text']=='63':
        button51['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=63
        d=0
        e+=1
        if (a==7 and b==9 or b==7 and a==9 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()


    elif x==51 and d==0 and button51['text']=="63":
        button51['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=63
        d=1
        e+=1
        if (a==7 and b==9 or b==7 and a==9 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==52 and d==1 and button52['text']=='42':
        button52['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=42
        d=0
        e+=1
        if (a==7 and b==6 or b==7 and a==6 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==52 and d==0 and button52['text']=="42":
        button52['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=42
        d=1
        e+=1
        if (a==7 and b==6 or b==7 and a==6 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()
    
    elif x==53 and d==1 and button53['text']=='9':
        button53['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=9
        d=0
        e+=1
        if (a==9 and b==1 or b==9 and a==1 or a==3 and b==3 or a==3 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==53 and d==0 and button53['text']=="9":
        button53['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=9
        d=1
        e+=1
        if (a==9 and b==1 or b==9 and a==1 or a==3 and b==3 or a==3 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==54 and d==1 and button54['text']=='45':
        button54['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=45
        d=0
        e+=1
        if (a==9 and b==5 or b==9 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==54 and d==0 and button54['text']=="45":
        button54['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=45
        d=1
        e+=1
        if (a==9 and b==5 or b==9 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()
    
    elif x==55 and d==1 and button55['text']=='16':
        button55['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=16
        d=0
        e+=1
        if (a==4 and b==4 or b==4 and a==4 or a==2 and b==8 or b==2 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==55 and d==0 and button55['text']=="16":
        button55['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=16
        d=1
        e+=1
        if (a==4 and b==4 or b==4 and a==4 or a==2 and b==8 or b==2 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()
    
    elif x==57 and d==1 and button57['text']=='40':
        button57['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=40
        d=0
        e+=1
        if (a==8 and b==5 or b==8 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==57 and d==0 and button57['text']=="40":
        button57['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=40
        d=1
        e+=1
        if (a==8 and b==5 or b==8 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()
    
    elif x==58 and d==1 and button58['text']=='6':
        button58['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=6
        d=0
        e+=1
        if (a==6 and b==1 or b==6 and a==1 or a==3 and b==2 or a==2 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==58 and d==0 and button58['text']=="6":
        button58['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=6
        d=1
        e+=1
        if (a==6 and b==1 or b==6 and a==1 or a==3 and b==2 or a==2 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==59 and d==1 and button59['text']=='2':
        button59['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=2
        d=0
        e+=1
        if (a==2 and b==1 or b==2 and a==1 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==59 and d==0 and button59['text']=="2":
        button59['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=2
        d=1
        e+=1
        if (a==2 and b==1 or b==2 and a==1 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==60 and d==1 and button60['text']=='27':
        button60['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=27
        d=0
        e+=1
        if (a==9 and b==3 or b==9 and a==3 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()


    elif x==60 and d==0 and button60['text']=="27":
        button60['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=27
        d=1
        e+=1
        if (a==9 and b==3 or b==9 and a==3 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==61 and d==1 and button61['text']=='12':
        button61['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=12
        d=0
        e+=1
        if (a==4 and b==3 or b==4 and a==3 or a==2 and b==6 or b==2 and a==6):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==61 and d==0 and button61['text']=="12":
        button61['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=12
        d=1
        e+=1
        if (a==4 and b==3 or b==4 and a==3 or a==2 and b==6 or b==2 and a==6):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==62 and d==1 and button62['text']=='72':
        button62['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=72
        d=0
        e+=1
        if (a==9 and b==8 or b==9 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==62 and d==0 and button62['text']=="72":
        button62['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=72
        d=1
        e+=1
        if (a==9 and b==8 or b==9 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()
    
    elif x==63 and d==1 and button63['text']=='28':
        button63['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=28
        d=0
        e+=1
        if (a==7 and b==4 or b==7 and a==4 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()


    elif x==63 and d==0 and button63['text']=="28":
        button63['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=28
        d=1
        e+=1
        if (a==7 and b==4 or b==7 and a==4 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==64 and d==1 and button64['text']=='4':
        button64['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=4
        d=0
        e+=1
        if (a==4 and b==1 or b==4 and a==1 or a==2 and b==2 or a==2 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==64 and d==0 and button64['text']=="4":
        button64['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=4
        d=1
        e+=1
        if (a==4 and b==1 or b==4 and a==1 or a==2 and b==2 or a==2 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()
    
    elif x==65 and d==1 and button65['text']=='7':
        button65['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=7
        d=0
        e+=1
        if (a==7 and b==1 or b==7 and a==1):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()


    elif x==65 and d==0 and button65['text']=="7":
        button65['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=7
        d=1
        e+=1
        if (a==7 and b==1 or b==7 and a==1):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==66 and d==1 and button66['text']=='32':
        button66['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=32
        d=0
        e+=1
        if (a==4 and b==8 or b==4 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()


    elif x==66 and d==0 and button66['text']=="32":
        button66['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=32
        d=1
        e+=1
        if (a==4 and b==8 or b==4 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==67 and d==1 and button67['text']=='48':
        button67['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=48
        d=0
        e+=1
        if (a==6 and b==8 or b==6 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==67 and d==0 and button67['text']=="48":
        button67['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=48
        d=1
        e+=1
        if (a==6 and b==8 or b==6 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    elif x==68 and d==1 and button68['text']=='6':
        button68['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=6
        d=0
        e+=1
        if (a==6 and b==1 or b==6 and a==1 or a==3 and b==2 or a==2 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==68 and d==0 and button68['text']=="6":
        button68['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=6
        d=1
        e+=1
        if (a==6 and b==1 or b==6 and a==1 or a==3 and b==2 or a==2 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==69 and d==1 and button69['text']=='40':
        button69['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=40
        d=0
        e+=1
        if (a==8 and b==5 or b==8 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==69 and d==0 and button69['text']=="40":
        button69['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=40
        d=1
        e+=1
        if (a==8 and b==5 or b==8 and a==5):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()
    
    elif x==70 and d==1 and button70['text']=='36':
        button70['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=36
        d=0
        e+=1
        if (a==9 and b==4 or b==9 and a==4 or a==6 and b==6):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==70 and d==0 and button70['text']=="36":
        button70['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=36
        d=1
        e+=1
        if (a==9 and b==4 or b==9 and a==4 or a==6 and b==6):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()
    
    elif x==71 and d==1 and button71['text']=='18':
        button71['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=18
        d=0
        e+=1
        if (a==9 and b==2 or b==9 and a==2 or a==3 and b==6 or a==6 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==71 and d==0 and button71['text']=="18":
        button71['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=18
        d=1
        e+=1
        if (a==9 and b==2 or b==9 and a==2 or a==3 and b==6 or a==6 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==72 and d==1 and button72['text']=='48':
        button72['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=48
        d=0
        e+=1
        if (a==6 and b==8 or b==6 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==72 and d==0 and button72['text']=="48":
        button72['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=48
        d=1
        e+=1
        if (a==6 and b==8 or b==6 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==73 and d==1 and button73['text']=='56':
        button73['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=56
        d=0
        e+=1
        if (a==8 and b==7 or b==8 and a==7 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==73 and d==0 and button73['text']=="56":
        button73['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=56
        d=1
        e+=1
        if (a==8 and b==7 or b==8 and a==7 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 1")
            disablebutton()
    
    elif x==74 and d==1 and button74['text']=='10':
        button74['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=10
        d=0
        e+=1
        if (a==5 and b==2 or b==5 and a==2 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==74 and d==0 and button74['text']=="10":
        button74['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=10
        d=1
        e+=1
        if (a==5 and b==2 or b==5 and a==2 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==75 and d==1 and button75['text']=='8':
        button75['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=8
        d=0
        e+=1
        if (a==8 and b==1 or b==8 and a==1 or a==2 and b==4 or a==4 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()

    elif x==75 and d==0 and button75['text']=="8":
        button75['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=8
        d=1
        e+=1
        if (a==8 and b==1 or b==8 and a==1 or a==2 and b==4 or a==4 and b==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\n The winner is Player 2")
            disablebutton()
    
    elif x==76 and d==1 and button76['text']=='27':
        button76['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=27
        d=0
        e+=1
        if (a==9 and b==3 or b==9 and a==3 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==76 and d==0 and button76['text']=="27":
        button76['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=27
        d=1
        e+=1
        if (a==9 and b==3 or b==9 and a==3 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==77 and d==1 and button77['text']=='14':
        button77['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=14
        d=0
        e+=1
        if (a==7 and b==2 or b==7 and a==2 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()


    elif x==77 and d==0 and button77['text']=="14":
        button77['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=14
        d=1
        e+=1
        if (a==7 and b==2 or b==7 and a==2 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()

    
    elif x==78 and d==1 and button78['text']=='28':
        button78['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=28
        d=0
        e+=1
        if (a==7 and b==4 or b==7 and a==4 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==78 and d==0 and button78['text']=="28":
        button78['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=28
        d=1
        e+=1
        if (a==7 and b==4 or b==7 and a==4 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==79 and d==1 and button79['text']=='6':
        button79['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=6
        d=0
        e+=1
        if (a==6 and b==1 or b==6 and a==1 or a==3 and b==2 or a==2 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==79 and d==0 and button79['text']=="6":
        button79['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=6
        d=1
        e+=1
        if (a==6 and b==1 or b==6 and a==1 or a==3 and b==2 or a==2 and b==3):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==80 and d==1 and button80['text']=='32':
        button80['bg']="green"
        player_label['text']='Player-2 Turn'
        player_label['bg']='red'
        c=32
        red=0
        e+=1
        if (a==4 and b==8 or b==4 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==80 and d==0 and button80['text']=="32":
        button80['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=32
        d=1
        e+=1
        if (a==4 and b==8 or b==4 and a==8):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==81 and d==1 and button81['text']=='54':
        button81['bg']="green"
        player_label['text']='Player-2 Turn'
        player_labered['bg']='red'
        c=red4
        d=0
        e+=1
        if (a==6 and b==9 or b==6 and a==9 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==81 and d==0 and button81['text']=="54":
        button81['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=54
        d=1
        e+=1
        if (a==6 and b==9 or b==6 and a==9 ):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
    
    elif x==82 and d==1 and button82['text']=='12':
        button82['bg']="green"
        playered_label['text']='Player-red Turn'
        player_label['bg']='red'
        c=12
        d=0
        e+=1
        if (a==4 and b==3 or b==4 and a==3 or a==2 and b==6 or b==6 and a==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 2")
            disablebutton()

    elif x==82 and d==0 and button82['text']=="12":
        button82['bg']="red"
        player_label['text']='Player-1 Turn'
        player_label['bg']='green'
        c=12
        d=1
        e+=1
        if (a==4 and b==3 or b==4 and a==3 or a==2 and b==6 or b==6 and a==2):
            ()
        else:
            messagebox.showinfo('information',"DingDong!\nYou're Wrong\nThe winner is Player 1")
            disablebutton()
            
    #--------redGame Draw
    if (e==32):
        disablebutton()
        messagebox.showinfo('The Result','Game Draw!!!') 

    #--------Player 2 win

    if(button1['bg']=='red' and button2['bg']=='red' and button3['bg']=='red' and button4['bg']=='red'
        or button1['bg']=='red' and button10['bg']=='red' and button19['bg']=='red' and button28['bg']=='red'
        or button1['bg']=='red' and button11['bg']=='red' and button21['bg']=='red' and button31['bg']=='red'
        or button2['bg']=='red' and button3['bg']=='red' and button4['bg']=='red' and button5['bg']=='red'
        or button2['bg']=='red' and button11['bg']=='red' and button20['bg']=='red' and button29['bg']=='red'
        or button2['bg']=='red' and button12['bg']=='red' and button22['bg']=='red' and button32['bg']=='red'
        or button3['bg']=='red' and button4['bg']=='red' and button5['bg']=='red' and button6['bg']=='red'
        or button3['bg']=='red' and button12['bg']=='red' and button21['bg']=='red' and button30['bg']=='red'
        or button3['bg']=='red' and button13['bg']=='red' and button23['bg']=='red' and button33['bg']=='red'
        or button4['bg']=='red' and button5['bg']=='red' and button6['bg']=='red' and button7['bg']=='red'
        or button4['bg']=='red' and button13['bg']=='red' and button22['bg']=='red' and button31['bg']=='red'
        or button4['bg']=='red' and button14['bg']=='red' and button24['bg']=='red' and button34['bg']=='red'
        or button4['bg']=='red' and button12['bg']=='red' and button20['bg']=='red' and button28['bg']=='red'
        or button5['bg']=='red' and button6['bg']=='red' and button7['bg']=='red' and button8['bg']=='red'
        or button5['bg']=='red' and button14['bg']=='red' and button23['bg']=='red' and button32['bg']=='red'
        or button5['bg']=='red' and button15['bg']=='red' and button25['bg']=='red' and button35['bg']=='red'
        or button5['bg']=='red' and button13['bg']=='red' and button21['bg']=='red' and button29['bg']=='red'
        or button6['bg']=='red' and button7['bg']=='red' and button8['bg']=='red' and button9['bg']=='red'
        or button6['bg']=='red' and button15['bg']=='red' and button24['bg']=='red' and button33['bg']=='red'
        or button6['bg']=='red' and button16['bg']=='red' and button26['bg']=='red' and button36['bg']=='red'
        or button6['bg']=='red' and button14['bg']=='red' and button22['bg']=='red' and button30['bg']=='red'
        or button7['bg']=='red' and button16['bg']=='red' and button25['bg']=='red' and button34['bg']=='red'
        or button7['bg']=='red' and button15['bg']=='red' and button23['bg']=='red' and button31['bg']=='red'
        or button8['bg']=='red' and button17['bg']=='red' and button26['bg']=='red' and button35['bg']=='red'
        or button8['bg']=='red' and button16['bg']=='red' and button24['bg']=='red' and button32['bg']=='red'
        or button9['bg']=='red' and button18['bg']=='red' and button27['bg']=='red' and button36['bg']=='red'
        or button9['bg']=='red' and button17['bg']=='red' and button25['bg']=='red' and button33['bg']=='red'
        or button10['bg']=='red' and button11['bg']=='red' and button12['bg']=='red' and button13['bg']=='red'
        or button10['bg']=='red' and button19['bg']=='red' and button28['bg']=='red' and button37['bg']=='red'
        or button10['bg']=='red' and button20['bg']=='red' and button30['bg']=='red' and button40['bg']=='red'
        or button11['bg']=='red' and button12['bg']=='red' and button13['bg']=='red' and button14['bg']=='red'
        or button11['bg']=='red' and button20['bg']=='red' and button29['bg']=='red' and button38['bg']=='red'
        or button11['bg']=='red' and button21['bg']=='red' and button31['bg']=='red' and button41['bg']=='red'
        or button12['bg']=='red' and button13['bg']=='red' and button14['bg']=='red' and button15['bg']=='red'
        or button12['bg']=='red' and button21['bg']=='red' and button30['bg']=='red' and button39['bg']=='red'
        or button12['bg']=='red' and button22['bg']=='red' and button32['bg']=='red' and button42['bg']=='red'
        or button13['bg']=='red' and button14['bg']=='red' and button15['bg']=='red' and button16['bg']=='red'
        or button13['bg']=='red' and button22['bg']=='red' and button31['bg']=='red' and button40['bg']=='red'
        or button13['bg']=='red' and button23['bg']=='red' and button33['bg']=='red' and button43['bg']=='red'
        or button13['bg']=='red' and button21['bg']=='red' and button29['bg']=='red' and button37['bg']=='red'
        or button14['bg']=='red' and button15['bg']=='red' and button16['bg']=='red' and button17['bg']=='red'
        or button14['bg']=='red' and button23['bg']=='red' and button32['bg']=='red' and button41['bg']=='red'
        or button14['bg']=='red' and button24['bg']=='red' and button34['bg']=='red' and button44['bg']=='red'
        or button14['bg']=='red' and button22['bg']=='red' and button30['bg']=='red' and button38['bg']=='red'
        or button15['bg']=='red' and button16['bg']=='red' and button17['bg']=='red' and button18['bg']=='red'
        or button15['bg']=='red' and button24['bg']=='red' and button33['bg']=='red' and button42['bg']=='red'
        or button15['bg']=='red' and button25['bg']=='red' and button35['bg']=='red' and button45['bg']=='red'
        or button15['bg']=='red' and button23['bg']=='red' and button31['bg']=='red' and button38['bg']=='red'
        or button16['bg']=='red' and button25['bg']=='red' and button34['bg']=='red' and button43['bg']=='red'
        or button16['bg']=='red' and button24['bg']=='red' and button32['bg']=='red' and button40['bg']=='red'
        or button17['bg']=='red' and button26['bg']=='red' and button35['bg']=='red' and button44['bg']=='red'
        or button17['bg']=='red' and button25['bg']=='red' and button33['bg']=='red' and button41['bg']=='red'
        or button18['bg']=='red' and button27['bg']=='red' and button36['bg']=='red' and button45['bg']=='red'
        or button18['bg']=='red' and button26['bg']=='red' and button34['bg']=='red' and button42['bg']=='red'
        or button19['bg']=='red' and button20['bg']=='red' and button21['bg']=='red' and button22['bg']=='red'
        or button19['bg']=='red' and button28['bg']=='red' and button37['bg']=='red' and button46['bg']=='red'
        or button19['bg']=='red' and button29['bg']=='red' and button39['bg']=='red' and button49['bg']=='red'
        or button20['bg']=='red' and button21['bg']=='red' and button22['bg']=='red' and button23['bg']=='red'
        or button20['bg']=='red' and button29['bg']=='red' and button38['bg']=='red' and button47['bg']=='red'
        or button20['bg']=='red' and button30['bg']=='red' and button40['bg']=='red' and button50['bg']=='red'
        or button21['bg']=='red' and button22['bg']=='red' and button23['bg']=='red' and button24['bg']=='red'
        or button21['bg']=='red' and button30['bg']=='red' and button39['bg']=='red' and button48['bg']=='red'
        or button21['bg']=='red' and button31['bg']=='red' and button41['bg']=='red' and button51['bg']=='red'
        or button22['bg']=='red' and button23['bg']=='red' and button24['bg']=='red' and button25['bg']=='red'
        or button22['bg']=='red' and button31['bg']=='red' and button40['bg']=='red' and button49['bg']=='red'
        or button22['bg']=='red' and button32['bg']=='red' and button42['bg']=='red' and button52['bg']=='red'
        or button22['bg']=='red' and button30['bg']=='red' and button38['bg']=='red' and button46['bg']=='red'
        or button23['bg']=='red' and button24['bg']=='red' and button25['bg']=='red' and button26['bg']=='red'
        or button23['bg']=='red' and button32['bg']=='red' and button41['bg']=='red' and button50['bg']=='red'
        or button23['bg']=='red' and button31['bg']=='red' and button39['bg']=='red' and button47['bg']=='red'
        or button23['bg']=='red' and button33['bg']=='red' and button43['bg']=='red' and button53['bg']=='red'
        or button24['bg']=='red' and button25['bg']=='red' and button26['bg']=='red' and button27['bg']=='red'
        or button24['bg']=='red' and button23['bg']=='red' and button42['bg']=='red' and button51['bg']=='red'
        or button24['bg']=='red' and button32['bg']=='red' and button40['bg']=='red' and button48['bg']=='red'
        or button24['bg']=='red' and button34['bg']=='red' and button44['bg']=='red' and button54['bg']=='red'
        or button25['bg']=='red' and button34['bg']=='red' and button43['bg']=='red' and button52['bg']=='red'
        or button25['bg']=='red' and button33['bg']=='red' and button41['bg']=='red' and button49['bg']=='red'
        or button26['bg']=='red' and button35['bg']=='red' and button44['bg']=='red' and button53['bg']=='red'
        or button26['bg']=='red' and button34['bg']=='red' and button42['bg']=='red' and button50['bg']=='red'
        or button27['bg']=='red' and button36['bg']=='red' and button45['bg']=='red' and button54['bg']=='red'
        or button27['bg']=='red' and button35['bg']=='red' and button43['bg']=='red' and button51['bg']=='red'
        or button28['bg']=='red' and button29['bg']=='red' and button30['bg']=='red' and button31['bg']=='red'
        or button28['bg']=='red' and button37['bg']=='red' and button46['bg']=='red' and button55['bg']=='red'
        or button28['bg']=='red' and button38['bg']=='red' and button48['bg']=='red' and button59['bg']=='red'
        or button29['bg']=='red' and button30['bg']=='red' and button31['bg']=='red' and button32['bg']=='red'
        or button29['bg']=='red' and button38['bg']=='red' and button47['bg']=='red' and button57['bg']=='red'
        or button29['bg']=='red' and button39['bg']=='red' and button49['bg']=='red' and button60['bg']=='red'
        or button30['bg']=='red' and button31['bg']=='red' and button32['bg']=='red' and button33['bg']=='red'
        or button30['bg']=='red' and button39['bg']=='red' and button48['bg']=='red' and button58['bg']=='red'
        or button30['bg']=='red' and button40['bg']=='red' and button50['bg']=='red' and button61['bg']=='red'
        or button31['bg']=='red' and button32['bg']=='red' and button33['bg']=='red' and button34['bg']=='red'
        or button31['bg']=='red' and button40['bg']=='red' and button49['bg']=='red' and button59['bg']=='red'
        or button31['bg']=='red' and button39['bg']=='red' and button47['bg']=='red' and button55['bg']=='red'
        or button31['bg']=='red' and button41['bg']=='red' and button51['bg']=='red' and button62['bg']=='red'
        or button32['bg']=='red' and button33['bg']=='red' and button34['bg']=='red' and button35['bg']=='red'
        or button32['bg']=='red' and button41['bg']=='red' and button50['bg']=='red' and button60['bg']=='red'
        or button32['bg']=='red' and button40['bg']=='red' and button48['bg']=='red' and button57['bg']=='red'
        or button32['bg']=='red' and button42['bg']=='red' and button52['bg']=='red' and button63['bg']=='red'
        or button33['bg']=='red' and button34['bg']=='red' and button35['bg']=='red' and button61['bg']=='red'
        or button33['bg']=='red' and button41['bg']=='red' and button49['bg']=='red' and button58['bg']=='red'
        or button33['bg']=='red' and button43['bg']=='red' and button53['bg']=='red' and button64['bg']=='red'
        or button34['bg']=='red' and button43['bg']=='red' and button52['bg']=='red' and button62['bg']=='red'
        or button34['bg']=='red' and button42['bg']=='red' and button50['bg']=='red' and button59['bg']=='red'
        or button35['bg']=='red' and button44['bg']=='red' and button53['bg']=='red' and button63['bg']=='red'
        or button35['bg']=='red' and button43['bg']=='red' and button51['bg']=='red' and button60['bg']=='red'
        or button36['bg']=='red' and button45['bg']=='red' and button54['bg']=='red' and button64['bg']=='red'
        or button36['bg']=='red' and button44['bg']=='red' and button52['bg']=='red' and button61['bg']=='red'
        or button37['bg']=='red' and button38['bg']=='red' and button39['bg']=='red' and button40['bg']=='red'
        or button37['bg']=='red' and button46['bg']=='red' and button55['bg']=='red' and button65['bg']=='red'
        or button37['bg']=='red' and button47['bg']=='red' and button58['bg']=='red' and button68['bg']=='red'
        or button38['bg']=='red' and button39['bg']=='red' and button40['bg']=='red' and button41['bg']=='red'
        or button38['bg']=='red' and button47['bg']=='red' and button57['bg']=='red' and button66['bg']=='red'
        or button38['bg']=='red' and button48['bg']=='red' and button59['bg']=='red' and button69['bg']=='red'
        or button39['bg']=='red' and button40['bg']=='red' and button41['bg']=='red' and button42['bg']=='red'
        or button39['bg']=='red' and button48['bg']=='red' and button58['bg']=='red' and button67['bg']=='red'
        or button39['bg']=='red' and button49['bg']=='red' and button60['bg']=='red' and button70['bg']=='red'
        or button40['bg']=='red' and button41['bg']=='red' and button42['bg']=='red' and button43['bg']=='red'
        or button40['bg']=='red' and button49['bg']=='red' and button59['bg']=='red' and button68['bg']=='red'
        or button40['bg']=='red' and button48['bg']=='red' and button57['bg']=='red' and button65['bg']=='red'
        or button40['bg']=='red' and button50['bg']=='red' and button61['bg']=='red' and button71['bg']=='red'
        or button41['bg']=='red' and button42['bg']=='red' and button43['bg']=='red' and button44['bg']=='red'
        or button41['bg']=='red' and button50['bg']=='red' and button60['bg']=='red' and button69['bg']=='red'
        or button41['bg']=='red' and button49['bg']=='red' and button58['bg']=='red' and button66['bg']=='red'
        or button41['bg']=='red' and button51['bg']=='red' and button62['bg']=='red' and button72['bg']=='red'
        or button42['bg']=='red' and button43['bg']=='red' and button44['bg']=='red' and button45['bg']=='red'
        or button42['bg']=='red' and button51['bg']=='red' and button61['bg']=='red' and button70['bg']=='red'
        or button42['bg']=='red' and button50['bg']=='red' and button59['bg']=='red' and button67['bg']=='red'
        or button42['bg']=='red' and button52['bg']=='red' and button63['bg']=='red' and button73['bg']=='red'
        or button43['bg']=='red' and button52['bg']=='red' and button62['bg']=='red' and button71['bg']=='red'
        or button43['bg']=='red' and button51['bg']=='red' and button60['bg']=='red' and button68['bg']=='red'
        or button44['bg']=='red' and button53['bg']=='red' and button63['bg']=='red' and button72['bg']=='red'
        or button44['bg']=='red' and button52['bg']=='red' and button61['bg']=='red' and button69['bg']=='red'
        or button45['bg']=='red' and button54['bg']=='red' and button64['bg']=='red' and button73['bg']=='red'
        or button45['bg']=='red' and button53['bg']=='red' and button62['bg']=='red' and button70['bg']=='red'
        or button46['bg']=='red' and button47['bg']=='red' and button48['bg']=='red' and button49['bg']=='red'
        or button46['bg']=='red' and button55['bg']=='red' and button65['bg']=='red' and button74['bg']=='red'
        or button46['bg']=='red' and button57['bg']=='red' and button67['bg']=='red' and button77['bg']=='red'
        or button47['bg']=='red' and button48['bg']=='red' and button49['bg']=='red' and button50['bg']=='red'
        or button47['bg']=='red' and button57['bg']=='red' and button66['bg']=='red' and button75['bg']=='red'
        or button47['bg']=='red' and button58['bg']=='red' and button68['bg']=='red' and button78['bg']=='red'
        or button48['bg']=='red' and button49['bg']=='red' and button50['bg']=='red' and button51['bg']=='red'
        or button48['bg']=='red' and button58['bg']=='red' and button67['bg']=='red' and button76['bg']=='red'
        or button48['bg']=='red' and button59['bg']=='red' and button69['bg']=='red' and button79['bg']=='red'
        or button49['bg']=='red' and button50['bg']=='red' and button51['bg']=='red' and button52['bg']=='red'
        or button49['bg']=='red' and button59['bg']=='red' and button68['bg']=='red' and button77['bg']=='red'
        or button49['bg']=='red' and button58['bg']=='red' and button66['bg']=='red' and button74['bg']=='red'
        or button49['bg']=='red' and button60['bg']=='red' and button70['bg']=='red' and button80['bg']=='red'
        or button50['bg']=='red' and button51['bg']=='red' and button52['bg']=='red' and button53['bg']=='red'
        or button50['bg']=='red' and button60['bg']=='red' and button69['bg']=='red' and button78['bg']=='red'
        or button50['bg']=='red' and button59['bg']=='red' and button67['bg']=='red' and button75['bg']=='red'
        or button50['bg']=='red' and button61['bg']=='red' and button71['bg']=='red' and button81['bg']=='red'
        or button51['bg']=='red' and button52['bg']=='red' and button53['bg']=='red' and button54['bg']=='red'
        or button51['bg']=='red' and button61['bg']=='red' and button70['bg']=='red' and button79['bg']=='red'
        or button51['bg']=='red' and button60['bg']=='red' and button68['bg']=='red' and button76['bg']=='red'
        or button51['bg']=='red' and button62['bg']=='red' and button72['bg']=='red' and button82['bg']=='red'
        or button52['bg']=='red' and button62['bg']=='red' and button71['bg']=='red' and button80['bg']=='red'
        or button52['bg']=='red' and button61['bg']=='red' and button69['bg']=='red' and button77['bg']=='red'
        or button53['bg']=='red' and button63['bg']=='red' and button72['bg']=='red' and button81['bg']=='red'
        or button53['bg']=='red' and button62['bg']=='red' and button70['bg']=='red' and button78['bg']=='red'
        or button54['bg']=='red' and button64['bg']=='red' and button73['bg']=='red' and button82['bg']=='red'
        or button54['bg']=='red' and button63['bg']=='red' and button71['bg']=='red' and button79['bg']=='red'
        or button55['bg']=='red' and button57['bg']=='red' and button58['bg']=='red' and button59['bg']=='red'
        or button57['bg']=='red' and button58['bg']=='red' and button59['bg']=='red' and button60['bg']=='red'
        or button58['bg']=='red' and button59['bg']=='red' and button60['bg']=='red' and button61['bg']=='red'
        or button59['bg']=='red' and button60['bg']=='red' and button61['bg']=='red' and button62['bg']=='red'
        or button60['bg']=='red' and button61['bg']=='red' and button62['bg']=='red' and button63['bg']=='red'
        or button61['bg']=='red' and button62['bg']=='red' and button63['bg']=='red' and button64['bg']=='red'
        or button65['bg']=='red' and button66['bg']=='red' and button67['bg']=='red' and button68['bg']=='red'
        or button66['bg']=='red' and button67['bg']=='red' and button68['bg']=='red' and button69['bg']=='red'
        or button67['bg']=='red' and button68['bg']=='red' and button69['bg']=='red' and button70['bg']=='red'
        or button68['bg']=='red' and button69['bg']=='red' and button70['bg']=='red' and button71['bg']=='red'
        or button69['bg']=='red' and button70['bg']=='red' and button71['bg']=='red' and button72['bg']=='red'
        or button70['bg']=='red' and button71['bg']=='red' and button72['bg']=='red' and button73['bg']=='red'
        or button73['bg']=='red' and button74['bg']=='red' and button76['bg']=='red' and button77['bg']=='red'
        or button75['bg']=='red' and button76['bg']=='red' and button77['bg']=='red' and button78['bg']=='red'
        or button76['bg']=='red' and button77['bg']=='red' and button78['bg']=='red' and button79['bg']=='red'
        or button77['bg']=='red' and button78['bg']=='red' and button79['bg']=='red' and button80['bg']=='red'
        or button78['bg']=='red' and button79['bg']=='red' and button80['bg']=='red' and button81['bg']=='red'
        or button79['bg']=='red' and button80['bg']=='red' and button81['bg']=='red' and button82['bg']=='red'):
                disablebutton()
                messagebox.showinfo("THE WINNER!!!","Winner is player 2")
    #-------- Player 1 Win
    if(button1['bg']=='green' and button2['bg']=='green' and button3['bg']=='green' and button4['bg']=='green'
        or button1['bg']=='green' and button10['bg']=='green' and button19['bg']=='green' and button28['bg']=='green'
        or button1['bg']=='green' and button11['bg']=='green' and button21['bg']=='green' and button31['bg']=='green'
        or button2['bg']=='green' and button3['bg']=='green' and button4['bg']=='green' and button5['bg']=='green'
        or button2['bg']=='green' and button11['bg']=='green' and button20['bg']=='green' and button29['bg']=='green'
        or button2['bg']=='green' and button12['bg']=='green' and button22['bg']=='green' and button32['bg']=='green'
        or button3['bg']=='green' and button4['bg']=='green' and button5['bg']=='green' and button6['bg']=='green'
        or button3['bg']=='green' and button12['bg']=='green' and button21['bg']=='green' and button30['bg']=='green'
        or button3['bg']=='green' and button13['bg']=='green' and button23['bg']=='green' and button33['bg']=='green'
        or button4['bg']=='green' and button5['bg']=='green' and button6['bg']=='green' and button7['bg']=='green'
        or button4['bg']=='green' and button13['bg']=='green' and button22['bg']=='green' and button31['bg']=='green'
        or button4['bg']=='green' and button14['bg']=='green' and button24['bg']=='green' and button34['bg']=='green'
        or button4['bg']=='green' and button12['bg']=='green' and button20['bg']=='green' and button28['bg']=='green'
        or button5['bg']=='green' and button6['bg']=='green' and button7['bg']=='green' and button8['bg']=='green'
        or button5['bg']=='green' and button15['bg']=='green' and button25['bg']=='green' and button35['bg']=='green'
        or button5['bg']=='green' and button13['bg']=='green' and button21['bg']=='green' and button29['bg']=='green'
        or button6['bg']=='green' and button7['bg']=='green' and button8['bg']=='green' and button9['bg']=='green'
        or button6['bg']=='green' and button15['bg']=='green' and button24['bg']=='green' and button33['bg']=='green'
        or button6['bg']=='green' and button16['bg']=='green' and button26['bg']=='green' and button36['bg']=='green'
        or button6['bg']=='green' and button14['bg']=='green' and button22['bg']=='green' and button30['bg']=='green'
        or button7['bg']=='green' and button16['bg']=='green' and button25['bg']=='green' and button34['bg']=='green'
        or button7['bg']=='green' and button15['bg']=='green' and button23['bg']=='green' and button31['bg']=='green'
        or button8['bg']=='green' and button17['bg']=='green' and button26['bg']=='green' and button35['bg']=='green'
        or button8['bg']=='green' and button16['bg']=='green' and button24['bg']=='green' and button32['bg']=='green'
        or button9['bg']=='green' and button18['bg']=='green' and button27['bg']=='green' and button36['bg']=='green'
        or button9['bg']=='green' and button17['bg']=='green' and button25['bg']=='green' and button33['bg']=='green'
        or button10['bg']=='green' and button11['bg']=='green' and button12['bg']=='green' and button13['bg']=='green'
        or button10['bg']=='green' and button19['bg']=='green' and button28['bg']=='green' and button37['bg']=='green'
        or button10['bg']=='green' and button20['bg']=='green' and button30['bg']=='green' and button40['bg']=='green'
        or button11['bg']=='green' and button12['bg']=='green' and button13['bg']=='green' and button14['bg']=='green'
        or button11['bg']=='green' and button20['bg']=='green' and button29['bg']=='green' and button38['bg']=='green'
        or button11['bg']=='green' and button21['bg']=='green' and button31['bg']=='green' and button41['bg']=='green'
        or button12['bg']=='green' and button13['bg']=='green' and button14['bg']=='green' and button15['bg']=='green'
        or button12['bg']=='green' and button21['bg']=='green' and button30['bg']=='green' and button39['bg']=='green'
        or button12['bg']=='green' and button22['bg']=='green' and button32['bg']=='green' and button42['bg']=='green'
        or button13['bg']=='green' and button14['bg']=='green' and button15['bg']=='green' and button16['bg']=='green'
        or button13['bg']=='green' and button22['bg']=='green' and button31['bg']=='green' and button40['bg']=='green'
        or button13['bg']=='green' and button23['bg']=='green' and button33['bg']=='green' and button43['bg']=='green'
        or button13['bg']=='green' and button21['bg']=='green' and button29['bg']=='green' and button37['bg']=='green'
        or button14['bg']=='green' and button15['bg']=='green' and button16['bg']=='green' and button17['bg']=='green'
        or button14['bg']=='green' and button23['bg']=='green' and button32['bg']=='green' and button41['bg']=='green'
        or button14['bg']=='green' and button24['bg']=='green' and button34['bg']=='green' and button44['bg']=='green'
        or button14['bg']=='green' and button22['bg']=='green' and button30['bg']=='green' and button38['bg']=='green'
        or button15['bg']=='green' and button16['bg']=='green' and button17['bg']=='green' and button18['bg']=='green'
        or button15['bg']=='green' and button24['bg']=='green' and button33['bg']=='green' and button42['bg']=='green'
        or button15['bg']=='green' and button25['bg']=='green' and button35['bg']=='green' and button45['bg']=='green'
        or button15['bg']=='green' and button23['bg']=='green' and button31['bg']=='green' and button38['bg']=='green'
        or button16['bg']=='green' and button25['bg']=='green' and button34['bg']=='green' and button43['bg']=='green'
        or button16['bg']=='green' and button24['bg']=='green' and button32['bg']=='green' and button40['bg']=='green'
        or button17['bg']=='green' and button26['bg']=='green' and button35['bg']=='green' and button44['bg']=='green'
        or button17['bg']=='green' and button25['bg']=='green' and button33['bg']=='green' and button41['bg']=='green'
        or button18['bg']=='green' and button27['bg']=='green' and button36['bg']=='green' and button45['bg']=='green'
        or button18['bg']=='green' and button26['bg']=='green' and button34['bg']=='green' and button42['bg']=='green'
        or button19['bg']=='green' and button20['bg']=='green' and button21['bg']=='green' and button22['bg']=='green'
        or button19['bg']=='green' and button28['bg']=='green' and button37['bg']=='green' and button46['bg']=='green'
        or button19['bg']=='green' and button29['bg']=='green' and button39['bg']=='green' and button49['bg']=='green'
        or button20['bg']=='green' and button21['bg']=='green' and button22['bg']=='green' and button23['bg']=='green'
        or button20['bg']=='green' and button29['bg']=='green' and button38['bg']=='green' and button47['bg']=='green'
        or button20['bg']=='green' and button30['bg']=='green' and button40['bg']=='green' and button50['bg']=='green'
        or button21['bg']=='green' and button22['bg']=='green' and button23['bg']=='green' and button24['bg']=='green'
        or button21['bg']=='green' and button30['bg']=='green' and button39['bg']=='green' and button48['bg']=='green'
        or button21['bg']=='green' and button31['bg']=='green' and button41['bg']=='green' and button51['bg']=='green'
        or button22['bg']=='green' and button23['bg']=='green' and button24['bg']=='green' and button25['bg']=='green'
        or button22['bg']=='green' and button31['bg']=='green' and button40['bg']=='green' and button49['bg']=='green'
        or button22['bg']=='green' and button32['bg']=='green' and button42['bg']=='green' and button52['bg']=='green'
        or button22['bg']=='green' and button30['bg']=='green' and button38['bg']=='green' and button46['bg']=='green'
        or button23['bg']=='green' and button24['bg']=='green' and button25['bg']=='green' and button26['bg']=='green'
        or button23['bg']=='green' and button32['bg']=='green' and button41['bg']=='green' and button50['bg']=='green'
        or button23['bg']=='green' and button31['bg']=='green' and button39['bg']=='green' and button47['bg']=='green'
        or button23['bg']=='green' and button33['bg']=='green' and button43['bg']=='green' and button53['bg']=='green'
        or button24['bg']=='green' and button25['bg']=='green' and button26['bg']=='green' and button27['bg']=='green'
        or button24['bg']=='green' and button23['bg']=='green' and button42['bg']=='green' and button51['bg']=='green'
        or button24['bg']=='green' and button32['bg']=='green' and button40['bg']=='green' and button48['bg']=='green'
        or button24['bg']=='green' and button34['bg']=='green' and button44['bg']=='green' and button54['bg']=='green'
        or button25['bg']=='green' and button34['bg']=='green' and button43['bg']=='green' and button52['bg']=='green'
        or button25['bg']=='green' and button33['bg']=='green' and button41['bg']=='green' and button49['bg']=='green'
        or button26['bg']=='green' and button35['bg']=='green' and button44['bg']=='green' and button53['bg']=='green'
        or button26['bg']=='green' and button34['bg']=='green' and button42['bg']=='green' and button50['bg']=='green'
        or button27['bg']=='green' and button36['bg']=='green' and button45['bg']=='green' and button54['bg']=='green'
        or button27['bg']=='green' and button35['bg']=='green' and button43['bg']=='green' and button51['bg']=='green'
        or button28['bg']=='green' and button29['bg']=='green' and button30['bg']=='green' and button31['bg']=='green'
        or button28['bg']=='green' and button37['bg']=='green' and button46['bg']=='green' and button55['bg']=='green'
        or button28['bg']=='green' and button38['bg']=='green' and button48['bg']=='green' and button59['bg']=='green'
        or button29['bg']=='green' and button30['bg']=='green' and button31['bg']=='green' and button32['bg']=='green'
        or button29['bg']=='green' and button38['bg']=='green' and button47['bg']=='green' and button57['bg']=='green'
        or button29['bg']=='green' and button39['bg']=='green' and button49['bg']=='green' and button60['bg']=='green'
        or button30['bg']=='green' and button31['bg']=='green' and button32['bg']=='green' and button33['bg']=='green'
        or button30['bg']=='green' and button39['bg']=='green' and button48['bg']=='green' and button58['bg']=='green'
        or button30['bg']=='green' and button40['bg']=='green' and button50['bg']=='green' and button61['bg']=='green'
        or button31['bg']=='green' and button32['bg']=='green' and button33['bg']=='green' and button34['bg']=='green'
        or button31['bg']=='green' and button40['bg']=='green' and button49['bg']=='green' and button59['bg']=='green'
        or button31['bg']=='green' and button39['bg']=='green' and button47['bg']=='green' and button55['bg']=='green'
        or button31['bg']=='green' and button41['bg']=='green' and button51['bg']=='green' and button62['bg']=='green'
        or button32['bg']=='green' and button33['bg']=='green' and button34['bg']=='green' and button35['bg']=='green'
        or button32['bg']=='green' and button41['bg']=='green' and button50['bg']=='green' and button60['bg']=='green'
        or button32['bg']=='green' and button40['bg']=='green' and button48['bg']=='green' and button57['bg']=='green'
        or button32['bg']=='green' and button42['bg']=='green' and button52['bg']=='green' and button63['bg']=='green'
        or button33['bg']=='green' and button34['bg']=='green' and button35['bg']=='green' and button36['bg']=='green'
        or button33['bg']=='green' and button42['bg']=='green' and button51['bg']=='green' and button61['bg']=='green'
        or button33['bg']=='green' and button41['bg']=='green' and button49['bg']=='green' and button58['bg']=='green'
        or button33['bg']=='green' and button43['bg']=='green' and button53['bg']=='green' and button64['bg']=='green'
        or button34['bg']=='green' and button43['bg']=='green' and button52['bg']=='green' and button62['bg']=='green'
        or button34['bg']=='green' and button42['bg']=='green' and button50['bg']=='green' and button59['bg']=='green'
        or button35['bg']=='green' and button44['bg']=='green' and button53['bg']=='green' and button63['bg']=='green'
        or button35['bg']=='green' and button43['bg']=='green' and button51['bg']=='green' and button60['bg']=='green'
        or button36['bg']=='green' and button45['bg']=='green' and button54['bg']=='green' and button64['bg']=='green'
        or button36['bg']=='green' and button44['bg']=='green' and button52['bg']=='green' and button61['bg']=='green'
        or button37['bg']=='green' and button38['bg']=='green' and button39['bg']=='green' and button40['bg']=='green'
        or button37['bg']=='green' and button46['bg']=='green' and button55['bg']=='green' and button65['bg']=='green'
        or button37['bg']=='green' and button47['bg']=='green' and button58['bg']=='green' and button68['bg']=='green'
        or button38['bg']=='green' and button39['bg']=='green' and button40['bg']=='green' and button41['bg']=='green'
        or button38['bg']=='green' and button47['bg']=='green' and button57['bg']=='green' and button66['bg']=='green'
        or button38['bg']=='green' and button48['bg']=='green' and button59['bg']=='green' and button69['bg']=='green'
        or button39['bg']=='green' and button40['bg']=='green' and button41['bg']=='green' and button42['bg']=='green'
        or button39['bg']=='green' and button48['bg']=='green' and button58['bg']=='green' and button67['bg']=='green'
        or button39['bg']=='green' and button49['bg']=='green' and button60['bg']=='green' and button70['bg']=='green'
        or button40['bg']=='green' and button41['bg']=='green' and button42['bg']=='green' and button43['bg']=='green'
        or button40['bg']=='green' and button49['bg']=='green' and button59['bg']=='green' and button68['bg']=='green'
        or button40['bg']=='green' and button48['bg']=='green' and button57['bg']=='green' and button65['bg']=='green'
        or button40['bg']=='green' and button50['bg']=='green' and button61['bg']=='green' and button71['bg']=='green'
        or button41['bg']=='green' and button42['bg']=='green' and button43['bg']=='green' and button44['bg']=='green'
        or button41['bg']=='green' and button50['bg']=='green' and button60['bg']=='green' and button69['bg']=='green'
        or button41['bg']=='green' and button49['bg']=='green' and button58['bg']=='green' and button66['bg']=='green'
        or button41['bg']=='green' and button51['bg']=='green' and button62['bg']=='green' and button72['bg']=='green'
        or button42['bg']=='green' and button43['bg']=='green' and button44['bg']=='green' and button45['bg']=='green'
        or button42['bg']=='green' and button51['bg']=='green' and button61['bg']=='green' and button70['bg']=='green'
        or button42['bg']=='green' and button50['bg']=='green' and button59['bg']=='green' and button67['bg']=='green'
        or button42['bg']=='green' and button52['bg']=='green' and button63['bg']=='green' and button73['bg']=='green'
        or button43['bg']=='green' and button52['bg']=='green' and button62['bg']=='green' and button71['bg']=='green'
        or button43['bg']=='green' and button51['bg']=='green' and button60['bg']=='green' and button68['bg']=='green'
        or button44['bg']=='green' and button53['bg']=='green' and button63['bg']=='green' and button72['bg']=='green'
        or button44['bg']=='green' and button52['bg']=='green' and button61['bg']=='green' and button69['bg']=='green'
        or button45['bg']=='green' and button54['bg']=='green' and button64['bg']=='green' and button73['bg']=='green'
        or button45['bg']=='green' and button53['bg']=='green' and button62['bg']=='green' and button70['bg']=='green'
        or button46['bg']=='green' and button47['bg']=='green' and button48['bg']=='green' and button49['bg']=='green'
        or button46['bg']=='green' and button55['bg']=='green' and button65['bg']=='green' and button74['bg']=='green'
        or button46['bg']=='green' and button57['bg']=='green' and button67['bg']=='green' and button77['bg']=='green'
        or button47['bg']=='green' and button48['bg']=='green' and button49['bg']=='green' and button50['bg']=='green'
        or button47['bg']=='green' and button57['bg']=='green' and button66['bg']=='green' and button75['bg']=='green'
        or button47['bg']=='green' and button58['bg']=='green' and button68['bg']=='green' and button78['bg']=='green'
        or button48['bg']=='green' and button49['bg']=='green' and button50['bg']=='green' and button51['bg']=='green'
        or button48['bg']=='green' and button58['bg']=='green' and button67['bg']=='green' and button76['bg']=='green'
        or button48['bg']=='green' and button59['bg']=='green' and button69['bg']=='green' and button79['bg']=='green'
        or button49['bg']=='green' and button50['bg']=='green' and button51['bg']=='green' and button52['bg']=='green'
        or button49['bg']=='green' and button59['bg']=='green' and button68['bg']=='green' and button77['bg']=='green'
        or button49['bg']=='green' and button58['bg']=='green' and button66['bg']=='green' and button74['bg']=='green'
        or button49['bg']=='green' and button60['bg']=='green' and button70['bg']=='green' and button80['bg']=='green'
        or button50['bg']=='green' and button51['bg']=='green' and button52['bg']=='green' and button53['bg']=='green'
        or button50['bg']=='green' and button60['bg']=='green' and button69['bg']=='green' and button78['bg']=='green'
        or button50['bg']=='green' and button59['bg']=='green' and button67['bg']=='green' and button75['bg']=='green'
        or button50['bg']=='green' and button61['bg']=='green' and button71['bg']=='green' and button81['bg']=='green'
        or button51['bg']=='green' and button52['bg']=='green' and button53['bg']=='green' and button54['bg']=='green'
        or button51['bg']=='green' and button61['bg']=='green' and button70['bg']=='green' and button79['bg']=='green'
        or button51['bg']=='green' and button60['bg']=='green' and button68['bg']=='green' and button76['bg']=='green'
        or button51['bg']=='green' and button62['bg']=='green' and button72['bg']=='green' and button82['bg']=='green'
        or button52['bg']=='green' and button62['bg']=='green' and button71['bg']=='green' and button80['bg']=='green'
        or button52['bg']=='green' and button61['bg']=='green' and button69['bg']=='green' and button77['bg']=='green'
        or button53['bg']=='green' and button63['bg']=='green' and button72['bg']=='green' and button81['bg']=='green'
        or button53['bg']=='green' and button62['bg']=='green' and button70['bg']=='green' and button78['bg']=='green'
        or button54['bg']=='green' and button64['bg']=='green' and button73['bg']=='green' and button82['bg']=='green'
        or button54['bg']=='green' and button63['bg']=='green' and button71['bg']=='green' and button79['bg']=='green'
        or button55['bg']=='green' and button57['bg']=='green' and button58['bg']=='green' and button59['bg']=='green'
        or button57['bg']=='green' and button58['bg']=='green' and button59['bg']=='green' and button60['bg']=='green'
        or button58['bg']=='green' and button59['bg']=='green' and button60['bg']=='green' and button61['bg']=='green'
        or button59['bg']=='green' and button60['bg']=='green' and button61['bg']=='green' and button62['bg']=='green'
        or button60['bg']=='green' and button61['bg']=='green' and button62['bg']=='green' and button63['bg']=='green'
        or button61['bg']=='green' and button62['bg']=='green' and button63['bg']=='green' and button64['bg']=='green'
        or button65['bg']=='green' and button66['bg']=='green' and button67['bg']=='green' and button68['bg']=='green'
        or button66['bg']=='green' and button67['bg']=='green' and button68['bg']=='green' and button69['bg']=='green'
        or button67['bg']=='green' and button68['bg']=='green' and button69['bg']=='green' and button70['bg']=='green'
        or button68['bg']=='green' and button69['bg']=='green' and button70['bg']=='green' and button71['bg']=='green'
        or button69['bg']=='green' and button70['bg']=='green' and button71['bg']=='green' and button72['bg']=='green'
        or button70['bg']=='green' and button71['bg']=='green' and button72['bg']=='green' and button73['bg']=='green'
        or button74['bg']=='green' and button75['bg']=='green' and button76['bg']=='green' and button77['bg']=='green'
        or button75['bg']=='green' and button76['bg']=='green' and button77['bg']=='green' and button78['bg']=='green'
        or button76['bg']=='green' and button77['bg']=='green' and button78['bg']=='green' and button79['bg']=='green'
        or button77['bg']=='green' and button78['bg']=='green' and button79['bg']=='green' and button80['bg']=='green'
        or button78['bg']=='green' and button79['bg']=='green' and button80['bg']=='green' and button81['bg']=='green'
        or button79['bg']=='green' and button80['bg']=='green' and button81['bg']=='green' and button82['bg']=='green'):
                disablebutton()
                messagebox.showinfo("THE WINNER!!!","Winner is player 1")

#--------Config Frame Upper
def push_a():
    global a,b,c,d,e
    a=1
    if buttona.cget('bg')=='white':
        buttona.config(bg='red',activebackground='red')
    else:
        buttona.config(bg='white', activebackground='white')
    buttonb['bg']='white'
    buttonc['bg']='white'
    buttond['bg']='white'
    buttone['bg']='white'
    buttonf['bg']='white'
    buttong['bg']='white'
    buttonh['bg']='white'
    buttoni['bg']='white'
    

def push_b():
    global a,b,c,d,e
    a=2
    if buttonb.cget('bg')=='white':
        buttonb.config(bg='red',activebackground='red')
    else:
        buttonb.config(bg='white', activebackground='white')
    buttona['bg']='white'
    buttonc['bg']='white'
    buttond['bg']='white'
    buttone['bg']='white'
    buttonf['bg']='white'
    buttong['bg']='white'
    buttonh['bg']='white'
    buttoni['bg']='white'
    
def push_c():
    global a,b,c,d,e
    a=3
    if buttonc.cget('bg')=='white':
        buttonc.config(bg='red',activebackground='red')
    else:
        buttonc.config(bg='white', activebackground='white')
    buttonb['bg']='white'
    buttona['bg']='white'
    buttond['bg']='white'
    buttone['bg']='white'
    buttonf['bg']='white'
    buttong['bg']='white'
    buttonh['bg']='white'
    buttoni['bg']='white'
    
def push_d():
    global a,b,c,d,e
    a=4
    if buttond.cget('bg')=='white':
        buttond.config(bg='red',activebackground='red')
    else:
        buttond.config(bg='white', activebackground='white')
    buttonb['bg']='white'
    buttonc['bg']='white'
    buttona['bg']='white'
    buttone['bg']='white'
    buttonf['bg']='white'
    buttong['bg']='white'
    buttonh['bg']='white'
    buttoni['bg']='white'
    

def push_e():
    global a,b,c,d,e
    a=5
    if buttone.cget('bg')=='white':
        buttone.config(bg='red',activebackground='red')
    else:
        buttone.config(bg='white', activebackground='white')
    buttonb['bg']='white'
    buttonc['bg']='white'
    buttond['bg']='white'
    buttona['bg']='white'
    buttonf['bg']='white'
    buttong['bg']='white'
    buttonh['bg']='white'
    buttoni['bg']='white'
    

def push_f():
    global a,b,c,d,e
    a=6
    if buttonf.cget('bg')=='white':
        buttonf.config(bg='red',activebackground='red')
    else:
        buttonf.config(bg='white', activebackground='white')
    buttonb['bg']='white'
    buttonc['bg']='white'
    buttond['bg']='white'
    buttone['bg']='white'
    buttona['bg']='white'
    buttong['bg']='white'
    buttonh['bg']='white'
    buttoni['bg']='white'
   

def push_g():
    global a,b,c,d,e
    a=7
    if buttong.cget('bg')=='white':
        buttong.config(bg='red',activebackground='red')
    else:
        buttong.config(bg='white', activebackground='white')
    buttonb['bg']='white'
    buttonc['bg']='white'
    buttond['bg']='white'
    buttone['bg']='white'
    buttonf['bg']='white'
    buttona['bg']='white'
    buttonh['bg']='white'
    buttoni['bg']='white'
    
def push_h():
    global a,b,c,d,e
    a=8
    if buttonh.cget('bg')=='white':
        buttonh.config(bg='red',activebackground='red')
    else:
        buttonh.config(bg='white', activebackground='white')
    buttonb['bg']='white'
    buttonc['bg']='white'
    buttond['bg']='white'
    buttone['bg']='white'
    buttonf['bg']='white'
    buttong['bg']='white'
    buttona['bg']='white'
    buttoni['bg']='white'
    
def push_i():
    global a,b,c,d,e
    a=9
    if buttoni.cget('bg')=='white':
        buttoni.config(bg='red',activebackground='red')
    else:
        buttoni.config(bg='white', activebackground='white')
    buttonb['bg']='white'
    buttonc['bg']='white'
    buttond['bg']='white'
    buttone['bg']='white'
    buttonf['bg']='white'
    buttong['bg']='white'
    buttonh['bg']='white'
    buttona['bg']='white'

#--------Config Frame Lower
def push_j():
    global a,b,c
    b=1
    if buttonj.cget('bg')=='white':
        buttonj.config(bg='green',activebackground='green')
    else:
        buttonj.config(bg='white', activebackground='white')
    buttonl['bg']='white'
    buttonm['bg']='white'
    buttonn['bg']='white'
    buttono['bg']='white'
    buttonp['bg']='white'
    buttonq['bg']='white'
    buttonr['bg']='white'
    buttonk['bg']='white'
    
def push_k():
    global a,b,c
    b=2
    if buttonk.cget('bg')=='white':
        buttonk.config(bg='green',activebackground='green')
    else:
        buttonk.config(bg='white', activebackground='white')
    buttonj['bg']='white'
    buttonl['bg']='white'
    buttonm['bg']='white'
    buttonn['bg']='white'
    buttono['bg']='white'
    buttonp['bg']='white'
    buttonq['bg']='white'
    buttonr['bg']='white'


def push_l():
    global a,b,c
    b=3
    if buttonl.cget('bg')=='white':
        buttonl.config(bg='green',activebackground='green')
    else:
        buttonl.config(bg='white', activebackground='white')
    buttonj['bg']='white'
    buttonk['bg']='white'
    buttonm['bg']='white'
    buttonn['bg']='white'
    buttono['bg']='white'
    buttonp['bg']='white'
    buttonq['bg']='white'
    buttonr['bg']='white'

def push_m():
    global a,b,c
    b=4
    if buttonm.cget('bg')=='white':
        buttonm.config(bg='green',activebackground='green')
    else:
        buttonm.config(bg='white', activebackground='white')
    buttonj['bg']='white'
    buttonl['bg']='white'
    buttonk['bg']='white'
    buttonn['bg']='white'
    buttono['bg']='white'
    buttonp['bg']='white'
    buttonq['bg']='white'
    buttonr['bg']='white'

def push_n():
    global a,b,c
    b=5
    if buttonn.cget('bg')=='white':
        buttonn.config(bg='green',activebackground='green')
    else:
        buttonn.config(bg='white', activebackground='white')
    buttonj['bg']='white'
    buttonl['bg']='white'
    buttonm['bg']='white'
    buttonk['bg']='white'
    buttono['bg']='white'
    buttonp['bg']='white'
    buttonq['bg']='white'
    buttonr['bg']='white'

def push_o():
    global a,b,c
    b=6
    if buttono.cget('bg')=='white':
        buttono.config(bg='green',activebackground='green')
    else:
        buttono.config(bg='white', activebackground='white')
    buttonj['bg']='white'
    buttonl['bg']='white'
    buttonm['bg']='white'
    buttonn['bg']='white'
    buttonk['bg']='white'
    buttonp['bg']='white'
    buttonq['bg']='white'
    buttonr['bg']='white'

def push_p():
    global a,b,c
    b=7
    if buttonp.cget('bg')=='white':
        buttonp.config(bg='green',activebackground='green')
    else:
        buttonp.config(bg='white', activebackground='white')
    buttonj['bg']='white'
    buttonl['bg']='white'
    buttonm['bg']='white'
    buttonn['bg']='white'
    buttono['bg']='white'
    buttonk['bg']='white'
    buttonq['bg']='white'
    buttonr['bg']='white'

def push_q():
    global a,b,c
    b=8
    if buttonq.cget('bg')=='white':
        buttonq.config(bg='green',activebackground='green')
    else:
        buttonq.config(bg='white', activebackground='white')
    
    buttonj['bg']='white'
    buttonl['bg']='white'
    buttonm['bg']='white'
    buttonn['bg']='white'
    buttono['bg']='white'
    buttonp['bg']='white'
    buttonk['bg']='white'
    buttonr['bg']='white'

def push_r():
    global a,b,c
    b=9
    if buttonr.cget('bg')=='white':
        buttonr.config(bg='green',activebackground='green')
    else:
        buttonr.config(bg='white', activebackground='white')
    buttonj['bg']='white'
    buttonl['bg']='white'
    buttonm['bg']='white'
    buttonn['bg']='white'
    buttono['bg']='white'
    buttonp['bg']='white'
    buttonq['bg']='white'
    buttonk['bg']='white'
        
#--------Frame 1
frame1=tk.Frame(window,borderwidth=2,relief=tk.RIDGE,bg='#A0BFE0')
frame1.pack(padx=10,pady=10)

#--------Answer Frame
button1=tk.Button(frame1,text='64',width=3,height=2,bg='white',command=lambda:buttonclick(1))
button1.grid(row=0,column=0,padx=5,pady=5)

button2=tk.Button(frame1,text='24',width=3,height=2,bg='white',command=lambda:buttonclick(2))
button2.grid(row=0,column=1,padx=5,pady=5)

button3=tk.Button(frame1,text='5',width=3,height=2,bg='white',command=lambda:buttonclick(3))
button3.grid(row=0,column=2,padx=5,pady=5)

button4=tk.Button(frame1,text='16',width=3,height=2,bg='white',command=lambda:buttonclick(4))
button4.grid(row=0,column=3,padx=5,pady=5)

button5=tk.Button(frame1,text='45',width=3,height=2,bg='white',command=lambda:buttonclick(5))
button5.grid(row=0,column=4,padx=5,pady=5)

button6=tk.Button(frame1,text='18',width=3,height=2,bg='white',command=lambda:buttonclick(6))
button6.grid(row=0,column=5,padx=5,pady=5)

button7=tk.Button(frame1,text='72',width=3,height=2,bg='white',command=lambda:buttonclick(7))
button7.grid(row=0,column=6,padx=5,pady=5)

button8=tk.Button(frame1,text='36',width=3,height=2,bg='white',command=lambda:buttonclick(8))
button8.grid(row=0,column=7,padx=5,pady=5)

button9=tk.Button(frame1,text='8',width=3,height=2,bg='white',command=lambda:buttonclick(9))
button9.grid(row=0,column=8,padx=5,pady=5)

button10=tk.Button(frame1,text='4',width=3,height=2,bg='white',command=lambda:buttonclick(10))
button10.grid(row=1,column=0,padx=5,pady=5)

button11=tk.Button(frame1,text='9',width=3,height=2,bg='white',command=lambda:buttonclick(11))
button11.grid(row=1,column=1,padx=5,pady=5)

button12=tk.Button(frame1,text='18',width=3,height=2,bg='white',command=lambda:buttonclick(12))
button12.grid(row=1,column=2,padx=5,pady=5)

button13=tk.Button(frame1,text='56',width=3,height=2,bg='white',command=lambda:buttonclick(13))
button13.grid(row=1,column=3,padx=5,pady=5)

button14=tk.Button(frame1,text='20',width=3,height=2,bg='white',command=lambda:buttonclick(14))
button14.grid(row=1,column=4,padx=5,pady=5)

button15=tk.Button(frame1,text='49',width=3,height=2,bg='white',command=lambda:buttonclick(15))
button15.grid(row=1,column=5,padx=5,pady=5)

button16=tk.Button(frame1,text='2',width=3,height=2,bg='white',command=lambda:buttonclick(16))
button16.grid(row=1,column=6,padx=5,pady=5)

button17=tk.Button(frame1,text='21',width=3,height=2,bg='white',command=lambda:buttonclick(17))
button17.grid(row=1,column=7,padx=5,pady=5)

button18=tk.Button(frame1,text='54',width=3,height=2,bg='white',command=lambda:buttonclick(18))
button18.grid(row=1,column=8,padx=5,pady=5)

button19=tk.Button(frame1,text='63',width=3,height=2,bg='white',command=lambda:buttonclick(19))
button19.grid(row=2,column=0,padx=5,pady=5)

button20=tk.Button(frame1,text='30',width=3,height=2,bg='white',command=lambda:buttonclick(20))
button20.grid(row=2,column=1,padx=5,pady=5)

button21=tk.Button(frame1,text='3',width=3,height=2,bg='white',command=lambda:buttonclick(21))
button21.grid(row=2,column=2,padx=5,pady=5)

button22=tk.Button(frame1,text='28',width=3,height=2,bg='white',command=lambda:buttonclick(22))
button22.grid(row=2,column=3,padx=5,pady=5)

button23=tk.Button(frame1,text='6',width=3,height=2,bg='white',command=lambda:buttonclick(23))
button23.grid(row=2,column=4,padx=5,pady=5)

button24=tk.Button(frame1,text='24',width=3,height=2,bg='white',command=lambda:buttonclick(24))
button24.grid(row=2,column=5,padx=5,pady=5)

button25=tk.Button(frame1,text='15',width=3,height=2,bg='white',command=lambda:buttonclick(25))
button25.grid(row=2,column=6,padx=5,pady=5)

button26=tk.Button(frame1,text='30',width=3,height=2,bg='white',command=lambda:buttonclick(26))
button26.grid(row=2,column=7,padx=5,pady=5)

button27=tk.Button(frame1,text='24',width=3,height=2,bg='white',command=lambda:buttonclick(27))
button27.grid(row=2,column=8,padx=5,pady=5)

button28=tk.Button(frame1,text='15',width=3,height=2,bg='white',command=lambda:buttonclick(28))
button28.grid(row=3,column=0,padx=5,pady=5)

button29=tk.Button(frame1,text='8',width=3,height=2,bg='white',command=lambda:buttonclick(29))
button29.grid(row=3,column=1,padx=5,pady=5)

button30=tk.Button(frame1,text='42',width=3,height=2,bg='white',command=lambda:buttonclick(30))
button30.grid(row=3,column=2,padx=5,pady=5)

button31=tk.Button(frame1,text='8',width=3,height=2,bg='white',command=lambda:buttonclick(31))
button31.grid(row=3,column=3,padx=5,pady=5)

button32=tk.Button(frame1,text='54',width=3,height=2,bg='white',command=lambda:buttonclick(32))
button32.grid(row=3,column=4,padx=5,pady=5)

button33=tk.Button(frame1,text='21',width=3,height=2,bg='white',command=lambda:buttonclick(33))
button33.grid(row=3,column=5,padx=5,pady=5)

button34=tk.Button(frame1,text='9',width=3,height=2,bg='white',command=lambda:buttonclick(34))
button34.grid(row=3,column=6,padx=5,pady=5)

button35=tk.Button(frame1,text='7',width=3,height=2,bg='white',command=lambda:buttonclick(35))
button35.grid(row=3,column=7,padx=5,pady=5)

button36=tk.Button(frame1,text='16',width=3,height=2,bg='white',command=lambda:buttonclick(36))
button36.grid(row=3,column=8,padx=5,pady=5)

button37=tk.Button(frame1,text='12',width=3,height=2,bg='white',command=lambda:buttonclick(37))
button37.grid(row=4,column=0,padx=5,pady=5)

button38=tk.Button(frame1,text='18',width=3,height=2,bg='white',command=lambda:buttonclick(38))
button38.grid(row=4,column=1,padx=5,pady=5)

button39=tk.Button(frame1,text='24',width=3,height=2,bg='white',command=lambda:buttonclick(39))
button39.grid(row=4,column=2,padx=5,pady=5)

button40=tk.Button(frame1,text='4',width=3,height=2,bg='white',command=lambda:buttonclick(40))
button40.grid(row=4,column=3,padx=5,pady=5)

button41=tk.Button(frame1,text='1',width=3,height=2,bg='white',command=lambda:buttonclick(41))
button41.grid(row=4,column=4,padx=5,pady=5)

button42=tk.Button(frame1,text='35',width=3,height=2,bg='white',command=lambda:buttonclick(42))
button42.grid(row=4,column=5,padx=5,pady=5)

button43=tk.Button(frame1,text='5',width=3,height=2,bg='white',command=lambda:buttonclick(43))
button43.grid(row=4,column=6,padx=5,pady=5)

button44=tk.Button(frame1,text='12',width=3,height=2,bg='white',command=lambda:buttonclick(44))
button44.grid(row=4,column=7,padx=5,pady=5)

button45=tk.Button(frame1,text='81',width=3,height=2,bg='white',command=lambda:buttonclick(45))
button45.grid(row=4,column=8,padx=5,pady=5)

button46=tk.Button(frame1,text='35',width=3,height=2,bg='white',command=lambda:buttonclick(46))
button46.grid(row=5,column=0,padx=5,pady=5)

button47=tk.Button(frame1,text='3',width=3,height=2,bg='white',command=lambda:buttonclick(47))
button47.grid(row=5,column=1,padx=5,pady=5)

button48=tk.Button(frame1,text='10',width=3,height=2,bg='white',command=lambda:buttonclick(48))
button48.grid(row=5,column=2,padx=5,pady=5)

button49=tk.Button(frame1,text='25',width=3,height=2,bg='white',command=lambda:buttonclick(49))
button49.grid(row=5,column=3,padx=5,pady=5)

button50=tk.Button(frame1,text='14',width=3,height=2,bg='white',command=lambda:buttonclick(50))
button50.grid(row=5,column=4,padx=5,pady=5)

button51=tk.Button(frame1,text='63',width=3,height=2,bg='white',command=lambda:buttonclick(51))
button51.grid(row=5,column=5,padx=5,pady=5)

button52=tk.Button(frame1,text='42',width=3,height=2,bg='white',command=lambda:buttonclick(52))
button52.grid(row=5,column=6,padx=5,pady=5)

button53=tk.Button(frame1,text='9',width=3,height=2,bg='white',command=lambda:buttonclick(53))
button53.grid(row=5,column=7,padx=5,pady=5)

button54=tk.Button(frame1,text='45',width=3,height=2,bg='white',command=lambda:buttonclick(54))
button54.grid(row=5,column=8,padx=5,pady=5)

button55=tk.Button(frame1,text='16',width=3,height=2,bg='white',command=lambda:buttonclick(55))
button55.grid(row=6,column=0,padx=5,pady=5)

button57=tk.Button(frame1,text='40',width=3,height=2,bg='white',command=lambda:buttonclick(57))
button57.grid(row=6,column=1,padx=5,pady=5)

button58=tk.Button(frame1,text='6',width=3,height=2,bg='white',command=lambda:buttonclick(58))
button58.grid(row=6,column=2,padx=5,pady=5)

button59=tk.Button(frame1,text='2',width=3,height=2,bg='white',command=lambda:buttonclick(59))
button59.grid(row=6,column=3,padx=5,pady=5)

button60=tk.Button(frame1,text='27',width=3,height=2,bg='white',command=lambda:buttonclick(60))
button60.grid(row=6,column=4,padx=5,pady=5)

button61=tk.Button(frame1,text='12',width=3,height=2,bg='white',command=lambda:buttonclick(61))
button61.grid(row=6,column=5,padx=5,pady=5)

button62=tk.Button(frame1,text='72',width=3,height=2,bg='white',command=lambda:buttonclick(62))
button62.grid(row=6,column=6,padx=5,pady=5)

button63=tk.Button(frame1,text='28',width=3,height=2,bg='white',command=lambda:buttonclick(63))
button63.grid(row=6,column=7,padx=5,pady=5)

button64=tk.Button(frame1,text='4',width=3,height=2,bg='white',command=lambda:buttonclick(64))
button64.grid(row=6,column=8,padx=5,pady=5)

button65=tk.Button(frame1,text='7',width=3,height=2,bg='white',command=lambda:buttonclick(65))
button65.grid(row=7,column=0,padx=5,pady=5)

button66=tk.Button(frame1,text='32',width=3,height=2,bg='white',command=lambda:buttonclick(66))
button66.grid(row=7,column=1,padx=5,pady=5)

button67=tk.Button(frame1,text='48',width=3,height=2,bg='white',command=lambda:buttonclick(67))
button67.grid(row=7,column=2,padx=5,pady=5)

button68=tk.Button(frame1,text='6',width=3,height=2,bg='white',command=lambda:buttonclick(68))
button68.grid(row=7,column=3,padx=5,pady=5)

button69=tk.Button(frame1,text='40',width=3,height=2,bg='white',command=lambda:buttonclick(69))
button69.grid(row=7,column=4,padx=5,pady=5)

button70=tk.Button(frame1,text='36',width=3,height=2,bg='white',command=lambda:buttonclick(70))
button70.grid(row=7,column=5,padx=5,pady=5)

button71=tk.Button(frame1,text='18',width=3,height=2,bg='white',command=lambda:buttonclick(71))
button71.grid(row=7,column=6,padx=5,pady=5)

button72=tk.Button(frame1,text='48',width=3,height=2,bg='white',command=lambda:buttonclick(72))
button72.grid(row=7,column=7,padx=5,pady=5)

button73=tk.Button(frame1,text='56',width=3,height=2,bg='white',command=lambda:buttonclick(73))
button73.grid(row=7,column=8,padx=5,pady=5)

button74=tk.Button(frame1,text='10',width=3,height=2,bg='white',command=lambda:buttonclick(74))
button74.grid(row=8,column=0,padx=5,pady=5)

button75=tk.Button(frame1,text='8',width=3,height=2,bg='white',command=lambda:buttonclick(75))
button75.grid(row=8,column=1,padx=5,pady=5)

button76=tk.Button(frame1,text='27',width=3,height=2,bg='white',command=lambda:buttonclick(76))
button76.grid(row=8,column=2,padx=5,pady=5)

button77=tk.Button(frame1,text='14',width=3,height=2,bg='white',command=lambda:buttonclick(77))
button77.grid(row=8,column=3,padx=5,pady=5)

button78=tk.Button(frame1,text='28',width=3,height=2,bg='white',command=lambda:buttonclick(78))
button78.grid(row=8,column=4,padx=5,pady=5)

button79=tk.Button(frame1,text='6',width=3,height=2,bg='white',command=lambda:buttonclick(79))
button79.grid(row=8,column=5,padx=5,pady=5)

button80=tk.Button(frame1,text='32',width=3,height=2,bg='white',command=lambda:buttonclick(80))
button80.grid(row=8,column=6,padx=5,pady=5)

button81=tk.Button(frame1,text='54',width=3,height=2,bg='white',command=lambda:buttonclick(81))
button81.grid(row=8,column=7,padx=5,pady=5)

button82=tk.Button(frame1,text='12',width=3,height=2,bg='white',command=lambda:buttonclick(82))
button82.grid(row=8,column=8,padx=5,pady=5)


#--------Frame 2
frame2=tk.Frame(master=window,border=2,relief=tk.GROOVE,bg='#7895CB')
frame2.pack()

#-------Back Button
back_botton= tk.Button(master=frame2,command=back,text='Back')
back_botton.grid(row=3,column=0,columnspan=3,sticky='news')

#-------Reset Button
reset_button= tk.Button(frame2,text='Reset',command=reset)
reset_button.grid(row=3,column=3,columnspan=3,sticky='news')

#--------Player Label
player_label=tk.Label(frame2,text="Player-1 Turn",bg='green')
player_label.grid(row=3,column=6,columnspan=3,sticky='news')

#--------Button Upper
buttona=tk.Button(master=frame2,text='1',width=3,height=2,bg='white',command=push_a, activebackground='white')
buttona.grid(row=0,column=0,padx=5,pady=5)

buttonb=tk.Button(master=frame2,text='2',width=3,height=2,bg='white',command=push_b, activebackground='white')
buttonb.grid(row=0,column=1,padx=5,pady=5)

buttonc=tk.Button(master=frame2,text='3',width=3,height=2,bg='white',command=push_c, activebackground='white')
buttonc.grid(row=0,column=2,padx=5,pady=5)

buttond=tk.Button(master=frame2,text='4',width=3,height=2,bg='white',command=push_d, activebackground='white')
buttond.grid(row=0,column=3,padx=5,pady=5)

buttone=tk.Button(master=frame2,text='5',width=3,height=2,bg='white',command=push_e, activebackground='white')
buttone.grid(row=0,column=4,padx=5,pady=5)

buttonf=tk.Button(master=frame2,text='6',width=3,height=2,bg='white',command=push_f, activebackground='white')
buttonf.grid(row=0,column=5,padx=5,pady=5)

buttong=tk.Button(master=frame2,text='7',width=3,height=2,bg='white',command=push_g, activebackground='white')
buttong.grid(row=0,column=6,padx=5,pady=5)

buttonh=tk.Button(master=frame2,text='8',width=3,height=2,bg='white',command=push_h, activebackground='white')
buttonh.grid(row=0,column=7,padx=5,pady=5)

buttoni=tk.Button(master=frame2,text='9',width=3,height=2,bg='white',command=push_i, activebackground='white')
buttoni.grid(row=0,column=8,padx=5,pady=5)


#-------Button Lower
buttonj=tk.Button(master=frame2,text='1',width=3,height=2,bg='white',command=push_j,activebackground='white')
buttonj.grid(row=1,column=0,padx=5,pady=5)

buttonk=tk.Button(master=frame2,text='2',width=3,height=2,bg='white',command=push_k, activebackground='white')
buttonk.grid(row=1,column=1,padx=5,pady=5)

buttonl=tk.Button(master=frame2,text='3',width=3,height=2,bg='white',command=push_l, activebackground='white')
buttonl.grid(row=1,column=2,padx=5,pady=5)

buttonm=tk.Button(master=frame2,text='4',width=3,height=2,bg='white',command=push_m, activebackground='white')
buttonm.grid(row=1,column=3,padx=5,pady=5)

buttonn=tk.Button(master=frame2,text='5',width=3,height=2,bg='white',command=push_n, activebackground='white')
buttonn.grid(row=1,column=4,padx=5,pady=5)

buttono=tk.Button(master=frame2,text='6',width=3,height=2,bg='white',command=push_o, activebackground='white')
buttono.grid(row=1,column=5,padx=5,pady=5)

buttonp=tk.Button(master=frame2,text='7',width=3,height=2,bg='white',command=push_p, activebackground='white')
buttonp.grid(row=1,column=6,padx=5,pady=5)

buttonq=tk.Button(master=frame2,text='8',width=3,height=2,bg='white',command=push_q, activebackground='white')
buttonq.grid(row=1,column=7,padx=5,pady=5)

buttonr=tk.Button(master=frame2,text='9',width=3,height=2,bg='white',command=push_r, activebackground='white')
buttonr.grid(row=1,column=8,padx=5,pady=5)


window.mainloop()
