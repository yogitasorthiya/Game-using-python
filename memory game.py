from tkinter import*
def callback(r,c):
    global player

    if player=='x' and states[r][c]==0 and stop_game==False:
       b[r][c].configure(text='X' ,fg='blue',bg='white')
       states[r][c]='x'
       player='o'

    if player=='o' and states[r][c]==0 and stop_game==False:
        b[r][c].configure(text='o' ,fg='orange',bg='black')
        states[r][c]='o'
        player='x'
    check_for_winner()

def check_for_winner():
    global stop_game
    for i in range(3):
        if states[i][0] == states[i][1]==states[i][2]!=0:
            b[i][0].config(bg='grey')
            b[i][1].config(bg='grey')
            b[i][2].config(bg='grey')
            stop_game=True
    for i in range(3):
        if states[0][i] == states[1][i]==states[2][i]!=0:
            b[0][i].config(bg='grey')
            b[1][i].config(bg='grey')
            b[2][i].config(bg='grey')
            stop_game=True       
        if states[0][0] == states[1][1]==states[2][2]!=0:
            b[0][0].config(bg='grey')
            b[1][1].config(bg='grey')
            b[2][2].config(bg='grey')
            stop_game=True

        if states[2][0]==states[1][1]==states[0][2]!=0:
           b[2][0].config(bg='grey')
           b[1][1].config(bg='grey')
           b[0][2].config(bg='grey')
           stop_game=True  
window = Tk()
window.title("Tkinter game")
b=[[0,0,0],
   [0,0,0],
   [0,0,0]]
states=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in  range(3):
    for j in range (3):
        b[i][j]=Button(font=("arial",60),width=4,bg='powder blue',
                       command= lambda r=i, c=j: callback(r,c))
        b[i][j].grid(row=i,column=j)
player='x'
stop_game=False
mainloop()
window.configure(width=500, height=300)
window.configure(bg='lightgray')
window.mainloop()
print("Congratulations you are winner")