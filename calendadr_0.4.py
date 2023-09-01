import datetime
from tkinter import *
from datetime import *
calendar_1 = Tk()
calendar_1.title("Calendar")
calendar_1.config(bg = "Grey")
calendar_1.attributes("-alpha",0.93)
dt = datetime.now()
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
months_buttons = []
weekdays = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
btn = []
btn_wk = []
current_year = datetime.now().year
qoldiq_year = current_year % 10
current_decade = current_year - qoldiq_year
starting_year = current_decade - 10
current_month = datetime.now().month-1
a = months[current_month]
years = current_year
lucky_year = years % 4
change = dt.replace(day = 1,year = years)
wk_change = change.weekday()
def colour(i):
    if current_month == datetime.now().month-1:
       if i==datetime.now().day-1:
          return "#cb4154"
       return "Grey"
    return "Grey"
def sort(current_month_a):
    days_31 = [0,2,4,6,7,9,11]
    days_30 = [3,5,8,10]
    days_feb = [1]
    print(current_month_a)
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
    months_window = Toplevel()
    months_window.title("Months")
    months_window.attributes("-alpha",0.93)
    months_window.config(bg="Grey")
    months_buttons = []
    for mnth_btn_number in range(0,12):
        mnth_r = mnth_btn_number//3
        mnth_l = mnth_btn_number%3
        months_buttons.append(Button(months_window, text = months[mnth_btn_number],
                              padx = 10,pady = 10,fg = "White",bg=btn_colour(mnth_btn_number),
                              command = lambda mnth_btn_number_a = mnth_btn_number,
                              mw = months_window: chng_month(mnth_btn_number_a, mw)))
        months_buttons[mnth_btn_number].grid(row = mnth_r,column = mnth_l)
    return
def years_f():
    years_window = Toplevel()
    years_window.title("Years")
    years_window.attributes("-alpha", 0.93)
    years_window.config(bg="Grey")
    years_buttons = []
    for year_btn_number in range(0,20):
        global year
        year_r = year_btn_number//4
        year_l = year_btn_number%4
        years = starting_year + year_btn_number
        years_buttons.append(Button(years_window, text=int(years),
                                    padx = 10,pady = 10,fg="White",bg="Grey",
                                    command = lambda year_btn_number_a = years,
                                    yw = years_window: chng_year(year_btn_number_a, yw,)))
        years_buttons[year_btn_number].grid(row = year_r, column=year_l)
def init_chlds(first_time):
    global years
    global current_month
    if (first_time):
        btn = []
        btn_wk = []
        for wkdays in range(0,7):
           btn_wk.append(Button(calendar_1,text = weekdays[wkdays], bg="Grey",))
           j = (wkdays//7)+1
           m = int(wkdays%7)
           btn_wk[wkdays].grid(row = j, column = m)
    for i in range(0, sort(current_month)):
        if (first_time):
            btn.append(Button(calendar_1, text = str(i+1), padx = 5, pady = 5,
                                          fg = "White",bg = colour(i)))
        qoldiq = int((i+wk_change)%7)
        r = ((i+wk_change)//7)
        btn[i].grid(row = r+2, column = qoldiq)
    btn_mnth = Button(calendar_1, text = a, padx = 50,bg = "Grey",foreground = "White",
                                                    command = lambda : months_f())
    btn_year = Button(calendar_1, text = str(years), padx = 10, bg = "Grey", foreground = "White",
                      command = lambda  : years_f())
    btn_mnth.grid(row = 8,columnspan = 4)
    btn_year.grid(row=8,column=3,columnspan=3)
    global change
def chng_month(mnth_btn_number_a, months_window):
    global change
    global wk_change
    global a
    global current_month
    current_month = mnth_btn_number_a
    months_window.destroy()
    change = dt.replace(month=current_month + 1, day=1, year=years)
    wk_change = change.weekday()
    a = months[current_month]
    for item in calendar_1.winfo_children():
        item.destroy()
    init_chlds(True)
    return
def chng_year(year_btn_number_a,years_window):
    global years
    global wk_change
    global a
    global current_month
    years = year_btn_number_a
    years_window.destroy()
    change = dt.replace(month=current_month + 1, day=1, year=years)
    wk_change = change.weekday()
    a = months[current_month]
    for item_y in calendar_1.winfo_children():
        item_y.destroy()
    init_chlds(True)
init_chlds(True)
calendar_1.mainloop()