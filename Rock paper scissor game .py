#Rock-Paper-Scissor

from tkinter import *
import random

play = Tk()
play.geometry('800x500')
play.title('Rock-Paper-Scissor Game')
play.configure(bg='lightblue')

choice = {'0':'Rock','1':'Paper','2': 'Scissor'}

def player_rock():
    global cs, ps 
    selected = choice[str(random.randint(0,2))]
    if selected == 'Rock':
        resultdata = 'Tie!..'
    elif selected =='Scissor':
        resultdata = 'Player Wins!..'
        ps += 1
    else:
        resultdata = 'Computer Wins!..'
        cs +=1
    l1.config(text='Rock')
    l2.config(text=selected)
    l6.config(text=ps)
    l7.config(text=cs)
    result.config(text=resultdata)
    disable_btn()

def player_paper():
    global cs, ps 
    selected = choice[str(random.randint(0,2))]
    if selected == 'Scissor' :
        resultdata = 'Computer Wins!..'
        cs += 1
    elif selected == 'Rock':
        resultdata = 'Player Wins!..'
        ps += 1
    else:
        resultdata = 'Tie!..'
    l1.config(text='Paper')
    l2.config(text=selected)
    l6.config(text=ps)
    l7.config(text=cs)
    result.config(text=resultdata)
    disable_btn()

def player_scissor():
    global ps,cs 
    selected = choice[str(random.randint(0,2))]
    if selected == 'Paper':
        resultdata ='Paper Wins!..'
        ps += 1
    elif selected =='Scissor':
        resultdata = 'Tie!..'
    else:
        resultdata = 'Computer Wins!..'
        cs += 1
    l1.config(text='Scissor')
    l2.config(text=selected)
    l6.config(text=ps)
    l7.config(text=cs)
    result.config(text=resultdata)
    disable_btn()

def disable_btn():
    b1['state'] = 'disable'
    b2['state'] = 'disable'
    b3['state'] = 'disable'

def reset():
    b1['state'] = 'active'
    b2['state'] = 'active'
    b3['state'] = 'active'
    l1.config(text = '')
    l2.config(text = '')
    result.config(text = '')


score_frame = Frame(play, width=150, height=100, bg='white')
score_frame.place(x=630,y=50)

Label(score_frame, text='P', font=('calbiri', 20, 'bold')).place(x=20,y=10)
l6 = Label(score_frame, font=('calibri',20,'bold'), fg='red')
l6.place(x=20,y=50)

Label(score_frame, text='C', font=('calibri',20,'bold')).place(x=100,y=10)
l7 = Label(score_frame, font=('calibri',20,'bold'), fg='red')
l7.place(x=100,y=50)

ps = 0
cs = 0

Label(play, text='Rock-Paper-Scissor', font=('calibri',20)).place(x=30,y=80)

l1 = Label(play, font=('calibri',20), bg='green', fg='white')
l1.place(x=100,y=130)

Label(play, text='Computer Selected ',font=('calibri',20)).place(x=330,y=80)

l2 = Label(play, font=('calibri',20), bg='green', fg='white')
l2.place(x=400,y=130)

Label(play, text='Choose any one', font=('calibri',25), bg='blue', fg='white').place(x=180,y=210)

b1 = Button(play, text='Rock', command=player_rock, font=('calibri',20), width='10', height='1', bg='gray', fg='white')
b1.place(x=60,y=270)

b2 = Button(play, text='Paper', command=player_paper, font=('calibri',20), width='10', height='1',bg='gray', fg='white')
b2.place(x=230,y=270)

b3 = Button(play, text='Scissor', command=player_scissor, font=('calibri',20), width='10', height='1', bg='gray', fg='white')
b3.place(x=400,y=270)

result =Label(play, text='', font=('calibri',25), bg='orange', fg='white', relief='solid')
result.place(x=200,y=350)

Button(play,text='Reset Game', command=reset, font=('calibri',15), width='10', height='1', bg='gray', fg='white').place(x=450,y=400)
play.mainloop()