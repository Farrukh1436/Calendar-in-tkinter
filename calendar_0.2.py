from tkinter import *
from datetime import *
calendar_1 =Tk()
calendar_1.title("Calendar")
dt =datetime.now()
change = dt.replace(day=1)
wk_change = change.weekday()
def colour():
    if i==int(dt.strftime("%d"))-1:
      return "Lime"
    return
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
weekdays = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
btn = []
btn_wk = []
lucky_year =int(dt.strftime("%y")) % 4
current_month =int(dt.strftime("%m")) - 1
a =months[current_month]
def sort(current_month_a):
    days_31 = [0,2,4,6,7,9,11]
    days_30 = [3,5,8,10]
    days_feb = [1]
    if current_month_a in days_feb:
        if lucky_year == 0:
            return 29
        else:
            return 28

    elif current_month_a in days_30:
        return 30
    elif current_month_a in days_31:
        return 31
    return 31
for wkdays in range(0,7):
   btn_wk.append(Button(calendar_1,text = weekdays[wkdays]))
   j = (wkdays//7)+1
   m = int(wkdays%7)
   btn_wk[wkdays].grid(row = j, column = m)
#buttons_days
for i in range(0,sort(current_month)):
    btn.append(Button(calendar_1, text = str(i+1), padx = 5, pady = 5,bg = colour()))
    qoldiq = int((i+wk_change)%7)
    r = ((i+wk_change)//7)
    btn[i].grid(row = r+2, column = qoldiq)
btn_mnth = Button(calendar_1, text = a,padx = 60,)
btn_mnth.grid(row = 8,columnspan = 5)
calendar_1.mainloop()