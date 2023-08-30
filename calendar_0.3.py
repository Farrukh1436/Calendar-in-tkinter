from tkinter import *
from datetime import *
calendar_1 = Tk()
calendar_1.title("Calendar")
calendar_1.config(bg = "Grey")
calendar_1.attributes("-alpha",0.93)
dt = datetime.now()
change = dt.replace(day=1)
wk_change = change.weekday()
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
months_buttons = []
weekdays = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
btn = []
btn_wk = []
lucky_year = int(dt.strftime("%y")) % 4
current_month = int(dt.strftime("%m")) - 1
a = months[current_month]
def colour(i):
    if current_month == int(dt.strftime("%m"))-1:
       if i==int(dt.strftime("%d"))-1:
          return "#cb4154"
       return "Grey"
    return "Grey"
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
def btn_colour(mnth_btn_number):
    global current_month
    if mnth_btn_number == current_month:
       return "#cb4154"
    return "Grey"
def months_f():
    newwindow = Toplevel()
    newwindow.title("Months")
    newwindow.attributes("-alpha",0.93)
    newwindow.config(bg="Grey")
    months_buttons = []
    for mnth_btn_number in range(0,12):
        mnth_r = mnth_btn_number//3
        mnth_l= mnth_btn_number%3
        months_buttons.append(Button(newwindow, text = months[mnth_btn_number],
                              padx = 10,pady = 10,fg = "White",bg=btn_colour(mnth_btn_number),
                              command = lambda mnth_btn_number_a = mnth_btn_number,
                              nw = newwindow: chng_month(mnth_btn_number_a, nw)))
        months_buttons[mnth_btn_number].grid(row = mnth_r,column = mnth_l)
    return
def init_chlds(first_time):
    if (first_time):
        btn = []
        btn_wk = []
        for wkdays in range(0,7):
           btn_wk.append(Button(calendar_1,text = weekdays[wkdays], bg="Grey",))
           j = (wkdays//7)+1
           m = int(wkdays%7)
           btn_wk[wkdays].grid(row = j, column = m)
    global current_month
    for i in range(0, sort(current_month)):
        if (first_time):
            btn.append(Button(calendar_1, text = str(i+1), padx = 5, pady = 5,
                                          fg = "White",bg = colour(i)))
        qoldiq = int((i+wk_change)%7)
        r = ((i+wk_change)//7)
        btn[i].grid(row = r+2, column = qoldiq)
    btn_mnth = Button(calendar_1, text = a, padx = 50,bg = "Grey",foreground = "White",
                                                    command = lambda : months_f())
    btn_mnth.grid(row = 8,columnspan = 4)
    global change
    return
def chng_month(mnth_btn_number_a, new_window):
    global current_month
    global change
    global wk_change
    global a
    current_month = mnth_btn_number_a
    change  = dt.replace(month = current_month+1, day=1)
    wk_change = change.weekday()
    a = months[current_month]
    new_window.destroy()
    for item in calendar_1.winfo_children():
        item.destroy()
    init_chlds(True)
    return
init_chlds(True)
calendar_1.mainloop()
