import datetime
from tkinter import *
from datetime import *
root =Tk()
root.title("Calendar")
dt =datetime.now()

numbers_day = []
def colour():
    if i==int(dt.strftime("%d"))-1:
      return "Yellow"
    return
#buttons
btn = []
#buttons_days
for i in range(0,31):
    btn.append(Button(root, text=str(i+1), padx=5, pady=5,bg=colour()))
    r = (i//6) + 1
    l = int(i%6)
    #btn[i]=Button(root, text=str(i), padx=5, pady=5,bg=mnth())
    btn[i].grid(row=r, column=l)

root.mainloop()

